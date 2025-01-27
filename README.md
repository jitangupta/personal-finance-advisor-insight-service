### Run Locally
- Activate the environment: `venv/Scripts\activate`
- Run on HTTP: `uvicorn app.main:app --reload`
- Run on HTTPS: `uvicorn app.main:app --host 127.0.0.1 --port 8443 --ssl-certfile local-dev-certificate.pem --ssl-keyfile local-dev-certificate.pem`
- Access app at `https://127.0.0.1:8443/`