# DIGITIZE Backend Coding Standards

**Status:** AUTHORITATIVE  
**Code:** `digitize-services`  
**Companion runtime wiring:** [BACKEND_FOUNDATION.md](BACKEND_FOUNDATION.md)  
**Architectural freeze:** [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md)  
**Authentication contract:** [AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md)

This is the repository-wide backend engineering standard. Implementers follow this
file. Runtime wiring details stay in `BACKEND_FOUNDATION.md`. Do not create a
second coding-standard document.

---

## 1. Invariants

1. Physical schema is `database/migrations/001`–`008` plus additive `009` for Authentication recovery. Alembic `db11_foundation_baseline` is the DB-11 stamp; `009_authentication_recovery` is the next revision.
2. API-00 envelope is the only HTTP response format for product APIs.
3. One configuration system, one logging system, one request context, one error model, one database session mechanism, one Principal type.
4. Request-path I/O is async. No synchronous database sessions or blocking HTTP clients on the request path.
5. Secrets never enter git, logs, API error bodies, or process listings.
6. Authentication HTTP endpoints live under `/api/v1/auth/*` and are outside the 222 numbered inventory.
7. Numbered product APIs (API-01–14, 222 endpoints) stay in `API_CONTRACT_REGISTRY.md`. Do not add Authentication to that count.

---

## 2. Package layout

```text
app/
├── api/                 # HTTP: envelopes, errors, deps, v1 routers, Pydantic API models
├── config/              # typed Settings (the only configuration system)
├── core/                # request context, Principal, clock, security primitives
├── infrastructure/      # logging, middleware, async engine, UoW, cache/storage protocols
├── modules/<capability>/  # routes, schemas, service, repository, models
└── cli/                 # operator commands (bootstrap)
```

Do not create empty packages to match a diagram. Add files when a vertical needs them.

Preferred module shape: `modules/<capability>/{routes,schemas,service,repository,models}`.

Divergent scaffold ORM under `modules/users/models` (`identity.users`, `identity.sessions`) is **not** the identity authority. New identity work uses migration tables (`identity.user_account`, `identity.user_session`, …).

### 2.1 Naming identities

Name a code symbol according to what it represents, not according to which API
collection, migration, ticket, phase, or implementation step introduced it.

These identities must stay distinct:

| Identity | Examples | Where it lives |
| --- | --- | --- |
| API inventory | `API-01`, `API-02-007` | Registry, catalog, contract tests |
| OpenAPI operation | `organizations_create` | Frozen OpenAPI `operationId` |
| Authorization | `organization.create`, `PLATFORM_PERMISSION_CODES` | `identity.constants`, RBAC |
| Application/domain | `OrganizationService`, `FacilityRepository` | `app/modules/*` |
| Error | `AUTHENTICATION_FAILED` | `app/api/error_codes.py` |
| Audit/event | `organization.created` | audit payloads / logs |
| Database | `tenant.organization` | schema / ORM |
| Migration | `011_api02_org_facility_site` | Alembic history |

Do not name permission registries, services, schemas, or error codes after API
collection numbers. See [NAMING_AUDIT.md](NAMING_AUDIT.md).

---

## 3. API layer

### 3.1 FastAPI conventions

| Topic | Rule |
| --- | --- |
| Versioning | All product HTTP under `/api/v1`. No unversioned `/auth` or `/users` product APIs. |
| Methods | GET read, POST create/action, PATCH partial update, PUT only if a contract requires full replace, DELETE only if contracted. |
| `operation_id` | Required, stable, snake_case, unique across the app. |
| Tags | Use `OPENAPI_TAGS` in `app/main.py`. |
| Routes | Thin: parse input, inject deps, call one service, return envelope. |
| Request body | Explicit Pydantic request model. No undocumented `dict`. |
| Response body | API-00 envelope. Payload models are explicit Pydantic response models. |
| Errors | Typed `DigitizeError` subclasses. Do not `raise HTTPException` in services or repositories. |
| AuthN dep | `require_authenticated` (Bearer access JWT). |
| AuthZ dep | `require_platform_admin` and future permission/scope deps. Do not trust client tenant headers. |

### 3.2 Pagination, filtering, sorting

