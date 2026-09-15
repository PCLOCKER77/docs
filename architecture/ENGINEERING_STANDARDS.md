# DIGITIZE Engineering Standards Freeze

**Status:** FROZEN WITH DEFERRED ITEMS  
**Date:** 2026-09-12  
**Product:** Digitize by OreeOn  
**Scope:** Cross-cutting backend foundation. Not Authentication. Not product modules.

This freeze inspects existing BE/API/DB documents and the running `digitize-services` code. It does not rewrite those documents. Where runtime code and design docs conflict, this freeze states the implementation rule.

**Implementer coding standard:** [BACKEND_CODING_STANDARDS.md](BACKEND_CODING_STANDARDS.md). That file is authoritative for day-to-day backend engineering. This freeze remains the architectural invariant list.

---

## 1. Invariants (must remain true)

1. Hierarchy is Platform → Organization → Facility → Site. Site is a child of Facility. There is no Branch.
2. Platform-owned SaaS subscription plans (`commercial.subscription_plan`) stay separate from customer membership plans (`membership.membership_plan`).
3. Physical schema is `database/migrations/001`–`008`. Do not run Alembic autogenerate. Do not call `Base.metadata.create_all()`.
4. API-00 envelope and error-code format remain the client contract.
5. Routers stay thin. Services own use cases. Repositories own SQL. Repositories do not import FastAPI.
6. Secrets never enter git, logs, API bodies, or Flutter.
7. Backend enforces authentication, authorization, and tenant scope. UI restrictions are not sufficient.
8. One SQLAlchemy engine per process. One session / Unit of Work per request.
9. Caching, queues, object storage, and JWT login are not required to serve traffic today.

---

## 2. Standard labels

| Label | Meaning |
| --- | --- |
| **FROZEN** | Implementers must follow this now |
| **DEFERRED** | Approved direction exists or is likely; do not build it in this gate |
| **REQUIRES DECISION** | Must not be implemented until an owner decides |

---

## 3. Coding and project structure — FROZEN

| Topic | Rule |
| --- | --- |
| Language | Python 3.13, async FastAPI + SQLAlchemy 2.0 async |
| Package | `digitize-services/app` (existing layout retained; no `src/` move in this gate) |
| Module shape | `modules/<capability>/{routes,schemas,service,repository,models}` |
| Shared HTTP | `app/api/` envelopes, errors, dependencies |
| Shared runtime | `app/infrastructure/` |
| Config | `app/config/settings.py` typed `Settings` |
| Formatter / lint | Ruff, line length 88 |
| Types | MyPy on `app` |
| JSON | `snake_case` |
| URLs | `/api/v1` + kebab-case resources |
| Async | `async def` for IO (HTTP, DB). Do not block the event loop with sync DB or HTTP SDKs |
| Docstrings | Public modules and non-obvious invariants. Do not narrate obvious code |
| SOLID / DRY | Prefer explicit module code over generic magic repositories |

Do not rename packages solely to match BE-02 `src/digitize_backend`. Ownership boundaries matter more than folder names.

---

## 4. Configuration and secrets — FROZEN

Environment-driven `pydantic-settings`. Precedence:

1. Process environment  
2. `digitize-services/.env` (gitignored)  
3. Code defaults (non-secret only)

Environments: `development`, `test`, `staging`, `production`.

Categories: application, database pool, cache (disabled), object storage (disabled), JWT placeholders, observability, HTTP/CORS.

Secrets must never be committed. `.env` and `.env.*` are gitignored except `*.example`. Staging/production require explicit DB credentials (`app/config/db_config.py`). Vault (DR-011) is **DEFERRED** for local/dev; environment injection remains the runtime mechanism.

---

## 5. Identifiers and request context — FROZEN

| ID | Header / field | Purpose |
| --- | --- | --- |
| Correlation ID | `X-Correlation-ID` → `correlation_id` | Workflow across retries |
| Request ID | `X-Request-ID` → `request_id` | One HTTP attempt |
| Trace ID | W3C `traceparent` → `trace_id` | Distributed trace |
| Span ID | from `traceparent` → `span_id` | Current span |

Propagate if valid; otherwise generate. Bind with `contextvars`. Do not pass IDs through every service signature. API JSON stays snake_case. Do not expose `traceId`.

Tenant IDs in context (`organization_id`, `facility_id`, `site_id`) are **informational until authorized**. Clients cannot grant access by sending `X-Organization-ID`.

---

## 6. Logging and tracing — FROZEN (exporters DEFERRED)

JSON structured logs to stdout. Factory: `get_logger(module)`.

Required semantic fields when available: `timestamp`, `environment`, `service`, `module`, `operation`, `correlation_id`, `request_id`, `trace_id`, `span_id`, `principal_id`, `organization_id`, `facility_id`, `site_id`, `http.method`, `http.path`, `http.status_code`, `outcome`, `latency_ms`, `error_code`, `severity`.

Access log: once per request. 2xx/3xx INFO, 4xx WARNING, 5xx ERROR.

Never log passwords, hashes, JWTs, Authorization headers, API keys, storage credentials, DB passwords, or sensitive PII. Redact centrally.

OpenTelemetry vendor exporters, Tempo, Prometheus scrape, and Loki shipping are **DEFERRED**. Local development records `trace_id`/`span_id` in logs. DR-013 remains the long-term tooling baseline.

Audit tables are not application logs.

---

## 7. API envelope and errors — FROZEN

API-00 success envelope is the contract:

`success`, `data`, `message`, `metadata`, `correlation_id`, `timestamp`

