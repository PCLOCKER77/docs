# API-01 Platform Administration — Pre-Implementation Gate

**Status:** PRE-IMPLEMENTATION GATE PASS  
**Date:** 2026-09-12  
**Scope:** Contract, database, ORM, authorization, and architecture reconciliation only.  
**Does not implement API-01.**

This revision is the second readiness pass after the error-code / exception / logging freeze. PASS means API-01 can be implemented without architectural redesign. Remaining work is first-slice implementation (seed, ORM alignment, `require_permission`), classified **P2**.

Authoritative sources for this gate, in descending order when they conflict:

1. `docs/architecture/API_CONTRACT_REGISTRY.md` and `app/api/contracts/catalog.py` (numbered identity, paths, counts)
2. `database/migrations/001`–`009` (physical schema)
3. `docs/architecture/AUTH_CONTRACT_FREEZE.md` (authentication, 401/403 families, Principal)
4. `docs/architecture/BACKEND_CODING_STANDARDS.md` (layering, API-00, UoW, logging, idempotency deferral)
5. `docs/07_API_Collections/API-01_Platform_Administration_Collection.md` (verbose request/response/audit prose)
6. `docs/04_Functional_Requirements/FR-02_Platform_Administration.md` (business intent)

The design-draft OpenAPI file `docs/07_API_Collections/openapi/API-01_Platform_Administration_OpenAPI.yaml` is **not** authoritative. Its paths and operation IDs contradict the frozen registry.

Authentication Phase 1 is implemented and gated. This document treats `/api/v1/auth/*` as live supporting infrastructure, even where the registry still says Authentication is unrouted.

---

## 1. API-01 Scope

API-01 is **platform-scoped administration** of Digitize itself:

- platform settings
- global master data
- feature-flag state
- maintenance windows
- release publication
- platform health summary (product, not ops probes)
- platform security-policy updates
- platform report execution requests

API-01 is **not**:

- Authentication (`/api/v1/auth/*` — already implemented)
- Organization / facility / site lifecycle (API-02)
- Staff identity, roles, assignments (API-03)
- SaaS plan or license **lifecycle** (API-09; FR-PLT-003/004)
- Facility-scoped operational reports (API-11)
- Audit search APIs (API-13)
- Common reference aliases (API-14)

All 11 endpoints are `PLATFORM` tenant scope. Client tenant headers remain untrusted.

Live numbered handlers today: **API-01-003, API-01-004, API-01-005** only. The other eight must be registered only when implemented. Do not add 501 skeletons.

### Frozen implementation decisions (no longer open)

These were previously listed as P1. They are now binding rules for the implementation task. They do not require redesign.

| Topic | Frozen rule |
| --- | --- |
| 011 permission | Registry field remains `TBD` (do not edit the 222 inventory in this gate). Implementation uses `platform.reports.view`. If `export_format` is present, also require `platform.reports.export`. |
| 403 / 401 | `AUTHORIZATION_DENIED` / `AUTHENTICATION_FAILED` |
| Principal | After JWT validation, load `roles` / `permissions` from `role_assignment` → `role_permission`. `require_permission(code)` raises `AuthorizationFailed`. `is_platform_admin` is a fast reject when false, not the allow rule. |
| Permission seed | Additive migration: insert collection dotted codes; bind to `PLATFORM_ADMIN`. Keep `PLATFORM_ADMIN_MANAGE_SETTINGS` for bootstrap. |
| 006 `scope_type` | Persist/accept `PLATFORM` (DDL). Reject collection `GLOBAL` with 422 `VALIDATION_FAILED`. API-01 does not PATCH org/facility-scoped flags. Lookup: `feature_code` + `PLATFORM` + `scope_id IS NULL`. |
| 007 `impacted_services` | Required non-empty string array. Persist at `notification_payload.impacted_services`. No new column. |
| 007 `impact_level` | Allow-list `LOW`, `MEDIUM`, `HIGH`. Unknown → 422. |
| 009 HTTP 503 | `SERVICE_UNAVAILABLE` or `DATABASE_ERROR`. Unexpected bugs remain 500 `INTERNAL_ERROR`. |
| 009 `service` filter | Optional; allow-list `api`, `database`, `reporting` (case-insensitive). Unknown → 422. No pagination despite operation ID `platform_health_list`. |
| 008 missing / invalid state | Missing row → 404 `PLATFORM_NOT_FOUND`. Non-`PLANNED` → 409 `INVALID_STATE`. |
| 001 `setting_type` | Filter allow-list: `CONFIGURATION`, `LOCALIZATION`, `COMMERCIAL`, `AUDIT`, `COMMUNICATION`. Default sort `setting_key ASC`. No `sort=` query param. |
| 011 report | `report_code` must match platform `reporting.report_definition` (`organization_id` NULL). Seed `PLATFORM_USAGE`. Optional `export_format` v1 allow-list `CSV`. Always 202 `QUEUED`. No GET status route. No Celery. No idempotency table. |
| Deactivate GMD | `is_active=false` uses `platform.masterdata.update`. |
| Soft delete | None. Status/`is_active` only. No hard DELETE in the 11. |
| Bootstrap | CLI-only. API-01 does not create Platform Admin users. |
| ORM | Map `audit.audit_event` and `reporting.report_*`. Do not use `audit.audit_logs` or `analytics.*`. New schemas use `APIModel`. |

---

## 2. Official 11-API Inventory

