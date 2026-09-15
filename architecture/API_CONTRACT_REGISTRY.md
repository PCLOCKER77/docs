# DIGITIZE API Contract Registry

**Status:** API CONTRACTS READY WITH DEFERRED ITEMS
**Gate:** Contract / Skeleton Freeze
**Machine-readable source:** `digitize-services/app/api/contracts/catalog.py`
**Numbered inventory source:** `docs/07_API_Collections/API-01` through `API-14`
**Client envelope:** `docs/07_API_Collections/API-00`
**Foundation:** [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md), [BACKEND_FOUNDATION.md](BACKEND_FOUNDATION.md)

This registry is the authoritative product API inventory for `/api/v1`.
It does not replace API-00..14 collection documents. Those remain the
verbose contract prose. This file freezes identity, ownership, status,
and implementation roadmap.

Do not invent endpoints because a CRUD operation seems useful.
Do not return fake 200 payloads for unimplemented operations.
Do not register unimplemented numbered APIs as runtime FastAPI routes.

---

## 1. How to read a record

Every numbered endpoint is an `EndpointContract` with:

| Field | Meaning |
| --- | --- |
| API ID | Stable ID from the collection inventory |
| Collection / module | API-01..14 and owning backend module |
| Method / path | Canonical `/api/v1` kebab-case URL |
| Purpose / FR mapping | Business meaning and FR trace |
| Request / response schema | Live DTO or deferred vertical DTO |
| HTTP success status | Intended 200 / 201 / 202 when implemented |
| Authentication | `REQUIRED` or `NOT_REQUIRED` |
| Authorization | Permission code or `TBD` |
| Principal requirement | `platform_admin` or `authenticated_staff` |
| Tenant scope | PLATFORM / ORGANIZATION / FACILITY / SITE / SYSTEM / PUBLIC |
| Pagination | OFFSET (`page`/`page_size`, default 20, max 100) or NOT_APPLICABLE |
| Filtering / sorting | Approved fields only, or NOT_APPLICABLE / TBD |
| Idempotency | REQUIRED / NOT_REQUIRED / TBD. No idempotency table in this gate. |
| Concurrency | IF_MATCH for PATCH; NOT_APPLICABLE otherwise |
| Expected error codes | Semantic API-00 codes from `app/api/error_codes.py` |
| Database entities | `schema.table` from migrations 001–008 |
| Backend / frontend / integration / test / docs status | Lifecycle below |
| Flutter feature / screens | Future traceability; not implemented in this gate |

Unimplemented numbered APIs are **not registered** as FastAPI routes.
The documented success status is the future implemented status.

---

## 2. Lifecycle status

| Status | Meaning |
| --- | --- |
| PLANNED | Known need, no contract yet |
| CONTRACT_DEFINED | Registry record exists |
| SKELETON_CREATED | Contract frozen; runtime route not registered until the owning vertical |
| BACKEND_IMPLEMENTED | Live handler against approved schema |
| FRONTEND_IMPLEMENTED | Flutter wired to the live API |
| INTEGRATED | Backend + Flutter + envelope verified |
| TESTED | Required tests passed for that vertical |
| CERTIFIED | Passed the owning feature gate |
| SCAFFOLD | Legacy non-product route; retire later |
| REQUIRES_DECISION | Referenced elsewhere; no approved path |

Do not use COMPLETE. CERTIFIED is the only full-gate label.

This gate:

| Backend status | Count |
| --- | --- |
| SKELETON_CREATED | 197 |
| BACKEND_IMPLEMENTED (numbered) | 31 |
| Numbered product total | 228 |

All numbered endpoints are also `CONTRACT_DEFINED` for documentation.
Frontend, integration, and certification remain NOT_STARTED.

---

## 3. Count reconciliation

Previous documentation stated **222** business APIs. The numbered inventory
now includes six approved API-02 read operations.

| Collection | Title | Count |
| --- | --- | --- |
| API-01 | Platform Admin | 11 |
| API-02 | Organization / Facility / Site | 20 |
| API-03 | Identity / User / Role | 12 |
| API-04 | Customer | 12 |
| API-05 | Membership | 12 |
| API-06 | Attendance / Walk-in | 15 |
| API-07 | Trainer / Activity / Batch | 32 |
| API-08 | Billing / Payment | 18 |
| API-09 | Subscription / License | 24 |
| API-10 | Notification / Campaign | 24 |
| API-11 | Reports / Analytics | 12 |
| API-12 | Support Tickets | 12 |
| API-13 | Audit / Security | 12 |
| API-14 | Common Reference | 12 |
| **Total numbered product APIs** | | **228** |

Result: official numbered product count is **228**.

The following live routes are **not** in the 228:

| ID | Method | Path | Why excluded |
| --- | --- | --- | --- |
| OPS-HEALTH-001 | GET | `/api/v1/health/liveness` | Operational. Not in the 222 product count. Not API-00 enveloped. |
| OPS-HEALTH-002 | GET | `/api/v1/health/readiness` | Operational. Not in the 222 product count. Not API-00 enveloped. |
| CAT-FACILITY-TYPE-001 | GET | `/api/v1/facility-types` | Live catalog. Alias of API-14-006; this path is canonical for FK reads. |
| CAT-PLAN-001 | GET | `/api/v1/platform/subscription-plans` | Catalog read of commercial.subscription_plan, not API-09 lifecycle. |
| CAT-CAPABILITY-001 | GET | `/api/v1/platform/license-capabilities` | Catalog read of commercial.license_capability, not API-09 lifecycle. |
| SCAFFOLD-USERS-001 | GET | `/api/v1/users` | Retire at Authentication. Self-commits. Not a product API. Do not expand. |
| SCAFFOLD-USERS-002 | POST | `/api/v1/users` | Retire at Authentication. Self-commits. Not a product API. Do not expand. |