| Topic | Rule |
| --- | --- |
| Offset pagination | `page` default 1, `page_size` default 20, max 100. Metadata: `page`, `page_size`, `total_records`, `total_pages`. |
| Filtering | Explicit query params validated against approved vocabularies. |
| Sorting | Explicit allow-list. Default documented per endpoint. |
| Cursor pagination | Deferred. |
| Search | Existing catalog search: 2–100 characters. |

### 3.3 Idempotency and concurrency

| Topic | Rule |
| --- | --- |
| Idempotency | Deferred until payments/webhooks/membership purchase. No invented idempotency table. |
| Optimistic concurrency | `version_number` + `If-Match` on mutable records. Missing `If-Match` → 428. Stale → 412. |

### 3.4 Layering

```text
FastAPI route
    → application service / use case   (business rules, transaction boundary)
        → repository                   (SQL only)
            → AsyncSession / asyncpg / PostgreSQL 17
```

Routes may depend on `AsyncSession` via `get_session()`. The service owns the use case. The Unit of Work commits after the route returns successfully.

Repositories:

- query, insert, update, delete, `flush` when required;
- never `commit()` / `rollback()` unless a documented exception exists (legacy `users` scaffold only);
- never return FastAPI responses;
- never raise `HTTPException` or know HTTP status codes.

---

## 4. Async-first rule

All request-path application I/O is asynchronous:

```python
async def route(...)
async def service(...)
async def repository(...)
await session.execute(...)
await session.commit(...)   # Unit of Work / service boundary only
await session.refresh(...)
```

Do not introduce:

- `sqlalchemy.orm.Session` / `sessionmaker` / `create_engine` in application code;
- `requests` or other blocking HTTP SDKs on the request path;
- `time.sleep` in async handlers (use `asyncio.sleep`);
- `httpx.Client` on the request path (`httpx.AsyncClient` only).

The unused `app/infrastructure/external/http_client.py` synchronous client must not be wired into routes. Replace it with an async client if a vertical needs outbound HTTP.

**CPU-bound exception:** password hashing (Argon2id) and JWT signing/verification are CPU-bound. They may run in a worker thread (`asyncio.to_thread`) if they block the event loop under load. Bootstrap may hash in-process. Do not silently add a process pool.

CLI commands may drive async code with `asyncio.run`.

---

## 5. Pydantic standard

Pydantic v2 is the only validation framework.

Base class for new API schemas: `app.api.schemas.APIModel`.

```python
class ExampleRequest(APIModel):
    login_identifier: str

class ExampleResponse(APIModel):
    record_id: UUID
```

| Topic | Rule |
| --- | --- |
| `ConfigDict` | `extra="forbid"` for request bodies; `from_attributes=True` for ORM-out models; `populate_by_name=True` when aliases exist. |
| Field names | snake_case JSON. No camelCase in new APIs. |
| Aliases | Use only to map ORM column names (example: `metadata_payload` → `metadata`). |
| UUID | `uuid.UUID` in schemas and domain code. Do not stringify identifiers internally. |
| datetime | Timezone-aware UTC. Persist `TIMESTAMPTZ`. Serialize RFC3339 with `Z`. |
| Enum | Explicit `str` Enum or approved vocabulary sets. Reject unknown values with 422. |
| Optional vs nullable | `T \| None = None` means omitted-or-null. Required-but-nullable is `T \| None` without a default. |
| Nested data | Explicit models, not untyped `dict`, unless the physical column is JSONB `metadata`. |
| Validation errors | FastAPI `RequestValidationError` → HTTP 422 `VALIDATION_FAILED`. |

Existing catalog schemas remain valid. New endpoints must use `APIModel` (or an equivalent explicit `ConfigDict`).

---

## 6. API-00 envelope

Success:

```json
{
  "success": true,
  "data": {},
  "message": "string",
  "metadata": {},
  "correlation_id": "uuid",
  "timestamp": "RFC3339"
}
```