Permission codes in this table are from `OPERATION_AUTHORIZATION` in `catalog.py`
(API-01 inventory keys). They are also rows in `identity.permission` after
migration 010.

Operation IDs are those produced by `make_operation_id()` in `catalog.py`. Live GMD handlers already match these IDs.

### API-01-001 — Retrieve Platform Settings

| Field | Value |
| --- | --- |
| Method / path | `GET /api/v1/platform/settings` |
| Operation ID | `platform_settings_list` |
| Purpose | List platform settings for review |
| AuthN | Bearer access JWT required |
| AuthZ | `platform.settings.view` |
| Request | Query: `page`, `page_size`, `setting_type`, `is_active`, `search` (2–100) |
| Response | 200 API-00; `data` array of settings; pagination metadata |
| DB | `platform.platform_setting` |
| Transaction | Read-only |
| Pagination | OFFSET default 20 max 100 |
| Filters | `setting_type`, `is_active`, `search` on setting key |
| Sort | Contract: deterministic. **Recommend:** `setting_key ASC` |
| Errors | 401 `AUTHENTICATION_FAILED`; 403 `AUTHORIZATION_DENIED`; 422 `VALIDATION_FAILED` |
| Dependencies | None on API-02..14 |
| Live overlap | None |

### API-01-002 — Update Platform Setting

| Field | Value |
| --- | --- |
| Method / path | `PATCH /api/v1/platform/settings/{setting_key}` |
| Operation ID | `platform_settings_setting_key_update` |
| Purpose | Update one mutable platform setting |
| AuthN | Bearer JWT |
| AuthZ | `platform.settings.update` |
| Request | Body: `setting_value` (object, required), `effective_at` (optional RFC3339), `change_reason` (10–500). Header: `If-Match` required |
| Response | 200 API-00; ETag from `version_number` |
| DB | `platform.platform_setting`; audit `audit.audit_event` |
| Transaction | Atomic update + audit insert |
| Concurrency | `IF_MATCH` / `version_number` |
| Idempotency | Collection optional `Idempotency-Key`. Registry: NOT_REQUIRED. **Follow registry:** uniqueness is `(setting_key, scope_type)`; no idempotency table |
| Errors | 401; 403; 404 `PLATFORM_NOT_FOUND`; 409 `RESOURCE_CONFLICT` (immutable); 412 `CONCURRENCY_CONFLICT`; 422 |
| Dependencies | None |
| Live overlap | None |

### API-01-003 — Retrieve Global Master Data

| Field | Value |
| --- | --- |
| Method / path | `GET /api/v1/platform/global-master-data` |
| Operation ID | `platform_global_master_data_list` |
| Purpose | List platform-owned reference data |
| AuthN / AuthZ | JWT; collection `platform.masterdata.view`. **Live today:** `require_platform_admin` (JWT `is_platform_admin`) |
| Request | Query: `page`, `page_size`, `reference_group`, `search`, `is_active` |
| Response | 200 API-00 + `GlobalMasterDataOut` |
| DB | `platform.global_master_data` |
| Pagination | OFFSET 20/100 |
| Sort (live) | `display_order ASC NULLS LAST`, `name ASC` |
| Status | **BACKEND_IMPLEMENTED** |
| Live overlap | This is the live handler |

### API-01-004 — Create Global Master Data Record

| Field | Value |
| --- | --- |
| Method / path | `POST /api/v1/platform/global-master-data` |
| Operation ID | `platform_global_master_data_create` |
| Purpose | Create an approved-group master-data row |
| AuthZ | Collection `platform.masterdata.create`. Live: platform admin JWT |
| Request | `GlobalMasterDataCreate`: `reference_group`, `reference_code`, `name`, optional `description`, `display_order`, `metadata` |
| Response | 201; `Location`; ETag |
| DB | `platform.global_master_data` unique `(reference_group, reference_code)` |
| Idempotency | Registry TBD; unique constraint is the conflict control |
| Status | **BACKEND_IMPLEMENTED** |

### API-01-005 — Update Global Master Data Record

| Field | Value |
| --- | --- |
| Method / path | `PATCH /api/v1/platform/global-master-data/{record_id}` |
| Operation ID | `platform_global_master_data_record_id_update` |
| Purpose | Update name/description/order/active with `change_reason` |
| AuthZ | Collection `platform.masterdata.update` (deactivate also mentions `platform.masterdata.deactivate` — not in registry). Live: platform admin JWT |
| Request | `GlobalMasterDataUpdate` + required `If-Match` |
| Response | 200 + ETag |
| Status | **BACKEND_IMPLEMENTED** |

### API-01-006 — Update Feature Flag State

| Field | Value |
| --- | --- |
| Method / path | `PATCH /api/v1/platform/feature-flags/{feature_code}` |
| Operation ID | `platform_feature_flags_feature_code_update` |
| Purpose | Enable/disable/schedule a flag |
| AuthZ | `platform.featureFlags.update` |
| Request | `is_enabled`, `scope_type`, optional `scope_id`, `rollout_percentage`, `effective_at`, `change_reason`; `If-Match` required |
| Response | 200 + ETag |
| DB | `platform.feature_flag` |
| Concurrency | IF_MATCH |
| Dependencies | None. No GET/list/create in the 11 — rows must exist (seed) |
| Live overlap | None. Design OpenAPI lists GET `/platform/feature-flags` — **not** a numbered API; do not register it |

### API-01-007 — Schedule Maintenance Window