If these extras were added to 228, the count would be 235. They stay outside
the product inventory.

---

## 4. Canonical URLs and aliases

| Resource | Canonical URL | Alias / extra | Rule |
| --- | --- | --- | --- |
| Global master data | `/api/v1/platform/global-master-data` | none | Live API-01-003/004/005 |
| Facility types (FK catalog) | `/api/v1/facility-types` | `/api/v1/reference/facility-types` (API-14-006) | Live path is canonical for `tenant.facility_type`. API-14-006 is not registered until Reference is implemented. Do not duplicate handlers. |
| SaaS plans | `/api/v1/platform/subscription-plans` | none | Catalog extra; not API-09 lifecycle |
| License capabilities | `/api/v1/platform/license-capabilities` | none | Catalog extra; not API-09 lifecycle |
| Health | `/api/v1/health/liveness`, `/readiness` | `/api/v1/platform/health` is API-01-009 (not registered) | Different purposes |
| Users scaffold | `/api/v1/users` | not API-03 | Retire at Authentication. Do not expand. |

Duplicate method/path combinations in the numbered inventory: **none**.
Duplicate method/path combinations in the running FastAPI app: **none**
(verified by contract tests).

---

## 5. Vertical implementation rules (frozen)

The 228 numbered APIs are the contract inventory and roadmap.
They are not a requirement to register empty or 501 FastAPI routes
before a vertical is implemented.

A future vertical may add: explicit router functions, OpenAPI metadata,
auth dependency, pagination, If-Match, and real use-case handlers.

An unimplemented contract must not: exist as a runtime 501 placeholder,
return fake production data, mutate the database, invent request bodies,
or invent HTTP paths.

JSON remains snake_case. URLs remain `/api/v1` kebab-case.
Envelope remains API-00 (`success`, `data`, `message`, `metadata`,
`correlation_id`, `timestamp`).

SaaS `commercial.subscription_plan` and customer
`membership.membership_plan` stay separate.

---

## 5.1 HTTP route modules

Runtime FastAPI routes are registered only for implemented or scaffold
handlers. Unimplemented owning modules keep an empty `routes.py` until
their vertical starts. The v1 router includes only live/scaffold module
routers.

Contract ownership (roadmap, not runtime):

| Owner package | Contracts | Runtime today |
| --- | --- | --- |
| `platform` | API-01, API-14 | Live GMD only (API-01-003/004/005) |
| `organization` | API-02 organization paths | none |
| `facility` | API-02 facility and site paths | Live `/facility-types` catalog |
| `users` | API-03 identity | Scaffold `/users` only |
| `customer` | API-04 | none |
| `membership` | API-05 | none |
| `attendance` | API-06 attendance and walk-in | none |
| `training` | API-07 trainer, activity, batch, PT | none |
| `billing` | API-08 | none |
| `subscription` | API-09 | Live SaaS catalog reads |
| `campaign` | API-10 campaign paths | none |
| `communication` | API-10 notification paths | none |
| `reportsandanalytics` | API-11 | none |
| `support` | API-12 | none |
| `audit` | API-13 | none |
| `staff` | models only | no HTTP routes |

No `site`, `identity`, or `auth` package exists yet. Sites stay on
`facility`. Identity HTTP stays on `users` when API-03 starts.
Authentication paths are frozen in
[AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md) and must not be
registered until the Authentication implementation vertical.
Org/facility/site list/get remain REQUIRES DECISION and are not routed.

---

## 6. Numbered inventory

Full field records live in `app/api/contracts/catalog.py`.
Compact tables below are the human index.

### API-01 — Platform Admin

- Module: `platform`
- OpenAPI tag default: Platform Admin
- Flutter: TBD — no digitize-ui platform-admin feature module yet
- Screens: UI-PLT-001..UI-PLT-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-01-001 | GET | `/api/v1/platform/settings` | Retrieve Platform Settings | 200 | PLATFORM | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.platform_setting |
| API-01-002 | PATCH | `/api/v1/platform/settings/{setting_key}` | Update Platform Setting | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | platform.platform_setting |
| API-01-003 | GET | `/api/v1/platform/global-master-data` | Retrieve Global Master Data | 200 | PLATFORM | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-004 | POST | `/api/v1/platform/global-master-data` | Create Global Master Data Record | 201 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-005 | PATCH | `/api/v1/platform/global-master-data/{record_id}` | Update Global Master Data Record | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-006 | PATCH | `/api/v1/platform/feature-flags/{feature_code}` | Update Feature Flag State | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | platform.feature_flag |
| API-01-007 | POST | `/api/v1/platform/maintenance-windows` | Schedule Maintenance Window | 201 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | platform.maintenance_window |
| API-01-008 | POST | `/api/v1/platform/releases/{record_id}/publish` | Publish Platform Release | 200 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | platform.release_record |
| API-01-009 | GET | `/api/v1/platform/health` | Retrieve Platform Health Summary | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | — |
| API-01-010 | PATCH | `/api/v1/platform/security-policies/{record_id}` | Update Platform Security Policy | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | security.security_policy |
| API-01-011 | POST | `/api/v1/platform/reports/executions` | Generate Platform Report | 202 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution |

### API-02 — Organization / Facility / Site

- Module: `organization / facility`
- OpenAPI tag default: Organizations
- Flutter: digitize-ui/lib/features/organization, facility (mocks; Site TBD)
- Screens: UI-ORG-001..UI-SITE-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-02-001 | POST | `/api/v1/organizations` | Create Organization Profile | 201 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-002 | PATCH | `/api/v1/organizations/{organization_id}` | Update Organization Profile | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-003 | PATCH | `/api/v1/organizations/{organization_id}/settings/{setting_key}` | Configure Organization Setting | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.organization_setting |
| API-02-004 | POST | `/api/v1/organizations/{organization_id}/policies` | Configure Organization Policy | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization_policy |
| API-02-005 | POST | `/api/v1/organizations/{organization_id}/activate` | Activate Organization | 200 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-006 | POST | `/api/v1/organizations/{organization_id}/suspend` | Suspend Organization | 200 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-007 | POST | `/api/v1/facilities` | Create Facility | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.facility, tenant.facility_type |
| API-02-008 | PATCH | `/api/v1/facilities/{facility_id}` | Update Facility Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.facility |
| API-02-009 | PATCH | `/api/v1/facilities/{facility_id}/settings/{setting_key}` | Configure Facility Setting | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.facility_setting |
| API-02-010 | POST | `/api/v1/facilities/{facility_id}/activate` | Activate Facility | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.facility |
| API-02-011 | POST | `/api/v1/sites` | Create Site | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.site |
| API-02-012 | PATCH | `/api/v1/sites/{site_id}` | Update Site Details | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.site |
| API-02-013 | PATCH | `/api/v1/sites/{site_id}/settings/{setting_key}` | Configure Site Setting | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | tenant.site_setting |
| API-02-014 | POST | `/api/v1/sites/{site_id}/activate` | Activate Site | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.site |
| API-02-015 | GET | `/api/v1/organizations` | List Organizations | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-016 | GET | `/api/v1/organizations/{organization_id}` | View Organization Profile | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.organization |
| API-02-017 | GET | `/api/v1/facilities` | List Facilities | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.facility |
| API-02-018 | GET | `/api/v1/facilities/{facility_id}` | View Facility Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.facility |
| API-02-019 | GET | `/api/v1/sites` | List Sites | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.site |
| API-02-020 | GET | `/api/v1/sites/{site_id}` | View Site Details | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.site |

### API-03 — Identity / User / Role

- Module: `identity`
- OpenAPI tag default: Identity
- Flutter: digitize-ui/lib/features/authentication (mock only)
- Screens: UI-IAM-001..UI-IAM-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-03-001 | POST | `/api/v1/identity/staff-accounts` | Create Staff Account | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-002 | PATCH | `/api/v1/identity/staff-profiles/{staff_profile_id}` | Update Staff Profile | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-003 | POST | `/api/v1/identity/role-assignments` | Assign Staff Role | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-004 | POST | `/api/v1/identity/access-scopes/facility` | Assign Facility Access | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-005 | POST | `/api/v1/identity/access-scopes/site` | Assign Site Access | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-006 | PATCH | `/api/v1/identity/roles/{role_id}/permissions` | Configure Staff Permissions | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-007 | POST | `/api/v1/identity/users/{user_id}/activate` | Activate Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-008 | POST | `/api/v1/identity/users/{user_id}/suspend` | Suspend Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-009 | POST | `/api/v1/identity/users/{user_id}/credential-reset` | Reset Staff Credentials | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-010 | POST | `/api/v1/identity/users/{user_id}/deactivate` | Deactivate Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-011 | GET | `/api/v1/identity/users/{user_id}/activity` | View Staff Activity | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-012 | GET | `/api/v1/identity/staff-directory` | View Staff Directory | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |

### API-04 — Customer

- Module: `customer`
- OpenAPI tag default: Customers
- Flutter: TBD
- Screens: UI-CUS-001..UI-CUS-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-04-001 | POST | `/api/v1/customers` | Register Customer | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-002 | PATCH | `/api/v1/customers/{customer_id}` | Update Customer Profile | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-003 | POST | `/api/v1/customers/{customer_id}/verify-identity` | Verify Customer Identity | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-004 | GET | `/api/v1/customers` | Search Customers | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-005 | GET | `/api/v1/customers/{customer_id}` | View Customer Profile | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-006 | POST | `/api/v1/customers/{customer_id}/transfer-site` | Transfer Customer Between Sites | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-007 | POST | `/api/v1/customers/{customer_id}/suspend` | Suspend Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-008 | POST | `/api/v1/customers/{customer_id}/reactivate` | Reactivate Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-009 | POST | `/api/v1/customers/{customer_id}/archive` | Archive Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-010 | POST | `/api/v1/customers/{customer_id}/documents` | Manage Customer Document Metadata | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-011 | POST | `/api/v1/customers/{customer_id}/emergency-contacts` | Manage Emergency Contacts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |
| API-04-012 | GET | `/api/v1/customers/{customer_id}/history` | View Customer History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | customer.customer, customer.customer_history |

