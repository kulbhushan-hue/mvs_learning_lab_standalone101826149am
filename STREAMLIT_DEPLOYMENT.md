# MVS SYSPROG Learning Lab

This is a standalone Streamlit app for learning z/OS concepts.

## Run locally

From this folder, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On macOS/Linux, activate the environment with
`source .venv/bin/activate` and start it with `streamlit run app.py`.

## Deploy to Streamlit Community Cloud

1. Push this folder's app files to a GitHub repository.
2. Create an app in Streamlit Community Cloud, select the repository and branch,
   and set the main file path to `app.py`.
3. Deploy. Streamlit installs dependencies from `requirements.txt`.
4. Open the app and try `HELP`, `D IPLINFO`, `D PROG,LNKLST`, `$D JOB`,
   `APPLY CHECK`, and `SUBMIT`.

Keep `app.py`, `zos_learning_lab.py`, `requirements.txt`, and `Dockerfile`
together. The retrieval index is built locally from the lesson corpus and can be
downloaded from the tutor as a `.joblib` file. This index covers the authored
course and command cards; it does not include uploaded manual text. Do not load
joblib files from untrusted sources.

In **Manual RAG tutor**, click the IBM Redbooks fetch button to index the
provided Volume 2 PDF, or upload other PDF manuals. Extraction is page-aware and
session-only. Scanned/image-only PDFs need OCR before upload. The deployed app
needs outbound HTTPS to `www.redbooks.ibm.com` only if you choose to fetch the
supplied manual; uploading PDFs does not require that network access.

Retrieval combines TF-IDF/cosine similarity and BM25 with reciprocal-rank
fusion. It indexes all course units, command cards, JCL statement references,
plus any loaded PDF passages. The JES3 lesson is also included. This is a search
index, not a fine-tuned language model. Optional Granite answer generation is
pretrained and grounds answers in the retrieved passages. If you request a
Granite answer, your question and retrieved passages (which may contain excerpts
from uploaded manuals) are sent to the configured IBM watsonx.ai endpoint.
Uploaded PDF files are not retained by this app.

## Optional watsonx.ai Granite tutor

The lessons and local TF-IDF/BM25 retrieval work without cloud credentials. To enable
generated answers, configure Streamlit secrets:

```toml
WATSONX_APIKEY = "your-IBM-Cloud-API-key"
WATSONX_PROJECT_ID = "your-watsonx-project-id"
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
WATSONX_MODEL_ID = "ibm/granite-3-3-8b-instruct"
```

Use either `WATSONX_PROJECT_ID` or `WATSONX_SPACE_ID`. Set secrets in the
deployment platform, never in source code. The selected project/space must have
access to the chosen model and regional endpoint.

## Safety and certificate

The 3270-style console is a local simulator. It has no host connection and never
submits JCL or changes a z/OS system. SMP/E examples contain placeholders and
are for a disposable sandbox only; confirm procedures against IBM documentation
and site change controls.

The quiz certificate is an unofficial learning certificate, not issued or
endorsed by IBM. A learner may upload a PNG/JPG logo they are authorized to use.