| Field | Value |
| --- | --- |
| Method / path | `POST /api/v1/platform/maintenance-windows` |
| Operation ID | `platform_maintenance_windows_create` |
| Purpose | Create a scheduled maintenance window |
| AuthZ | `platform.maintenance.schedule` |
| Request | `window_code`, `title`, `starts_at`, `ends_at`, `impact_level`, `impacted_services[]`, optional `notification_payload` |
| Response | 201 |
| DB | `platform.maintenance_window` unique `window_code` |
| Idempotency | Collection required. Registry TBD. Coding standards: no idempotency table. **Use unique `window_code` → 409 `RESOURCE_CONFLICT`** |
| Notification | Persist window; optional `integration.outbox_event` PENDING. Do not fake delivery. API-10 remains deferred |
| Live overlap | None |

### API-01-008 — Publish Platform Release

| Field | Value |
| --- | --- |
| Method / path | `POST /api/v1/platform/releases/{record_id}/publish` |
| Operation ID | `platform_releases_record_id_publish` |
| Purpose | Transition an existing release to published |
| AuthZ | `platform.releases.publish` |
| Request | Optional `publish_notes`, `notify_platform_users`; `If-Match` required |
| Response | 200 |
| DB | `platform.release_record` |
| Preconditions | Row must already exist (`release_status` PLANNED/draft). **There is no create-release API in the 11** |
| Concurrency | IF_MATCH |
| Live overlap | None |

### API-01-009 — Retrieve Platform Health Summary

| Field | Value |
| --- | --- |
| Method / path | `GET /api/v1/platform/health` |
| Operation ID | `platform_health_list` (generator suffix `_list` for param-less GET) |
| Purpose | Authorized product health summary |
| AuthZ | `platform.health.view` |
| Request | Optional query `service` |
| Response | 200 API-00; `overall_status`, `services[]` |
| DB | None (registry `—`). Derive from process readiness, DB connectivity, optional maintenance windows |
| Distinct from | `GET /api/v1/health/liveness` and `/readiness` (unauthenticated ops JSON, not API-00) |
| Collection 503 code | `SERVICE_UNAVAILABLE` — **not frozen**. Use `SERVICE_UNAVAILABLE` or `DATABASE_ERROR` with HTTP 503 if dependencies are down |
| Live overlap | Path differs from ops health; do not merge handlers |

### API-01-010 — Update Platform Security Policy

| Field | Value |
| --- | --- |
| Method / path | `PATCH /api/v1/platform/security-policies/{record_id}` |
| Operation ID | `platform_security_policies_record_id_update` |
| Purpose | Update platform authentication/session/password policy parameters |
| AuthZ | `platform.securityPolicies.update` |
| Request | `policy_payload` required; optional `policy_name`, `policy_type`, `effective_at`; `change_reason` required; `If-Match` required |
| Response | 200 + ETag |
| DB | `security.security_policy`; when `policy_type` is PASSWORD/SESSION also update `security.password_policy` / `security.session_policy` in the same transaction |
| Scope | Platform rows have `organization_id` NULL. Org-scoped policies are **not** API-01 |
| Live overlap | Authentication **reads** these tables; it does not expose PATCH |

### API-01-011 — Generate Platform Report

| Field | Value |
| --- | --- |
| Method / path | `POST /api/v1/platform/reports/executions` |
| Operation ID | `platform_reports_executions_create` |
| Success | 202 |
| Purpose | Enqueue a platform-scoped report execution |
| AuthZ | Registry **TBD**. Collection: `platform.reports.view`; export needs `platform.reports.export` |
| Request | `report_code`, `parameters`, optional `export_format`, `run_async` |
| Response | 202 API-00; execution id and `QUEUED` status. Collection `status_url` GET is **not** a numbered API — do not register it |
| DB | `reporting.report_definition`, `reporting.report_execution`; optional `reporting.report_export` |
| Async | Persist `QUEUED`. Do not introduce Celery/Redis on the request path. Worker/export completion is API-11 / later |
| Distinct from | API-11 facility reports under `/api/v1/reports/*` |
| Live overlap | None |

---

## 3. Contract Reconciliation

Legend: **NO GAP** / **CONTRACT GAP** / **DATABASE GAP** / **ORM GAP** / **AUTHORIZATION GAP** / **IMPLEMENTATION GAP** / **DOCUMENTATION GAP**.