Error:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "safe client message",
    "category": "Validation",
    "details": []
  },
  "metadata": { "request_id": "...", "trace_id": "..." },
  "correlation_id": "uuid",
  "timestamp": "RFC3339"
}
```

`request_id` and `trace_id` live in `metadata` and response headers. Do not add `traceId`.

Health probes may return operational JSON `{ "status": ... }` without the business envelope.

| Situation | HTTP | Code | Category |
| --- | --- | --- | --- |
| Success read/update | 200 | — | — |
| Success create | 201 | — | — |
| Accepted async | 202 | — | — |
| Malformed / validation | 422 | `VALIDATION_FAILED` | Validation |
| Authentication | 401 | `AUTHENTICATION_FAILED` | Authentication |
| Authorization | 403 | `AUTHORIZATION_DENIED` | Authorization |
| Not found | 404 | `RESOURCE_NOT_FOUND` or a domain code such as `PLATFORM_NOT_FOUND` | NotFound |
| Conflict | 409 | `RESOURCE_CONFLICT` or a domain code such as `PLATFORM_ALREADY_EXISTS` | Conflict |
| Missing / stale `If-Match` | 428 / 412 | `CONCURRENCY_CONFLICT` | Concurrency |
| Rate limit | 429 | `RATE_LIMIT_EXCEEDED` | RateLimit |
| Unhandled | 500 | `INTERNAL_ERROR` | System |
| Upstream failure | 502 | `EXTERNAL_SERVICE_ERROR` | System |
| Dependency down | 503 | `SERVICE_UNAVAILABLE` or `DATABASE_ERROR` | System |

Never return SQLSTATE, stack traces, connection strings, passwords, hashes, JWTs, peppers, or internal paths.

---

## 7. Exception ownership and error-code architecture

This section is the repository-wide freeze for exceptions, error codes, middleware, logging, and layer ownership. Live constants live in `app/api/error_codes.py`. Exception classes live in `app/api/errors.py`. There is no second exception hierarchy and no per-module error framework.

### 7.1 HTTP status vs application error code

These are independent:

```text
HTTP status:           404
Application error code: FACILITY_NOT_FOUND
Message:               Facility was not found.
```

Never encode HTTP status into `error.code`. Do not use `404`, `FACILITY_404`, or `NOT_FOUND_404` as application codes.

### 7.2 Semantic error-code convention

Pattern: `<DOMAIN>_<SEMANTIC_ERROR>` (uppercase snake case).

Do **not** use `<DOMAIN>_<CATEGORY>_<NNN>`. Numeric suffixes are not part of the contract.

Examples: `AUTHENTICATION_FAILED`, `AUTHORIZATION_DENIED`, `ORGANIZATION_NOT_FOUND`, `FACILITY_ALREADY_EXISTS`, `RATE_LIMIT_EXCEEDED`, `INTERNAL_ERROR`.

The code describes a stable application condition. Frontend, mobile, integrations, tests, and support tooling may depend on it. Changing a code is an intentional contract change.

### 7.3 API identifiers are independent

```text
API identifier:         API-02-005
OpenAPI operation ID:   facility_get
Application error code: FACILITY_NOT_FOUND
```

Do not derive error codes from API numbers (`API_02_FACILITY_NOT_FOUND` is forbidden).

### 7.4 Do not over-create codes

Prefer `FACILITY_INVALID` over per-field codes such as `FACILITY_NAME_INVALID`. Pydantic `error.details` carries field-level validation. Add a new code only when a vertical has a distinct client-visible condition.

Authoritative registered codes: `app/api/error_codes.py`. Modules must not invent string literals outside that file.

### 7.5 Domain naming

Use Digitize business domains (`AUTHENTICATION`, `AUTHORIZATION`, `PLATFORM`, `ORGANIZATION`, `FACILITY`, `IDENTITY`, `MEMBERSHIP`, `BILLING`, `PAYMENT`, `SUBSCRIPTION`, `REPORTING`, `SYSTEM`, …). Do not create a domain merely because an API registry section exists.

System/technical failures use:

- `INTERNAL_ERROR` (HTTP 500; programming bugs)
- `DATABASE_ERROR` (HTTP 503; database unavailable)
- `SERVICE_UNAVAILABLE` (HTTP 503)
- `EXTERNAL_SERVICE_ERROR` (HTTP 502)

Do not use `PLATFORM_INTERNAL_ERROR` or `API_500_ERROR` for programming failures.

### 7.6 Exception hierarchy

```text
DigitizeError
├── AuthenticationFailed          401 AUTHENTICATION_FAILED
├── AuthorizationFailed           403 AUTHORIZATION_DENIED
├── ValidationFailed              422 VALIDATION_FAILED
├── RateLimitError                429 RATE_LIMIT_EXCEEDED
├── NotFoundError                 404 RESOURCE_NOT_FOUND (override per domain)
├── ConflictError                 409 RESOURCE_CONFLICT (override per domain)
├── BusinessRuleError             422 BUSINESS_RULE_VIOLATED
├── InvalidStateError             409 INVALID_STATE
├── ConcurrencyError              412/428 CONCURRENCY_CONFLICT
├── InfrastructureError           500 INTERNAL_ERROR
├── ExternalServiceError          502 EXTERNAL_SERVICE_ERROR
└── ServiceUnavailableError       503 SERVICE_UNAVAILABLE
    └── DatabaseUnavailable       503 DATABASE_ERROR
