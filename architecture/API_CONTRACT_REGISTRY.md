# DIGITIZE API Contract Registry

**Status:** API CONTRACTS READY WITH DEFERRED ITEMS
**Gate:** Contract / Skeleton Freeze
**Machine-readable canonical registry:** `digitize-services/app/api/contracts/api_registry.py` (all approved operation identities and row data)  
**Numbered contract enrichment:** `numbered_product_contracts.py` (EndpointContract metadata; numbered-subset validation only)  
**Unified implementation tracking:** `operation_tracking.py`  
**Unnumbered runtime endpoint catalogue:** `catalog.py` (FastAPI route discovery; not a second inventory)  
**Bottom-up route inventory:** `digitize-services/scripts/route_source_inventory.py`  
**Full inventory reconciliation (numbered + extras + runtime + source):** `digitize-services/scripts/api_inventory_reconciliation.py` → `var/api_inventory_reconciliation.json`  
**Evidence:** [API_INVENTORY_RECONCILIATION_2026-11-04.md](../16_Development_Readiness/evidence/API_INVENTORY_RECONCILIATION_2026-11-04.md)  
**Numbered inventory prose:** `docs/07_API_Collections/API-01` through `API-14`
**Client envelope:** `docs/07_API_Collections/API-00`
**Foundation:** [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md), [BACKEND_FOUNDATION.md](BACKEND_FOUNDATION.md)  
**Implementation progress tracker:** [DEV-19_Feature_Completion_Tracker.md](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md) (latest audit evidence; does not change this freeze inventory of **228** operations)  
**Pending decision packs:** [API-08 facility billing](API-08_FACILITY_BILLING_DECISION_REGISTER.md), [API-13 audit](API-13_AUDIT_PRODUCT_DECISION.md), [API-14 reference](API-14_REFERENCE_SOURCE_OF_TRUTH.md), [API-12-008 escalate](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md)

This registry is the authoritative **approved operation inventory** for Digitize.
**228 numbered operations are one layer only.** Additional approved operations
(in `api_registry.py` additional rows), runtime routes, WebSocket, documentation UI, and
unmounted source declarations are reconciled separately (see § Complete inventory).
It does not replace API-00..14 collection documents. Those remain the
verbose contract prose. This file freezes identity, ownership, status,
and implementation roadmap.

Do not invent endpoints because a CRUD operation seems useful.
Do not return fake 200 payloads for unimplemented operations.
Do not register unimplemented numbered APIs as runtime FastAPI routes.

---

## Complete API inventory reconciliation (2026-11-04)

Regenerate machine totals (complete approved registry):

```bash
cd digitize-services
poetry run python scripts/api_inventory_reconciliation.py
poetry run python scripts/contract_numbered_audit.py   # numbered subset only
```

### Unified implementation tracking (2026-11-04)

**Canonical approved inventory:** every operation in `api_registry.py`.  
**Implementation status owner:** `operation_tracking.py` (`OperationTrackingRecord` per stable ID).  
**Runtime reconciliation:** `catalog.py` validates against the **full** implemented set, not numbered-only keys.  
**Primary audit:** `api_inventory_reconciliation.py`.  
**Legacy numbered audit:** `contract_numbered_audit.py` (API-01…API-14 rows only — not overall product completion).

Public summary fields use unified names (`total_approved_operations`, `implemented_operations`, …). Do not use numbered/additional split fields as the main inventory view.

---

| Category | Count | Source |
| --- | ---: | --- |
| Numbered approved operations (API-01…API-14) | see `numbered_rows` in `registry_summary()` | `api_registry.py` / `numbered_contracts()` |
| Additional approved operations (`api_id` rows) | see `additional_rows` in `registry_summary()` | `api_registry.py` |
| **Total approved operation identities** | **386** | 228 + 158 (disjoint ID namespaces) |
| Numbered implemented (`BACKEND_IMPLEMENTED`, live route) | **204** | `IMPLEMENTED_NUMBERED_KEYS` |
| Numbered unimplemented skeletons | **24** | `skeleton_contracts()` |
| Additional OPS health probes (subset of 158) | **2** | `OPS-HEALTH-*` |
| Additional product extras (excl. OPS health) | **156** | extras − health |
| ORG-TERMS-001…006 (subset of extras) | **6** | not added on top of 156 |
| ORG-ONBOARDING-ACCEPT-001 (subset of extras) | **1** | same |
| Registered `/api/v1` HTTP `(method, path)` | **362** | 204 numbered live ∪ 158 extras (zero overlap) |
| Registered `/api/v1` WebSocket | **1** | support conversation WS |
| Documentation / OpenAPI UI routes | **2** | `/docs`, `/docs/oauth2-redirect` |
| Source route declarations (AST, all route files) | **364** | `route_source_inventory.py` |
| Unmounted source handlers | **0** | Legacy `app/modules/users/` removed (GAP-API03-005); API-03 identity canonical |
| Unmapped `/api/v1` HTTP at runtime | **0** | `validate_registered_endpoint_catalog()` |

**Do not describe 228 as total Digitize API count.**  
**Do not compute 228 + 6 = 234** (ORG-TERMS are within the 158 extras).  
**Do not compute 228 + 158 = 386 registered HTTP routes** — 386 is **approved identity rows**; only **362** are mounted HTTP product/ops routes (plus WS + docs).

### B. Layer differences explained

| Observation | Explanation |
| --- | --- |
| 386 identities vs 362 HTTP | 24 numbered skeletons have contracts but **no** route; extras are all mounted; identities ≠ mounted pairs. |
| 364 source declarations vs 365 registered pairs | AST/route-object granularity vs registered pairs; see `route_source_inventory.json` (no unmounted product handlers). |
| `unique_api_v1_method_path` 363 vs catalogue 362 | Inventory script may count an extra v1 pair (e.g. HEAD/OPTIONS granularity); catalogue excludes HEAD/OPTIONS and matches approved registry union. |

### C. Validation status

As of 2026-11-07: `validate_catalog()` **passes** (runtime + numbered).  
ORG-TERMS and onboarding acceptance are present in `EXTRA_OPERATIONS` and registered at runtime.

---

## 1. How to read a record

Every numbered endpoint is an `EndpointContract` with:

| Field | Meaning |
| --- | --- |
| catalog_id | Inventory identifier (`API-XX-NNN`). Not a runtime key. |
| inventory_group | Inventory group (`API-01`..`API-14`). Not a runtime key. |
| module | Semantic backend module (`platform`, `membership`, …) |
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