| API | Registry vs collection vs DB vs ORM vs authz vs live | Classification |
| --- | --- | --- |
| All 11 | Registry paths match collection inventory table. Design OpenAPI uses `/platform/master-data`, GET lists, different operationIds | DOCUMENTATION GAP (OpenAPI draft is stale) |
| All 11 | Collection 403, auth freeze, and live GMD use `AUTHORIZATION_DENIED` | NO GAP (403 code unified in the error-architecture freeze) |
| All 11 | Collection permission codes (`platform.settings.view`, …) vs seed `PLATFORM_ADMIN_MANAGE_SETTINGS` | AUTHORIZATION GAP + DATABASE GAP (additive seed required) |
| 001–002 | Tables, ORM `PlatformSetting`, seed rows exist. No live route | IMPLEMENTATION GAP |
| 001 | Approved `setting_type` vocabulary not closed (seed: LOCALIZATION, COMMERCIAL, AUDIT, COMMUNICATION; DDL default CONFIGURATION; collection example SECURITY) | CONTRACT GAP — freeze allow-list in implementation from seed + `CONFIGURATION` |
| 002 | Collection optional idempotency store vs coding standards (deferred table) | CONTRACT GAP — no idempotency table; If-Match is the concurrency control |
| 003–005 | Live and aligned to `platform.global_master_data`. AuthZ is JWT admin flag, not permission codes | IMPLEMENTATION GAP (upgrade authz in this vertical) |
| 003–005 | Collection extra `platform.masterdata.deactivate` not in registry | CONTRACT GAP — treat deactivate as `platform.masterdata.update` |
| 006 | Table + ORM exist. No seed flags. Collection `scope_type=GLOBAL` vs DDL default `PLATFORM` | DATABASE GAP (seed) + CONTRACT GAP (use DDL `PLATFORM`) |
| 006 | Unique `(feature_code, scope_type, scope_id)` allows duplicate NULLs for `scope_id` in PostgreSQL | DATABASE GAP — look up by `feature_code` + `scope_type` + `scope_id` including NULL-safe match; do not add historical-migration unique rewrite |
| 007 | `impacted_services` not a column | DATABASE GAP — persist inside `notification_payload` JSONB; no ad-hoc column |
| 007 | Collection `RESOURCE_CONFLICT` not in frozen error catalog | CONTRACT GAP — use `RESOURCE_CONFLICT` |
| 008 | No create-release API; no seed releases | CONTRACT GAP — publish requires a pre-existing row (seed or operator insert documented in implementation) |
| 009 | No table (intentional). 503 uses `SERVICE_UNAVAILABLE` / `DATABASE_ERROR` | NO GAP (frozen this gate) |
| 010 | `security.security_policy` exists; typed password/session children exist; no platform policy seed | DATABASE GAP (seed) + IMPLEMENTATION GAP (update parent + child rows) |
| 010 | `UNIQUE (organization_id, policy_code)` does not uniquely constrain NULL `organization_id` | DATABASE GAP — identify by `record_id` only (path already does) |
| 011 | Registry authz TBD; collection has report permissions; no report-definition seed; no aligned ORM | AUTHORIZATION GAP + DATABASE GAP + ORM GAP |
| 011 | Collection `status_url` GET not in 222 | CONTRACT GAP — return execution in `data`; do not add a GET |
| 011 | Celery/workers deferred | IMPLEMENTATION GAP — persist QUEUED only |
| Registry §5.1 | Still says Authentication must not be registered | DOCUMENTATION GAP — ignore; auth is live |
| FR-PLT-003/004/006/010 | FR-02 capabilities with no API-01 numbered endpoint | NO GAP for this vertical — belong to API-09 / later / out of 11 |

No silent path or method inventions. Where collection and registry disagree on idempotency or extra permissions, **registry + coding standards win**.

---

## 4. Database Mapping

Migrations **001–009** are authority. Do not edit historical files. Additive work belongs in a new revision (010+) during implementation.

### 4.1 Entities that support API-01

#### `platform.platform_setting` (001–002, indexes 007, seed 008)

| Item | Value |
| --- | --- |
| PK | `record_id UUID` |
| Unique | `(setting_key, scope_type)` |
| Index | `idx_platform_setting_active (is_active, setting_key)` |
| Status | `is_active` |
| Concurrency | `version_number` |
| Audit columns | `created_at/by`, `updated_at/by` |
| Soft delete | None |
| Seed | DEFAULT_LOCALE, DEFAULT_TIMEZONE, DEFAULT_CURRENCY, AUDIT_CAPTURE_ENABLED, NOTIFICATION_DELIVERY_ENABLED |

#### `platform.global_master_data`

| Item | Value |
| --- | --- |
| Unique | `(reference_group, reference_code)` |
| Concurrency | `version_number` |
| Soft delete | None (`is_active` only) |
| Seed groups | FACILITY_TYPE, STATUS, CHANNEL_TYPE, CURRENCY (008 + catalogs.py) |

Facility types are **also** in `tenant.facility_type`. API-01 GMD must not write `tenant.facility_type`. Catalog `GET /api/v1/facility-types` remains the FK read.

#### `platform.feature_flag`

| Item | Value |
| --- | --- |
| Unique | `(feature_code, scope_type, scope_id)` |
| Checks | rollout 0–100; date order |
| Seed | **None** — migration requirement: seed platform-scoped flags used by product, or PATCH returns 404 |

#### `platform.maintenance_window`

| Item | Value |
| --- | --- |
| Unique | `window_code` |
| Status | `SCHEDULED` default |
| Check | `ends_at > starts_at` |
| Missing column | `impacted_services` — store on `notification_payload` |

#### `platform.release_record`

| Item | Value |
| --- | --- |
| Unique | `release_code` |
| Status | `PLANNED` default |
| Seed | **None** |

#### `security.security_policy` + children (003)

| Item | Value |
| --- | --- |
| Unique | `(organization_id, policy_code)` |
| Children | `password_policy`, `session_policy` via `security_policy_id` |
| Seed | **None** (Authentication falls back to schema DDL defaults when absent) |
| Migration requirement | Insert one platform policy (`organization_id` NULL) plus password/session child rows so 010 has a target |

#### `reporting.report_definition` / `report_execution` / `report_export` (006)

| Item | Value |
| --- | --- |
| Unique definition | `(organization_id, report_code)` — same NULL uniqueness caveat |
| Execution status | default `QUEUED` |
| Seed | **None** — need at least `PLATFORM_USAGE` (or collection-approved codes) for 011 |
| `version_number` | **Not present** on reporting tables — 011 is POST/202, not PATCH |

#### `audit.audit_event` (006)