### API-05 — Membership

- Module: `membership`
- OpenAPI tag default: Memberships
- Flutter: digitize-ui/lib/features/membership_plan (plans, not customer memberships)
- Screens: UI-MEM-001..UI-MEM-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-05-001 | POST | `/api/v1/memberships` | Create Membership | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-002 | POST | `/api/v1/memberships/{membership_id}/activate` | Activate Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-003 | POST | `/api/v1/memberships/{membership_id}/renewals` | Renew Membership | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-004 | POST | `/api/v1/memberships/{membership_id}/upgrade` | Upgrade Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-005 | POST | `/api/v1/memberships/{membership_id}/downgrade` | Downgrade Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-006 | POST | `/api/v1/memberships/{membership_id}/freeze` | Freeze Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-007 | POST | `/api/v1/memberships/{membership_id}/resume` | Resume Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-008 | POST | `/api/v1/memberships/{membership_id}/transfer` | Transfer Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-009 | POST | `/api/v1/memberships/{membership_id}/cancel` | Cancel Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-010 | POST | `/api/v1/memberships/{membership_id}/expire` | Expire Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-011 | GET | `/api/v1/memberships/{membership_id}` | View Membership Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-012 | GET | `/api/v1/memberships/{membership_id}/history` | View Membership History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |

### API-06 — Attendance / Walk-in

- Module: `attendance`
- OpenAPI tag default: Attendance
- Flutter: TBD
- Screens: UI-ATT-001..UI-WLK-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-06-001 | POST | `/api/v1/attendance/check-in` | Record Customer Check-in | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-002 | POST | `/api/v1/attendance/eligibility` | Validate Attendance Eligibility | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-003 | POST | `/api/v1/attendance/session` | Record Session Attendance | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-004 | POST | `/api/v1/attendance/walk-in` | Record Walk-in Attendance | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-005 | POST | `/api/v1/attendance/{attendance_id}/check-out` | Record Customer Check-out | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-006 | PATCH | `/api/v1/attendance/{attendance_id}` | Update Attendance Record | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | operations.attendance |
| API-06-007 | POST | `/api/v1/attendance/{attendance_id}/cancel` | Cancel Attendance Record | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-008 | GET | `/api/v1/customers/{customer_id}/attendance-history` | View Attendance History | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-009 | GET | `/api/v1/attendance/reports` | Generate Attendance Report | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-010 | GET | `/api/v1/attendance/{attendance_id}/audit` | Audit Attendance Records | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.attendance |
| API-06-011 | POST | `/api/v1/walkin-visits/identify` | Identify or Register Walk-in Customer | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.walkin_visit |
| API-06-012 | POST | `/api/v1/walkin-visits` | Create Walk-in Visit | 201 | SITE | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.walkin_visit |
| API-06-013 | POST | `/api/v1/walkin-visits/{walkin_visit_id}/charges` | Calculate Walk-in Charges | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | operations.walkin_visit |
| API-06-014 | POST | `/api/v1/walkin-visits/{walkin_visit_id}/payments` | Associate Walk-in Payment | 200 | SITE | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.walkin_visit |
| API-06-015 | GET | `/api/v1/walkin-visits` | View Walk-in History and Reports | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | operations.walkin_visit |

### API-07 — Trainer / Activity / Batch

- Module: `training`
- OpenAPI tag default: Trainers
- Flutter: TBD
- Screens: UI-TRN-001..UI-BAT-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-07-001 | POST | `/api/v1/trainers` | Register Trainer Profile | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-002 | POST | `/api/v1/trainers/{trainer_id}/facility-assignments` | Assign Trainer to Facilities and Sites | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-003 | POST | `/api/v1/trainers/{trainer_id}/availability` | Maintain Trainer Availability | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-004 | POST | `/api/v1/trainers/{trainer_id}/schedule-conflicts` | Validate Trainer Schedule Conflicts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-005 | POST | `/api/v1/batches/{batch_id}/trainer-assignment` | Assign Trainer to Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-006 | POST | `/api/v1/personal-training-sessions/{session_id}/trainer-assignment` | Assign Trainer to Personal Training Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-007 | POST | `/api/v1/trainers/{trainer_id}/attendance` | Record Trainer Attendance | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-008 | POST | `/api/v1/trainers/{trainer_id}/status` | Manage Trainer Status | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-009 | GET | `/api/v1/trainers/{trainer_id}/history` | View Trainer History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-010 | GET | `/api/v1/trainers/{trainer_id}/performance-summary` | Generate Trainer Performance Summary | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.trainer, training.trainer_assignment |
| API-07-011 | POST | `/api/v1/activities` | Create Activity | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.activity |
| API-07-012 | PATCH | `/api/v1/activities/{activity_id}` | Update Activity | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | training.activity |
| API-07-013 | POST | `/api/v1/activities/{activity_id}/rules` | Configure Activity Rules | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.activity |
| API-07-014 | POST | `/api/v1/batches` | Create Batch | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-015 | PATCH | `/api/v1/batches/{batch_id}` | Update Batch | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | training.batch |
| API-07-016 | POST | `/api/v1/batches/{batch_id}/schedule` | Schedule Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-017 | POST | `/api/v1/batches/{batch_id}/capacity` | Configure Batch Capacity | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-018 | POST | `/api/v1/batches/{batch_id}/enrollments` | Enroll Customer into Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-019 | POST | `/api/v1/batches/{batch_id}/enrollments/{enrollment_id}/remove` | Remove Customer from Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-020 | POST | `/api/v1/class-sessions/{session_id}/start` | Start Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.class_session |
| API-07-021 | POST | `/api/v1/class-sessions/{session_id}/complete` | Complete Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.class_session |
| API-07-022 | POST | `/api/v1/class-sessions/{session_id}/cancel` | Cancel Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.class_session |
| API-07-023 | GET | `/api/v1/batches/{batch_id}/schedule` | View Batch Schedule | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.batch |
| API-07-024 | GET | `/api/v1/activities/{activity_id}/performance` | View Activity Performance | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.activity |
| API-07-025 | POST | `/api/v1/personal-training-packages` | Create Personal Training Package | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-026 | PATCH | `/api/v1/personal-training-packages/{package_id}/configuration` | Configure Training Package | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-027 | POST | `/api/v1/personal-training-sessions` | Book Personal Training Session | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-028 | POST | `/api/v1/personal-training-sessions/{session_id}/reschedule` | Reschedule Training Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-029 | POST | `/api/v1/personal-training-sessions/{session_id}/notes` | Record Training Notes | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |
| API-07-030 | POST | `/api/v1/customers/{customer_id}/progress` | Record Customer Progress | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | training.customer_progress |
| API-07-031 | GET | `/api/v1/customers/{customer_id}/training-history` | View Training History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.customer_progress |
| API-07-032 | GET | `/api/v1/personal-training/reports/trainer-performance` | Generate Trainer Performance Report | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | training.personal_training_package, training.personal_training_session |