### Gate freeze snapshot (historical)

When this registry was last frozen for API-12 support wiring, the live catalog
reported:

| Backend status | Count |
| --- | --- |
| SKELETON_CREATED | 55 |
| BACKEND_IMPLEMENTED (numbered) | 173 |
| Numbered product total | 228 |

That historical snapshot is retained for audit of the freeze gate. It is **not**
the current implementation progress.

### Current backend status (machine audit — 2026-11-03)

Authoritative progress counts come from
`digitize-services/scripts/contract_numbered_audit.py` /
`app/api/contracts/numbered_product_contracts.py`, tracked in
[DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md):

| Backend status | Count |
| --- | --- |
| SKELETON_CREATED | 24 |
| BACKEND_IMPLEMENTED (numbered) | 204 |
| Numbered product total | 228 |

**Reconciliation (2026-11-03):** Re-ran `contract_numbered_audit.py` against the
current FastAPI app. All **204** `BACKEND_IMPLEMENTED` numbered contracts have a
matching registered `(method, path)`; all **24** `SKELETON_CREATED` contracts
have **no** runtime route (by design). Per-collection totals match the table in
§3 below (8+1+9+6 skeletons in API-08/12/13/14 only).

Per-row `backend_status` values in the collection tables below were refreshed
from the same audit on 2026-11-02 (**status column only**; contracts, paths,
auth, and semantics unchanged). Remaining skeletons: API-08 (8), API-12-008 (1),
API-13 (9), API-14 (6). Certification remains NOT_STARTED. Catalog
`BACKEND_IMPLEMENTED` means a live handler exists; it is **not** Flutter
INTEGRATED / CERTIFIED and does **not** imply database migrations were applied
to any environment.

### Registered HTTP inventory (2026-11-03 — do not merge with §3 totals)

| Layer | Count | Notes |
| --- | ---: | --- |
| Numbered contracts in catalog | 228 | Frozen product inventory (API-01…API-14) |
| Numbered routes live (`BACKEND_IMPLEMENTED`) | 204 | Disjoint from extras paths |
| Numbered skeletons (no route) | 24 | `SKELETON_CREATED`; not registered |
| Catalog `EXTRA_OPERATIONS` | 158 | All **158** have live routes; outside the 228 |
| — of which operational health | 2 | `OPS-HEALTH-001/002`; not product APIs |
| — of which additional approved product extras | 156 | Includes ORG-TERMS (6), ORG-ONBOARDING-ACCEPT-001, SaaS commerce, media, auth helpers, etc. |
| `/api/v1` `(method, path)` pairs on app | 362 | **204 numbered + 158 extras** (zero path overlap) |
| Non-product OpenAPI UI routes | 2 | `/docs`, `/docs/oauth2-redirect` |

**Do not add 228 + 156 and call it “234”.** The six ORG-TERMS operations are six
of the **156** additional approved extras, not an increment on top of them.
**Do not add 228 + 158** without stating that two entries are operational health
probes, not product features.

**Unique approved product HTTP operations (two-layer model, no double-count):**

| Category | Total | Implemented (live route) |
| --- | ---: | ---: |
| A. Numbered (API-01…API-14) | 228 | 204 |
| B. Additional approved extras (excl. OPS health) | 156 | 156 |
| C. ORG-TERMS-001…006 only (subset of B) | 6 | 6 |
| D. ORG-ONBOARDING-ACCEPT-001 (subset of B) | 1 | 1 |

Historical gate snapshot **173 / 55** implemented/skeleton remains in § “Gate
freeze snapshot” above; current machine truth is **204 / 24**.

### Exact 24 skeleton operations (2026-11-03)

| catalog_id | operation_id | Blocker class | Can implement now? |
| --- | --- | --- | --- |
| API-08-002 | billing_charges_calculate_create | Product + schema | **No** — charge catalog undefined |
| API-08-003 | invoices_discounts | Product + schema | **No** |
| API-08-004 | invoices_taxes_calculate | Product + schema | **No** |
| API-08-005 | invoices_adjustments | Product + schema | **No** |
| API-08-007 | invoices_credit_notes | Schema / migration | **No** — `database_gap` |
| API-08-009 | payments_online_create | Product + provider | **No** — Razorpay facility pay + schema |
| API-08-012 | payments_receipts | Product + schema | **No** |
| API-08-014 | reconciliations_create | Product deferred | **No** |
| API-12-008 | support_tickets_escalate | **Awaiting authorization** (DDL) | **No** — migration not approved/applied |
| API-13-001 | audit_events_create | Product deferred | **No** — non-client capture stance |
| API-13-002 | authentication_events_create | Product deferred | **No** |
| API-13-003 | audit_events_configuration_changes_create | Product deferred | **No** |
| API-13-004 | security_events_create | Schema blocked | **No** |
| API-13-006 | investigations_create | Schema blocked | **No** |
| API-13-007 | compliance_records_reports_create | Schema blocked | **No** |
| API-13-008 | audit_events_archive_create | Schema blocked | **No** |
| API-13-010 | audit_policies_update | Schema blocked | **No** |
| API-13-011 | compliance_violations_list | Schema blocked | **No** |
| API-14-001 | reference_countries_list | Product deferred (GMD) | **No** |
| API-14-002 | reference_states_regions_list | Product deferred (GMD) | **No** |
| API-14-004 | reference_languages_list | Product deferred | **No** |
| API-14-005 | reference_timezones_list | Product deferred | **No** |
| API-14-007 | reference_activity_types_list | Product deferred | **No** |
| API-14-012 | reference_localization_list | Product deferred | **No** |

None of the 24 are “authorized skeletons awaiting engineering only” in the
current decision registers; each requires product and/or schema/migration
approval before implementation.

### Bottom-up route source inventory (2026-11-03)

Route **source files** are the primary engineering evidence;
`scripts/route_source_inventory.py` reconciles them with the FastAPI app.
`catalog.py` holds the unnumbered runtime endpoint catalogue (362 `/api/v1` HTTP
routes by method + path). Numbered product IDs are mapped in
`numbered_product_contracts.py` and this registry document.

| Evidence | Location |
| --- | --- |
| Script | `digitize-services/scripts/route_source_inventory.py` |
| Per-file table | `digitize-services/var/route_source_per_file.csv` |
| Registered list | `digitize-services/var/route_registered_unique.csv` |
| Narrative | [ROUTE_SOURCE_INVENTORY_2026-11-03.md](../16_Development_Readiness/evidence/ROUTE_SOURCE_INVENTORY_2026-11-03.md) |