| Item | Value |
| --- | --- |
| Mutation | Trigger `trg_audit_event_prevent_mutation` blocks UPDATE/DELETE |
| Columns | `actor_id`, `action`, `entity_type`, `entity_id`, `event_payload`, `ip_address`, `user_agent`, `correlation_id`, `occurred_at` |
| Soft delete | N/A (immutable) |

#### `integration.outbox_event` (006)

Available for durable “notify later” from 007/008/011. Publication worker is deferred. Inserting PENDING rows is allowed; pretending they were sent is not.

### 4.2 Not API-01 tables

Do **not** create or use:

- `platform.platform_configuration` / `platform.platform_modules` — ORM-only; **not** in 001–009
- `audit.audit_logs` — ORM-only; not `audit.audit_event`
- `analytics.events` / `analytics.dashboards` — not reporting schema
- `identity.users` / `identity.sessions` — retired scaffold

### 4.3 Migration requirements (implementation-time, not this task)

1. Seed `identity.permission` rows for API-01-001..010 collection codes; bind to `PLATFORM_ADMIN` system role.
2. Seed `platform.feature_flag` platform-scoped rows for flags the product actually toggles.
3. Seed at least one `platform.release_record` **or** document an operator insert path for 008.
4. Seed platform `security.security_policy` + password/session children.
5. Seed `reporting.report_definition` rows for allowed `report_code` values.
6. Optionally seed API-01-011 permission `platform.reports.view` (and `.export`).

Do not invent new tables for health, idempotency, or impacted_services.

---

## 5. ORM Mapping

### Use (migration-aligned)

| Table | Model | Notes |
| --- | --- | --- |
| `platform.platform_setting` | `PlatformSetting` | Ready |
| `platform.global_master_data` | `GlobalMasterData` | Live GMD |
| `platform.feature_flag` | `PlatformFeatureFlag` | Ready |
| `platform.maintenance_window` | `MaintenanceWindow` | Ready |
| `platform.release_record` | `ReleaseRecord` | Ready |
| `security.security_policy` | `SecurityPolicy` | Identity module; reuse |
| `security.password_policy` | `PasswordPolicy` | Reuse |
| `security.session_policy` | `SessionPolicy` | Reuse |
| `identity.permission` / role / assignment | `IdentityPermission`, `IdentityRole`, `IdentityRoleAssignment`, `IdentityRolePermission` | Permission load |
| `identity.user_account` | `UserAccount` | Principal `sub` |

### Must add during implementation (no second ORM style)

| Table | Gap |
| --- | --- |
| `audit.audit_event` | No aligned model. `AuditLog` → `audit.audit_logs` is divergent. Add `AuditEvent` mapped to `audit.audit_event` |
| `reporting.report_definition` | No aligned model |
| `reporting.report_execution` | No aligned model |
| `reporting.report_export` | Optional, if `export_format` is set |
| `integration.outbox_event` | Optional for notify-later |

### Must not use

| Model | Why |
| --- | --- |
| `PlatformConfiguration`, `PlatformModule`, `PlatformAnnouncement` | Not in migrations 001–009 |
| `AuditLog` (`audit.audit_logs`) | Divergent |
| analytics `Event` / `Dashboard` | Wrong schema |
| users scaffold models | Not identity authority |

Async SQLAlchemy, request-scoped `AsyncSession`, and `paginate()` stay. No sync engine, no second session factory, no second repository pattern. Follow `GlobalMasterDataRepository`: query / add / flush; no commit.

---

## 6. Authorization Matrix

### Frozen HTTP authn

All 11 require a valid RS256 access JWT (`typ=access`). Unauthenticated → 401 `AUTHENTICATION_FAILED`. Development `AUTH_DEV_BYPASS` must **not** authorize API-01 in staging/production. For API-01 implementation, bypass without a real principal should 401.

### Do not authorize with JWT `is_platform_admin` alone

Auth freeze: roles/permissions are not in the JWT and **may be loaded later by authorization**. Coding standards already allow `require_platform_admin` as a coarse dep; this gate requires the **role/permission model** for API-01.

Required implementation slice **before** new mutating routes:

1. After JWT validation, load active `identity.role_assignment` → `role_permission` → `permission_code` into `Principal.permissions` (and role codes into `Principal.roles`).
2. Add `require_permission(code)` (or equivalent) that raises `AuthorizationFailed()`.
3. Platform scope: assignments with `role_scope=PLATFORM` / `organization_id` NULL. Tenant headers never grant platform access.

`is_platform_admin` remains a JWT claim for Principal and may stay a fast reject when false, but **allow** only when the required permission is present.

### Permission codes (collection / catalog) vs database

| API ID | Required permission (frozen for implementation) | In `identity.permission` seed today |
| --- | --- | --- |
| API-01-001 | `platform.settings.view` | No |
| API-01-002 | `platform.settings.update` | No |
| API-01-003 | `platform.masterdata.view` | No |
| API-01-004 | `platform.masterdata.create` | No |
| API-01-005 | `platform.masterdata.update` | No |
| API-01-006 | `platform.featureFlags.update` | No |
| API-01-007 | `platform.maintenance.schedule` | No |
| API-01-008 | `platform.releases.publish` | No |
| API-01-009 | `platform.health.view` | No |
| API-01-010 | `platform.securityPolicies.update` | No |
| API-01-011 | `platform.reports.view`; if `export_format` set, also `platform.reports.export` | No (registry TBD) |