### API-08 — Billing / Payment

- Module: `billing`
- OpenAPI tag default: Billing
- Flutter: TBD
- Screens: UI-BIL-001..UI-PAY-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-08-001 | POST | `/api/v1/invoices` | Generate Invoice | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.invoice, commercial.invoice_item |
| API-08-002 | POST | `/api/v1/billing/charges/calculate` | Calculate Service Charges | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.billing_account |
| API-08-003 | POST | `/api/v1/invoices/{invoice_id}/discounts` | Apply Discounts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.invoice, commercial.invoice_item |
| API-08-004 | POST | `/api/v1/invoices/{invoice_id}/taxes/calculate` | Calculate Taxes | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.invoice, commercial.invoice_item |
| API-08-005 | POST | `/api/v1/invoices/{invoice_id}/adjustments` | Apply Billing Adjustments | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.invoice, commercial.invoice_item |
| API-08-006 | POST | `/api/v1/invoices/{invoice_id}/cancel` | Cancel Invoice | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.invoice, commercial.invoice_item |
| API-08-007 | POST | `/api/v1/invoices/{invoice_id}/credit-notes` | Generate Credit Note | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-08-008 | POST | `/api/v1/payments` | Collect Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-009 | POST | `/api/v1/payments/online` | Process Online Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-010 | POST | `/api/v1/payments/offline` | Record Offline Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-011 | GET | `/api/v1/payments/{payment_id}/status` | Verify Payment Status | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-012 | POST | `/api/v1/payments/{payment_id}/receipts` | Generate Payment Receipt | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-013 | POST | `/api/v1/payments/{payment_id}/refunds` | Process Refund | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-014 | POST | `/api/v1/reconciliations` | Reconcile Payment | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.reconciliation |
| API-08-015 | POST | `/api/v1/payments/{payment_id}/cancel` | Cancel Payment | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.payment, commercial.receipt |
| API-08-016 | GET | `/api/v1/billing/history` | View Billing and Payment History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.billing_account |
| API-08-017 | GET | `/api/v1/commercial/reports` | Generate Commercial Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.billing_account |
| API-08-018 | GET | `/api/v1/billing/outstanding-statements` | Generate Outstanding Statement | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.billing_account |

### API-09 — Subscription / License

- Module: `subscription`
- OpenAPI tag default: Subscriptions
- Flutter: TBD
- Screens: UI-SUB-001..UI-LIC-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-09-001 | POST | `/api/v1/subscriptions` | Create Subscription | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-002 | POST | `/api/v1/subscriptions/{subscription_id}/plan-assignment` | Assign Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-003 | POST | `/api/v1/subscriptions/{subscription_id}/activate` | Activate Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-004 | POST | `/api/v1/subscriptions/{subscription_id}/renew` | Renew Subscription | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-005 | POST | `/api/v1/subscriptions/{subscription_id}/upgrade` | Upgrade Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-006 | POST | `/api/v1/subscriptions/{subscription_id}/downgrade` | Downgrade Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-007 | POST | `/api/v1/subscriptions/{subscription_id}/suspend` | Suspend Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-008 | POST | `/api/v1/subscriptions/{subscription_id}/cancel` | Cancel Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-009 | POST | `/api/v1/subscriptions/{subscription_id}/expire` | Expire Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-010 | POST | `/api/v1/subscriptions/{subscription_id}/renewal-invoices` | Generate Renewal Invoice | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-011 | GET | `/api/v1/subscriptions/{subscription_id}/history` | View Subscription History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-012 | GET | `/api/v1/subscriptions/reports` | Generate Subscription Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.subscription, commercial.subscription_plan |
| API-09-013 | POST | `/api/v1/licenses` | Generate License | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-014 | POST | `/api/v1/licenses/{license_id}/facility-assignment` | Assign License to Facility | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-015 | POST | `/api/v1/licenses/{license_id}/activate` | Activate License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-016 | POST | `/api/v1/licenses/{license_id}/renew` | Renew License | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-017 | PATCH | `/api/v1/licenses/{license_id}/capabilities` | Modify Licensed Capabilities | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-018 | POST | `/api/v1/licenses/{license_id}/suspend` | Suspend License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-019 | POST | `/api/v1/licenses/{license_id}/expire` | Expire License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-020 | POST | `/api/v1/licenses/{license_id}/cancel` | Cancel License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-021 | POST | `/api/v1/licenses/validate-login` | Validate License During Login | 201 | SYSTEM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-022 | GET | `/api/v1/licenses/{license_id}` | View License Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-023 | GET | `/api/v1/licenses/{license_id}/history` | View License History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |
| API-09-024 | GET | `/api/v1/licenses/reports` | Generate License Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | commercial.license, commercial.license_assignment |

