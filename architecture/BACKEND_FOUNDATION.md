# DIGITIZE Backend Foundation Runtime

**Status:** FROZEN WITH DEFERRED ITEMS  
**Code:** `digitize-services`  
**Coding standard:** [BACKEND_CODING_STANDARDS.md](BACKEND_CODING_STANDARDS.md)  
**Companion freeze:** [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md)

This file records **runtime wiring**. Coding rules live in `BACKEND_CODING_STANDARDS.md`.

---

## 1. Request path

```text
HTTP
  CORSMiddleware                    # outermost (added last)
  SecurityHeadersMiddleware         # API-safe response headers
  RequestContextMiddleware          # correlation, request, W3C trace, contextvars
  AccessLogMiddleware               # received / completed / failed
  ExceptionHandlingMiddleware       # last-resort safe 500
  FastAPI router
    exception handlers (DigitizeError, validation, HTTP, unhandled)
    dependencies (Principal from access JWT, UoW session, pagination)
    thin route
    application service
    repository
    PostgreSQL
```

Starlette executes middleware in reverse add order. The list above is the **effective** outer-to-inner order after `create_app()`.

IDs are bound before the route and before exception handlers, so logs, envelopes, and 500s share the same `correlation_id`, `request_id`, and `trace_id`.

CORS: `allow_credentials=True` with an **explicit** origin list from `CORS_ALLOW_ORIGINS`. Never `*` with credentials. Staging/production refuse empty or wildcard origins.

---

## 2. Logging

`configure_logging()` installs a JSON formatter on the root logger. `get_logger("app.module")` is the only supported factory.

Access logs are emitted by `AccessLogMiddleware`, not by routers. Bodies, Authorization, cookies, passwords, hashes, JWTs, and peppers are never logged.

---

## 3. Unit of Work

`app/infrastructure/database/uow.py` plus `get_session()`:

- Open one `AsyncSession` for the request
- Yield it to the route/service/repository
- Commit if the handler returns
- Rollback on any exception
- Close with the session context manager

The service/use-case layer owns the transaction boundary. Catalog repositories flush only. The obsolete `users` repository still self-commits; it is scaffold, not the pattern.

---

## 4. Engine and pool

`init_engine()` creates at most one engine. Pool settings come from `Settings` (`DB_POOL_*`). Lifespan disposes the engine on shutdown.

Approximate connections = ASGI workers × (`DB_POOL_SIZE` + `DB_MAX_OVERFLOW`). Development defaults (5 + 5) assume a single local uvicorn worker.

CLI commands (Platform Admin bootstrap) call `init_engine` / `dispose_engine` around a single Unit of Work.

---

## 5. Health

| Path | Meaning |
| --- | --- |
| `/api/v1/health/liveness` | Process up (`status=alive`) |
| `/api/v1/health/readiness` | Engine initialized and `SELECT 1` succeeds (`status=ready` / `not_ready`) |

---

## 6. Platform Admin bootstrap

```bash
poetry run digitize bootstrap-platform-admin
```

Creates the first Platform Admin against `identity.user_account` (and the `PLATFORM_ADMIN` system role). It does not implement Authentication.

Production requires `--confirm-production`. Staging requires `--confirm-staging`. There is no `--force`.

Password hashing: Argon2id + `PASSWORD_PEPPER` via `app.core.security.passwords.hash_password`.
The same module implements `verify_password()` for Authentication.

---

## 7. Authentication

Frozen contract: [AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md).

| Path | Behavior |
| --- | --- |
| `POST /api/v1/auth/login` | Verify password; create `identity.user_session`; RS256 access JWT; `digitize_refresh` cookie |
| `POST /api/v1/auth/refresh` | Rotate hashed refresh token; replay of an old hash revokes the session |
| `POST /api/v1/auth/logout` | Revoke session; clear cookie (idempotent) |
| `POST /api/v1/auth/password-reset` | Non-enumerating 202; persist hashed recovery token with `delivery_status=PENDING` |
| `POST /api/v1/auth/password-reset/confirm` | Policy-check new password; consume token; revoke all sessions |

`get_principal` validates `Authorization: Bearer` RS256 JWTs. Development/test may use `AUTH_DEV_BYPASS` only when no Authorization header is present. Staging/production never use the stub.

Phase-1 rate limits are process-local (`ProcessRateLimiter`). They are not shared across application instances. Redis is not required for Phase 1.

Additive schema: `database/migrations/009_create_authentication_recovery.sql` (`identity.password_reset_request`, `user_session.previous_token_hash`, `user_session.last_activity_at`). Migrations 001–008 are unchanged.

---

## 8. What this foundation does not do

- MFA, SSO, or `/api/v1/auth/me`
- Redis, Celery, S3, Vault
- Product Organization / Facility / Site business implementations
  (contracts frozen; runtime routes are added per vertical;
  see API_CONTRACT_REGISTRY.md)
- Fake successful business responses
- API-01 business APIs other than the live catalog (API-01-003/004/005)