Today’s only platform seed permission is `PLATFORM_ADMIN_MANAGE_SETTINGS`. Bootstrap assigns that to the `PLATFORM_ADMIN` system role.

**Implementation mapping (not a new invented catalog):** insert the collection strings above as `permission_code` values; attach all of them to `PLATFORM_ADMIN`. Keep `PLATFORM_ADMIN_MANAGE_SETTINGS` for bootstrap compatibility; do not treat it as a substitute for the per-API checks.

Collection extras (`platform.settings.approve`, `platform.masterdata.deactivate`, `platform.maintenance.publish`, `platform.securityPolicies.activate`) are **not** in the registry. Do not implement separate checks in v1.

### Scoped resources

API-01-006 may set `scope_type` / `scope_id`. That is a **flag targeting** attribute, not a grant of tenant admin rights. API-01-010 must refuse policies with non-null `organization_id` (those are org security policies, not platform).

---

## 7. Existing Endpoint Relationship

| Live route | Numbered? | Relationship to API-01 | Action in this vertical |
| --- | --- | --- | --- |
| `GET/POST/PATCH /api/v1/platform/global-master-data` | API-01-003/004/005 | **Is** API-01 | Keep handlers; upgrade authz to permissions; reuse service/repository |
| `GET /api/v1/facility-types` | CAT extra; alias of API-14-006 | FK catalog of `tenant.facility_type`, not GMD | **Keep.** Do not fold into API-01. Do not duplicate writes |
| `GET /api/v1/platform/subscription-plans` | CAT extra; not API-09 | Read `commercial.subscription_plan` | **Keep.** FR-PLT-003 plan **lifecycle** stays API-09 |
| `GET /api/v1/platform/license-capabilities` | CAT extra | Read `commercial.license_capability` | **Keep.** FR-PLT-004 stays API-09 |
| `GET /api/v1/health/liveness\|readiness` | Ops extras | Not API-01-009 | **Keep.** API-01-009 is a separate API-00 authorized summary |
| `POST /api/v1/auth/*` | Outside 222 | Supplies Principal | **Keep.** API-01 consumes; does not own |
| `GET/POST /api/v1/users` | Scaffold | Not API-01 or API-03 | Do not expand. Out of this vertical |

Do not remove or rename any of the above in the API-01 implementation task.

---

## 8. Error Code Matrix

Frozen codes to use (API-00 / Auth freeze / coding standards):

| HTTP | Code | When |
| --- | --- | --- |
| 401 | `AUTHENTICATION_FAILED` | Missing/invalid/expired JWT |
| 403 | `AUTHORIZATION_DENIED` | Authenticated but missing permission (not collection `AUTHORIZATION_DENIED`) |
| 404 | `PLATFORM_NOT_FOUND` | Unknown setting_key, record_id, feature_code, report_code |
| 409 | `RESOURCE_CONFLICT` | Unique violation, immutable setting, duplicate window_code, invalid release state |
| 412 | `CONCURRENCY_CONFLICT` | Stale or missing `If-Match` on PATCH (missing → 428 already used by concurrency helper if wired like GMD) |
| 422 | `VALIDATION_FAILED` | Schema/query/body validation |
| 202/200/201 | — | Success per inventory |
| 500 | `INTERNAL_ERROR` | Unexpected |
| 503 | `SERVICE_UNAVAILABLE` / `DATABASE_ERROR` | Health/monitoring/DB unusable for 009 |

### Unfrozen codes — do not mint

| Appears in | Code | Replacement |
| --- | --- | --- |
| Collection 007 | `RESOURCE_CONFLICT` | `RESOURCE_CONFLICT` |
| Collection 009 | `SERVICE_UNAVAILABLE` | `SERVICE_UNAVAILABLE` (503) |

Live GMD already uses `DigitizeError` / `APIError` aliases and the central handler. New API-01 code must not raise `HTTPException`.

428 vs 412: live GMD treats missing `If-Match` as invalid concurrency (`etag_matches` false → conflict/concurrency error). Implementation of 002/005/006/008/010 must match that existing GMD behaviour unless a dedicated 428 path is added consistently.

---

## 9. Logging / Audit Requirements

Reuse the Authentication-gated split. No route-level loggers.

### Access log

`AccessLogMiddleware` only: method, path, operation_id, status, duration, request/correlation/trace IDs. No bodies, cookies, Authorization, setting secrets.

### Application / security log (structured `extra` only)

| Event | APIs |
| --- | --- |
| `platform.settings.listed` / `.updated` | 001 / 002 |
| `platform.masterdata.*` | 003–005 (003 list is optional info) |
| `platform.feature_flag.updated` | 006 |
| `platform.maintenance.scheduled` | 007 |
| `platform.release.published` | 008 |
| `platform.health.viewed` | 009 (do not log every ops probe) |
| `platform.security_policy.updated` | 010 |
| `platform.report.requested` | 011 |

Never log `setting_value` when the key is secret-bearing, password material, tokens, peppers, JWTs, or full policy secrets.

### Durable audit (`audit.audit_event`)

Required for mutations (collection + FR-PLT audit rules):

| Action | API |
| --- | --- |
| `PLATFORM_SETTING_UPDATED` | 002 |
| `MASTER_DATA_CREATED` / `MASTER_DATA_UPDATED` | 004 / 005 |
| `FEATURE_FLAG_ENABLED` / `FEATURE_FLAG_DISABLED` | 006 |
| `MAINTENANCE_SCHEDULED` | 007 |
| `PLATFORM_RELEASE_PUBLISHED` | 008 |
| `SECURITY_POLICY_UPDATED` | 010 |
| `PLATFORM_REPORT_REQUESTED` | 011 |