### API-10 — Notification / Campaign

- Module: `communication`
- OpenAPI tag default: Notifications
- Flutter: TBD
- Screens: UI-NOT-001..UI-CMP-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-10-001 | POST | `/api/v1/campaigns` | Create Campaign | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-002 | PATCH | `/api/v1/campaigns/{campaign_id}/configuration` | Configure Campaign | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-003 | POST | `/api/v1/campaigns/{campaign_id}/audiences` | Select Target Audience | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-004 | POST | `/api/v1/campaigns/{campaign_id}/submit-for-approval` | Submit Campaign for Approval | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-005 | POST | `/api/v1/campaigns/{campaign_id}/approve` | Approve Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-006 | POST | `/api/v1/campaigns/{campaign_id}/schedule` | Schedule Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-007 | POST | `/api/v1/campaigns/{campaign_id}/launch` | Launch Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-008 | POST | `/api/v1/campaigns/{campaign_id}/pause` | Pause Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-009 | POST | `/api/v1/campaigns/{campaign_id}/complete` | Complete Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-010 | POST | `/api/v1/campaigns/{campaign_id}/cancel` | Cancel Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-011 | GET | `/api/v1/campaigns/{campaign_id}/performance` | Monitor Campaign Performance | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-012 | GET | `/api/v1/campaigns/{campaign_id}/reports` | Generate Campaign Report | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-10-013 | POST | `/api/v1/notification-templates` | Create Notification Template | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-014 | POST | `/api/v1/notification-rules` | Configure Notification Rules | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | communication.notification_template GAP |
| API-10-015 | POST | `/api/v1/notifications/system` | Generate System Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-016 | POST | `/api/v1/notifications/manual` | Send Manual Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-017 | POST | `/api/v1/notifications/schedule` | Schedule Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-018 | POST | `/api/v1/notifications/{notification_id}/deliver` | Deliver Notification | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-019 | POST | `/api/v1/notifications/{notification_id}/retry` | Retry Failed Notification | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-020 | GET | `/api/v1/notifications` | View Notification History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-021 | GET | `/api/v1/notifications/{notification_id}/delivery-status` | Track Delivery Status | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-022 | POST | `/api/v1/notifications/{notification_id}/archive` | Archive Notification | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-023 | GET | `/api/v1/notifications/reports` | Generate Notification Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-024 | PATCH | `/api/v1/notification-preferences/{preference_id}` | Manage Notification Preferences | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | DATABASE GAP GAP |

### API-11 — Reports / Analytics

- Module: `reportsandanalytics`
- OpenAPI tag default: Reports
- Flutter: TBD
- Screens: UI-RPT-001..UI-ANA-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-11-001 | GET | `/api/v1/dashboards/operational` | View Operational Dashboard | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-002 | POST | `/api/v1/reports/membership` | Generate Membership Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-003 | POST | `/api/v1/reports/attendance` | Generate Attendance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-004 | POST | `/api/v1/reports/revenue` | Generate Revenue Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-005 | POST | `/api/v1/reports/customer` | Generate Customer Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-006 | POST | `/api/v1/reports/trainer-performance` | Generate Trainer Performance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-007 | POST | `/api/v1/reports/activity-performance` | Generate Activity Performance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-008 | POST | `/api/v1/reports/subscription` | Generate Subscription Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-009 | POST | `/api/v1/report-executions/{execution_id}/exports` | Export Report | 202 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-010 | POST | `/api/v1/report-schedules` | Schedule Automated Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-011 | GET | `/api/v1/kpis` | Monitor Business KPIs | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-012 | GET | `/api/v1/reports/historical-trends` | View Historical Trends | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |

### API-12 — Support Tickets

