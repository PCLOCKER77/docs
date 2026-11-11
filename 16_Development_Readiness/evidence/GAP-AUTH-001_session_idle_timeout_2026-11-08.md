# GAP-AUTH-001 — Authentication idle-timeout verification

**Date:** 2026-11-08  
**Authority:** `docs/architecture/AUTH_CONTRACT_FREEZE.md` §7–8  

## Established behavior (code + contract)

| Topic | Behavior |
| --- | --- |
| Idle timeout enforcement | **On refresh only**, not on every Bearer access request |
| Inactivity timestamp | `identity.user_session.last_activity_at` |
| Idle deadline | `last_activity_at + session_policy.idle_timeout_seconds` (default 30 min) |
| Absolute expiry | `user_session.expires_at` (remember-me vs `max_session_minutes`) |
| Refresh rejection | Non-ACTIVE, `expires_at <= now`, or idle deadline `<= now` → revoke session, 401 |
| Access JWT | RS256 validate only; **no** `user_session` lookup on hot path |
| Activity bump | Successful refresh sets `last_activity_at = now` and rotates refresh hash |
| Account eligibility | Refresh re-loads user; ineligible → revoke + 401 |
| Logout | Marks session REVOKED; refresh fails; access JWT may still work until `exp` (Phase 1) |
| Replay | Previous refresh hash → revoke + 401 |

## Code paths inspected

- `app/api/deps.py` — `get_principal`, `require_authenticated`, `load_authorized_principal`
- `app/modules/authentication/service.py` — `login`, `refresh`, `logout`
- `app/modules/authentication/helpers.py` — `session_refresh_is_blocked`
- `app/modules/authentication/repository.py` — `load_session_policy`, session FOR UPDATE
- `app/core/security/jwt.py` — access JWT claims (`sid`, `exp`)

## Tests executed

| Suite | Command | Result |
| --- | --- | --- |
| Unit boundaries | `poetry run pytest tests/authentication/test_session_refresh_policy.py tests/authentication/test_principal.py tests/authentication/test_helpers.py -q` | **18 passed** |
| PG IV (local `digitize`) | `DIGITIZE_AUTH_SESSION_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize poetry run pytest tests/authentication/test_auth_session_digitize_postgres.py -q` | **6 passed** |

## Production change

Refactor only: `session_refresh_is_blocked()` extracted in helpers; `refresh()` calls shared gate (no policy change).

## GAP status

**Verified — existing behavior matches frozen contract** (no authentication policy change required).
