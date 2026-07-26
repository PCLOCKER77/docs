# DEV-04 FastAPI Backend Start Plan

> Backend implementation start plan for the Digitize modular monolith.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-04 |
| Document Name | FastAPI Backend Start Plan |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Backend Engineering |
| Reviewers | Architecture, Database, API, Security, DevOps, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the backend work needed before feature modules are implemented.

---

# 2. Backend Baseline

Backend implementation shall use:

- FastAPI.
- Python.
- Modular monolith architecture.
- PostgreSQL.
- SQLAlchemy.
- Alembic.
- Redis.
- Celery with Redis broker.
- S3-compatible object storage where file workflows are active.

---

# 3. Start Sequence

Backend development should begin in this order:

| Order | Work Item |
|---|---|
| 1 | Create backend package and FastAPI app bootstrap |
| 2 | Add settings/configuration model |
| 3 | Add structured logging, request ID, and correlation ID |
| 4 | Add health and readiness endpoints |
| 5 | Add PostgreSQL connection and SQLAlchemy session handling |
| 6 | Add Alembic migration setup |
| 7 | Add Redis connection |
| 8 | Add Celery worker bootstrap |
| 9 | Add common error response handling |
| 10 | Add authentication scaffolding |
| 11 | Add tenant context dependency/middleware |
| 12 | Add module package structure |
| 13 | Add initial platform/organization/facility/site vertical slice |

---

# 4. Required Foundation Endpoints

Initial backend shall expose:

- `GET /api/v1/health`
- `GET /api/v1/readiness`
- `GET /api/v1/openapi.json`

Readiness shall verify at minimum:

- PostgreSQL connectivity.
- Redis connectivity.
- Required configuration presence.

---

# 5. Module Boundary Rules

Modules shall not directly mutate other modules' data.

Cross-module behavior shall use:

- Application service calls where same transaction ownership is valid.
- Query contracts for read-only cross-module access.
- Outbox events for asynchronous cross-module or provider behavior.

---

# 6. First Backend Done Criteria

The backend foundation is ready when:

- App starts locally.
- Database migration runs locally.
- Health and readiness endpoints work.
- Request IDs and correlation IDs appear in logs.
- Redis connectivity is verified.
- Celery worker starts.
- API tests run in CI.
- First vertical slice can be added without changing foundation architecture.

---

# 7. Backend Foundation Package Responsibilities

| Package | Responsibility |
|---|---|
| `app/core/config.py` | Settings and environment configuration |
| `app/core/logging.py` | Structured logging |
| `app/core/errors.py` | Common error classes and handlers |
| `app/core/security.py` | Auth helpers and security primitives |
| `app/db/session.py` | SQLAlchemy engine and session lifecycle |
| `app/api/router.py` | API router composition |
| `app/workers/celery_app.py` | Celery application bootstrap |
| `app/modules/` | Modular monolith feature modules |

---

# 8. Initial API Foundation

The first backend scaffold shall define:

- API version prefix: `/api/v1`.
- Health endpoint.
- Readiness endpoint.
- Common error response shape.
- Request ID middleware.
- Correlation ID middleware.
- CORS configuration for local Flutter web.
- OpenAPI metadata.

---

# 9. Initial Database Foundation

Database setup shall include:

- SQLAlchemy engine.
- Session dependency.
- Alembic environment.
- Initial migration baseline.
- PostgreSQL schema creation alignment.
- Test database strategy.

---

# 10. Backend Test Baseline

Backend foundation tests shall include:

- Health endpoint test.
- Readiness endpoint test with mocked dependencies.
- Database session test.
- Migration smoke test.
- Error response shape test.
- Request ID/correlation ID logging test where practical.

---

# 11. Backend Risks Before Feature Work

| Risk | Control |
|---|---|
| Module boundaries become unclear | Enforce folder layout and review checklist |
| Tenant context added too late | Add tenant dependency placeholder before module work |
| Alembic drift from DB docs | Review migrations against DB-11 and DB standards |
| Celery tasks bypass service layer | Require tasks to call application services or processors |
| API errors become inconsistent | Add common error handler before first module |