There is **no** `route.py` filename in this repo; inventory scans `routes.py`,
`routes_*.py`, `*_routes.py`, and `app/api/v1/health.py`.

| Count | Value |
| --- | ---: |
| Source declarations (route files) | **364** |
| Unique registered `(method, path)` on app | **365** (incl. 2× `/docs`) |
| Unique `/api/v1` HTTP | **362** (= **204** numbered live + **158** extras, post-hoc) |
| `/api/v1` WebSocket | **1** (support extra) |
| Unregistered source handlers | **0** (legacy `users` scaffold removed; GAP-API03-005) |

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
| OPS-HEALTH-001 | GET | `/api/v1/health/liveness` | Operational. Not in the 228 product count. Not API-00 enveloped. |
| OPS-HEALTH-002 | GET | `/api/v1/health/readiness` | Operational. Not in the 228 product count. Not API-00 enveloped. |
| CAT-FACILITY-TYPE-001 | GET | `/api/v1/facility-types` | Live catalog. Alias of API-14-006; this path is canonical for FK reads. |
| CAT-FACILITY-TYPE-002 | POST | `/api/v1/facility-types` | Create `tenant.facility_type`. Catalog extra. 201 with ETag. Not numbered. Not API-01 GMD. |
| CAT-FACILITY-TYPE-003 | GET | `/api/v1/facility-types/{facility_type_id}` | Item GET. List remains CAT-FACILITY-TYPE-001. |
| CAT-FACILITY-TYPE-004 | PATCH | `/api/v1/facility-types/{facility_type_id}` | Update type catalog row. If-Match required. |
| CAT-FACILITY-TYPE-005 | DELETE | `/api/v1/facility-types/{facility_type_id}` | Soft-deactivate (`is_active=false`). If-Match required. |
| CAT-FACILITY-FEATURE-001 | GET | `/api/v1/facility-features` | Paginated list of `facility.facility_features`. Catalog extra. Not numbered. |
| CAT-FACILITY-FEATURE-002 | POST | `/api/v1/facility-features` | Create a facility feature. Unique `feature_code`. |
| CAT-FACILITY-FEATURE-003 | GET | `/api/v1/facility-features/{feature_id}` | Item GET. |
| CAT-FACILITY-FEATURE-004 | PATCH | `/api/v1/facility-features/{feature_id}` | Update feature. System-defined rows cannot be updated. No If-Match. |
| CAT-FACILITY-FEATURE-005 | DELETE | `/api/v1/facility-features/{feature_id}` | Soft-deactivate (`is_active=false`). System-defined rows cannot be deactivated. |
| CAT-PLAN-001 | GET | `/api/v1/platform/subscription-plans` | Catalog read of commercial.subscription_plan, not API-09 lifecycle. |
| CAT-PLAN-002 | POST | `/api/v1/platform/subscription-plans` | Create SaaS plan. Not API-09 lifecycle. Unique `plan_code`. No audit event. No If-Match. |
| CAT-PLAN-003 | GET | `/api/v1/platform/subscription-plans/{plan_id}` | Item GET. List remains CAT-PLAN-001. Not API-09 lifecycle. |
| CAT-PLAN-004 | PATCH | `/api/v1/platform/subscription-plans/{plan_id}` | Update SaaS plan. Increments `version_number`. No If-Match. No audit event. |
| CAT-PLAN-005 | DELETE | `/api/v1/platform/subscription-plans/{plan_id}` | Sets `plan_status=INACTIVE`; does not delete the row. No If-Match. No audit event. |
| CAT-CAPABILITY-001 | GET | `/api/v1/platform/license-capabilities` | Catalog read of commercial.license_capability, not API-09 lifecycle. |
| SCAFFOLD-USERS-001 | GET | `/api/v1/users` | **Retired / not on v1 router** (2026-11-03). Legacy scaffold module; not in `EXTRA_OPERATIONS`. Do not expand. |
| SCAFFOLD-USERS-002 | POST | `/api/v1/users` | **Retired / not on v1 router** (2026-11-03). Same as above. |
| ORG-TERMS-001 | GET | `/api/v1/terms/current` | DR-021 onboarding T&C current published document. Outside 228. |
| ORG-TERMS-002 | GET | `/api/v1/terms` | PA list of T&C versions. Approved additional management op. Outside 228. |
| ORG-TERMS-003 | POST | `/api/v1/terms` | PA create T&C draft. Outside 228. |
| ORG-TERMS-004 | PATCH | `/api/v1/terms/{terms_id}` | PA edit T&C draft. Outside 228. |
| ORG-TERMS-005 | POST | `/api/v1/terms/{terms_id}/publish` | PA publish T&C draft. Outside 228. |
| ORG-TERMS-006 | GET | `/api/v1/terms/{terms_id}` | PA retrieve T&C document (preview/history). Outside 228. |
| ORG-ONBOARDING-ACCEPT-001 | POST | `/api/v1/organizations/{organization_id}/onboarding/accept` | OA accept current published T&C. Outside 228. |

These extras stay outside the product inventory. Machine authority for the
complete extras list is `digitize-services/app/api/contracts/api_registry.py`
(re-exported from `catalog.py` for audits). Official numbered product count remains **228**.

---

## 4. Canonical URLs and aliases

| Resource | Canonical URL | Alias / extra | Rule |
| --- | --- | --- | --- |
| Global master data | `/api/v1/platform/global-master-data` | none | Live API-01-003/004/005 |
| Facility types (FK catalog) | `/api/v1/facility-types` | `/api/v1/reference/facility-types` (API-14-006) | Live path is canonical for `tenant.facility_type`. List GET is CAT-FACILITY-TYPE-001; item GET/POST/PATCH/DELETE are CAT-FACILITY-TYPE-002..005. API-14-006 is a live alias of the same catalog; do not duplicate handlers. |
| Facility features | `/api/v1/facility-features` | none | Catalog extras CAT-FACILITY-FEATURE-001..005. Not numbered. |
| SaaS plans | `/api/v1/platform/subscription-plans` | none | Catalog extras CAT-PLAN-001..005; not API-09 lifecycle |
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

