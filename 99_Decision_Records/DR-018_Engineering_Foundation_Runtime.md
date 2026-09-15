# DR-018 Engineering Foundation Runtime

> Runtime decisions for logging, identifiers, session/UoW, pool, and deferred infrastructure at the engineering foundation gate.

---

# Document Control

| Field | Value |
| --- | --- |
| Document ID | DR-018 |
| Document Name | Engineering Foundation Runtime |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Backend Engineering / Architecture |
| Reviewers | Architecture, Backend, Security, QA |
| Version | 1.0 |
| Last Updated | 2026-09-12 |
| Supersedes | None |
| Clarifies | DR-007 (physical SQL vs Alembic stamp), DR-008/009/013/014 (defer runtime wiring) |

---

# 1. Decision Summary

The Digitize FastAPI process shall use:

- API-00 envelopes and error codes (not a parallel `meta`-only contract)
- `X-Correlation-ID`, `X-Request-ID`, and W3C `traceparent`
- JSON structured logs with contextvars
- One pooled async SQLAlchemy engine and one Unit of Work per request
- SQL `database/migrations/001`–`008` as the physical schema source
- Alembic only to stamp `db11_foundation_baseline`
- Principal / cache / storage protocols without JWT, Redis, S3, or Celery in this gate

---

# 2. Context

Design documents (BE-00–BE-11, DR-007–DR-014) already chose FastAPI, PostgreSQL, Redis, Celery, S3, and OpenTelemetry. The running service had catalog APIs and a partial envelope, but lacked structured logging, request IDs, tracing context, pooled UoW, and a Principal boundary.

The foundation gate must freeze runtime behavior without implementing Authentication or inventing schema.

---

# 3. Decisions

| Topic | Decision | Status |
| --- | --- | --- |
| Envelope | Keep API-00; put `request_id` / `trace_id` in `metadata` + headers | FROZEN |
| Migrations | SQL 001–008 authoritative; Alembic stamp-only; autogenerate disabled | FROZEN |
| Session / UoW | One session per request; centralized commit/rollback | FROZEN |
| Pool | Settings-driven; dev 5+5 with pre-ping | FROZEN |
| Logging | JSON stdout + redaction | FROZEN |
| Tracing | W3C `traceparent` in-process; OTLP exporter deferred | FROZEN / DEFERRED exporter |
| Cache | `CacheProvider` + NoOp; Redis (DR-008) not on the request path | DEFERRED |
| Object storage | Protocol only; S3 (DR-014) not wired | DEFERRED |
| Background jobs | Celery (DR-009) not introduced | DEFERRED |
| Auth | `Principal` protocol + env stub; no JWT login | DEFERRED |
| Pagination | Offset `page` / `page_size` | FROZEN |
| Idempotency store | Not created (no table invention) | DEFERRED |
| Concurrency | Optimistic `version_number` + If-Match | FROZEN |
| Architecture style | Modular monolith (DR-017); no Kafka/mesh/microservices | FROZEN |

---

# 4. Alternatives considered

| Option | Outcome |
| --- | --- |
| Replace API-00 with `{ data, meta }` only | Rejected — API-00 is frozen |
| Reactivate Alembic autogenerate | Rejected — conflicts with DB foundation freeze |
| Wire Redis/Celery/S3 now | Rejected — unused infrastructure |
| Full OpenTelemetry SDK + exporter | Deferred — local `trace_id` in logs is sufficient for this gate |

---

# 5. Consequences

Implementers follow `docs/architecture/ENGINEERING_STANDARDS.md` and `BACKEND_FOUNDATION.md`. Authentication remains the next product gate after this freeze is accepted.