Reads 001/003/009: collection mentions view-audit “where configured”. **v1 recommendation:** do not insert audit rows for list/health reads (high volume). Access log is enough.

`security.authentication_event` remains Authentication-owned. Do not write login events from API-01.

Audit insert is in the **same UoW** as the mutation. Audit trigger forbids update/delete. Failure to insert audit fails the mutation (no silent skip).

---

## 10. Pagination / Filtering / Sorting

Use existing `pagination_params` + `paginate()`. Do not add a second pager. Cursor pagination remains deferred.

| API | Pagination | Filters | Search | Default sort |
| --- | --- | --- | --- | --- |
| 001 | OFFSET 20/100 | `setting_type` allow-list, `is_active` | `setting_key` 2–100 | `setting_key ASC` (recommended; collection says deterministic only) |
| 003 (live) | OFFSET 20/100 | `reference_group` approved groups, `is_active` | code/name 2–100 | `display_order ASC NULLS LAST`, `name ASC` |
| 009 | N/A | optional `service` allow-list | — | — |
| 002, 004–008, 010, 011 | N/A | — | — | — |

Collection does not define a sort query param for 001. Do not invent `sort=`. If a client needs other orders, that is a later contract change.

Ambiguity: approved `setting_type` / `impact_level` / health `service` vocabularies are not closed lists in the registry. Implementation must freeze allow-lists in module catalogs (same pattern as `APPROVED_GLOBAL_MASTER_DATA_GROUPS`) and 422 unknown values.

---

## 11. Transaction / Concurrency Requirements

**Keep the live foundation pattern:** `get_session()` / `get_platform_session()` Unit of Work commits on successful route return and rolls back on any exception. Services orchestrate; repositories flush; routes do not commit.

| API | Boundary | Flush | Concurrency | Uniqueness |
| --- | --- | --- | --- | --- |
| 001, 003, 009 | Read-only | No | N/A | N/A |
| 002 | UPDATE setting + INSERT audit | Yes after update | If-Match `version_number`; increment version | `(setting_key, scope_type)` |
| 004 | INSERT GMD | Yes | N/A | `(reference_group, reference_code)` → 409 |
| 005 | UPDATE GMD + audit | Yes | If-Match | — |
| 006 | UPDATE flag + audit | Yes | If-Match | NULL-safe flag lookup |
| 007 | INSERT window + audit [+ outbox] | Yes | N/A | `window_code` → 409 |
| 008 | UPDATE release status + audit | Yes | If-Match; reject if not PLANNED | — |
| 010 | UPDATE policy [+ child policy] + audit | Yes | If-Match | `record_id`; refuse org-scoped rows |
| 011 | INSERT execution [+ export row] + audit | Yes | N/A | Definition must exist; no idempotency table |

Optimistic locking: PATCH targets all have `version_number` except reporting (POST). Missing If-Match on GMD-style PATCH is already treated as concurrency failure.

Idempotency keys: **out of scope** for this vertical (coding standards). Unique constraints and If-Match replace them.

---

## 12. Dependencies

```text
API-01 routes (modules/platform)
    → Platform*Service
        → repositories (platform / identity security / reporting / audit)
            → AsyncSession / PostgreSQL 17
```

Inbound: Authentication Principal, `require_permission`, API-00 envelopes, logging, request context, UoW, pagination.

Outbound: none to HTTP, Flutter, or other vertical routes.

Must **not**:

- call API-02/03/09/11 routes
- implement org/facility/site CRUD
- implement staff role APIs
- mutate `commercial.subscription_plan` / `license` lifecycle
- run Celery/Redis/S3
- put SQL in routes or business rules in Pydantic beyond field validation

API-01-011 may **insert** `reporting.report_execution` rows. Completing/exporting those rows is API-11/worker scope.

API-01-010 may update password/session policy rows that Authentication **reads**. That is a downward data dependency, not a module cycle. Authentication must not import API-01 services.

---

## 13. Test Matrix

All new tests use API-00 assertions, real secret-value leakage checks where bodies exist, and no traceback on expected 401/403/422/409/412.

For **each** of the 11:

### Happy path

| API | Scenario |
| --- | --- |
| 001 | Platform admin with `platform.settings.view` lists seeded settings |
| 002 | If-Match update DEFAULT_CURRENCY, ETag advances, audit row exists |
| 003 | Existing live list (keep); plus permission-based allow |
| 004 | Create in CURRENCY group; 201 Location |
| 005 | If-Match rename; conflict on stale ETag |
| 006 | Seeded flag toggled |
| 007 | Create window; unique window_code |
| 008 | Publish seeded/planned release |
| 009 | 200 envelope with overall_status; ops `/health/liveness` still unenveloped |
| 010 | Update platform password policy payload; Authentication still hashes with new rules on next bootstrap/login policy load |
| 011 | 202 QUEUED execution for seeded report_code |

### Authentication

Unauthenticated → 401. Invalid/expired/malformed Bearer → 401. No JWT contents in body/logs.

### Authorization

JWT valid but missing permission → 403 `AUTHORIZATION_DENIED`. Org-scoped staff JWT → 403. Tenant headers do not grant access.

### Validation

Malformed JSON/missing fields → 422. `page_size=101` → 422. Search length → 422. Unknown `reference_group` / `setting_type` → 422. Weak `change_reason` (<10) → 422.