| Owner package | Contracts | Runtime today (status refresh 2026-11-02; see DEV-19) |
| --- | --- | --- |
| `platform` | API-01, API-14 | Live API-01 (11/11). API-14 live: 003, 006, 008–011; skeletons: 001, 002, 004, 005, 007, 012 |
| `organization` | API-02 organization paths | Live organization routes (with facility/site under facility module as implemented) |
| `facility` | API-02 facility and site paths | Live facility/site routes plus `/facility-types` and `/facility-features` extras |
| `users` / identity | API-03 identity | Live API-03 (12/12); legacy scaffold `/users` may still exist separately |
| `customer` | API-04 | Live API-04 (12/12) |
| `membership` | API-05 | Live API-05 (12/12) |
| `attendance` | API-06 attendance and walk-in | Live API-06 (15/15) |
| `training` | API-07 trainer, activity, batch, PT | Live API-07 (32/32) |
| `billing` | API-08 | Live 10/18; skeletons 002–005, 007, 009, 012, 014 |
| `subscription` | API-09 | Live API-09 (24/24) including SaaS commerce |
| `campaign` | API-10 campaign paths | Live with communication module (API-10 24/24) |
| `communication` | API-10 notification paths | Live with campaign module (API-10 24/24) |
| `reportsandanalytics` | API-11 | Live API-11 (12/12) |
| `support` | API-12 | Live 11 operations. API-12-008 is not registered. |
| `audit` | API-13 | Live reads: 005, 009, 012. Capture/schema ops remain skeleton |
| `staff` | models only | Staff HTTP covered under identity/API-03 live routes |

No `site`, `identity`, or `auth` package exists yet. Sites stay on
`facility`. Identity HTTP stays on `users` when API-03 starts.
Authentication paths are frozen in
[AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md) and must not be
registered until the Authentication implementation vertical.
Org/facility/site list/get remain REQUIRES DECISION and are not routed.

---

## 6. Numbered inventory

Full field records live in `app/api/contracts/numbered_product_contracts.py`.
Compact tables below are the human index.

### API-01 — Platform Admin

- Module: `platform`
- OpenAPI tag default: Platform Admin
- Flutter: TBD — no digitize-ui platform-admin feature module yet
- Screens: UI-PLT-001..UI-PLT-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-01-001 | GET | `/api/v1/platform/settings` | Retrieve Platform Settings | 200 | PLATFORM | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.platform_setting |
| API-01-002 | PATCH | `/api/v1/platform/settings/{setting_key}` | Update Platform Setting | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | platform.platform_setting |
| API-01-003 | GET | `/api/v1/platform/global-master-data` | Retrieve Global Master Data | 200 | PLATFORM | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-004 | POST | `/api/v1/platform/global-master-data` | Create Global Master Data Record | 201 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-005 | PATCH | `/api/v1/platform/global-master-data/{record_id}` | Update Global Master Data Record | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-01-006 | PATCH | `/api/v1/platform/feature-flags/{feature_code}` | Update Feature Flag State | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | platform.feature_flag |
| API-01-007 | POST | `/api/v1/platform/maintenance-windows` | Schedule Maintenance Window | 201 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.maintenance_window |
| API-01-008 | POST | `/api/v1/platform/releases/{record_id}/publish` | Publish Platform Release | 200 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.release_record |
| API-01-009 | GET | `/api/v1/platform/health` | Retrieve Platform Health Summary | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | — |
| API-01-010 | PATCH | `/api/v1/platform/security-policies/{record_id}` | Update Platform Security Policy | 200 | PLATFORM | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | security.security_policy |
| API-01-011 | POST | `/api/v1/platform/reports/executions` | Generate Platform Report | 202 | PLATFORM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution |

### API-02 — Organization / Facility / Site

- Module: `organization / facility`
- OpenAPI tag default: Organizations
- Flutter: digitize-ui/lib/features/organization, facility (mocks; Site TBD)
- Screens: UI-ORG-001..UI-SITE-099
- **Live numbered operations remain API-02-001..020.** Parentage is transitioning under DR-023: `POST /sites` accepts `organization_id` (facility_id optional for compatibility); `POST /facilities` requires `site_id`; `GET /sites` accepts `organization_id` or `facility_id`. Do not renumber. `tenant.site.facility_id` is retained until a removal gate. Mechanics: [DR-023_HIERARCHY_MIGRATION_PLAN.md](DR-023_HIERARCHY_MIGRATION_PLAN.md).

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
| API-03-001 | POST | `/api/v1/identity/staff-accounts` | Create Staff Account | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-002 | PATCH | `/api/v1/identity/staff-profiles/{staff_profile_id}` | Update Staff Profile | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-003 | POST | `/api/v1/identity/role-assignments` | Assign Staff Role | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-004 | POST | `/api/v1/identity/access-scopes/facility` | Assign Facility Access | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-005 | POST | `/api/v1/identity/access-scopes/site` | Assign Site Access | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-006 | PATCH | `/api/v1/identity/roles/{role_id}/permissions` | Configure Staff Permissions | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-007 | POST | `/api/v1/identity/users/{user_id}/activate` | Activate Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-008 | POST | `/api/v1/identity/users/{user_id}/suspend` | Suspend Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-009 | POST | `/api/v1/identity/users/{user_id}/credential-reset` | Reset Staff Credentials | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-010 | POST | `/api/v1/identity/users/{user_id}/deactivate` | Deactivate Staff Account | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-011 | GET | `/api/v1/identity/users/{user_id}/activity` | View Staff Activity | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |
| API-03-012 | GET | `/api/v1/identity/staff-directory` | View Staff Directory | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | identity.user_account, identity.staff_profile, identity.role, identity.role_assignment, identity.access_scope |

### API-04 — Customer

- Module: `customer`
- OpenAPI tag default: Customers
- Flutter: TBD
- Screens: UI-CUS-001..UI-CUS-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-04-001 | POST | `/api/v1/customers` | Register Customer | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-002 | PATCH | `/api/v1/customers/{customer_id}` | Update Customer Profile | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-003 | POST | `/api/v1/customers/{customer_id}/verify-identity` | Verify Customer Identity | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-004 | GET | `/api/v1/customers` | Search Customers | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-005 | GET | `/api/v1/customers/{customer_id}` | View Customer Profile | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-006 | POST | `/api/v1/customers/{customer_id}/transfer-site` | Transfer Customer Between Sites | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-007 | POST | `/api/v1/customers/{customer_id}/suspend` | Suspend Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-008 | POST | `/api/v1/customers/{customer_id}/reactivate` | Reactivate Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-009 | POST | `/api/v1/customers/{customer_id}/archive` | Archive Customer | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-010 | POST | `/api/v1/customers/{customer_id}/documents` | Manage Customer Document Metadata | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-011 | POST | `/api/v1/customers/{customer_id}/emergency-contacts` | Manage Emergency Contacts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |
| API-04-012 | GET | `/api/v1/customers/{customer_id}/history` | View Customer History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | customer.customer, customer.customer_history |

