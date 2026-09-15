# API-09 SUBSCRIPTION / LICENSE IMPLEMENTATION GATE

**Date:** 2026-09-12  
**Scope:** Slices A+B+C only (16 numbered APIs)  
**Pre-implementation freeze:** the approved API-09 implementation prompt (file `API_09_SUBSCRIPTION_LICENSE_PREIMPLEMENTATION_GATE.md` was not present in `docs/architecture/`; product direction was treated as frozen and was not reopened)

---

## 1. Status

```text
API-09 SUBSCRIPTION / LICENSE IMPLEMENTATION GATE: PASS
```

Backend-only. Flutter was not modified. Authentication HTTP and JWT claims were not modified. Option E commercial enforcement is not implemented. API-08 was not implemented. Deferred API-09 operations remain unregistered.

---

## 2. Scope

Implemented numbered APIs:

| API ID | Method | Path | Operation ID | Success |
| --- | --- | --- | --- | --- |
| API-09-001 | POST | `/api/v1/subscriptions` | `subscriptions_create` | 201 |
| API-09-002 | POST | `/api/v1/subscriptions/{subscription_id}/plan-assignment` | `subscriptions_subscription_id_plan_assignment` | 200 |
| API-09-003 | POST | `/api/v1/subscriptions/{subscription_id}/activate` | `subscriptions_subscription_id_activate` | 200 |
| API-09-007 | POST | `/api/v1/subscriptions/{subscription_id}/suspend` | `subscriptions_subscription_id_suspend` | 200 |
| API-09-008 | POST | `/api/v1/subscriptions/{subscription_id}/cancel` | `subscriptions_subscription_id_cancel` | 200 |
| API-09-009 | POST | `/api/v1/subscriptions/{subscription_id}/expire` | `subscriptions_subscription_id_expire` | 200 |
| API-09-011 | GET | `/api/v1/subscriptions/{subscription_id}/history` | `subscriptions_subscription_id_history` | 200 |
| API-09-013 | POST | `/api/v1/licenses` | `licenses_create` | 201 |
| API-09-014 | POST | `/api/v1/licenses/{license_id}/facility-assignment` | `licenses_license_id_facility_assignment` | 200 |
| API-09-015 | POST | `/api/v1/licenses/{license_id}/activate` | `licenses_license_id_activate` | 200 |
| API-09-017 | PATCH | `/api/v1/licenses/{license_id}/capabilities` | `licenses_license_id_capabilities_update` | 200, If-Match |
| API-09-018 | POST | `/api/v1/licenses/{license_id}/suspend` | `licenses_license_id_suspend` | 200 |
| API-09-019 | POST | `/api/v1/licenses/{license_id}/expire` | `licenses_license_id_expire` | 200 |
| API-09-020 | POST | `/api/v1/licenses/{license_id}/cancel` | `licenses_license_id_cancel` | 200 |
| API-09-021 | POST | `/api/v1/licenses/validate-login` | `licenses_validate_login` | 201, SYSTEM |
| API-09-022 | GET | `/api/v1/licenses/{license_id}` | `licenses_license_id_get` | 200 |

Catalog GETs remain:

- `platform_subscription_plans_list`
- `platform_license_capabilities_list`

These are not numbered API-09 operations.

---

## 3. Deferred APIs

Unregistered. No placeholder handlers. No fake 200s.

| API ID | Path |
| --- | --- |
| API-09-004 | `POST /api/v1/subscriptions/{subscription_id}/renew` |
| API-09-005 | `POST /api/v1/subscriptions/{subscription_id}/upgrade` |
| API-09-006 | `POST /api/v1/subscriptions/{subscription_id}/downgrade` |
| API-09-010 | `POST /api/v1/subscriptions/{subscription_id}/renewal-invoices` |
| API-09-012 | `GET /api/v1/subscriptions/reports` |
| API-09-016 | `POST /api/v1/licenses/{license_id}/renew` |
| API-09-023 | `GET /api/v1/licenses/{license_id}/history` |
| API-09-024 | `GET /api/v1/licenses/reports` |

Also deferred (not solved in this slice): Option E enforcement date, SaaS renewal billing, site add-on licensing, customer membership plans, notification/campaign infrastructure, BR-SUB-006 payment-before-activation.

---

## 4. Database

**Migration:** `014_subscription_license`  
**Parent:** `013_customer_master`  
**SQL twin:** `database/migrations/014_subscription_license.sql`  
**Alembic head after upgrade:** `014_subscription_license`

