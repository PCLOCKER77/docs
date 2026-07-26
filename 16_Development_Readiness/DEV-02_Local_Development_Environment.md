# DEV-02 Local Development Environment

> Local environment baseline for running Digitize frontend, backend, database, cache, workers, and supporting services.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-02 |
| Document Name | Local Development Environment |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | DevOps / Engineering |
| Reviewers | Frontend, Backend, QA, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the local development services required before coding begins.

---

# 2. Required Local Services

Local development shall provide:

- FastAPI backend.
- Flutter web runtime.
- PostgreSQL.
- Redis.
- Celery worker.
- Optional Celery scheduler.
- S3-compatible local object storage where file workflows are tested.
- Optional ClamAV scanner where file scanning is tested.

---

# 3. Local Docker Compose Baseline

The initial `docker-compose.yml` should include:

| Service | Purpose |
|---|---|
| `postgres` | Local PostgreSQL database |
| `redis` | Cache and Celery broker |
| `backend` | FastAPI API runtime |
| `worker` | Celery worker runtime |
| `frontend` | Flutter web development runtime where containerized |
| `minio` | Local S3-compatible object storage where file workflows are active |
| `clamav` | Local malware scanning service where file workflows are active |

---

# 4. Environment Files

The repository shall include `.env.example`.

It shall include only placeholder values and shall not include real credentials.

Required environment categories:

- App environment.
- Backend URLs.
- Database connection.
- Redis connection.
- JWT configuration placeholders.
- AWS configuration placeholders.
- S3-compatible storage placeholders.
- Logging and observability settings.
- Flutter API base URL.

---

# 5. Local Readiness Checks

Before feature development:

- Backend health endpoint returns healthy.
- Backend readiness endpoint confirms PostgreSQL and Redis connectivity.
- Alembic migration command runs locally.
- Flutter web starts locally.
- Backend can serve OpenAPI schema.
- A sample API call succeeds from Flutter to FastAPI.

---

# 6. Security Rules

- No real AWS credentials in local files.
- No secrets committed to Git.
- Local JWT secrets are development-only.
- Local object storage data is disposable.
- Test data must not contain real customer data.

---

# 7. Local Port Baseline

| Service | Default Port | Notes |
|---|---|
| FastAPI Backend | `8000` | Local API |
| Flutter Web | `3000` or Flutter-selected port | Local frontend |
| PostgreSQL | `5432` | Local database |
| Redis | `6379` | Cache and Celery broker |
| MinIO API | `9000` | Local S3-compatible API |
| MinIO Console | `9001` | Local storage console |
| ClamAV | `3310` | Optional scanner |

Ports may change if already in use, but `.env.example` and local README shall stay aligned.

---

# 8. Required Local Commands

The final scaffold should support equivalent commands for:

```text
start local services
start backend
run backend tests
run database migrations
start celery worker
start Flutter web
run Flutter tests
run all local checks
```

Exact commands shall be documented after scaffolding because they depend on generated package files.

---

# 9. Environment Variable Categories

| Category | Examples |
|---|---|
| App | `APP_ENV`, `APP_NAME`, `DEBUG` |
| API | `API_BASE_URL`, `CORS_ALLOWED_ORIGINS` |
| Database | `DATABASE_URL` |
| Redis | `REDIS_URL` |
| Auth | `JWT_SECRET_KEY`, `JWT_ISSUER`, `ACCESS_TOKEN_TTL` |
| Storage | `S3_ENDPOINT_URL`, `S3_BUCKET_NAME`, `S3_ACCESS_KEY_ID` |
| Worker | `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND` |
| Observability | `LOG_LEVEL`, `OTEL_EXPORTER_OTLP_ENDPOINT` |

---

# 10. Local Data Rules

- Local seed data shall be synthetic.
- Local migrations shall be repeatable from a clean database.
- Local object storage may be wiped at any time.
- Local Redis data shall be disposable.
- Developers shall not import production exports into local services.