- Module: `support`
- OpenAPI tag default: Support
- Flutter: TBD
- Screens: UI-SUP-001..UI-SUP-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-12-001 | POST | `/api/v1/support-tickets` | Create Support Ticket | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-002 | POST | `/api/v1/support-tickets/{ticket_id}/classify` | Classify Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-003 | POST | `/api/v1/support-tickets/{ticket_id}/assign` | Assign Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-004 | POST | `/api/v1/support-tickets/{ticket_id}/priority` | Set Ticket Priority | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-005 | POST | `/api/v1/support-tickets/{ticket_id}/accept` | Accept Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-006 | PATCH | `/api/v1/support-tickets/{ticket_id}/progress` | Update Ticket Progress | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-007 | POST | `/api/v1/support-tickets/{ticket_id}/information-requests` | Request Additional Information | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-008 | POST | `/api/v1/support-tickets/{ticket_id}/escalate` | Escalate Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment GAP |
| API-12-009 | POST | `/api/v1/support-tickets/{ticket_id}/resolve` | Resolve Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-010 | POST | `/api/v1/support-tickets/{ticket_id}/close` | Close Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-011 | POST | `/api/v1/support-tickets/{ticket_id}/reopen` | Reopen Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |
| API-12-012 | GET | `/api/v1/support-tickets/reports` | Generate Support Reports | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | support.support_ticket, support.ticket_assignment |

### API-13 — Audit / Security

- Module: `audit`
- OpenAPI tag default: Audit
- Flutter: TBD
- Screens: UI-AUD-001..UI-SEC-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-13-001 | POST | `/api/v1/audit-events` | Capture Business Activity | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-002 | POST | `/api/v1/authentication-events` | Capture User Login Activity | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | security.authentication_event |
| API-13-003 | POST | `/api/v1/audit-events/configuration-changes` | Record Business Configuration Changes | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-004 | POST | `/api/v1/security-events` | Monitor Security Events | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | security.security_event |
| API-13-005 | GET | `/api/v1/audit-events` | Review Audit Logs | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-006 | POST | `/api/v1/investigations` | Investigate Audit Records | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-007 | POST | `/api/v1/compliance-records/reports` | Generate Compliance Report | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-008 | POST | `/api/v1/audit-events/archive` | Archive Audit Records | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-009 | POST | `/api/v1/audit-events/export` | Export Audit History | 202 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-010 | PATCH | `/api/v1/audit-policies/{policy_id}` | Configure Audit Policies | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | DATABASE GAP GAP |
| API-13-011 | GET | `/api/v1/compliance-violations` | Monitor Compliance Violations | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-13-012 | GET | `/api/v1/audit-analytics` | Generate Audit Analytics | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |

### API-14 — Common Reference

- Module: `platform`
- OpenAPI tag default: Reference
- Flutter: digitize-ui/lib/features/reference
- Screens: UI-REF-001..UI-REF-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-14-001 | GET | `/api/v1/reference/countries` | List Countries | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-002 | GET | `/api/v1/reference/states-regions` | List States and Regions | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-003 | GET | `/api/v1/reference/currencies` | List Currencies | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-004 | GET | `/api/v1/reference/languages` | List Languages | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-005 | GET | `/api/v1/reference/timezones` | List Timezones | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-006 | GET | `/api/v1/reference/facility-types` | List Facility Types | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | tenant.facility_type |
| API-14-007 | GET | `/api/v1/reference/activity-types` | List Activity Types | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-008 | GET | `/api/v1/reference/status-values` | List Status Values | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-009 | GET | `/api/v1/reference/payment-methods` | List Payment Methods | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-010 | GET | `/api/v1/reference/communication-channels` | List Communication Channels | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-011 | GET | `/api/v1/reference/lookup-values/{reference_group}` | List Lookup Values | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-012 | GET | `/api/v1/reference/localization` | List Localization Values | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |

---

## 7. Missing contracts (REQUIRES DECISION)

Authentication HTTP contracts are **frozen** in
[AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md) and are **not** in the
228 count.

Organization / Facility / Site list and get are numbered API-02-015..020.

| Decision ID | Collection | Purpose | Status | Referenced by |
| --- | --- | --- | --- | --- |
| DECISION-AUTH-LOGIN | Authentication (`/api/v1/auth`) | Staff/user login | Frozen: `POST /api/v1/auth/login`. Not numbered. Not routed yet. | UI-AUTH-001; AUTH_CONTRACT_FREEZE.md |
| DECISION-AUTH-REFRESH | Authentication (`/api/v1/auth`) | Token refresh | Frozen: `POST /api/v1/auth/refresh`. Not numbered. Not routed yet. | AUTH_CONTRACT_FREEZE.md |
| DECISION-AUTH-LOGOUT | Authentication (`/api/v1/auth`) | Logout / session invalidation | Frozen: `POST /api/v1/auth/logout`. Not numbered. Not routed yet. | AUTH_CONTRACT_FREEZE.md |
| DECISION-AUTH-PASSWORD-RECOVERY | Authentication (`/api/v1/auth`) | Self-service password recovery | Frozen: `POST /api/v1/auth/password-reset` and `/confirm`. Distinct from API-03-009. Not routed yet. | UI-AUTH-002, UI-AUTH-003 |

Do not add Authentication endpoints to the 228 numbered inventory.

---

## 8. Database gaps

Mapped against `database/migrations/001`–`008` only. DB-11 may describe
additional tables; those remain a packaging gap from the database freeze.
Do not create tables in this gate.