### API-05 — Membership

- Module: `membership`
- OpenAPI tag default: Memberships
- Flutter: digitize-ui/lib/features/membership_plan (plans, not customer memberships)
- Screens: UI-MEM-001..UI-MEM-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-05-001 | POST | `/api/v1/memberships` | Create Membership | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-002 | POST | `/api/v1/memberships/{membership_id}/activate` | Activate Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-003 | POST | `/api/v1/memberships/{membership_id}/renewals` | Renew Membership | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-004 | POST | `/api/v1/memberships/{membership_id}/upgrade` | Upgrade Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-005 | POST | `/api/v1/memberships/{membership_id}/downgrade` | Downgrade Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-006 | POST | `/api/v1/memberships/{membership_id}/freeze` | Freeze Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-007 | POST | `/api/v1/memberships/{membership_id}/resume` | Resume Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-008 | POST | `/api/v1/memberships/{membership_id}/transfer` | Transfer Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-009 | POST | `/api/v1/memberships/{membership_id}/cancel` | Cancel Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-010 | POST | `/api/v1/memberships/{membership_id}/expire` | Expire Membership | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-011 | GET | `/api/v1/memberships/{membership_id}` | View Membership Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |
| API-05-012 | GET | `/api/v1/memberships/{membership_id}/history` | View Membership History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | membership.customer_membership, membership.membership_plan, membership.membership_lifecycle_history |

### API-06 — Attendance / Walk-in

- Module: `attendance`
- OpenAPI tag default: Attendance
- Flutter: TBD
- Screens: UI-ATT-001..UI-WLK-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-06-001 | POST | `/api/v1/attendance/check-in` | Record Customer Check-in | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-002 | POST | `/api/v1/attendance/eligibility` | Validate Attendance Eligibility | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-003 | POST | `/api/v1/attendance/session` | Record Session Attendance | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-004 | POST | `/api/v1/attendance/walk-in` | Record Walk-in Attendance | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-005 | POST | `/api/v1/attendance/{attendance_id}/check-out` | Record Customer Check-out | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-006 | PATCH | `/api/v1/attendance/{attendance_id}` | Update Attendance Record | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-007 | POST | `/api/v1/attendance/{attendance_id}/cancel` | Cancel Attendance Record | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-008 | GET | `/api/v1/customers/{customer_id}/attendance-history` | View Attendance History | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-009 | GET | `/api/v1/attendance/reports` | Generate Attendance Report | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-010 | GET | `/api/v1/attendance/{attendance_id}/audit` | Audit Attendance Records | 200 | SITE | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.attendance |
| API-06-011 | POST | `/api/v1/walkin-visits/identify` | Identify or Register Walk-in Customer | 201 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.walkin_visit |
| API-06-012 | POST | `/api/v1/walkin-visits` | Create Walk-in Visit | 201 | SITE | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.walkin_visit |
| API-06-013 | POST | `/api/v1/walkin-visits/{walkin_visit_id}/charges` | Calculate Walk-in Charges | 200 | SITE | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.walkin_visit |
| API-06-014 | POST | `/api/v1/walkin-visits/{walkin_visit_id}/payments` | Associate Walk-in Payment | 200 | SITE | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.walkin_visit |
| API-06-015 | GET | `/api/v1/walkin-visits` | View Walk-in History and Reports | 200 | SITE | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | operations.walkin_visit |

### API-07 — Trainer / Activity / Batch

- Module: `training`
- OpenAPI tag default: Trainers
- Flutter: TBD
- Screens: UI-TRN-001..UI-BAT-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-07-001 | POST | `/api/v1/trainers` | Register Trainer Profile | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-002 | POST | `/api/v1/trainers/{trainer_id}/facility-assignments` | Assign Trainer to Facilities and Sites | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-003 | POST | `/api/v1/trainers/{trainer_id}/availability` | Maintain Trainer Availability | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-004 | POST | `/api/v1/trainers/{trainer_id}/schedule-conflicts` | Validate Trainer Schedule Conflicts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-005 | POST | `/api/v1/batches/{batch_id}/trainer-assignment` | Assign Trainer to Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-006 | POST | `/api/v1/personal-training-sessions/{session_id}/trainer-assignment` | Assign Trainer to Personal Training Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-007 | POST | `/api/v1/trainers/{trainer_id}/attendance` | Record Trainer Attendance | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-008 | POST | `/api/v1/trainers/{trainer_id}/status` | Manage Trainer Status | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-009 | GET | `/api/v1/trainers/{trainer_id}/history` | View Trainer History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-010 | GET | `/api/v1/trainers/{trainer_id}/performance-summary` | Generate Trainer Performance Summary | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.trainer, training.trainer_assignment |
| API-07-011 | POST | `/api/v1/activities` | Create Activity | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.activity |
| API-07-012 | PATCH | `/api/v1/activities/{activity_id}` | Update Activity | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | training.activity |
| API-07-013 | POST | `/api/v1/activities/{activity_id}/rules` | Configure Activity Rules | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.activity |
| API-07-014 | POST | `/api/v1/batches` | Create Batch | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-015 | PATCH | `/api/v1/batches/{batch_id}` | Update Batch | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | training.batch |
| API-07-016 | POST | `/api/v1/batches/{batch_id}/schedule` | Schedule Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-017 | POST | `/api/v1/batches/{batch_id}/capacity` | Configure Batch Capacity | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-018 | POST | `/api/v1/batches/{batch_id}/enrollments` | Enroll Customer into Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-019 | POST | `/api/v1/batches/{batch_id}/enrollments/{enrollment_id}/remove` | Remove Customer from Batch | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-020 | POST | `/api/v1/class-sessions/{session_id}/start` | Start Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.class_session |
| API-07-021 | POST | `/api/v1/class-sessions/{session_id}/complete` | Complete Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.class_session |
| API-07-022 | POST | `/api/v1/class-sessions/{session_id}/cancel` | Cancel Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.class_session |
| API-07-023 | GET | `/api/v1/batches/{batch_id}/schedule` | View Batch Schedule | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.batch |
| API-07-024 | GET | `/api/v1/activities/{activity_id}/performance` | View Activity Performance | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.activity |
| API-07-025 | POST | `/api/v1/personal-training-packages` | Create Personal Training Package | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-026 | PATCH | `/api/v1/personal-training-packages/{package_id}/configuration` | Configure Training Package | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-027 | POST | `/api/v1/personal-training-sessions` | Book Personal Training Session | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-028 | POST | `/api/v1/personal-training-sessions/{session_id}/reschedule` | Reschedule Training Session | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-029 | POST | `/api/v1/personal-training-sessions/{session_id}/notes` | Record Training Notes | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |
| API-07-030 | POST | `/api/v1/customers/{customer_id}/progress` | Record Customer Progress | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.customer_progress |
| API-07-031 | GET | `/api/v1/customers/{customer_id}/training-history` | View Training History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.customer_progress |
| API-07-032 | GET | `/api/v1/personal-training/reports/trainer-performance` | Generate Trainer Performance Report | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | training.personal_training_package, training.personal_training_session |