```

`ResourceNotFound` and `InternalError` remain aliases. Authentication and every future domain use this hierarchy.

### 7.7 HTTP mapping (global FastAPI handler)

`register_exception_handlers` in `app/api/v1/envelopes.py` maps known `DigitizeError` instances to API-00. Routes do not construct error envelopes.

| Exception | HTTP | Default code |
| --- | --- | --- |
| `AuthenticationFailed` | 401 | `AUTHENTICATION_FAILED` |
| `AuthorizationFailed` | 403 | `AUTHORIZATION_DENIED` |
| `ValidationFailed` | 422 | `VALIDATION_FAILED` |
| `NotFoundError` | 404 | `RESOURCE_NOT_FOUND` |
| `ConflictError` | 409 | `RESOURCE_CONFLICT` |
| `RateLimitError` | 429 | `RATE_LIMIT_EXCEEDED` |
| unexpected `Exception` | 500 | `INTERNAL_ERROR` |

Unexpected failures produce one guarded diagnostic traceback (`log_unexpected_exception`) and a safe 500 body. No stack traces, SQL, or secrets in the response.

`StarletteHTTPException` is mapped only for framework failures (unmatched routes). Application modules must not raise `HTTPException`.

### 7.8 Middleware ownership

Starlette runs middleware in reverse add order. Effective outer → inner after `create_app()`:

1. `CORSMiddleware`
2. `SecurityHeadersMiddleware`
3. `RequestContextMiddleware` — request ID, correlation ID, W3C trace context, contextvars setup/cleanup. No business logic.
4. `AccessLogMiddleware` — `request received` / `request completed` / `request failed`. Method, path, status, duration, request/correlation/trace IDs. No bodies, cookies, Authorization, tokens, or secrets. Expected application errors do not emit tracebacks.
5. `ExceptionHandlingMiddleware` — last-resort unexpected-exception safety net. Delegates to `unexpected_error_response` so traceback logging cannot duplicate.
6. FastAPI router + exception handlers + dependencies

Do not add a second request-context or logging system.

### 7.9 Route / service / repository / transaction

```text
HTTP Request
    → RequestContextMiddleware
    → AccessLogMiddleware
    → Route (parse, deps, Principal, HTTP cookies/headers)
    → Service (rules, orchestration, transaction boundary)
    → Repository (query / add / update / delete / flush)
    → Service / UoW commit
    → Success envelope
    or DigitizeError → central handler → HTTP + API-00 error envelope
