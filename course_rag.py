"""Hybrid retrieval over original course notes and user-supplied IBM manuals."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from io import BytesIO
from typing import Any

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MAX_MANUAL_BYTES = 25 * 1024 * 1024
MAX_MANUAL_PAGES = 1200
MAX_MANUAL_FILES = 5
MAX_TOTAL_MANUAL_BYTES = 50 * 1024 * 1024
CHUNK_CHARS = 1200
CHUNK_OVERLAP = 180


def _tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9$#@]+", text.casefold())


def _split_page(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text).strip()
    if not clean:
        return []
    if len(clean) <= CHUNK_CHARS:
        return [clean]

    chunks = []
    start = 0
    while start < len(clean):
        end = min(start + CHUNK_CHARS, len(clean))
        if end < len(clean):
            boundary = clean.rfind(" ", start + CHUNK_CHARS // 2, end)
            if boundary > start:
                end = boundary
        chunks.append(clean[start:end].strip())
        if end >= len(clean):
            break
        start = max(end - CHUNK_OVERLAP, start + 1)
    return chunks


def extract_pdf_chunks(data: bytes, filename: str) -> list[dict[str, Any]]:
    """Extract page-aware chunks from a bounded PDF; no PDF is retained."""
    if len(data) > MAX_MANUAL_BYTES:
        raise ValueError("Each PDF must be 25 MB or smaller.")
    reader = PdfReader(BytesIO(data), strict=False)
    if len(reader.pages) > MAX_MANUAL_PAGES:
        raise ValueError(f"PDF exceeds the {MAX_MANUAL_PAGES}-page training limit.")

    docs = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        for chunk_number, chunk in enumerate(_split_page(text), start=1):
            docs.append(
                {
                    "id": f"{filename}:{page_number}:{chunk_number}",
                    "title": f"{filename} · page {page_number}",
                    "text": chunk,
                    "source": filename,
                    "page": page_number,
                    "url": "",
                    "kind": "uploaded manual",
                }
            )
    if not docs:
        raise ValueError(
            "No extractable text was found. Scanned/image-only PDFs need OCR before upload."
        )
    return docs


@dataclass
class HybridIndex:
    documents: list[dict[str, Any]]
    vectorizer: TfidfVectorizer
    tfidf_matrix: Any
    tokenized: list[list[str]]
    average_length: float
    idf: dict[str, float]

    @classmethod
    def build(cls, documents: list[dict[str, Any]]) -> "HybridIndex":
        if not documents:
            raise ValueError("At least one course document is required.")
        text = [
            f"{doc.get('title', '')} {doc.get('text', '')}"
            for doc in documents
        ]
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True,
            max_features=100_000,
        )
        matrix = vectorizer.fit_transform(text)
        tokenized = [_tokens(item) for item in text]
        total_tokens = sum(map(len, tokenized))
        average_length = total_tokens / max(len(tokenized), 1)
        document_frequency = Counter(
            token for tokens in tokenized for token in set(tokens)
        )
        idf = {
            term: math.log(
                1 + (len(tokenized) - count + 0.5) / (count + 0.5)
            )
            for term, count in document_frequency.items()
        }
        return cls(documents, vectorizer, matrix, tokenized, average_length, idf)

    def search(self, query: str, top_k: int = 6) -> list[dict[str, Any]]:
        terms = _tokens(query)
        if not terms:
            return []

        tfidf_scores = cosine_similarity(
            self.vectorizer.transform([query]), self.tfidf_matrix
        ).ravel()
        bm25_scores = []
        k1 = 1.5
        b = 0.75
        for tokens in self.tokenized:
            frequencies = Counter(tokens)
            length = len(tokens)
            score = 0.0
            for term in terms:
                frequency = frequencies.get(term, 0)
                if frequency:
                    norm = frequency + k1 * (
                        1 - b + b * length / max(self.average_length, 1)
                    )
                    score += self.idf.get(term, 0.0) * frequency * (k1 + 1) / norm
            bm25_scores.append(score)

        tfidf_order = tfidf_scores.argsort()[::-1]
        bm25_order = sorted(
            range(len(bm25_scores)), key=bm25_scores.__getitem__, reverse=True
        )
        rank_scores: dict[int, float] = {}
        for rank, index in enumerate(tfidf_order, start=1):
            if tfidf_scores[index] > 0:
                rank_scores[index] = rank_scores.get(index, 0) + 0.55 / (60 + rank)
        for rank, index in enumerate(bm25_order, start=1):
            if bm25_scores[index] > 0:
                rank_scores[index] = rank_scores.get(index, 0) + 0.45 / (60 + rank)

        ranked = sorted(rank_scores, key=rank_scores.__getitem__, reverse=True)[:top_k]
        results = []
        for index in ranked:
            document = dict(self.documents[index])
            document["relevance"] = round(rank_scores[index], 5)
            results.append(document)
        return results