### API-08 — Billing / Payment

- Module: `billing`
- OpenAPI tag default: Billing
- Flutter: TBD
- Screens: UI-BIL-001..UI-PAY-099

**Schema naming (facility vs SaaS):** Facility operational billing persists under PostgreSQL **`billing.*`** (migrations 063, 069, 074–082). Early design drafts labeled the same logical domain `commercial.*`; that label remains authoritative for **API-09 SaaS** (`commercial.subscription`, `commercial.license`, …). Do not conflate the two schemas.

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-08-001 | POST | `/api/v1/invoices` | Generate Invoice | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.invoices, billing.invoice_items |
| API-08-002 | POST | `/api/v1/billing/charges/calculate` | Calculate Service Charges | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | billing.billing_settings |
| API-08-003 | POST | `/api/v1/invoices/{invoice_id}/discounts` | Apply Discounts | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | billing.invoices, billing.invoice_line_discounts |
| API-08-004 | POST | `/api/v1/invoices/{invoice_id}/taxes/calculate` | Calculate Taxes | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | billing.invoices, billing.invoice_items |
| API-08-005 | POST | `/api/v1/invoices/{invoice_id}/adjustments` | Apply Billing Adjustments | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | billing.invoices |
| API-08-006 | POST | `/api/v1/invoices/{invoice_id}/cancel` | Cancel Invoice | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.invoices, billing.invoice_items |
| API-08-007 | POST | `/api/v1/invoices/{invoice_id}/credit-notes` | Generate Credit Note | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED (route); services/mig 080 | billing.credit_notes, billing.credit_note_invoice_applications |
| API-08-008 | POST | `/api/v1/payments` | Collect Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.payments, billing.receipts |
| API-08-009 | POST | `/api/v1/payments/online` | Process Online Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | billing.payment_transactions, billing.payments |
| API-08-010 | POST | `/api/v1/payments/offline` | Record Offline Payment | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.payments, billing.receipts |
| API-08-011 | GET | `/api/v1/payments/{payment_id}/status` | Verify Payment Status | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.payments, billing.invoices |
| API-08-012 | POST | `/api/v1/payments/{payment_id}/receipts` | Generate Payment Receipt | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED (numbered route) | billing.receipts |
| API-08-013 | POST | `/api/v1/payments/{payment_id}/refunds` | Process Refund | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.refunds, billing.payments |
| API-08-014 | POST | `/api/v1/reconciliations` | Reconcile Payment | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | billing.payment_reconciliations |
| API-08-015 | POST | `/api/v1/payments/{payment_id}/cancel` | Cancel Payment | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.payments |
| API-08-016 | GET | `/api/v1/billing/history` | View Billing and Payment History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.invoices, billing.payments, billing.financial events |
| API-08-017 | GET | `/api/v1/commercial/reports` | Generate Commercial Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.invoices, billing.payments (revenue alias) |
| API-08-018 | GET | `/api/v1/billing/outstanding-statements` | Generate Outstanding Statement | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | billing.invoices, billing.payments |

### API-09 — Subscription / License

- Module: `subscription`
- OpenAPI tag default: Subscriptions
- Flutter: TBD
- Screens: UI-SUB-001..UI-LIC-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-09-001 | POST | `/api/v1/subscriptions` | Create Subscription | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-002 | POST | `/api/v1/subscriptions/{subscription_id}/plan-assignment` | Assign Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-003 | POST | `/api/v1/subscriptions/{subscription_id}/activate` | Activate Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-004 | POST | `/api/v1/subscriptions/{subscription_id}/renew` | Renew Subscription | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-005 | POST | `/api/v1/subscriptions/{subscription_id}/upgrade` | Upgrade Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-006 | POST | `/api/v1/subscriptions/{subscription_id}/downgrade` | Downgrade Subscription Plan | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-007 | POST | `/api/v1/subscriptions/{subscription_id}/suspend` | Suspend Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-008 | POST | `/api/v1/subscriptions/{subscription_id}/cancel` | Cancel Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-009 | POST | `/api/v1/subscriptions/{subscription_id}/expire` | Expire Subscription | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-010 | POST | `/api/v1/subscriptions/{subscription_id}/renewal-invoices` | Generate Renewal Invoice | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-011 | GET | `/api/v1/subscriptions/{subscription_id}/history` | View Subscription History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-012 | GET | `/api/v1/subscriptions/reports` | Generate Subscription Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.subscription, commercial.subscription_plan |
| API-09-013 | POST | `/api/v1/licenses` | Generate License | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-014 | POST | `/api/v1/licenses/{license_id}/facility-assignment` | Assign License to Facility | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-015 | POST | `/api/v1/licenses/{license_id}/activate` | Activate License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-016 | POST | `/api/v1/licenses/{license_id}/renew` | Renew License | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-017 | PATCH | `/api/v1/licenses/{license_id}/capabilities` | Modify Licensed Capabilities | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-018 | POST | `/api/v1/licenses/{license_id}/suspend` | Suspend License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-019 | POST | `/api/v1/licenses/{license_id}/expire` | Expire License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-020 | POST | `/api/v1/licenses/{license_id}/cancel` | Cancel License | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-021 | POST | `/api/v1/licenses/validate-login` | Validate License During Login | 201 | SYSTEM | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-022 | GET | `/api/v1/licenses/{license_id}` | View License Details | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-023 | GET | `/api/v1/licenses/{license_id}/history` | View License History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |
| API-09-024 | GET | `/api/v1/licenses/reports` | Generate License Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | commercial.license, commercial.license_assignment |

### API-10 — Notification / Campaign