```

Routes must not implement business rules, query the database, commit, catch broad exceptions, translate `DigitizeError` into HTTP, or raise `HTTPException` for application failures. Refresh-cookie cleanup may register a response mutator and **re-raise** the original `AuthenticationFailed`. Do not generalize that pattern.

Services raise `DigitizeError` subclasses. They do not raise `HTTPException`, build envelopes, or manipulate cookies.

Repositories do not commit, do not import FastAPI, and do not build envelopes. A known unique violation may become `ConflictError`. Unknown database failures propagate.

### 7.10 Logging categories

1. **Access** — HTTP transaction (`app.access`). No traceback for expected 4xx.
2. **Application / security events** — meaningful domain events (`auth.login`, `auth.login.failed`, future `organization.created`). Not every method call.
3. **Diagnostic** — unexpected failures only. `logger.exception` is restricted to `log_unexpected_exception` and the CLI bootstrap diagnostic boundary.

One unexpected failure produces exactly one traceback per request (request-scoped guard).

### 7.11 Secret protection

Never log or return: passwords, hashes, `PASSWORD_PEPPER`, access/refresh/reset tokens, JWTs, private keys, cookie values, Authorization headers, client secrets, database passwords.

Central redaction (`redact_text` / `redact_mapping`) covers structured fields, exception text, and traceback text. Do not rely on developers remembering.

### 7.12 Request / correlation / trace IDs

Preserve `app.core.request_context`. Accept valid incoming IDs; generate when missing/invalid; echo per the API-00 contract; preserve W3C `traceparent` (valid trace_id, new span_id); clear context after the request. Do not create another implementation.

Historical collection documents (API-01–14, API-19) may still list `{DOMAIN}_{CATEGORY}_{NNN}` identifiers. Those are **not** live application error codes. Implementation and tests use `app/api/error_codes.py` only.

---

## 8. Logging, trace, correlation

Factory: `get_logger("app.module")`. Formatter: JSON to stdout.

Required fields when available:

`timestamp`, `level`, `severity`, `service`, `environment`, `module`, `trace_id`, `correlation_id`, `request_id`, `span_id`, `method`/`http.method`, `path`/`http.path`, `operation_id`, `status_code`/`http.status_code`, `duration_ms`

Also when known: `user_id` / `principal_id`, `organization_id`, `facility_id`, `site_id`, `error_code`.

Access log events: `request received`, `request completed`, `request failed`. No request bodies. No Authorization, Cookie, or Set-Cookie headers.

Redact keys matching password, token, secret, authorization, cookie, pepper, private key, jwt, credential, hash, refresh, api key.

IDs:

| ID | Header | Rule |
| --- | --- | --- |
| Correlation | `X-Correlation-ID` | Accept if 1–128 chars of `[A-Za-z0-9._-]`. Otherwise generate a UUID. Echo in envelope and header. |
| Request | `X-Request-ID` | Same validation. One HTTP attempt. |
| Trace | W3C `traceparent` | Preserve valid trace_id; always create a new span_id. |

Context is `contextvars` (`app.core.request_context`). Do not pass IDs through every signature. Do not use process-global mutable request state.

---

## 9. Middleware order

Starlette runs middleware in reverse add order. Effective outer → inner after `create_app()`:

1. `CORSMiddleware` — credentials allowed; explicit origin list; never `*` with credentials
2. `SecurityHeadersMiddleware` — API-safe headers
3. `RequestContextMiddleware` — bind IDs before anything else logs or handles errors
4. `AccessLogMiddleware` — received / completed / failed
5. `ExceptionHandlingMiddleware` — last-resort 500 envelope
6. FastAPI router + exception handlers + dependencies

Do not add middleware that logs bodies or that duplicates request context.

---

## 10. Configuration and secrets

One system: `app.config.settings.Settings` (pydantic-settings).

Precedence: process environment → `digitize-services/.env` (gitignored) → non-secret code defaults.

Environments: `development`, `test`, `staging`, `production`.

Categories: application, database pool, CORS, logging, JWT keys, password pepper, process-local rate limits, cache/storage (deferred).

Staging/production fail fast when:

- database credentials are missing;
- `JWT_ISSUER`, `JWT_AUDIENCE`, and signing key material are missing;
- `PASSWORD_PEPPER` is missing or too short;
- CORS is `*` or empty while credentials are enabled.

Development defaults must never be used as production credentials.

Never commit `.env`, PEM private keys, peppers, or generated secrets. `.gitignore` excludes `.env`, `.env.*` (except `*.example`), `*.pem`, and `*.key`.

Production secret manager / Vault remains deferred (DR-011). Runtime injection is environment variables.

JWT issuance and validation are implemented in `app/core/security/jwt.py` (RS256).

---

## 11. Security headers

Applied to all HTTP responses:

| Header | Value | Reason |
| --- | --- | --- |
| `X-Content-Type-Options` | `nosniff` | Block MIME sniffing |
| `X-Frame-Options` | `DENY` | API is not framed |
| `Referrer-Policy` | `no-referrer` | No referrer leakage |
| `Content-Security-Policy` | `default-src 'none'; frame-ancestors 'none'; base-uri 'none'` | JSON API is not an HTML app |
| `X-Permitted-Cross-Domain-Policies` | `none` | No Adobe cross-domain policy |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | No ambient browser features |

Not set here:

- `Strict-Transport-Security` — belongs at the TLS terminator
- Global `Cache-Control: no-store` — would harm public catalog GETs. Authentication responses set `Cache-Control: no-store`
- CORS headers — owned by `CORSMiddleware`

These headers do not conflict with Flutter Web calling the API as a separate origin.

---

## 12. Database and transactions

```text
FastAPI → request-scoped AsyncSession → async_sessionmaker → AsyncEngine (asyncpg) → PostgreSQL 17
```

- One engine per process (`init_engine` / `dispose_engine`).
- One `AsyncSession` per request (`get_session`).
- Unit of Work: commit on success, rollback on any exception, close always.
- Unique violations → `ConflictError` (409). Connection failure → `DatabaseUnavailable` (503).
- Repositories receive `AsyncSession` only.

**Transaction ownership:** the service / use-case (or the request UoW around the route) commits once after all repositories finish. Multi-repository operations share the same session and one commit.

```text
Service
  → Repository A (flush)
  → Repository B (flush)
  → Repository C (flush)
  → commit once