### Resource errors

Unknown setting_key / record_id / feature_code / report_code → 404. Duplicate GMD or window_code → 409. Publish non-PLANNED release → 409. Stale If-Match → 412.

### Database

Unique violation mapped to 409. Forced exception → 500 `INTERNAL_ERROR`, one traceback, rollback (no partial setting without audit).

### Contract

Status, envelope, operation_id, no stack traces, correlation_id present. Registry count remains 222. Auth and health routes unchanged.

### Live GMD regression

Keep existing catalog tests. When 003–005 switch to permission load, update fixtures to issue JWTs whose user has the seeded PLATFORM_ADMIN role assignment.

---

## 14. Implementation Boundary

### In API-01

- Permission load on Principal + `require_permission`
- Additive seed for API-01 permissions (and recommended flags/policy/report/release seeds)
- Aligned `AuditEvent` + reporting execution models
- Routes/services/repositories for 001, 002, 006, 007, 008, 009, 010, 011
- Authz upgrade for live 003–005
- Audit inserts for mutations
- API-00 + DigitizeError only

### Stay deferred / other verticals

| Item | Owner |
| --- | --- |
| Login, refresh, logout, password recovery | Authentication (done) |
| Org/facility/site CRUD and list/get | API-02 (list/get still REQUIRES DECISION) |
| Staff, roles, assignments | API-03 |
| Subscription/license lifecycle | API-09 (FR-PLT-003/004) |
| Facility reports, export download, dashboards | API-11 |
| Notification send | API-10 |
| Audit search/compliance APIs | API-13 |
| `GET /api/v1/reference/facility-types` | API-14-006 |
| Idempotency key table | Coding standards defer |
| Celery/Redis/S3/Vault | Engineering defer |
| MFA policy endpoints | Auth freeze defer |
| Flutter platform-admin module | Frontend NOT_STARTED |
| GET feature-flags / GET releases / GET report execution | Not in the 11 — do not add |

### FR-02 coverage vs the 11

| FR | Numbered API-01 | Notes |
| --- | --- | --- |
| FR-PLT-001 | 001, 002 | In |
| FR-PLT-002 | 003, 004, 005 | In (live) |
| FR-PLT-003 | — | API-09 + catalog GET plans |
| FR-PLT-004 | — | API-09 + catalog GET capabilities |
| FR-PLT-005 | 006 | PATCH only |
| FR-PLT-006 | — | No numbered API — out of this vertical |
| FR-PLT-007 | 009 | In |
| FR-PLT-008 | 007 | In |
| FR-PLT-009 | 008 | Publish only |
| FR-PLT-010 | — | No numbered API |
| FR-PLT-011 | 010 | In |
| FR-PLT-012 | 011 | Enqueue only |

---

## 15. Blocking Gaps

### P0 — Blocking / contract or security failure

**None.**

### P1 — Must resolve before implementation

**None.** Open contract questions from the first pass are frozen in §1. Implementation can proceed without redesign.

### P2 — Resolve during implementation (first slices)

1. Additive Alembic 010: collection permission codes + `PLATFORM_ADMIN` bindings; platform security policy + children; feature-flag seed; `PLATFORM_USAGE` report definition; at least one `PLANNED` release (or operator insert documented in tests).
2. Load permissions onto `Principal`; add `require_permission`; stop using `is_platform_admin` as the sole allow rule (including live GMD).
3. `AuditEvent` ORM on `audit.audit_event` + shared audit helper (no secrets in payload).
4. Reporting ORM on `reporting.report_definition` / `report_execution` / optional `report_export`.
5. 006 accept `PLATFORM` not `GLOBAL`; 007 persist `impacted_services` in JSONB.
6. New Pydantic schemas on `APIModel`; live GMD may be aligned without payload change.
7. Quarantine divergent `PlatformConfiguration` / `PlatformModule` / `AuditLog` from this vertical.
8. Happy-path fixtures that use real JWTs + role assignment.
9. Optionally set catalog `OPERATION_AUTHORIZATION["API-01-011"]` from `TBD` to `platform.reports.view` when implementing (does not change the 222 count or paths).

### P3 — Future

1. Registry/README still saying Authentication is unrouted.
2. Design OpenAPI YAML path drift.
3. Operation ID `platform_health_list`.
4. PostgreSQL NULL unique on org-nullable keys.
5. Outbox workers; GET report status; Celery; extra collection permissions; view-audit on GET.
6. Flutter platform-admin feature module (none exists today).

---

## 16. Recommended Implementation Order

1. Additive Alembic 010: API-01 permission seed + PLATFORM_ADMIN bindings; platform security policy seed; feature-flag seed; report-definition seed; optional release seed.
2. Principal permission load + `require_permission`.
3. `AuditEvent` model + shared audit helper (no secrets in payload).
4. Authz upgrade for live API-01-003/004/005; keep payloads/paths.
5. API-01-001 / 002 (settings) — proves list + If-Match + audit.
6. API-01-006 (flags).
7. API-01-007 (maintenance create).
8. API-01-010 (security policy + password/session children).
9. API-01-008 (publish) once a PLANNED row exists.
10. API-01-009 (health summary wrapping readiness/DB; distinct ops probes).
11. API-01-011 (QUEUED execution only) + reporting models.
12. Tests from §13; OpenAPI; registry still 222.

```text
API-01 PLATFORM ADMINISTRATION PRE-IMPLEMENTATION GATE: PASS
```