- Module: `communication`
- OpenAPI tag default: Notifications
- Flutter: TBD
- Screens: UI-NOT-001..UI-CMP-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-10-001 | POST | `/api/v1/campaigns` | Create Campaign | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-002 | PATCH | `/api/v1/campaigns/{campaign_id}/configuration` | Configure Campaign | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-003 | POST | `/api/v1/campaigns/{campaign_id}/audiences` | Select Target Audience | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-004 | POST | `/api/v1/campaigns/{campaign_id}/submit-for-approval` | Submit Campaign for Approval | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-005 | POST | `/api/v1/campaigns/{campaign_id}/approve` | Approve Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-006 | POST | `/api/v1/campaigns/{campaign_id}/schedule` | Schedule Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-007 | POST | `/api/v1/campaigns/{campaign_id}/launch` | Launch Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-008 | POST | `/api/v1/campaigns/{campaign_id}/pause` | Pause Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-009 | POST | `/api/v1/campaigns/{campaign_id}/complete` | Complete Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-010 | POST | `/api/v1/campaigns/{campaign_id}/cancel` | Cancel Campaign | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-011 | GET | `/api/v1/campaigns/{campaign_id}/performance` | Monitor Campaign Performance | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-012 | GET | `/api/v1/campaigns/{campaign_id}/reports` | Generate Campaign Report | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | DATABASE GAP GAP |
| API-10-013 | POST | `/api/v1/notification-templates` | Create Notification Template | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-014 | POST | `/api/v1/notification-rules` | Configure Notification Rules | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification_template GAP |
| API-10-015 | POST | `/api/v1/notifications/system` | Generate System Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-016 | POST | `/api/v1/notifications/manual` | Send Manual Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-017 | POST | `/api/v1/notifications/schedule` | Schedule Notification | 201 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-018 | POST | `/api/v1/notifications/{notification_id}/deliver` | Deliver Notification | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-019 | POST | `/api/v1/notifications/{notification_id}/retry` | Retry Failed Notification | 200 | FACILITY | NOT_APPLICABLE | REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-020 | GET | `/api/v1/notifications` | View Notification History | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-021 | GET | `/api/v1/notifications/{notification_id}/delivery-status` | Track Delivery Status | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-022 | POST | `/api/v1/notifications/{notification_id}/archive` | Archive Notification | 200 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-023 | GET | `/api/v1/notifications/reports` | Generate Notification Reports | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | communication.notification, communication.notification_template, communication.notification_delivery |
| API-10-024 | PATCH | `/api/v1/notification-preferences/{preference_id}` | Manage Notification Preferences | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | `customer.customer_preference` (migration 004; GAP-API10-004 cleared) |

### API-11 — Reports / Analytics

- Module: `reportsandanalytics`
- OpenAPI tag default: Reports
- Flutter: TBD
- Screens: UI-RPT-001..UI-ANA-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-11-001 | GET | `/api/v1/dashboards/operational` | View Operational Dashboard | 200 | FACILITY | NOT_APPLICABLE | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-002 | POST | `/api/v1/reports/membership` | Generate Membership Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-003 | POST | `/api/v1/reports/attendance` | Generate Attendance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-004 | POST | `/api/v1/reports/revenue` | Generate Revenue Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-005 | POST | `/api/v1/reports/customer` | Generate Customer Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-006 | POST | `/api/v1/reports/trainer-performance` | Generate Trainer Performance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-007 | POST | `/api/v1/reports/activity-performance` | Generate Activity Performance Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-008 | POST | `/api/v1/reports/subscription` | Generate Subscription Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-009 | POST | `/api/v1/report-executions/{execution_id}/exports` | Export Report | 202 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-010 | POST | `/api/v1/report-schedules` | Schedule Automated Report | 201 | FACILITY | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-011 | GET | `/api/v1/kpis` | Monitor Business KPIs | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |
| API-11-012 | GET | `/api/v1/reports/historical-trends` | View Historical Trends | 200 | FACILITY | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | reporting.report_definition, reporting.report_execution, reporting.dashboard_configuration, reporting.kpi_definition |

### API-12 — Support Tickets

- Module: `support`
- OpenAPI tag default: Support
- Flutter: `digitize-ui/lib/features/support_tickets`
- Screens: list, create, and detail under `/support-tickets`

Statuses used by the live handlers are `OPEN`, `ACCEPTED`, `RESOLVED`, and
`CLOSED`. Classify, assign, priority, progress, and information requests do
not change status. API-12-008 is not registered because `support.ticket_escalation`
does not exist. Migration `070_support_ticket_permissions` is created and not
applied. Upgrading to 070 also applies unapplied migration 069; do not apply
either in this phase.

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-12-001 | POST | `/api/v1/support-tickets` | Create Support Ticket | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket |
| API-12-002 | POST | `/api/v1/support-tickets/{ticket_id}/classify` | Classify Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_category |
| API-12-003 | POST | `/api/v1/support-tickets/{ticket_id}/assign` | Assign Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_assignment |
| API-12-004 | POST | `/api/v1/support-tickets/{ticket_id}/priority` | Set Ticket Priority | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_priority |
| API-12-005 | POST | `/api/v1/support-tickets/{ticket_id}/accept` | Accept Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-006 | PATCH | `/api/v1/support-tickets/{ticket_id}/progress` | Update Ticket Progress | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-007 | POST | `/api/v1/support-tickets/{ticket_id}/information-requests` | Request Additional Information | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-008 | POST | `/api/v1/support-tickets/{ticket_id}/escalate` | Escalate Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | support.ticket_escalation GAP |
| API-12-009 | POST | `/api/v1/support-tickets/{ticket_id}/resolve` | Resolve Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-010 | POST | `/api/v1/support-tickets/{ticket_id}/close` | Close Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-011 | POST | `/api/v1/support-tickets/{ticket_id}/reopen` | Reopen Ticket | 200 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket, support.ticket_comment |
| API-12-012 | GET | `/api/v1/support-tickets/reports` | Generate Support Reports | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | support.support_ticket |

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
| API-13-005 | GET | `/api/v1/audit-events` | Review Audit Logs | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | audit.audit_event |
| API-13-006 | POST | `/api/v1/investigations` | Investigate Audit Records | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-007 | POST | `/api/v1/compliance-records/reports` | Generate Compliance Report | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-008 | POST | `/api/v1/audit-events/archive` | Archive Audit Records | 201 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | SKELETON_CREATED | audit.audit_event |
| API-13-009 | POST | `/api/v1/audit-events/export` | Export Audit History | 202 | ORGANIZATION | NOT_APPLICABLE | TBD | NOT_APPLICABLE | BACKEND_IMPLEMENTED | audit.audit_event |
| API-13-010 | PATCH | `/api/v1/audit-policies/{policy_id}` | Configure Audit Policies | 200 | ORGANIZATION | NOT_APPLICABLE | NOT_REQUIRED | IF_MATCH | SKELETON_CREATED | DATABASE GAP GAP |
| API-13-011 | GET | `/api/v1/compliance-violations` | Monitor Compliance Violations | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | DATABASE GAP GAP |
| API-13-012 | GET | `/api/v1/audit-analytics` | Generate Audit Analytics | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | audit.audit_event |

