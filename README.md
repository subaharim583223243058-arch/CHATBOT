# Simple Google Gemini CLI Chatbot


This repository contains a Streamlit-based chatbot that calls Google's Generative API (Gemini/Vertex-like). It supports providing credentials via Streamlit Secrets or environment variables.

Setup (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Provide credentials (one of the two):

- API key: set `GOOGLE_API_KEY` environment variable or add it to Streamlit Secrets as `GOOGLE_API_KEY`.
- Service account: add the full service account JSON to Streamlit Secrets as `GOOGLE_SERVICE_ACCOUNT` (value should be the raw JSON), or set `GOOGLE_APPLICATION_CREDENTIALS` to a JSON file path on the server.

Run locally:

```bash
streamlit run app.py
```

Deploy to Streamlit Cloud

1. Push this repo to a GitHub repository.
2. In Streamlit Cloud, create a new app connected to the repo and branch.
3. In the app settings, add Secrets (under "Settings -> Secrets"):

```
GOOGLE_API_KEY="your_api_key_here"
```

or

```
GOOGLE_SERVICE_ACCOUNT="{ ... full service account JSON ... }"
```

4. Launch the app — Streamlit Cloud will install from `requirements.txt` and run `app.py`.

Notes

- The app reads credentials from Streamlit Secrets first, then falls back to environment variables.
- The `build_prompt` function concatenates the conversation history into a simple prompt; adapt it for different conversation formats.
- If you want a custom UI, message streaming, or storing chat logs, I can add those next.
