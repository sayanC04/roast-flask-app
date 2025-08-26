# GenZ Name Roast — Flask + Docker

A tiny, production-friendly Flask app that roasts a name with playful Gen‑Z humor.
Safe by default: avoids identity-targeting and violent language.

## Quick start (Docker)

```bash
docker build -t genz-roast-name .
docker run -p 5000:5000 genz-roast-name
```

Open http://localhost:5000

## Local dev (optional)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
FLASK_ENV=development python wsgi.py
```

## API

- `POST /api/v1/roast` JSON: `{ "name": "Sayan" }`
- `GET /api/v1/health`

## Notes

- Rate limiting: Flask-Limiter (memory storage by default).
- Caching: Flask-Caching (SimpleCache by default).
- Gunicorn: gthread workers, bound to port 5000.
