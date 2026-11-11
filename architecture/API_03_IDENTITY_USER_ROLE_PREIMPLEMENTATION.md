# API-03 Identity / User / Role — Pre-Implementation Gate

**Status:** PRE-IMPLEMENTATION GATE PASS  
**Date:** 2026-09-12  
**Scope:** Contract, database, ORM, authorization, authentication-boundary, and architecture reconciliation only.  
**Does not implement API-03.**

PASS means API-03 can be implemented without architectural redesign. Remaining work is first-slice implementation (permission seed, `staff_profile` ORM, identity HTTP routes, DTOs), classified **P2**.

Authoritative sources for this gate, in descending order when they conflict:

1. `docs/architecture/API_CONTRACT_REGISTRY.md` and `app/api/contracts/catalog.py` / `operations.py` (numbered identity, paths, counts, operation IDs, HTTP status, If-Match, pagination)
2. `database/migrations/001`–`011` (physical schema; history frozen)
3. `docs/architecture/AUTH_CONTRACT_FREEZE.md` (authentication, sessions, recovery, Principal, 401 family)
4. `docs/architecture/BACKEND_CODING_STANDARDS.md` and `NAMING_AUDIT.md` (layering, API-00, UoW, semantic authorization names)
5. `docs/07_API_Collections/API-03_Identity_User_Role_Collection.md` (verbose request/response/audit prose; **not** path or error-code authority)
6. `docs/04_Functional_Requirements/FR-06_User_Role_Management.md` (business intent)

The design-draft OpenAPI file `docs/07_API_Collections/openapi/API-03_Identity_User_Role_OpenAPI.yaml` is **not** authoritative. It covers 3 of 12 paths, uses non-canonical `operationId` values, and contradicts the frozen registry (for example API-03-003 as HTTP 200).

Authentication Phase 1 is implemented. `/api/v1/auth/*` is live supporting infrastructure **outside** the 222. API-03 consumes `Principal`; it does not redefine login, refresh, logout, or self-service recovery.

---

## 1. Executive summary

API-03 is **organization-scoped staff identity administration**:

- create staff account + staff profile
- update staff profile
- assign roles
- assign facility / site access scopes
- configure **role** permissions (not per-user permission-override tables)
- activate / suspend / deactivate staff
- administrative credential reset
- staff activity and staff directory

API-03 is **not**:

- Authentication (`/api/v1/auth/*` — already implemented)
- Platform Administrator provisioning (CLI bootstrap)
- Customer identity (API-04)
- Organization / facility / site resource mutation (API-02)
- Platform security-policy mutation (API-01)
- Audit search APIs (API-13)
- MFA / SSO
- Create-role, list-role, get-user, unassign-role, or per-staff permission-override HTTP APIs (not in the 12)

The physical identity schema **already exists** in migration `003`. API-03 does not need new identity tables. It needs an additive **permission seed** (and PLATFORM_ADMIN bindings), ORM mapping for `identity.staff_profile`, and HTTP/service/repository implementation on the existing authorization stack.

Live numbered handlers today: **none** of the 12. Do not add 501 skeletons. Register routes only when implemented.

### Frozen implementation decisions (no longer open)

These were previously implicit conflicts between the registry, collection prose, FR-06, and draft OpenAPI. They are now binding for the implementation task.

| Topic | Frozen rule |
| --- | --- |
| Paths / methods / counts | Registry + `NUMBERED_OPERATIONS`. Exactly 12. Do not invent `/api/v1/staff/...` or `/api/v1/users/{id}` product routes. |
| Operation IDs | `make_operation_id()` in `catalog.py`. Draft YAML IDs are void. |
| HTTP success | Registry/catalog: 201 for 001/003/004/005; 200 for the rest, including API-03-009. Collection `202` for 009 is superseded. |
| Error codes | `app/api/error_codes.py` only. Collection `IDENTITY_*_001` codes are void. |
| 403 / 401 / 404 | `AUTHORIZATION_DENIED` / `AUTHENTICATION_FAILED` / `RESOURCE_NOT_FOUND` (generic message). Cross-tenant objects → 404, not 403. |
| Tenant headers | Untrusted. `X-Organization-ID` / `X-Facility-ID` / `X-Site-ID` never grant access. Collection “headers required” is superseded. |
| Authorization loader | `load_authorized_principal` + `require_permission(..., loader=...)`. JWT permission lists are not the source of truth. |
| Permission **values** | One domain registry `IDENTITY_PERMISSION_CODES` (see §9). Not `API03_PERMISSION_CODES`. |
| If-Match | Registry: PATCH only (002, 006). Collection If-Match on lifecycle POSTs is superseded. |
| Idempotency | Registry: POST `TBD` → **NOT_REQUIRED**. Uniqueness constraints provide retry safety. No idempotency table. |
| Pagination | OFFSET for 011 and 012. Default page size 20, max 100. Collection cursor option is deferred. |
| HTTP module | `app/modules/identity/` (package already exists). Catalog `_COLLECTION_ROUTE_OWNER["API-03"] = "users"` is stale metadata; update it when routes are registered. Do not implement API-03 on the `/api/v1/users` scaffold. |
| `staff_profile` | Table exists in `003`. Add ORM at implementation. No schema migration for the table. |
| Scaffold `/api/v1/users` | Not API-03. Do not expand. Retire during API-03 implementation. |
| Admin vs self-service reset | API-03-009 is administrative. AUTH `/password-reset*` is self-service. Both may write `identity.password_reset_request`. Neither returns tokens/passwords. |
| Platform Admin accounts | API-03 does not create, activate, suspend, deactivate, or reset `user_type=PLATFORM_ADMIN` / `organization_id IS NULL` accounts. |
| Role HTTP surface | No create-role numbered API. Implementation may upsert **org-scoped standard roles** as an internal helper (not a new inventory path). |
| Per-staff permission overrides | FR-USR-006 `/api/v1/staff/{id}/permissions` is **not** in the 12. API-03-006 patches `identity.role_permission` for a role. Do not invent `staff_permission` tables. |
| Login eligibility | Unchanged: Authentication allows login only when `account_status == ACTIVE` and `deleted_at IS NULL`. |

---

## 2. Exact API-03 inventory

Permission codes below are the frozen API-03 seed values for `OPERATION_AUTHORIZATION` / `identity.permission`. They are **not** live in `OPERATION_AUTHORIZATION` today (`TBD`). Implementation adds them; it does not invent API-numbered registry names.

Operation IDs are those produced by `make_operation_id()`.

