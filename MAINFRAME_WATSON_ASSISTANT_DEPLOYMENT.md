# Deploying the MVS Learning Lab in an IBM Z environment

The MVS SYSPROG learning lab is a standalone Streamlit application. It does not
connect to a z/OS host, execute commands, submit JCL, or manage SMP/E zones. The
terminal output is simulated.

The supplied [ABCs Volume 2 (SG24-6982-04)](https://www.redbooks.ibm.com/redbooks/pdfs/sg246982.pdf)
was published in April 2018 for z/OS V2R3. Course links point to specific PDF
pages. Treat this book as a learning reference and verify procedures against
current IBM documentation for the installed release.

## Supported deployment patterns

### z/OS Container Extensions (zCX)

Run the supplied Linux container through the zCX procedures supported by your
installation. Have the z/OS and network administrators provision the container
environment, registry access, CPU/memory, DNS, persistent/logging requirements,
and approved inbound route. The Dockerfile listens on `0.0.0.0:8080`. Use a
secured TLS endpoint and a proxy configured for Streamlit WebSockets.

### Linux on IBM Z

Build or pull an image supported by the target architecture (commonly
`linux/s390x`) and run it with the site's approved Docker/Podman service. Verify
that all Python dependencies have wheels for the selected Python
version and architecture. Put the app behind an approved HTTPS reverse proxy
and configure WebSocket forwarding.

### IBM Cloud Code Engine

See [DEPLOY_CODE_ENGINE.md](./DEPLOY_CODE_ENGINE.md) for a source-build and
optional Granite configuration example.

## Build and check the container

From the project folder:

```sh
docker build -t mvs-learning-lab:1 .
docker run --rm -p 8080:8080 mvs-learning-lab:1
```

Open `http://localhost:8080`. The app requires no z/OS connection or external
data. The optional Granite tutor requires outbound HTTPS access to the selected
watsonx.ai endpoint. Fetching the supplied manual additionally needs access to
`www.redbooks.ibm.com`; user-uploaded manuals are indexed in session memory.

## Manual retrieval and optional watsonx.ai

The manual tutor indexes all authored units and command references with hybrid
TF-IDF/cosine and BM25 retrieval, then combines rankings using reciprocal-rank
fusion. It can also extract page-aware chunks from user-uploaded PDFs or the
supplied IBM-hosted PDF. Uploaded PDF content is not bundled in the container or
saved by the app. The `.joblib` download contains only the app-authored base
corpus. The Granite model is pretrained and is not fine-tuned by this app.
When a user requests a generated answer, the question and retrieved evidence
passages are sent to the configured IBM watsonx.ai endpoint. Retrieved passages
may include excerpts from a PDF uploaded during the current session.

To generate answers with IBM Granite, inject these values through the runtime's
secret manager:

- `WATSONX_APIKEY`
- `WATSONX_PROJECT_ID` or `WATSONX_SPACE_ID`
- `WATSONX_URL` (defaults to the US South endpoint)
- `WATSONX_MODEL_ID` (defaults to `ibm/granite-3-3-8b-instruct`)

Keep credentials out of source control and container images. Without these
secrets, the local lessons and TF-IDF retrieval tutor still work.

## Operational and learning-safety notes

- The simulated terminal does not connect to TSO/E, ISPF, JES, SDSF, or an
  operator console.
- JCL input receives only a simple structure check; it is never submitted.
- SMP/E examples are educational templates with placeholders. Practice only in
  a disposable sandbox with a valid test package, and use the applicable IBM
  manual and local change-control process before any real maintenance.
- Diagnostic dumps and DFSMSdss backup dumps are distinct concepts. Use an
  organization-approved recovery plan for real data.
- The quiz certificate is unofficial and is not issued, endorsed, or accredited
  by IBM. Upload only a logo you are authorized to use.

## IBM references

- [z/OS 3.2 Documentation](https://www.ibm.com/docs/en/zos/3.2.0)
- [IBM watsonx.ai documentation](https://www.ibm.com/docs/en/watsonx/saas)
- [z/OS Container Extensions documentation](https://www.ibm.com/docs/en/zos/3.2.0?topic=zcx-zos-container-extensions)