```

CLI commands (bootstrap) open their own session, use the same UoW rules, and dispose the engine on exit.

---

## 13. ORM, UUID, datetime

| Topic | Rule |
| --- | --- |
| Tables | Schema-qualified (`identity.user_account`). |
| Primary key | `record_id UUID` with `gen_random_uuid()` where the physical schema says so. |
| Timestamps | `TIMESTAMPTZ`. Application writes `utc_now()` from `app.core.clock`. Never `datetime.now()` without timezone. |
| JSONB | Map ORM attribute `metadata_payload` to column `metadata` when needed. |
| Enums | Physical schema uses `VARCHAR` vocabularies. Do not invent PostgreSQL ENUM types in this gate. |
| Optimistic concurrency | `version_number INTEGER`. |
| Relationships | Add when a vertical needs them; do not rewrite the entire ORM now. |

Internal layers keep `UUID` objects. Pydantic exposes `UUID`.

---

## 14. Dependency injection

Use FastAPI `Depends` for request-scoped resources:

- `get_session` / `get_platform_session`
- `get_principal` / `require_authenticated` / `require_platform_admin`
- `get_tenant_context` (untrusted until API-02)

Do not store mutable request state on process-level singletons. `AppContainer` holds the engine and settings only.

Authentication resolves `Principal` from a validated RS256 access JWT (`sub`, `sid`, `is_platform_admin`). Development/test may keep `AUTH_DEV_BYPASS` when no Authorization header is sent. Staging/production never use the stub.

---

## 15. Testing

Reuse pytest + pytest-asyncio (`asyncio_mode = auto`). Do not add a second async test framework.

Every implemented vertical should eventually cover:

- Route: success, validation, authentication, authorization, error envelope
- Service: business rules and edge cases
- Repository/integration: constraints and transactions against PostgreSQL (not SQLite)
- Security: privilege escalation, invalid credentials, session behavior
- Concurrency: idempotency / `If-Match` where contracted

Foundation tests must prove:

- trace and correlation IDs on every HTTP request;
- correlation ID in the API-00 envelope;
- structured log fields without asserting entire JSON strings;
- secrets redacted from logs;
- known `DigitizeError` → correct status/code/message/correlation_id;
- unexpected exception → 500 without stack traces in the body;
- production configuration fail-fast;
- Platform Admin bootstrap first-run / second-run / password policy / rollback / production safety.

Do not use synchronous `Session` fixtures to test async repositories.

---

## 16. Platform Admin bootstrap

Command:

```bash
poetry run digitize bootstrap-platform-admin
```

Creates the first `identity.user_account` with `user_type='PLATFORM_ADMIN'`, `organization_id` NULL, Argon2id password hash with configured pepper, and the `PLATFORM_ADMIN` system role assignment.

Does not itself issue JWTs or register `/api/v1/auth/*`; Authentication consumes the created account.

Production requires `--confirm-production`. There is no `--force` that skips security validation.

See [BACKEND_FOUNDATION.md](BACKEND_FOUNDATION.md) § Bootstrap.

---

## 17. What this standard does not do

- Implement API-01 business APIs beyond the existing live catalog (API-01-003/004/005)
- Add numbered APIs to the 222
- Introduce Redis, Celery, S3, or Vault on the request path
- Implement MFA or SSO