| API ID | Method | Path | Operation ID | Success | Scope | Page | Idem | Concurrency | AuthZ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-03-001 | POST | `/api/v1/identity/staff-accounts` | `identity_staff_accounts_create` | 201 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.create` |
| API-03-002 | PATCH | `/api/v1/identity/staff-profiles/{staff_profile_id}` | `identity_staff_profiles_staff_profile_id_update` | 200 | ORGANIZATION | NA | NOT_REQUIRED | IF_MATCH | `staff.update` |
| API-03-003 | POST | `/api/v1/identity/role-assignments` | `identity_role_assignments_create` | 201 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.role.assign` |
| API-03-004 | POST | `/api/v1/identity/access-scopes/facility` | `identity_access_scopes_facility_create` | 201 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.access.facility.assign` |
| API-03-005 | POST | `/api/v1/identity/access-scopes/site` | `identity_access_scopes_site_create` | 201 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.access.site.assign` |
| API-03-006 | PATCH | `/api/v1/identity/roles/{role_id}/permissions` | `identity_roles_role_id_permissions_update` | 200 | ORGANIZATION | NA | NOT_REQUIRED | IF_MATCH | `role.permissions.update` |
| API-03-007 | POST | `/api/v1/identity/users/{user_id}/activate` | `identity_users_user_id_activate` | 200 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.activate` |
| API-03-008 | POST | `/api/v1/identity/users/{user_id}/suspend` | `identity_users_user_id_suspend` | 200 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.suspend` |
| API-03-009 | POST | `/api/v1/identity/users/{user_id}/credential-reset` | `identity_users_user_id_credential_reset` | 200 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.credentials.reset` |
| API-03-010 | POST | `/api/v1/identity/users/{user_id}/deactivate` | `identity_users_user_id_deactivate` | 200 | ORGANIZATION | NA | NOT_REQUIRED | NA | `staff.deactivate` |
| API-03-011 | GET | `/api/v1/identity/users/{user_id}/activity` | `identity_users_user_id_activity_get` | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NA | `staff.activity.view` |
| API-03-012 | GET | `/api/v1/identity/staff-directory` | `identity_staff_directory_list` | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NA | `staff.directory.view` |

FR mapping for all twelve: `FR-USR-001` … `FR-USR-012` in order.

Authentication: Bearer access JWT required on every operation.

Path parameters:

- `{staff_profile_id}` = `identity.staff_profile.record_id`
- `{role_id}` = `identity.role.record_id`
- `{user_id}` = `identity.user_account.record_id`

### Source conflicts resolved by this gate

| Conflict | Losing source | Winning source |
| --- | --- | --- |
| Draft OpenAPI 3 paths / `identity_create_staff_account` | Collection OpenAPI YAML | Registry + `make_operation_id()` |
| FR-06 `/api/v1/staff/{staffId}/...` | FR-06 related-API tables | Registry `/api/v1/identity/...` |
| API-03-003 HTTP 200 in YAML | Draft OpenAPI | Registry 201 |
| API-03-009 HTTP 202 | Collection §29 | Registry / catalog `_success_status` → 200 |
| `IDENTITY_AUTHORIZATION_001` etc. | Collection §16 | Frozen `ErrorCode` |
| Required `X-Organization-ID` | Collection §12–13 | Untrusted `TenantContext`; body/path/object scope |
| Required `Idempotency-Key` on POSTs | Collection §23 | Registry NOT_REQUIRED |
| If-Match on lifecycle POSTs | Collection §24 | Registry: PATCH only |
| Catalog module owner `users` | Stale registry §5.1 / `_COLLECTION_ROUTE_OWNER` | Live `app/modules/identity/` |
| Registry “Authentication not routed yet” | Stale compact notes | `AUTH_CONTRACT_FREEZE.md` IMPLEMENTED |
| FR-USR-006 per-staff overrides | FR-06 | Numbered API-03-006 is role permissions |
| Collection resource bases `/identity/sessions`, `/identity/permissions` | Collection §8 | Not in the 12; do not route |

No remaining unresolved conflict that would change a path, method, count, or frozen error identity.

---

## 3. Existing architecture assessment

### What is already live and must be reused

| Mechanism | Location | Role for API-03 |
| --- | --- | --- |
| `UserAccount` ORM | `app/modules/identity/models/user_account.py` | Staff login subject |
| `IdentityRole` / `IdentityPermission` / `IdentityRolePermission` / `IdentityRoleAssignment` | `app/modules/identity/models/rbac.py` | RBAC |
| `IdentityAccessScope` ORM | `rbac.py` | Facility/site (and org) scope rows |
| `UserSession` | `models/user_session.py` | Session revoke on suspend/deactivate/reset |
| `PasswordResetRequest` | `models/password_reset_request.py` | AUTH recovery **and** API-03-009 |
| `AuthenticationEvent` | `models/security.py` | Login history for 011; security evidence |
| Argon2id + pepper | `app/core/security/passwords.py` | Do not duplicate |
| Password policy | `security.password_policy` via AuthenticationRepository | Confirm path; API-03 does not set the new password |
| RS256 JWT | `app/core/security/jwt.py` | AuthN only |
| `get_principal` / `require_authenticated` | `app/api/deps.py` | Bearer required |
| `load_authorized_principal` | `deps.py` | Tenant-capable principal |
| `require_permission` | `deps.py` | Permission gate |
| `AccessAssignment` + `app/core/access.py` | Object-level org/facility/site checks | Isolation |
| `record_audit_event` | `app/modules/audit/service.py` | Same UoW as mutation |
| API-00 envelopes | `app/api/v1/envelopes.py` | Success/error |
| `DigitizeError` hierarchy | `app/api/errors.py` | No `HTTPException` |
| Platform Admin bootstrap | `identity/bootstrap.py` CLI | Out of API-03 HTTP |
| Auth rate limit / lockout | `authentication/rate_limit.py`, account metadata | Reuse pattern for 009 |

`AuthenticationRepository.list_access_assignments` already joins `role_assignment` → `access_scope` and feeds `Principal.access_assignments`. API-03 writes those rows; it must not invent a second loader.

### What is missing for API-03 (implementation, not redesign)

- `identity.staff_profile` SQLAlchemy model (table exists)
- Identity HTTP router, schemas, service, repository for the 12
- `IDENTITY_PERMISSION_CODES` seed + PLATFORM_ADMIN bindings
- Catalog live keys / request schema names when handlers are registered
- Internal org standard-role upsert (no numbered create-role API)

### Stale documentation (do not treat as runtime truth)

- `API_CONTRACT_REGISTRY.md` §5.1 “No `identity` or `auth` package exists yet”
- `COLLECTION_META["API-03"]["service"]` “JWT login is the next gate”
- Registry missing-contract table still saying Authentication is “not routed yet”

---

## 4. Authoritative model decision

| Concept | Authoritative store | Authoritative ORM |
| --- | --- | --- |
| User / staff login subject | `identity.user_account` | `UserAccount` |
| Staff HR/profile | `identity.staff_profile` | **Add at implementation** (map 003) |
| Role | `identity.role` | `IdentityRole` |
| Permission catalog | `identity.permission` | `IdentityPermission` |
| Role ↔ permission | `identity.role_permission` | `IdentityRolePermission` |
| User ↔ role ↔ scope | `identity.role_assignment` | `IdentityRoleAssignment` |
| Access scope | `identity.access_scope` | `IdentityAccessScope` |
| Session | `identity.user_session` | `UserSession` |
| Recovery / admin reset token | `identity.password_reset_request` | `PasswordResetRequest` |
| Login/security events | `security.authentication_event` | `AuthenticationEvent` |
| Audit | `audit.audit_event` | `AuditEvent` |

Do **not** persist API-03 against `identity.users`, `identity.roles`, `identity.sessions`, `identity.staff`, or any scaffold table. Those relations are not created in `database/migrations/001`–`011`.

---

## 5. Divergent / scaffold classification

### Authoritative

API-03 must use these.

- `app/modules/identity/models/user_account.py`
- `app/modules/identity/models/rbac.py` (`IdentityAccessScope`, role, permission, assignment)
- `app/modules/identity/models/user_session.py`
- `app/modules/identity/models/password_reset_request.py`
- `app/modules/identity/models/security.py` / `session_policy.py`
- `app/modules/identity/constants.py` (extend with identity permission constants; no API03_ names)
- `app/modules/identity/bootstrap.py` (CLI only; do not call from API-03 routes)
- `app/core/access.py`, `app/core/principal.py`
- `app/api/deps.py` loaders
- `app/modules/authentication/*` for password hash verify, session revoke helpers, reset-request persistence patterns
- `app/modules/audit/service.py`
- `app/api/error_codes.py`, envelopes, `DigitizeError`
- Physical SQL `003` identity/security tables + `009` recovery columns/table + `010`/`011` permission seeds (do not edit)

### Reusable after alignment

- `app/modules/identity/repository.py` — today bootstrap-only; add staff/RBAC repositories beside it or split, same module
- `AuthenticationRepository` session revoke / reset-request methods — call from identity service; do not copy Argon2/JWT
- API-02 route pattern: `require_permission(..., loader=load_authorized_principal)` then `require_*_access` in the service
- Test helper style in `tests/api/platform_auth.py` (domain permission tuples, `test.user.{hex}` logins)

### Quarantined

Do not import these from API-03. Do not “align” them in this gate. Leave unrelated scaffold untouched until the implementation task retires HTTP `/users`.

- `app/modules/users/models/**` (`identity.users`, `identity.roles`, `identity.sessions`, …)
- ~~`app/modules/users/`~~ **Removed** (GAP-API03-005); use `app/modules/identity/` only.
- `app/modules/staff/models/**` (`identity.staff` and FKs to `identity.users`)
- `app/core/tenant_context.py` (broken / unused; `get_tenant_context` in `deps.py` is the parser)
- Collection OpenAPI YAML
- Historical collection error-code table

### Must be removed or replaced (implementation task, not this gate)

| Item | Why |
| --- | --- |
| HTTP `GET/POST /api/v1/users` | Duplicate identity HTTP; registry already says not API-03 |
| Any future `API03_PERMISSION_CODES` / `API03_AUTHORIZATION` | Naming architecture violation |
| Per-staff permission override table | Not in DDL; not in the 12 |
| Second JWT, password, or session stack | Authentication owns those |

---

## 6. Authentication boundary

### Authentication responsibilities (frozen, do not reopen)

- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/logout`
- `POST /api/v1/auth/password-reset`
- `POST /api/v1/auth/password-reset/confirm`
- Argon2id hashing + pepper
- `identity.user_session` lifecycle and refresh-cookie rotation
- Access JWT issue/verify (`typ=access`, `sub`, `sid`, `is_platform_admin`)
- Generic 401 `AUTHENTICATION_FAILED` (no account enumeration)
- Login eligibility (`ACTIVE` + not deleted)
- Lockout metadata on the account
- Writing `security.authentication_event` for auth flows

### API-03 identity responsibilities

- Staff `user_account` + `staff_profile` administration
- Role assignment and role-permission configuration
- Access-scope assignment (facility / site; org-wide via null scope)
- Lifecycle: create → activate → suspend → deactivate
- **Administrative** credential reset (API-03-009)
- Directory and activity **read** APIs
- Binding identity permissions to roles
- Revoking sessions **as a consequence** of suspend / deactivate / admin reset (by calling Authentication persistence helpers, not by minting tokens)

### AUTH recovery vs API-03-009

| | AUTH password recovery | API-03-009 |
| --- | --- | --- |
| Path | `/api/v1/auth/password-reset` (+ `/confirm`) | `/api/v1/identity/users/{user_id}/credential-reset` |
| Actor | Unauthenticated claimant | Authenticated administrator with `staff.credentials.reset` |
| Enumeration | Always 202 `{accepted: true}` | Target must exist **in scope**; missing → 404 generic |
| Token in JSON | Never | Never |
| Confirm | Public `/confirm` with `reset_token` + `new_password` | No numbered confirm; staff completes via AUTH confirm after notification |
| Session revoke | On successful confirm | On successful admin request (freeze: revoke all ACTIVE sessions immediately) |
| Notification | Delivery unimplemented; row `PENDING` | Same |

API-03-009 does **not** accept `new_password`. It creates a `password_reset_request`, audits, revokes sessions, and returns HTTP 200 with generic `data` (recommended `{ "accepted": true }`). Password policy is enforced on AUTH confirm, not on 009.

Do not expose passwords, hashes, refresh tokens, recovery tokens, peppers, or Argon2 parameters in API-03 responses or logs.

---

## 7. Identity terminology

| Term | Meaning | Not |
| --- | --- | --- |
| **UserAccount** | Authenticated identity/access subject. Table `identity.user_account`. Path `{user_id}`. | A customer, a staff profile row, a session |
| **Staff / Staff profile** | Organization employment/profile record `identity.staff_profile`, 1:1 with a tenant UserAccount | A UserAccount by itself; a customer |
| **User** (prose) | Ambiguous. In API-03 it means UserAccount. Prefer `user_account` in code. | Customer |
| **Customer** | Business customer who uses or purchases services. API-04 / `customer.customer`. | UserAccount |
| **Staff** (actor) | Tenant operator of Digitize | Platform Administrator; Customer |
| **Role** | Named permission bundle `identity.role` with `role_scope` and optional `organization_id` | Permission; Access scope |
| **Permission** | Global capability code `identity.permission.permission_code` | Role; API inventory ID |
| **Access scope** | Hierarchical grant target `identity.access_scope` (org / facility / site) | Tenant HTTP headers |
| **Role assignment** | UserAccount + Role + optional AccessScope | JWT claim |
| **Organization / Facility / Site** | Tenant hierarchy from API-02 | Identity tables |
| **Platform Administrator** | `user_type=PLATFORM_ADMIN`, `organization_id` NULL, `PLATFORM_ADMIN` system role. CLI-provisioned. | Org staff; not created by API-03 |

**UserAccount ≠ Customer** remains explicit. API-03 never inserts `customer.customer`. Customers do not receive `identity.staff_profile` rows.

`login_identifier` is the canonical login field (CITEXT). UI may say email or username; the API field is not `username` or `email`. Contact email/mobile belong in `staff_profile.profile_payload` (or future columns). They are not a second login key in v1.

---

## 8. Domain model

No columns or tables are added in this gate. Field lists are the physical `003`/`009` schema.

### 8.1 UserAccount (`identity.user_account`)

| | |
| --- | --- |
| Purpose | Login subject and account lifecycle |
| PK | `record_id` UUID |
| Important fields | `organization_id` (NULL for platform; required for staff), `login_identifier` CITEXT unique, `display_name`, `account_status`, `user_type`, `password_hash`, `mfa_enabled`, `last_login_at`, `metadata`, `version_number`, `deleted_at` |
| Lifecycle | `CREATED` → `ACTIVE` → `SUSPENDED` (reversible via 007) → `DEACTIVATED` (terminal). Login only `ACTIVE`. |
| Ownership | Staff accounts belong to exactly one Organization (`organization_id` NOT NULL). |
| Relationships | 1:1 `staff_profile`; 1:N role_assignment, user_session, password_reset_request |
| Uniqueness | `uq_user_account_login` on `login_identifier` (global, not per-org) |
| FK | `organization_id` → `tenant.organization` |
| Soft-delete | `deleted_at` exists. API-03 **does not** set it; deactivation is status-based. |
| Concurrency | `version_number` present; If-Match not required on lifecycle POSTs |
| Audit | All mutations |

DDL default `account_status='ACTIVE'` is **not** used for API-03-001. Creates write `CREATED`.

`user_type` for API-03 staff: `TENANT_USER`. Do not write `PLATFORM_ADMIN` from API-03.

### 8.2 Staff profile (`identity.staff_profile`) — ORM to add

| | |
| --- | --- |
| Purpose | Org staff profile; directory source |
| PK | `record_id` |
| Important fields | `organization_id` NOT NULL, optional `facility_id` / `site_id` (home placement), `user_account_id`, `staff_code`, `staff_type`, `employment_status`, `profile_payload` JSONB, `version_number` |
| Lifecycle | Created with the account. `employment_status` default `ACTIVE` is independent of `account_status`. |
| Uniqueness | `(organization_id, staff_code)`; `(user_account_id)` |
| Soft-delete | None |
| Concurrency | If-Match on API-03-002 |

`staff_type` allow-list (422 otherwise): `ORGANIZATION_ADMIN`, `FACILITY_MANAGER`, `SITE_ADMINISTRATOR`, `STAFF`.

### 8.3 Role (`identity.role`)

| | |
| --- | --- |
| Purpose | Named permission bundle |
| PK | `record_id` |
| Important fields | `organization_id` (NULL = platform/system), `role_code`, `role_name`, `role_scope`, `role_status`, `is_system_role`, `version_number` |
| Uniqueness | `(organization_id, role_code)` |
| Concurrency | If-Match on API-03-006 |
| System role | `PLATFORM_ADMIN` (`organization_id` NULL, `role_scope=PLATFORM`, `is_system_role=true`). Tenant callers must not mutate it. |

### 8.4 Permission (`identity.permission`)

| | |
| --- | --- |
| Purpose | Global capability catalog |
| Uniqueness | `permission_code` |
| API-03 impact | Seed `IDENTITY_PERMISSION_CODES`; do not duplicate existing platform/org/facility/site codes |

### 8.5 RolePermission (`identity.role_permission`)

| | |
| --- | --- |
| Purpose | Role → permission membership |
| Uniqueness | `(role_id, permission_id)` |
| Delete | ON DELETE CASCADE from role |

API-03-006 replaces the permission set for a tenant role (insert/delete in one UoW). Least privilege: a non-platform principal may only grant codes they themselves hold.

### 8.6 IdentityAccessScope (`identity.access_scope`)

| | |
| --- | --- |
| Purpose | Scope target attached to a role assignment |
| Fields | `organization_id`, `facility_id`, `site_id`, `scope_level`, `scope_name` |
| Uniqueness | **None in DDL.** Implementation must lookup-or-insert by (`organization_id`, `facility_id`, `site_id`, `scope_level`) to avoid duplicate rows. No speculative unique index in this gate. |
| Soft-delete | None |

`scope_level` vocabulary: `ORGANIZATION`, `FACILITY`, `SITE` (match existing `SCOPE_*` constants).

Org-wide assignment: `role_assignment.access_scope_id IS NULL` (already used by live API-02 tests). There is no numbered “assign organization access” API.

### 8.7 UserRole / Role assignment (`identity.role_assignment`)

There is no `UserRole` table. The authoritative relation is `role_assignment`.

| | |
| --- | --- |
| Purpose | UserAccount + Role + optional AccessScope |
| Uniqueness | `(user_account_id, role_id, access_scope_id)` |
| Status | `assignment_status` default `ACTIVE`. Only `ACTIVE` rows load into Principal. |
| Dates | `effective_at` / `expires_at` with CHECK |
| Multiple roles | Allowed |
| Multiple scopes | Allowed as separate assignment rows |

### 8.8 UserSession (`identity.user_session`)

Owned by Authentication. API-03 may set `session_status=REVOKED` / `ended_at` for all ACTIVE sessions of a target user on suspend, deactivate, and admin credential reset. It must not issue JWTs or set cookies.

---

## 9. Authorization and scope semantics

Do not create a second authorization framework.

```text
Bearer JWT
    → get_principal / require_authenticated
    → load_authorized_principal          (roles, permissions, access_assignments from DB)
    → require_permission(code, loader=load_authorized_principal)
    → service object checks via app/core/access.py
```

`load_platform_principal` stays API-01-only (rejects non-platform principals). API-03 always uses `load_authorized_principal`.

### Permission registry (implementation naming)

Single domain registry — identity is one vertical:

```text
IDENTITY_PERMISSION_CODES
  staff.create
  staff.update
  staff.role.assign
  staff.access.facility.assign
  staff.access.site.assign
  role.permissions.update
  staff.activate
  staff.suspend
  staff.credentials.reset
  staff.deactivate
  staff.activity.view
  staff.directory.view
```

Do **not** introduce `API03_PERMISSION_CODES`, `API03_AUTHORIZATION`, `USER_PERMISSION_CODES`, `ROLE_PERMISSION_CODES`, or `ACCESS_SCOPE_PERMISSION_CODES` unless a later contract split is explicit. Constants should be `PERM_STAFF_*` / `PERM_ROLE_PERMISSIONS_UPDATE`.

FR-06 extra codes (`staff.account.create`, `staff.roles.assign`, `staff.directory.facility-view`, approval/export variants) are **not** seeded. Directory/activity scope filtering uses `access_assignments`, not extra permission codes.

Bind all twelve codes to `PLATFORM_ADMIN` so platform operators can bootstrap tenant IAM (same pattern as API-02).

### Scope levels

| Scope | How it is represented | Inherits |
| --- | --- | --- |
| Platform | Assignment `role_scope=PLATFORM` and `organization_id IS NULL` | All tenant objects (`has_platform_assignment`) |
| Organization | `role_assignment.organization_id = org` and `access_scope_id` NULL (or scope_level ORGANIZATION with facility/site NULL) | All facilities and sites of that org |
| Facility | `access_scope.facility_id` set, `site_id` NULL | Sites of that facility |
| Site | `access_scope.site_id` set | That site only |

Inherited facility/site checks already exist in `can_access_facility` / `can_access_site`. API-03 must call them when the target staff home facility/site or the assigned facility/site is in play.

### Multiple / inactive assignments

- Multiple active assignments are unioned for permissions and access.
- `assignment_status != ACTIVE` is ignored by `list_permission_codes` / `list_access_assignments`.
- Expired `expires_at` is **not** currently filtered in the loader. **P2 implementation:** treat `expires_at < now` as inactive when loading, or refuse to create already-expired assignments. Do not silently change API-01/02 behavior without tests. Recommended: filter expired rows in the loader (additive correctness) and cover with tests.

### Cross-organization isolation

- Target `user_account.organization_id` must equal the object org.
- Role `organization_id` must match (or be a documented template copied into the org).
- Facility/site FKs must belong to that organization (and site to facility).
- Failure → 404 `RESOURCE_NOT_FOUND` with generic message (same as API-02).

### Platform administrator behavior

- JWT `is_platform_admin` is a fast signal, not the allow rule.
- Allow = identity permission present **and** (platform assignment **or** object in tenant assignments).
- Platform admins with `IDENTITY_PERMISSION_CODES` may manage **all tenant** staff.
- Platform admins cannot use API-03 to manage other platform-admin accounts.
- Organization administrators cannot manage platform administrators.

### Object-not-found vs authorization-denied

| Condition | Result |
| --- | --- |
| Missing/invalid JWT | 401 `AUTHENTICATION_FAILED` |
| Authenticated, missing permission | 403 `AUTHORIZATION_DENIED` |
| Has permission, object missing or out of scope | 404 `RESOURCE_NOT_FOUND` |
| Invalid lifecycle | 409 `INVALID_STATE` |
| Duplicate login / assignment | 409 `RESOURCE_CONFLICT` |
| Stale If-Match | 412 `CONCURRENCY_CONFLICT` |
| Bad body/query | 422 `VALIDATION_FAILED` |

### Forged tenant headers

`get_tenant_context` may parse headers for logs. Authorization and object selection use JWT principal + DB assignments + path/body IDs only. A forged `X-Organization-ID` must not expand or change the result.

### JWT permission lists

Login JSON may include `roles` / `permissions` as a **snapshot**. Authorization always reloads from `role_assignment` / `role_permission`. Do not put permission lists into the access JWT as authority.

---

## 10. Lifecycle rules

### Account status machine

```text
(API-03-001) CREATED ──API-03-007──► ACTIVE ──API-03-008──► SUSPENDED
                                      ▲                      │
                                      └────API-03-007────────┘
ACTIVE or SUSPENDED ──API-03-010──► DEACTIVATED (terminal)
```

| From | To | API | Reversible? |
| --- | --- | --- | --- |
| — | CREATED | 001 | N/A |
| CREATED | ACTIVE | 007 | No (can later suspend) |
| ACTIVE | SUSPENDED | 008 | Yes via 007 |
| SUSPENDED | ACTIVE | 007 | Yes |
| CREATED/ACTIVE/SUSPENDED | DEACTIVATED | 010 | No |
| DEACTIVATED | * | — | Reject 409 |
| CREATED | SUSPENDED | 008 | Reject 409 (not Active) |

007 from CREATED requires: at least one ACTIVE role assignment. Facility/site assignment is required only when the role’s `role_scope` is `FACILITY` or `SITE`. Credential: `password_hash` may still be null; activation enables login **once** a password exists (invitation/reset confirm). If hash is null, 007 still moves status to ACTIVE; Authentication continues to fail password login until a hash exists. That matches FR “credential setup or invitation.”

### Who can do what

| Action | Actor |
| --- | --- |
| Create users (staff) | Principal with `staff.create` in the target org (or platform assignment) |
| Create roles | **No numbered API.** Internal helper may upsert standard org roles. Callers do not POST a role resource. |
| Assign roles | `staff.role.assign` |
| Assign permissions to a role | `role.permissions.update`; cannot exceed caller's permission set unless platform assignment |
| Assign access scopes | `staff.access.facility.assign` / `staff.access.site.assign` |
| Org admins manage platform admins | **No** |
| Platform admins manage all tenants | **Yes**, if they hold the relevant identity permission |
| User in multiple organizations | **No** in v1 (`user_account.organization_id` is singular) |
| User with multiple roles | **Yes** |
| Role applied to multiple scopes | **Yes** (multiple assignment rows) |

### Side effects

| Event | Sessions | Assignments | Audit |
| --- | --- | --- | --- |
| 001 create | none | optional initial role | required |
| 002 profile | none | none | required |
| 003 assign role | none | insert ACTIVE | required |
| 004/005 access | none | insert/update assignment + scope | required |
| 006 role permissions | none (effective perms change at next load) | role_permission rewrite | required |
| 007 activate | none | unchanged | required |
| 008 suspend | revoke all ACTIVE | unchanged | required |
| 009 admin reset | revoke all ACTIVE | unchanged | required + authentication_event |
| 010 deactivate | revoke all ACTIVE | set assignment_status inactive (freeze: `INACTIVE`) | required |
| 011/012 reads | none | none | 011/012 collection listed view audits; **freeze: do not write audit on GET** (API-01/02 reads do not). Collection `STAFF_ACTIVITY_VIEWED` is superseded. |

Child relationships: deactivate does not delete role_assignment or staff_profile rows. History remains.

Hard DELETE: none in the 12.

### Standard org roles (internal, not HTTP)

Because there is no create-role API, implementation may upsert, per organization, inactive-until-used or immediately ACTIVE roles such as:

- `ORGANIZATION_ADMIN` (`role_scope=ORGANIZATION`) with all `IDENTITY_PERMISSION_CODES`
- optional `FACILITY_MANAGER` / `SITE_ADMINISTRATOR` with directory/activity + narrower subset

This helper is supporting domain logic, not a 13th API. It must not create `PLATFORM_ADMIN` under an organization.

---

## 11. Security boundaries

Preserve Authentication freeze:

- Argon2id only for new hashes; HMAC-SHA256 pepper from secret config; `MIN_PEPPER_LENGTH` enforced at bootstrap/settings
- No password/hash/token logging; redaction middleware stays
- Refresh token only in Secure + HttpOnly `digitize_refresh`; never in API-03 JSON
- Generic authentication failures on AUTH; API-03 404 must not leak whether a login_identifier exists in another org
- Central `DigitizeError` handling; no route-level `HTTPException`
- Same-UoW mutation + audit; rollback if audit insert fails
- Rate-limit administrative credential reset (reuse authentication limiter keyed by actor + target)
- Inactive/suspended/deactivated users cannot login (existing `account_is_login_eligible`)
- Enumerate-safe admin reset: in-scope missing user → 404 generic; do not return “no such login”
- `AUTH_DEV_BYPASS` without `principal_id` is already rejected by `load_authorized_principal`
- Notification delivery remains unimplemented; reset rows stay `delivery_status=PENDING` (same as AUTH)

API-03-001 must **not** accept a `password` field. Temporary credentials are not returned.

Least privilege on 006: refuse granting permissions the caller does not hold (platform assignment exempt). Refuse mutating `is_system_role` platform roles.

---

## 12. Endpoint implementation-readiness matrix

Request/response DTO names are implementation names to register in `_request_schema` when live. Catalog currently records unimplemented request schema as TBD.

Shared errors unless noted: 401 `AUTHENTICATION_FAILED`, 403 `AUTHORIZATION_DENIED`, 422 `VALIDATION_FAILED`, 500 `INTERNAL_ERROR`.

### API-03-001

```text
API ID:        API-03-001
Method:        POST
Path:          /api/v1/identity/staff-accounts
Operation ID:  identity_staff_accounts_create
Request:       StaffAccountCreate
                 organization_id UUID required
                 display_name required
                 login_identifier required
                 staff_code required
                 staff_type required (allow-list)
                 profile_payload object optional (email, mobile, designation)
                 initial_role_id UUID optional
               No password. No tenant-header authz.
Response:      API-00 + staff account/profile references (record_ids, statuses). No hash.
Status:        201
Permission:    staff.create
Scope:         ORGANIZATION (platform assignment may target any org)
Object check:  organization exists and ACTIVE; require_organization_access
Concurrency:   NA
Audit:         STAFF_ACCOUNT_CREATED / staff.account.created
Errors:        404 org missing/out of scope; 409 duplicate login or staff_code;
               409 org not ACTIVE
Database:      INSERT user_account (CREATED, TENANT_USER, password_hash NULL)
               INSERT staff_profile; optional role_assignment; audit
Dependencies:  API-02 org ACTIVE; identity permissions seeded
Open questions: none blocking (invitation notification deferred)
```

### API-03-002

```text
API ID:        API-03-002
Method:        PATCH
Path:          /api/v1/identity/staff-profiles/{staff_profile_id}
Operation ID:  identity_staff_profiles_staff_profile_id_update
Request:       StaffProfileUpdate + If-Match required
                 display_name optional (writes user_account)
                 staff_type, employment_status, facility_id, site_id,
                 profile_payload optional
               Does not change login_identifier, user_type, or account_status
Response:      API-00 + profile; ETag from staff_profile.version_number
Status:        200
Permission:    staff.update
Scope:         ORGANIZATION
Object check:  profile's organization; inherited facility/site if those IDs set
Concurrency:   IF_MATCH / version_number
Audit:         STAFF_PROFILE_UPDATED
Errors:        404; 412
Database:      UPDATE staff_profile [+ user_account.display_name]; audit
Dependencies:  001
Open questions: none blocking
```

### API-03-003

```text
API ID:        API-03-003
Method:        POST
Path:          /api/v1/identity/role-assignments
Operation ID:  identity_role_assignments_create
Request:       RoleAssignmentCreate
                 user_account_id, role_id required
                 access_scope_id optional (omit = org-wide)
                 effective_at / expires_at optional
Response:      API-00 + assignment
Status:        201
Permission:    staff.role.assign
Scope:         ORGANIZATION
Object check:  user and role in same org; role ACTIVE; not PLATFORM_ADMIN role
Concurrency:   NA (unique constraint)
Audit:         STAFF_ROLE_ASSIGNED
Errors:        404; 409 duplicate assignment
Database:      INSERT role_assignment
Dependencies:  role exists (helper or prior seed)
Open questions: none blocking
```

### API-03-004

```text
API ID:        API-03-004
Method:        POST
Path:          /api/v1/identity/access-scopes/facility
Operation ID:  identity_access_scopes_facility_create
Request:       FacilityAccessAssign
                 user_account_id, facility_id, role_id required
Response:      API-00 + access_scope + assignment
Status:        201
Permission:    staff.access.facility.assign
Scope:         ORGANIZATION (facility must belong to user's org)
Object check:  require_facility_access for caller; facility in org; org ACTIVE
Concurrency:   NA
Audit:         FACILITY_ACCESS_ASSIGNED
Errors:        404 hierarchy/isolation; 409 duplicate
Database:      lookup-or-insert access_scope FACILITY; INSERT role_assignment
Dependencies:  API-02 facility; 003 role
Open questions: none blocking
```

### API-03-005

```text
API ID:        API-03-005
Method:        POST
Path:          /api/v1/identity/access-scopes/site
Operation ID:  identity_access_scopes_site_create
Request:       SiteAccessAssign
                 user_account_id, site_id, role_id required
Response:      API-00 + access_scope + assignment
Status:        201
Permission:    staff.access.site.assign
Scope:         ORGANIZATION
Object check:  site → facility → org; require_site_access
Concurrency:   NA
Audit:         SITE_ACCESS_ASSIGNED
Errors:        404; 409
Database:      lookup-or-insert access_scope SITE; INSERT role_assignment
Dependencies:  API-02 site
Open questions: none blocking
```

### API-03-006

```text
API ID:        API-03-006
Method:        PATCH
Path:          /api/v1/identity/roles/{role_id}/permissions
Operation ID:  identity_roles_role_id_permissions_update
Request:       RolePermissionsUpdate + If-Match
                 permission_codes: list[str] replacing the set
Response:      API-00 + permission set; ETag role.version_number
Status:        200
Permission:    role.permissions.update
Scope:         ORGANIZATION (role.organization_id)
Object check:  tenant role only; reject is_system_role platform role
Concurrency:   IF_MATCH
Audit:         ROLE_PERMISSION_UPDATED
Errors:        404; 412; 403 if granting unheld permissions (non-platform);
               422 unknown permission_code
Database:      DELETE/INSERT role_permission; bump role.version_number
Dependencies:  permission catalog seeded
Open questions: none blocking
```

### API-03-007

```text
API ID:        API-03-007
Method:        POST
Path:          /api/v1/identity/users/{user_id}/activate
Operation ID:  identity_users_user_id_activate
Request:       StaffActivate { activation_reason 10–500 }
Response:      API-00 + account_status ACTIVE
Status:        200
Permission:    staff.activate
Scope:         ORGANIZATION
Object check:  tenant staff only; require_organization_access
Concurrency:   NA
Audit:         STAFF_ACCOUNT_ACTIVATED
Errors:        404; 409 INVALID_STATE if not CREATED/SUSPENDED;
               409 if no ACTIVE role assignment
Database:      UPDATE account_status; audit
Dependencies:  001, 003
Open questions: none blocking
```

### API-03-008

```text
API ID:        API-03-008
Method:        POST
Path:          /api/v1/identity/users/{user_id}/suspend
Operation ID:  identity_users_user_id_suspend
Request:       StaffSuspend { suspension_reason 10–500 }
Response:      API-00 + account_status SUSPENDED
Status:        200
Permission:    staff.suspend
Scope:         ORGANIZATION
Object check:  tenant staff; not platform admin
Concurrency:   NA
Audit:         STAFF_ACCOUNT_SUSPENDED
Errors:        404; 409 if not ACTIVE
Database:      UPDATE account_status; revoke sessions; audit
Dependencies:  Authentication session helpers
Open questions: none blocking
```

### API-03-009

```text
API ID:        API-03-009
Method:        POST
Path:          /api/v1/identity/users/{user_id}/credential-reset
Operation ID:  identity_users_user_id_credential_reset
Request:       StaffCredentialReset { reset_reason 10–500 }
Response:      API-00 data { accepted: true } — no token
Status:        200
Permission:    staff.credentials.reset
Scope:         ORGANIZATION
Object check:  tenant staff; not DEACTIVATED; not platform admin
Concurrency:   NA
Audit:         STAFF_CREDENTIAL_RESET_REQUESTED + authentication_event
Errors:        404; 409 DEACTIVATED; 429 if limiter trips
Database:      INSERT password_reset_request; revoke sessions; audit
Dependencies:  AUTH confirm path; notification delivery deferred
Open questions: none blocking
```

### API-03-010

```text
API ID:        API-03-010
Method:        POST
Path:          /api/v1/identity/users/{user_id}/deactivate
Operation ID:  identity_users_user_id_deactivate
Request:       StaffDeactivate { deactivation_reason 10–500 }
Response:      API-00 + account_status DEACTIVATED
Status:        200
Permission:    staff.deactivate
Scope:         ORGANIZATION
Object check:  tenant staff; not already DEACTIVATED; not platform admin
Concurrency:   NA
Audit:         STAFF_ACCOUNT_DEACTIVATED
Errors:        404; 409
Database:      UPDATE account_status; INACTIVE assignments; revoke sessions; audit
               Do not SET deleted_at
Dependencies:  session helpers
Open questions: none blocking
```

### API-03-011

```text
API ID:        API-03-011
Method:        GET
Path:          /api/v1/identity/users/{user_id}/activity
Operation ID:  identity_users_user_id_activity_get
Request:       query page, page_size, from_date, to_date
Response:      API-00 + authentication_event (and optionally audit_event) list
               No secrets. OFFSET metadata
Status:        200
Permission:    staff.activity.view
Scope:         ORGANIZATION
Object check:  target user in caller org (or platform)
Concurrency:   NA
Audit:         none (GET)
Errors:        404; 422
Database:      READ security.authentication_event [+ audit.audit_event]
Dependencies:  Authentication event writers
Open questions: whether to include audit_event in v1 payload — default yes,
                authentication_event first, then audit_event, same OFFSET page
```

### API-03-012

```text
API ID:        API-03-012
Method:        GET
Path:          /api/v1/identity/staff-directory
Operation ID:  identity_staff_directory_list
Request:       query page, page_size, account_status, staff_status (employment_status),
               role_id, facility_id, site_id, search (2–100)
               Platform callers: organization_id query required
               Tenant callers: organization_id from assignments; ignore header
Response:      API-00 + staff list (no password_hash). OFFSET
Status:        200
Permission:    staff.directory.view
Scope:         ORGANIZATION; results filtered to inherited facility/site
Concurrency:   NA
Audit:         none (GET)
Errors:        422; platform missing organization_id → 422
Database:      READ staff_profile JOIN user_account [roles/scopes]
Dependencies:  001
Open questions: none blocking
```

---

## 13. Migration assessment

**Required: seed-only additive migration after `011`.** No identity table create. No edits to `001`–`011`.

| Item | Decision |
| --- | --- |
| Type | Seed-only (permissions + PLATFORM_ADMIN `role_permission` bindings) |
| Schema | None required for the 12 |
| Data | Insert twelve `IDENTITY_PERMISSION_CODES` with `ON CONFLICT (permission_code) DO NOTHING`; bind to `PLATFORM_ADMIN` |
| Compatibility | None |
| Alembic revision ID | `012_identity_user_role` (fits `alembic_version` VARCHAR; semantic, not `012_api03_*`) |
| Python file | `migrations/versions/012_identity_user_role.py` |
| SQL twin | `database/migrations/012_seed_identity_user_role.sql` |
| Down | Delete role_permission rows for those codes; delete permission rows if unused |

Do **not** duplicate `organization.*` / `facility.*` / `site.*` / `platform.*` permission rows.

Do **not** create `identity.users` or `identity.staff`.

Optional later (not this gate, not required to start the 12): unique index on access_scope natural key; expired-assignment loader filter.

Alembic head today: `011_api02_org_facility_site`. Implementation head becomes `012_identity_user_role`.

---

## 14. Test strategy

Use real PostgreSQL (`DIGITIZE_API_TEST=1`) for constraints, transactions, and isolation. Default suite keeps live tests skipped.

### Contract

- Exact method/path for all 12; unused `/api/v1/staff/...` remains unrouted
- Operation IDs listed in §2; unique in OpenAPI
- Request validation (allow-lists, reason length, If-Match presence on PATCH)
- API-00 success/error envelopes; snake_case
- 201 vs 200 as frozen
- Registry count **222**; API-03 remains 12; API-01 11; API-02 14

### Authentication

- Missing / malformed / expired / wrong iss-aud token → 401
- Inactive (`CREATED`/`SUSPENDED`/`DEACTIVATED`) user token if somehow issued → 401 on AUTH login; API-03 as caller still 401/403 per principal load
- Revoked session on AUTH refresh; after 008/009/010 target cannot refresh

### Authorization

- Platform administrator with identity permissions: success across orgs
- Organization-scoped user: success in org; 404 cross-org
- Facility-scoped / site-scoped: directory and assignments inherit as in `access.py`
- Missing permission → 403
- Wrong object / forged tenant headers → 404 / no extra access
- Org admin cannot mutate platform admin
- 006 cannot grant unheld permissions

### Lifecycle

- 001 → CREATED; login still fails
- 007 CREATED→ACTIVE and SUSPENDED→ACTIVE; reject DEACTIVATED
- 008 only from ACTIVE; sessions revoked
- 010 terminal; assignments INACTIVE
- Invalid transitions 409
- Role assignment uniqueness; scope hierarchy

### Concurrency

- 002/006 missing If-Match → 428 `CONCURRENCY_CONFLICT` (same helper as API-01/02)
- Stale If-Match → 412 `CONCURRENCY_CONFLICT`
- Correct If-Match increments version and ETag

### Audit

- Each mutation inserts `audit.audit_event` in the same UoW
- Forced audit failure rolls back the business write
- 009 does not persist plaintext token

### Security

- 001/009 responses contain no password, hash, or reset token
- Logs redacted

### Regression

- API-01 live suite
- API-02 live suite
- Authentication contract tests
- `validate_catalog()`; OpenAPI uniqueness; Alembic current head after 012
- No runtime `API01_PERMISSION_CODES` / `API02_PERMISSION_CODES` / `API03_PERMISSION_CODES`

---

## 15. Open decisions

Non-blocking **P2**. Defaults above are binding if implementation starts without a further product pass.

| ID | Topic | Default if unchanged |
| --- | --- | --- |
| P2-1 | 011 mix of `authentication_event` vs `audit_event` | Both, authentication first |
| P2-2 | Expired `role_assignment.expires_at` in principal loader | Filter expired as inactive; regression-test API-02 |
| P2-3 | Standard org role codes beyond ORGANIZATION_ADMIN | Helper upserts ORGANIZATION_ADMIN only unless product expands |
| P2-4 | `staff_type` extra values | Allow-list in §8.2 only |
| P2-5 | Catalog `_COLLECTION_ROUTE_OWNER` / `HTTP_ROUTE_OWNERS` | Add `identity` when routes go live |
| P2-6 | Notification / email delivery for invitation and 009 | Remain unimplemented; `PENDING` rows |
| P2-7 | FR export of directory/activity | Out of the 12 |

No P1 decision remains that would change a numbered path, count, or frozen error/auth contract.

---

## 16. Explicit implementation scope

When implementation is authorized:

1. Additive Alembic `012_identity_user_role` + SQL twin (permission seed + PLATFORM_ADMIN bind).
2. Map `identity.staff_profile` ORM. Extend `identity.constants` with `IDENTITY_PERMISSION_CODES` / `PERM_STAFF_*`.
3. Set `OPERATION_AUTHORIZATION` for `API-03-001`…`API-03-012` to the frozen values (catalog metadata only; 222 count unchanged).
4. Identity module HTTP: 12 routes, APIModel DTOs, service, repository. `load_authorized_principal` + `app/core/access.py`.
5. Internal `ensure_organization_standard_roles` helper.
6. Admin reset via existing `password_reset_request` + session revoke helpers.
7. Retire scaffold `GET/POST /api/v1/users`.
8. Live contract tests under `DIGITIZE_API_TEST=1`.
9. Update catalog route owner `users` → `identity` and OpenAPI tag `Identity`.

---

## 17. Explicit out-of-scope items

- Implementing any of the 12 in **this** gate
- Route skeletons / 501 placeholders / fake payloads
- Schema changes or edits to migrations `001`–`011`
- Authentication redesign, JWT claim expansion as authz source, MFA, SSO
- Platform Admin HTTP provisioning
- Customer identity (API-04)
- Create/list/get/delete role APIs; unassign-role; get-user; `/identity/sessions`
- Per-staff permission overrides; approval workflows; directory export
- Organization / facility / site list/get (still REQUIRES DECISION for API-02)
- Flutter
- Changing the 222 count, API-01, or API-02
- API-numbered runtime authorization registries
- Notification transport
- Duplicate password/JWT/session implementations

---

## 18. Final gate result

| Criterion | Status |
| --- | --- |
| Exact 12 API-03 endpoints identified | Yes |
| Contract conflicts resolved with a winning source | Yes (§2 freeze table) |
| Authoritative identity models identified | Yes (`identity.*` migration tables) |
| Divergent scaffold classified | Yes |
| Authentication / API-03 boundary explicit | Yes |
| Role / permission / access-scope semantics defined | Yes |
| Platform and tenant isolation defined | Yes |
| Lifecycle rules defined | Yes |
| Security boundaries preserved | Yes |
| Migration impact identified (seed-only 012) | Yes |
| Test strategy complete | Yes |
| No speculative endpoint or schema implementation in this task | Yes |
| No API-numbered runtime authorization registry introduced | Yes |

```text
API-03 IDENTITY / USER / ROLE PRE-IMPLEMENTATION GATE: PASS
```

Do not begin API-03 implementation until this gate is explicitly accepted. Implementation must follow the frozen rules in §1 and the matrix in §12.