Do not replace this with a `meta`-only envelope. `request_id` and `trace_id` are added under `metadata` and as response headers.

Error envelope: `success: false`, `error.code`, `error.message`, `error.category`, `error.details`, plus `correlation_id` and `timestamp`. Codes use `<DOMAIN>_<SEMANTIC_ERROR>` (no numeric suffix, no HTTP status, no API-number prefix). Authoritative list: `digitize-services/app/api/error_codes.py` and [BACKEND_CODING_STANDARDS.md](BACKEND_CODING_STANDARDS.md) §7.

HTTP usage (API-00): 200 read/update, 201 create, 202 async, 204 no body, 400 malformed, 401 unauthenticated, 403 unauthorized, 404 not found, 409 conflict, 412/428 concurrency, 422 validation, 429 rate limit, 500 unexpected, 502 upstream, 503 dependency, 504 timeout.

Health probes are operational JSON `{ "status": ... }` and are not required to use the business envelope.

---

## 8. Database runtime — FROZEN

| Topic | Rule |
| --- | --- |
| Engine | One `AsyncEngine` per process, `postgresql+asyncpg` |
| Pool | Tunable: size, max overflow, timeout, recycle, pre-ping |
| Dev defaults | `pool_size=5`, `max_overflow=5`, `pool_timeout=30`, `pool_recycle=1800`, `pre_ping=true` |
| Capacity | Approx. workers × (pool_size + max_overflow). Stay under PostgreSQL `max_connections` |
| Session | One session per request |
| UoW | Commit on success, rollback on any exception, close always |
| Repositories | add/query/flush only — no `commit()` |
| Errors | Translate unique → 409, connection failure → 503. Never return SQL text |

Physical DDL remains SQL 001–008. Alembic `db11_foundation_baseline` is stamp-only.

---

## 9. Authn / authz / tenant — FROZEN boundary, JWT DEFERRED

| Concept | Owner | This gate |
| --- | --- | --- |
| Authentication | Who is the caller? | `Principal` protocol + development stub |
| Authorization | What may they do? | Platform-admin stub: allow in development/test, 401 in staging/production |
| Tenant scope | Which org/facility/site? | Parse headers into context; do not trust them |

Do not implement login, refresh, password reset, or permission catalog writes here.

---

## 10. Pagination, idempotency, concurrency

| Topic | Status | Rule |
| --- | --- | --- |
| Offset pagination | **FROZEN** | `page` default 1, `page_size` default 20, max 100. Metadata: `page`, `page_size`, `total_records`, `total_pages` |
| Cursor pagination | **DEFERRED** | For later high-volume histories (API-00) |
| Idempotency | **DEFERRED** | Required later for payments, webhooks, membership purchase. No table invented now |
| Optimistic concurrency | **FROZEN** | `version_number` + `If-Match` on mutable records (already used by GMD PATCH) |
| Pessimistic locks | **DEFERRED** | Only where a future FR requires them |

---

## 11. Cache, storage, jobs, integrations — DEFERRED

| Capability | Long-term DR | This gate |
| --- | --- | --- |
| Redis cache | DR-008 Accepted | `CacheProvider` + `NoOpCacheProvider`. Do not put Redis on the request path |
| Object storage | DR-014 Accepted | `ObjectStorage` protocol only. No fake S3 |
| Celery workers | DR-009 Accepted | Documented boundary only. Outbox remains the future durable event path |
| Payment / SMS / email | IC / API-08 / API-10 | Adapter protocols later, with the feature |

Do not cache transactional writes. Future cache keys must include tenant scope and a TTL/invalidation rule.

---

## 12. Health — FROZEN

- `GET /api/v1/health/liveness` — process is running  
- `GET /api/v1/health/readiness` — process can serve; may check PostgreSQL  

Do not expose connection strings, credentials, or pool internals.

---

## 13. Testing and quality gates — FROZEN

| Layer | Use |
| --- | --- |
| Unit | envelopes, redaction, context, pagination, error mapping |
| API | HTTP contract via ASGI client; no fake business success |
| Model | ORM vs DB-11 invariants |
| Migration contract | `DIGITIZE_MIGRATION_TEST=1` on a dedicated database |
| Live catalog | `DIGITIZE_API_TEST=1` against local `digitize` |
| E2E | Later, feature by feature with Flutter |

Do not use SQLite to prove PostgreSQL constraints.

Commands (from `digitize-services`):

```text
poetry run ruff check app tests
poetry run mypy
poetry run pytest -q
```

CI already runs ruff, mypy, and pytest.

---

## 14. API registry — FROZEN inventory; live runtime only

222 numbered product endpoints from API-01–14 are recorded in
`API_CONTRACT_REGISTRY.md` and `app/api/contracts/catalog.py`.
They are the roadmap. Unimplemented product APIs are not registered as
FastAPI routes and must not return fake 200 payloads.

Live numbered handlers today: API-01-003, API-01-004, API-01-005.
Live extras: health, facility-types catalog, SaaS catalog reads.

Scaffold `GET/POST /api/v1/users` is not a product API. Retire it when API-03 starts.

Login, refresh, logout, and self-service password recovery are frozen in
`docs/architecture/AUTH_CONTRACT_FREEZE.md` and are not in the 222 count.
They are not registered as FastAPI routes until Authentication
implementation. Organization/Facility/Site list/get remain REQUIRES
DECISION.

---

## 15. Flutter

No Flutter change in this gate. When Authentication starts, Flutter must send `X-Correlation-ID` and may send `X-Request-ID` / `traceparent` (IC-01).
