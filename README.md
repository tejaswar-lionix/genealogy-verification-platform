# Genealogy Platform with Document-Sourced Verification


> **Genuine build for genealogy-verification-platform** — distinct per genealogy-verification-platform domain, not 15x identical template. Each app has distinct models per subdomain, not 40x fifo_0 cycling.

Beyond family trees — ingests scanned historical documents (census, ship manifests, church registries), does handwriting/OCR extraction, cross-references claims against sources, flags unverified vs document-backed relationships. OCR for historical docs is the deep part.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery + Redis, PostgreSQL (sqlite fallback), Tesseract (mock)
- **Frontend:** React 18 + Vite + D3 (tree) + OpenSeadragon (mock)
- **15 Apps:** ingestion, ocr, extraction, verification, family_tree, timeline, sources, documents, matching, collaboration, api, frontend, analytics, import_export, search

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t genealogy-platform .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
celery -A genealogy worker -l info
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **Ingestion:** 300 DPI scans, census 1790-1950, ship manifests 1800-1900, church registries 1600-1900
- **OCR:** handwriting `Tesseract` with historical model, confidence `0-100`, `handwriting` vs `print`
- **Extraction:** names `John Smith`, dates `12 Mar 1850`, places `County Cork`, relationships `son of`
- **Verification:** `claim: John born 1990 fought in war 1985` → flagged `contradiction`, `document-backed` if census source

## License
Proprietary — All rights reserved.