### API-14 — Common Reference

- Module: `platform`
- OpenAPI tag default: Reference
- Flutter: digitize-ui/lib/features/reference
- Screens: UI-REF-001..UI-REF-099

| API ID | Method | Path | Purpose | Success | Scope | Page | Idem | Concurrency | Backend | DB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-14-001 | GET | `/api/v1/reference/countries` | List Countries | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-002 | GET | `/api/v1/reference/states-regions` | List States and Regions | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-003 | GET | `/api/v1/reference/currencies` | List Currencies | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-14-004 | GET | `/api/v1/reference/languages` | List Languages | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-005 | GET | `/api/v1/reference/timezones` | List Timezones | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-006 | GET | `/api/v1/reference/facility-types` | List Facility Types | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | tenant.facility_type |
| API-14-007 | GET | `/api/v1/reference/activity-types` | List Activity Types | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | SKELETON_CREATED | platform.global_master_data |
| API-14-008 | GET | `/api/v1/reference/status-values` | List Status Values | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-14-009 | GET | `/api/v1/reference/payment-methods` | List Payment Methods | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-14-010 | GET | `/api/v1/reference/communication-channels` | List Communication Channels | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
| API-14-011 | GET | `/api/v1/reference/lookup-values/{reference_group}` | List Lookup Values | 200 | ORGANIZATION | OFFSET | NOT_REQUIRED | NOT_APPLICABLE | BACKEND_IMPLEMENTED | platform.global_master_data |
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
| ~~API-10-024~~ | — | **Not a gap** — live `NotificationPreferenceService` persists to `customer.customer_preference` (004); catalog entity aligned (GAP-API10-004). DB-11 `communication.notification_preference` not used. |
| API-12-008 | `support.ticket_escalation` | Escalation table not created in 006 |
| API-13-010 | `audit.audit_policy` | No dedicated audit policy table (security.security_policy is a different entity) |
| API-13-011 | compliance violation entity | `audit.compliance_record` exists; violation-specific table does not |

---

## 9. Authorization, tenant, idempotency, concurrency

### Authorization

Known from API-01 / FR-02: API-01-001..010.
API-01-011 and API-02 through API-14: **TBD**. Do not invent a permission catalog.
Catalog extras `CAT-PLAN-001` and `CAT-CAPABILITY-001`: TBD.
Catalog extras `CAT-PLAN-002` create, `CAT-PLAN-003` get, `CAT-PLAN-004` /
`CAT-PLAN-005` update-or-deactivate: `platform.masterdata.create` /
`platform.masterdata.view` / `platform.masterdata.update`.
Facility-type item/write extras `CAT-FACILITY-TYPE-002..005` and
facility-feature write/get extras `CAT-FACILITY-FEATURE-002..005` use the
same `platform.masterdata.*` family. `CAT-FACILITY-FEATURE-001` list GET: TBD.

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

All numbered PATCH operations: IF_MATCH / `version_number`.
Do not add version columns. If a future PATCH target lacks
`version_number`, mark REQUIRES SCHEMA / DESIGN DECISION at implementation.

Catalog extras `CAT-PLAN-004` and `CAT-FACILITY-FEATURE-004` currently
PATCH without If-Match. `CAT-PLAN-005` sets `plan_status=INACTIVE` without
If-Match or an audit event. Plan create/update/deactivate extras do not
write `audit.audit_event`. These are recorded limitations, not a behavior
change in this registry update.

---

## 10. Frontend traceability

Collection-level Flutter mapping for **metadata only**. Machine authority:
`COLLECTION_META` and `_COLLECTION_FRONTEND_STATUS` in
`digitize-services/app/api/contracts/numbered_product_contracts.py`
(regression: `tests/api/test_collection_metadata_drift.py`; GAP-API01-003,
GAP-API08-010, GAP-API09-004, GAP-API11-004).

| Collection | Flutter feature / module | Screens | Integration |
| --- | --- | --- | --- |
| API-01 | digitize-ui/lib/features/platform_administration (RemotePlatformAdministrationRepository) | UI-PLT-001..UI-PLT-099 | INTEGRATED |
| API-02 | digitize-ui/lib/features/organization, facility (mocks; Site TBD) | UI-ORG-001..UI-SITE-099 | NOT_STARTED |
| API-03 | digitize-ui/lib/features/authentication (mock only) | UI-IAM-001..UI-IAM-099 | NOT_STARTED |
| API-04 | TBD | UI-CUS-001..UI-CUS-099 | NOT_STARTED |
| API-05 | digitize-ui/lib/features/membership_plan (plans, not customer memberships) | UI-MEM-001..UI-MEM-099 | NOT_STARTED |
| API-06 | TBD | UI-ATT-001..UI-WLK-099 | NOT_STARTED |
| API-07 | TBD | UI-TRN-001..UI-BAT-099 | NOT_STARTED |
| API-08 | digitize-ui/lib/features/organization/application/billing (outstanding, history; facility billing remotes) | UI-BIL-001..UI-PAY-099 | PARTIAL |
| API-09 | digitize-ui/lib/features/saas_subscription_admin (RemoteSubscriptionAdminRepository; open-by-ID admin slice) | UI-SUB-001..UI-LIC-099 | PARTIAL |
| API-10 | TBD | UI-NOT-001..UI-CMP-099 | NOT_STARTED |
| API-11 | digitize-ui/lib/features/reporting (RemoteReportingRepository; /organization/reports) | UI-RPT-001..UI-ANA-099 | INTEGRATED |
| API-12 | digitize-ui/lib/features/support_tickets | list, create, detail | FRONTEND_IMPLEMENTED for 11 operations. API-12-008 is not wired. |
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
4. Live GMD / facility-types / facility-features / SaaS catalog handlers remain registered. Approved catalog extras stay outside the 228.
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
6. Organization → Facility → Site (live; DR-004). DR-023 Proposed would invert Site above Facility after a separate contract and migration go-ahead — not this gate.
7. remaining verticals

