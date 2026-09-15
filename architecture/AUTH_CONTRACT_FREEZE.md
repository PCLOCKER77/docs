# AUTHENTICATION CONTRACT — FROZEN

**Status:** IMPLEMENTED (Phase 1)  
**Phase:** Authentication Phase 1  
**Owner:** Security Architecture / API Architecture  
**Implementation:** COMPLETE — `digitize-services` `/api/v1/auth/*`  
**Related:** [API_CONTRACT_REGISTRY.md](API_CONTRACT_REGISTRY.md)

This is the **single authoritative Authentication HTTP and security contract**.

Older drafts (API-03 TBD login notes, UX-05 `POST /auth/login`,
`auth_api_proposal.md`, IC-02, BE-05, FR-06 related-API tables, Flutter
provisional DTOs) are superseded for Authentication Phase 1. They remain
useful as history. If they conflict with this file, **this file wins**.

The 222 numbered product APIs (API-01 through API-14) are unchanged.
Authentication is a dedicated `/api/v1/auth/*` collection **outside** the
222. Runtime routes are registered by the Authentication implementation
vertical.

---

## 1. Scope

In scope for Phase 1:

- Staff/user login with password
- Access JWT issuance
- Refresh-token rotation via HttpOnly cookie
- Logout / session revocation
- Self-service password recovery (request + confirm)
- Principal establishment for `require_authenticated`
- Abuse protection (rate limit + lockout) without account enumeration

Out of scope (deferred):

- MFA
- SSO
- API-01 Platform Admin business APIs
- API-03 staff identity APIs (except they remain the future consumer of Principal)
- Notification delivery implementation
- Flutter implementation of this contract
- Database migrations (documented as implementation dependencies only)

---

## 2. Endpoints

Authentication is **not** inserted into API-03 as API-03-013+.
Local collection IDs below are **not** part of the 222 inventory.
Promoting them to numbered API IDs later is a separate registry decision.

| Local ID | Method | Path | AuthN | Purpose |
| --- | --- | --- | --- | --- |
| AUTH-LOGIN-001 | POST | `/api/v1/auth/login` | Public | Verify credentials; start session |
| AUTH-REFRESH-001 | POST | `/api/v1/auth/refresh` | Refresh cookie | Rotate refresh; issue access JWT |
| AUTH-LOGOUT-001 | POST | `/api/v1/auth/logout` | Access JWT and/or refresh cookie | Revoke session |
| AUTH-PASSWORD-RESET-001 | POST | `/api/v1/auth/password-reset` | Public | Start self-service recovery |
| AUTH-PASSWORD-RESET-CONFIRM-001 | POST | `/api/v1/auth/password-reset/confirm` | Public (recovery token) | Complete recovery |

Keep separate (existing numbered API-03, unimplemented):

| API ID | Method | Path | Purpose |
| --- | --- | --- | --- |
| API-03-009 | POST | `/api/v1/identity/users/{user_id}/credential-reset` | **Administrative** staff credential reset |

API-03-009 is not UI-AUTH-002/003.

Do not create `/auth/login` (unversioned), MFA, or SSO paths.

---

## 3. Request schemas

JSON is snake_case. Field `login_identifier` is canonical. It maps to
`identity.user_account.login_identifier` (CITEXT). UI labels may say
username or email; the API field is not `username` or `email`.

### POST `/api/v1/auth/login`

```json
{
  "login_identifier": "string",
  "password": "string",
  "remember_me": false
}
```

| Field | Required | Notes |
| --- | --- | --- |
| `login_identifier` | Yes | Non-empty string |
| `password` | Yes | Non-empty string; never logged |
| `remember_me` | No | Default `false`. Extends refresh cookie lifetime (see §8) |

### POST `/api/v1/auth/refresh`

Empty JSON object `{}` or no body. The refresh credential is the cookie
`digitize_refresh` only. Do not accept refresh tokens in JSON or
`Authorization`.

### POST `/api/v1/auth/logout`

Empty body. Client should send `Authorization: Bearer <access_token>`
when it has one, and must send credentials so the refresh cookie is
included. Server revokes the session even if only the cookie is present.

### POST `/api/v1/auth/password-reset`

```json
{
  "login_identifier": "string"
}
```

### POST `/api/v1/auth/password-reset/confirm`