Applied cleanly against local PostgreSQL (`localhost:5434` / `digitize`). Migrations `001`–`013` were not modified. No new commercial tables. No credit-note, campaign, idempotency, or license-history tables.

Indexes:

```text
uq_subscription_facility_open
ON commercial.subscription(facility_id)
WHERE subscription_status IN ('PENDING', 'ACTIVE')

uq_license_facility_open
ON commercial.license(facility_id)
WHERE license_status IN ('PENDING', 'ACTIVE')
```

Permission seed: 16 codes in `identity.permission`, bound to `PLATFORM_ADMIN` only (`role_scope = PLATFORM`, `organization_id IS NULL`). Deferred API-09 permission codes were not seeded. Constant name is `SUBSCRIPTION_LICENSE_PERMISSION_CODES` (not `API09_PERMISSION_CODES`).

Authoritative tables used (existing ORM):

- `commercial.subscription_plan`
- `commercial.subscription`
- `commercial.subscription_term` (not mutated in this slice)
- `commercial.subscription_lifecycle_history`
- `commercial.license`
- `commercial.license_assignment`
- `commercial.license_capability`
- `commercial.entitlement`
- `commercial.feature_access`

`subscription/models/pricing.py` is not imported.

---

## 5. Runtime

**Numbered API-09 count:** 16  
**Implemented numbered total:** 65 (49 previous + 16)  
**Registry:** 222 unchanged  

Auth behavior:

- All 16 require Bearer authentication (`401 AUTHENTICATION_FAILED`)
- Missing permission: `403 AUTHORIZATION_DENIED`
- Wrong org/facility/object: `404 RESOURCE_NOT_FOUND`
- Open duplicate subscription/license: `409 RESOURCE_CONFLICT` (partial unique indexes + IntegrityError translation)
- Illegal lifecycle: `409 INVALID_STATE`
- API-09-017 only: missing If-Match `428`, stale `412`, success returns new `ETag`

Advisory enforcement:

- Subscription/license/entitlement/feature_access state is persisted
- `tenant.facility.subscription_scope_status` is updated (`ACTIVE` / `SUSPENDED` / `EXPIRED` / `PENDING` on cancel)
- API-09-021 is an independent HTTP validation API (`201`). It is **not** called by `/auth/login`
- Platform Admin: `valid = true` without a tenant facility license
- Facility staff with no ACTIVE license: `201` with `valid = false` (not 401)
- Login, JWT claims, API-01…04, and authentication middleware are unchanged
- Option E is not implemented

Facility-scoped subscription is preserved: `commercial.subscription.facility_id` is mandatory. One open subscription per facility. Organization is the commercial owner. No organization-level, multi-facility, or site subscriptions.

API-09-003 activation is one UoW: subscription ACTIVE, license generate/activate if required, entitlements, feature_access (`source_entity_type = LICENSE`), facility scope ACTIVE, lifecycle history, audit. Any failure rolls back everything.

FOUNDATION plan has no capability array; activation attaches all active `commercial.license_capability` catalog rows. Inactive licenses leave no `ENABLED` feature_access rows.

Payment is not required for Platform Admin activation. No invoices or fake payments.

---

## 6. Authorization

`load_authorized_principal` + `require_permission` + facility/object helpers.

Permission codes (1:1 with the 16 APIs):

```text
subscription.create
subscription.plan.assign
subscription.activate
subscription.suspend
subscription.cancel
subscription.expire
subscription.history.view
license.generate
license.facility.assign
license.activate
license.capabilities.update
license.suspend
license.expire
license.cancel
license.view
license.validate_login
```

Seeded to `PLATFORM_ADMIN` only. Not granted to Organization Admin / Facility Manager / Reception.

API-09-021 tenant_scope in the catalog: `SYSTEM`.

---

## 7. Audit

`record_audit_event` in the same UoW. Uppercase actions:

```text
SUBSCRIPTION_CREATED
SUBSCRIPTION_PLAN_ASSIGNED
SUBSCRIPTION_ACTIVATED
SUBSCRIPTION_SUSPENDED
SUBSCRIPTION_CANCELLED
SUBSCRIPTION_EXPIRED
LICENSE_CREATED
LICENSE_ASSIGNED
LICENSE_ACTIVATED
LICENSE_CAPABILITIES_UPDATED
LICENSE_SUSPENDED
LICENSE_EXPIRED
LICENSE_CANCELLED
```

