# Sentinel AI

Cloud-native cybersecurity analysis platform scaffold with AI-driven detection, SOAR automation, and observability.

## Features (MVP)
- Real-time event ingestion endpoint with background Elasticsearch indexing
- IsolationForest anomaly scoring with retrain/status endpoints
- SOAR automation: incident creation from high anomaly events, enrichment, notify (Slack support), containment stub
- Incidents API for listing and details
- Docker Compose for local stack (API, Postgres, Elasticsearch, Kibana, Frontend)
- CI with basic SAST and image scan

## Quickstart (Docker Compose)

1. Copy env file:

```bash
cp .env.example .env
```

Optional: add Slack webhook for notifications

```bash
echo 'SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz' >> .env
```

2. Build and start services:

```bash
docker compose up --build
```

3. Open services:
- API Docs: http://localhost:8000/api/docs
- Frontend: http://localhost:3000
- Kibana: http://localhost:5601

## Environment Variables
- Backend
  - `SECRET_KEY` (default: change-me)
  - `ACCESS_TOKEN_EXPIRE_MINUTES` (default: 60)
  - `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
  - `ELASTICSEARCH_URL` (default: http://elasticsearch:9200)
  - `SLACK_WEBHOOK_URL` (optional)
- Frontend
  - `NEXT_PUBLIC_API_BASE` (default: http://localhost:8000)

## API Overview
- Health
  - `GET /api/v1/health/healthz`
  - `GET /api/v1/health/readyz`
- Ingestion
  - `POST /api/v1/ingest/events` body: `{source, event_type, asset_id?, occurred_at?, raw?}`
- Anomaly
  - `POST /api/v1/anomaly/retrain` body: `{limit: number}` (async)
  - `GET /api/v1/anomaly/status`
- Incidents
  - `GET /api/v1/incidents/`
  - `GET /api/v1/incidents/{id}`

## Development

Backend (uvicorn):
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend (Next.js):
```bash
cd frontend
npm install
npm run dev
```

## Architecture
- FastAPI app with modular routers (`health`, `ingest`, `anomaly`, `incidents`)
- PostgreSQL for relational data (users, assets, events, incidents)
- Elasticsearch for search/analytics indices (`events_v1`, `incidents_v1`, `assets_v1`)
- Anomaly service using IsolationForest (simple feature extraction)
- SOAR orchestration triggers incidents on high anomaly scores and runs playbooks
- Notifier supports Slack via webhook; otherwise logs to stdout

## Next Steps
- AuthN/Z: JWT + RBAC
- Threat intel connectors (MISP, VirusTotal) and enrichment endpoint
- Map and charts in dashboard
- Compliance reporting and audit logging
- K8s production hardening, zero-trust policies