```json
{
  "reset_token": "string",
  "new_password": "string"
}
```

`reset_token` is the secret from the recovery notification link. It is
never returned by AUTH-PASSWORD-RESET-001.

---

## 4. Response schemas

All Authentication endpoints use the **API-00 envelope**.

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
    "code": "AUTHENTICATION_FAILED",
    "message": "string",
    "category": "Authentication",
    "details": []
  },
  "correlation_id": "uuid",
  "timestamp": "RFC3339"
}
```

### Login `data` (HTTP 200)

```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 900,
  "session_id": "uuid",
  "user": {
    "user_account_id": "uuid",
    "display_name": "string",
    "login_identifier": "string",
    "user_type": "TENANT_USER",
    "is_platform_admin": false,
    "organization_id": null,
    "roles": [],
    "permissions": []
  }
}
```

| Field | Meaning |
| --- | --- |
| `access_token` | RS256 JWT |
| `token_type` | Always `Bearer` |
| `expires_in` | Access TTL in seconds (900) |
| `session_id` | `identity.user_session.record_id` |
| `user.user_account_id` | `identity.user_account.record_id` |
| `user.roles` / `user.permissions` | Effective codes at login; may be empty until API-03 is live |
| `user.organization_id` | Account org or `null` for platform users |

HTTP 200 also **Set-Cookie** `digitize_refresh` (see §5).

### Refresh `data` (HTTP 200)

Same shape as login `data` (new access token, same `session_id`,
rotated cookie). User object may be omitted; clients must tolerate
either a full `user` object or `user` absent.

### Logout `data` (HTTP 200)

`{}` with message that the session was ended. Cookie cleared
(`Max-Age=0`).

### Password-reset request `data` (HTTP 202)

```json
{
  "accepted": true
}
```

Message is generic and identical whether or not the identifier exists.

### Password-reset confirm `data` (HTTP 200)

```json
{
  "password_updated": true
}
```

### Never return

- password or password hash
- refresh token in JSON
- recovery token
- Argon2 parameters, peppers, keys
- `metadata` internals, lockout counters, failed-attempt counts

---

## 5. Token transport

**One model. No dual JSON-refresh option.**

| Token | Transport |
| --- | --- |
| Access JWT | JSON `data.access_token`. Client sends `Authorization: Bearer <token>`. Keep in memory. |
| Refresh credential | `Set-Cookie` only. Never in JSON. |

Cookie:

| Attribute | Value |
| --- | --- |
| Name | `digitize_refresh` |
| HttpOnly | Yes |
| Secure | Yes in non-local environments |
| SameSite | `Lax` when API and UI share a site; `None` (with Secure) when they are cross-origin |
| Path | `/api/v1/auth` |
| Max-Age | See §8 (`remember_me` and session policy) |

CORS: `Allow-Credentials: true` and an **explicit** origin list.
`CORS_ALLOW_ORIGINS=*` is incompatible with credentialed cookies and
must not be used in Authentication implementation.

Flutter:

- **Web:** `withCredentials` / credentialed XHR. Dart must not parse a
  refresh token from JSON.
- **iOS/Android:** Dio cookie jar (or equivalent) at the HTTP client
  layer. Application Dart must not read or persist the refresh cookie
  value. Do not put `refreshToken` on DTOs.

This replaces the mock model that returned `refreshToken` in JSON and
stored it in secure storage.

API-03 prose that says tokens must never appear in response bodies is
**narrowed**: refresh and recovery secrets never appear in JSON; the
access JWT **does** appear in login/refresh `data` because the client
must send it as Bearer. That is the frozen exception.

---

## 6. Error contract

Use existing API-00 / `app/api/errors.py` families. Do not invent a
second envelope. Do not use HTTP 423 (it enumerates lockout).

Application `error.code` values follow the semantic convention
`<DOMAIN>_<SEMANTIC_ERROR>` in [BACKEND_CODING_STANDARDS.md](BACKEND_CODING_STANDARDS.md) §7.
Numbered codes such as `AUTH_AUTHENTICATION_001` are retired.

| Situation | HTTP | Code | External message (generic) |
| --- | --- | --- | --- |
| Malformed body / missing fields | 422 | `VALIDATION_FAILED` | Request validation failed. |
| Invalid credentials | 401 | `AUTHENTICATION_FAILED` | Authentication failed. |
| Account disabled, suspended, deactivated, or locked | 401 | `AUTHENTICATION_FAILED` | Authentication failed. |
| Missing, malformed, expired, or invalid access JWT | 401 | `AUTHENTICATION_FAILED` | Authentication is required. |
| Expired, invalid, reused, or revoked refresh | 401 | `AUTHENTICATION_FAILED` | Authentication is required. |
| Invalid, expired, or reused recovery token | 401 | `AUTHENTICATION_FAILED` | Authentication failed. |
| Rate limited (login, refresh, or recovery) | 429 | `RATE_LIMIT_EXCEEDED` | Too many attempts. Try again later. |
| Authenticated but not permitted | 403 | `AUTHORIZATION_DENIED` | You are not allowed to perform this action. |

**Enumeration rule:** login and password-reset **request** responses
must not reveal whether the identifier exists, whether the password was
wrong, or whether the account is locked. Timing should be comparable
(dummy hash verify when the account is missing).

Clients distinguish “go to login” from “validation error” via HTTP
status (401 vs 422), not via distinct credential-vs-lock codes.

Optional `Retry-After` on 429.

---

## 7. Security mechanics

### Password hashing

- Algorithm: **Argon2id**
- Per-record salt (library-managed)
- Application pepper from configuration/secret manager (`PASSWORD_PEPPER`)
- Never SHA-family, never bcrypt unless a later security standard
  supersedes this freeze
- Store only in `identity.user_account.password_hash`

### Access JWT

| Item | Frozen value |
| --- | --- |
| Algorithm | RS256 |
| Lifetime | 900 seconds (15 minutes) |
| Clock skew | 30 seconds |
| Issuer | Required config `JWT_ISSUER` (example: `digitize-services`) |
| Audience | Required config `JWT_AUDIENCE` (example: `digitize-api`) |

Production and staging must refuse to start if issuer, audience, or
signing keys are empty.

### Required JWT claims

| Claim | Meaning |
| --- | --- |
| `iss` | `JWT_ISSUER` |
| `aud` | `JWT_AUDIENCE` |
| `sub` | `user_account_id` |
| `sid` | `user_session.record_id` |
| `iat` | Issued-at |
| `exp` | Expiry |
| `typ` | `access` |
| `is_platform_admin` | boolean |

No refresh JWTs. Refresh material is an opaque high-entropy secret.

Do not put roles, permissions, passwords, or PII in the access JWT.

### Key storage

- Private signing key never committed
- Config: `JWT_PRIVATE_KEY` / `JWT_PUBLIC_KEY` (PEM) or
  `JWT_PRIVATE_KEY_PATH` / `JWT_PUBLIC_KEY_PATH`
- Local development may use a generated keypair under a gitignored path
- Rotation: accept current and one previous public key during a window

### Refresh token

| Item | Frozen value |
| --- | --- |
| Lifetime (remember_me=true) | 2_592_000 seconds (30 days) |
| Lifetime (remember_me=false) | `security.session_policy.max_session_minutes` (seed default 480 minutes) |
| Rotation | **Yes**, on every successful refresh |
| Storage | Hash only, in `identity.user_session.session_token_hash` |
| Replay | Reuse of a rotated hash revokes that session and rejects the call |

Idle timeout (`session_policy.idle_timeout_minutes`, default 30) is
enforced on **refresh**, not on every access-JWT request.

---

## 8. Session lifecycle

Physical session row: `identity.user_session`.

1. **Login success:** create `user_session` with status `ACTIVE`,
   store refresh hash, set cookie, return access JWT.
2. **Access request:** verify RS256 signature, `iss`, `aud`, `exp`
   (±30s), `typ=access`. **No session table lookup** on the hot path.
   Immediate access-token revocation is not required in Phase 1.
3. **Refresh:** lookup session by hash; require `ACTIVE` and not
   expired/idle; rotate secret; rewrite hash; Set-Cookie; new access JWT
   with same `sid`.
4. **Logout:** set `session_status` to a terminal revoked/ended value,
   set `ended_at`, clear cookie. Subsequent refresh fails.
5. **Password change / recovery confirm:** revoke all `ACTIVE` sessions
   for that `user_account_id`.
6. **Replay of an old refresh hash:** treat as theft; revoke the
   session; 401.

`session_id` in login JSON is `user_session.record_id`. Clients may
store it for display; it is not a credential.

---

## 9. Password recovery

Phase 1 includes both request and confirm. **Notification delivery is
not implemented in the Authentication vertical.**

### Request (`POST /api/v1/auth/password-reset`) → 202

- Always return the generic accepted envelope
- If the account exists and is eligible, generate a cryptographically
  secure token, store **only a hash**, expiry, one-time flag
- Invalidate outstanding unused recovery tokens for that account
- Enqueue a notification job / outbox record; **do not fake email/SMS
  success**
- If the notifier is not yet available, persist the hashed token and
  record `delivery_status=PENDING` (or equivalent). Implementation
  tests may read the token from a test-only seam; production APIs never
  return it

### Confirm (`POST /api/v1/auth/password-reset/confirm`) → 200

- Validate token, expiry, unused state
- Enforce `security.password_policy`
- Update `password_hash` (Argon2id)
- Consume the token
- Revoke all active sessions
- Generic 401 if the token is invalid/expired/reused (no enumeration of
  why beyond authentication failure)

Notification vertical (API-10) later delivers the message. This is an
implementation dependency, not a Phase-1 blocker for persisting hashed
tokens.

---

## 10. Rate limiting and lockout

No Redis requirement for Phase 1 (`CACHE_PROVIDER` may remain `noop`).

Minimum production-safe mechanism:

| Surface | Limit (starting point) | Storage |
| --- | --- | --- |
| Login failures | 5 per identifier+IP per 15 minutes | Process-local counter; persist lockout on the account |
| Recovery requests | 5 per identifier+IP per 60 minutes | Process-local |
| Refresh | 30 per session per minute | Process-local |

After the login failure threshold, set a temporary lockout on the
account (suggested 15 minutes). External clients still receive generic
401 `AUTHENTICATION_FAILED`.

`identity.user_account` has no `failed_login_count` / `lockout_until`
columns. Phase 1 implementation may:

- store counters in `metadata` JSONB, or
- add dedicated columns in the Authentication implementation migration
  (with the recovery table)

Do not build a distributed rate-limit platform in Phase 1. Multi-instance
deployments may tighten this later via Redis without changing the HTTP
contract.

---

## 11. MFA / SSO

- **MFA:** deferred from Authentication Phase 1. `user_account.mfa_enabled`
  exists; ignore except to reject login with a generic 401 if a future
  policy requires MFA before MFA APIs exist. Phase 1 does not add MFA
  verify endpoints.
- **SSO:** deferred. No `/auth/sso-init`.

---

## 12. Database authority

**Migrations 001–008 are authoritative.**

Use:

| Table | Role |
| --- | --- |
| `identity.user_account` | Credentials, `login_identifier`, `password_hash`, `account_status`, `user_type` |
| `identity.user_session` | Server session; `session_token_hash` holds the **refresh** hash |
| `identity.staff_profile` | Optional org/facility/site for the login payload |
| `identity.role` / `role_assignment` / `permission` | Optional roles/permissions at login |
| `security.password_policy` | New-password rules |
| `security.session_policy` | Idle / max session minutes |
| `security.authentication_event` | Login/refresh/logout/recovery audit rows |

Do **not** implement against divergent ORM-only tables:

- `identity.users`
- `identity.sessions`
- `identity.password_reset_requests`

Authentication implementation must realign SQLAlchemy models to the
migration tables (or replace those models). That is an implementation
task, not this freeze.

### Implementation-time schema dependency

No recovery table existed in 001–008. Authentication added additive
`database/migrations/009_create_authentication_recovery.sql` / Alembic
`009_authentication_recovery` for `identity.password_reset_request` plus
`identity.user_session.previous_token_hash` and `last_activity_at`.
Historical migrations 001–008 were not modified.

---

## 13. Principal contract

Authentication establishes identity. Authorization (later verticals)
consumes it.

Frozen `Principal` fields (extend today’s dataclass during
implementation; do not treat the development stub as production):

| Field | Source |
| --- | --- |
| `principal_id` | JWT `sub` |
| `session_id` | JWT `sid` (add this field) |
| `is_authenticated` | true after valid access JWT |
| `is_platform_admin` | JWT claim |
| `organization_id` / `facility_id` / `site_id` | Not taken from client headers as trusted identity. Headers remain untrusted `TenantContext` until API-02. Login JSON may include `organization_id`. |
| `roles` / `permissions` | Not required inside the access JWT. May be loaded later by authorization. |

`get_principal` in development/test currently returns a stub platform
admin. That stub is **not** the production mechanism. After
Authentication implementation:

- development may keep a documented test bypass behind explicit config
- staging/production must validate RS256 JWTs
- `require_authenticated` must use the real principal

---

## 14. Flutter alignment

Do **not** implement Flutter in this task. Required changes when
Authentication is implemented:

| Current mock | Frozen contract |
| --- | --- |
| `LoginRequestDto.email` | `login_identifier` (snake_case JSON) |
| `rememberMe` | `remember_me` |
| `LoginResponseDto` at JSON root | Unwrap API-00 `data` |
| `sessionId` / `accessToken` / `expiresInSeconds` | `session_id` / `access_token` / `expires_in` |
| `refreshToken` in JSON | **Remove.** Cookie only |
| `user.id` / `user.email` / camelCase | `user.user_account_id`, `user.login_identifier`, snake_case |
| Secure-storage of refresh token | Cookie jar / credentialed client; do not persist refresh plaintext |
| README “persist refresh_token in secure storage” | Superseded |
| `ApiAuthRemoteDataSource` deferred | Implement against `/api/v1/auth/*` |
| Error `invalid_credentials` / HTTP 423 | API-00 `AUTHENTICATION_FAILED` + 401/429 |
| `POST /auth/login` (UX-05) | `POST /api/v1/auth/login` |

Also: CORS/credentials, coalesced refresh on 401, logout must call
`POST /api/v1/auth/logout` with credentials so the cookie is sent.

---

## 15. Implementation dependencies

Before Authentication code is complete:

1. Align ORM to `identity.user_account` and `identity.user_session`
2. Alembic migration for recovery table (and optional lockout columns)
3. Config: `JWT_ISSUER`, `JWT_AUDIENCE`, key material, `PASSWORD_PEPPER`
4. Restrict CORS origins; enable credentials
5. Argon2id dependency
6. RS256 JWT library
7. Notification enqueue seam (no fake delivery)
8. Replace `get_principal` stub for staging/production
9. Tests: login/refresh/logout/recovery, replay, enumeration, 401 without token
10. Flutter DTO/interceptor migration (separate task)

---

## 16. Explicit exclusions

This freeze does **not**:

- Register FastAPI routes
- Issue or validate JWTs in code
- Hash passwords in code
- Create migrations or change ORM
- Add MFA/SSO endpoints
- Implement API-01 or other product verticals
- Add Authentication to the 222 numbered inventory
- Approve org/facility/site list/get (still REQUIRES DECISION)

---

## Conflicts reconciled

| Source | Conflict | Resolution |
| --- | --- | --- |
| UX-05 / proposal `POST /auth/login` | Unversioned path | `/api/v1/auth/login` |
| UX-05 `username`; Flutter `email`; DB `login_identifier` | Three identifiers | API field `login_identifier` |
| Proposal raw OAuth body vs API-00 | Envelope | API-00 |
| API-03 “never return tokens” vs Flutter tokens | Refresh vs access | Access JWT in JSON; refresh cookie only |
| Flutter JSON `refreshToken` vs HttpOnly cookie | Dual models | Cookie only |
| Proposal HTTP 423 lockout vs enumeration | Status | Generic 401 |
| FR-06 recovery paths | Match Phase 1 | Adopted under `/api/v1/auth/password-reset*` |
| FR-06 admin reset vs API-03-009 | Two resets | API-03-009 remains admin |
| ORM `identity.users` vs migration `user_account` | Schema | Migrations 001–008 win |
| Settings empty issuer/audience | Must not ship empty | Required config at implementation |
| session_policy 480 min vs 30-day refresh | `remember_me` | false → policy max; true → 30 days |
| FRS-BR Argon2id or bcrypt | Algorithm | Argon2id |

---

## Gate

**Authentication Phase 1 is implemented against this freeze.**

API-01 Platform Admin remains the next product vertical after the
Authentication security gate.