`commercial.commercial_audit_history` is not used. Monkeypatched audit failure on create → HTTP 500 and no subscription row. Capability-write failure during activation → HTTP 500, subscription remains `PENDING`, no license row, facility scope remains `PENDING`.

---

## 8. Test Results

Commands used the project Poetry venv at `~/Library/Caches/pypoetry/virtualenvs/digitize-services-G_7W_USx-py3.13`.

| Gate | Result |
| --- | --- |
| Focused API-09 (`tests/subscription`, `test_014_subscription_license.py`, `tests/api/test_subscription_license.py` with `DIGITIZE_API_TEST=1`) | **59 passed** |
| Default `pytest -q` | **207 passed, 233 skipped** |
| Live PostgreSQL `DIGITIZE_API_TEST=1 pytest -q` | **430 passed, 10 skipped** |
| Ruff (API-09 touched files) | **PASS** |
| MyPy (`app/modules/subscription`, `app/api/contracts/catalog.py`) | **PASS** |
| OpenAPI | **PASS** (16 new operation IDs, unique, deferred IDs absent, catalog IDs unchanged) |
| Migration | **PASS** (`014_subscription_license` head, SQL twin executed, indexes + 16 permissions verified in PostgreSQL) |
| Registry | **222 APIs**, numbered live **65**, API-09 implemented **16** |

The 10 live skips are `DIGITIZE_MIGRATION_TEST=1` DB-11 contract tests, not API-09.

Full-tree `ruff check app tests` still reports pre-existing import-sort issues in unrelated modules (users scaffold, etc.). Those files were not part of this slice. Full-tree `mypy app` still reports pre-existing errors in `tenant_context`, facility models, identity service, and users repository. None of those are in the API-09 module after the `SubscriptionPlan` return-type fix.

---

## 9. Regression Results

| Vertical | Result |
| --- | --- |
| API-01 Platform Admin | **PASS** (included in 430) |
| API-02 Organization / Facility / Site | **PASS** |
| API-03 Identity / User / Role | **PASS** |
| API-04 Customer | **PASS** |
| Authentication | **PASS** |
| SaaS catalog GETs | **PASS** (`FOUNDATION` plan + 8 capabilities) |
| API-02 facility create | **PASS** (`subscription_scope_status=PENDING`) |

No API-01…04 or Authentication failures.

---

## 10. Architecture confirmation

| Rule | Status |
| --- | --- |
| Authentication HTTP unchanged | Confirmed (`app/modules/authentication` not modified) |
| JWT claims unchanged | Confirmed (`REQUIRED_CLAIMS` still iss/aud/sub/sid/iat/exp/typ/is_platform_admin) |
| API-01…04 enforcement unchanged | Confirmed (advisory commercial marker only) |
| Facility-scoped subscription | Confirmed |
| API-08 not touched | Confirmed |
| No fake billing / invoices / payments | Confirmed |
| No new idempotency infrastructure | Confirmed (natural uniqueness + partial unique indexes) |
| No invented APIs / placeholders | Confirmed |
| No customer membership plan changes | Confirmed |
| Migrations 001–013 untouched | Confirmed |
| Authentication does not import subscription | Confirmed |
| Subscription does not import authentication | Confirmed |
| Option E not implemented | Confirmed |
| Catalog CAT-PLAN-001 / CAT-CAPABILITY-001 not duplicated | Confirmed |

---

## 11. Known Non-Blocking Notes

- HTTP license cancel is `ACTIVE|SUSPENDED → CANCELLED`. A `PENDING` license may still be cancelled in-process when a `PENDING` subscription is cancelled, so `uq_license_facility_open` is released.
- Capability PATCH is the only If-Match API in this slice. Suspend/resume of a patched license re-enables retained entitlements rather than resetting to the full plan catalog.
- `GET /api/v1/licenses/reports` is not registered. A request may collide with `GET /licenses/{license_id}` UUID parsing (`422`), which is not a fake success.

---

## 12. Gate checklist

- [x] All 16 APIs correctly implemented
- [x] Deferred APIs remain deferred
- [x] Migration 014 valid
- [x] SQL twin matches / executed
- [x] Authorization works
- [x] Tenant isolation works
- [x] Transaction boundaries work
- [x] Audit rollback works
- [x] Concurrency works (open subscription/license 201+409; If-Match 428/412)
- [x] OpenAPI correct
- [x] API-01…04 and Authentication regressions pass
- [x] No frozen architecture decision violated

```text
PASS
```