| API ID | Missing / incomplete entity | Notes |
| --- | --- | --- |
| API-08-007 | `commercial.credit_note` | Credit notes are not in migration 005 |
| API-10-001..012 | `communication.advertisement_campaign` and campaign_* tables | Documented in DB-11; not created in 006 |
| API-10-014 | `communication.notification_rule` | No rule table in 001–008 |
| API-10-024 | `communication.notification_preference` | Called out in DATABASE_FOUNDATION_FREEZE |
| API-12-008 | `support.ticket_escalation` | Escalation table not created in 006 |
| API-13-010 | `audit.audit_policy` | No dedicated audit policy table (security.security_policy is a different entity) |
| API-13-011 | compliance violation entity | `audit.compliance_record` exists; violation-specific table does not |

---

## 9. Authorization, tenant, idempotency, concurrency

### Authorization

Known from API-01 / FR-02: API-01-001..010.
API-01-011 and API-02 through API-14: **TBD**. Do not invent a permission catalog.
Catalog extras `CAT-PLAN-001` and `CAT-CAPABILITY-001`: TBD.

### Tenant scope

Every numbered endpoint has an explicit scope. None are TBD.
Scaffold `/api/v1/users` remains TBD until retirement.
Headers `X-Organization-ID` / `X-Facility-ID` / `X-Site-ID` stay untrusted.

### Idempotency

REQUIRED (future store; table still deferred): membership create/renew,
walk-in create/payment, invoice generate, credit note, payment collect
online/offline, refund, SaaS subscription create/renew/renewal-invoice,
license generate/renew, notification generate/send/schedule/deliver/retry.

GET: NOT_REQUIRED. PATCH: NOT_REQUIRED (If-Match covers concurrency).
Other POST commands: TBD.

### Concurrency

All PATCH operations: IF_MATCH / `version_number`.
Do not add version columns. If a future PATCH target lacks
`version_number`, mark REQUIRES SCHEMA / DESIGN DECISION at implementation.

---

## 10. Frontend traceability

Flutter integration is **not** in this gate. Collection-level mapping:

| Collection | Flutter feature / module | Screens | Integration |
| --- | --- | --- | --- |
| API-01 | TBD — no digitize-ui platform-admin feature module yet | UI-PLT-001..UI-PLT-099 | NOT_STARTED |
| API-02 | digitize-ui/lib/features/organization, facility (mocks; Site TBD) | UI-ORG-001..UI-SITE-099 | NOT_STARTED |
| API-03 | digitize-ui/lib/features/authentication (mock only) | UI-IAM-001..UI-IAM-099 | NOT_STARTED |
| API-04 | TBD | UI-CUS-001..UI-CUS-099 | NOT_STARTED |
| API-05 | digitize-ui/lib/features/membership_plan (plans, not customer memberships) | UI-MEM-001..UI-MEM-099 | NOT_STARTED |
| API-06 | TBD | UI-ATT-001..UI-WLK-099 | NOT_STARTED |
| API-07 | TBD | UI-TRN-001..UI-BAT-099 | NOT_STARTED |
| API-08 | TBD | UI-BIL-001..UI-PAY-099 | NOT_STARTED |
| API-09 | TBD | UI-SUB-001..UI-LIC-099 | NOT_STARTED |
| API-10 | TBD | UI-NOT-001..UI-CMP-099 | NOT_STARTED |
| API-11 | TBD | UI-RPT-001..UI-ANA-099 | NOT_STARTED |
| API-12 | TBD | UI-SUP-001..UI-SUP-099 | NOT_STARTED |
| API-13 | TBD | UI-AUD-001..UI-SEC-099 | NOT_STARTED |
| API-14 | digitize-ui/lib/features/reference | UI-REF-001..UI-REF-099 | NOT_STARTED |

Login UI (`UI-AUTH-001`) maps to frozen
`POST /api/v1/auth/login` in [AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md).
Those routes are not registered until Authentication implementation.
Organization/Facility Flutter list/details screens have no numbered
list/get APIs (see DECISION-ORG-* / FACILITY-* / SITE-*).

---

## 11. OpenAPI

FastAPI generates OpenAPI. Do not maintain a second YAML catalog.

- Stable `operation_id` values (path + method, e.g. `organizations_create`)
- Capability tags listed in `app/main.py` `OPENAPI_TAGS`
- Live catalog operations keep existing 200/201/422 contracts
- Unimplemented numbered APIs are absent from OpenAPI until their vertical
- Internal types (SQLAlchemy session) must not appear in the schema

---

## 12. Tests

`tests/api/test_contract_registry.py` and `tests/api/test_module_routes.py`
check:

1. Every numbered endpoint has exactly one API ID and method/path in the
   registry (222 frozen).
2. No duplicate canonical URLs in the catalog or FastAPI app.
3. OpenAPI operation IDs are unique.
4. Live GMD / facility-types / SaaS catalog handlers remain registered.
5. Unimplemented numbered contracts are **not** registered at runtime.
6. No invented Authentication paths exist.
7. SaaS subscription and membership paths remain distinct in the registry.
8. Deferred `register_skeleton_routes` / `deferred()` helpers are gone.

---

## 13. Next gate

Do not start Authentication implementation until this freeze is the
implemented contract. The freeze itself is complete:

1. Engineering Foundation — COMPLETE (with deferred items)
2. API Contract Registry — COMPLETE (inventory frozen; runtime is live-only)
3. Authentication contract freeze — COMPLETE
   ([AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md))
4. Authentication End-to-End — NEXT (not started)
5. Platform Admin (API-01) — blocked until Authentication implementation passes
6. Organization → Facility → Site
7. remaining verticals

