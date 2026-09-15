# API-04 CUSTOMER PRE-IMPLEMENTATION GATE

**Status:** PRE-IMPLEMENTATION GATE PASS  
**Date:** 2026-09-12  
**Scope:** Contract, database, ORM, authorization, tenancy, lifecycle, and architecture reconciliation only.  
**Does not implement API-04.**

PASS means API-04 can be implemented without architectural redesign. Remaining work is first-slice implementation (permission seed, additive typed home-facility/home-site columns, authoritative ORM, HTTP/service/repository), classified **P2**.

Authoritative sources for this gate, in descending order when they conflict:

1. `docs/architecture/API_CONTRACT_REGISTRY.md` and `app/api/contracts/catalog.py` / `operations.py` (numbered identity, paths, counts, operation IDs, HTTP status, If-Match, pagination, tenant scope)
2. `database/migrations/001`–`012` and twins under `database/migrations/` (physical schema; history frozen)
3. `docs/architecture/AUTH_CONTRACT_FREEZE.md` (authentication, Principal, 401 family)
4. `docs/architecture/BACKEND_CODING_STANDARDS.md` and `NAMING_AUDIT.md` (layering, API-00, UoW, semantic authorization/audit names)
5. Live API-01 / API-02 / API-03 implementation (`app/modules/platform`, `organization`, `facility`, `identity`)
6. `docs/07_API_Collections/API-04_Customer_Management_Collection.md` (verbose request/response/audit prose; **not** path, error-code, If-Match, or idempotency authority)
7. `docs/04_Functional_Requirements/FR-07_Customer_Management.md` (business intent)
8. `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md` and `DATABASE_FOUNDATION_FREEZE.md` (schema commentary)

The design-draft OpenAPI file `docs/07_API_Collections/openapi/API-04_Customer_Management_OpenAPI.yaml` is **not** authoritative.

Authentication is already implemented. `/api/v1/auth/*` is live supporting infrastructure **outside** the 222. API-04 is **staff-operated** customer administration. It does not create Customer logins, Customer UserAccounts, or a Customer portal.

---

## 1. Executive Summary

API-04 is **organization-owned, facility-authorized customer master data**:

- register a Customer under one Organization
- update profile
- record identity-verification outcome (staff-recorded; not Customer authentication)
- search and view
- transfer primary Site
- suspend / reactivate / archive
- manage document **metadata**
- manage emergency contacts
- view customer history

API-04 is **not**:

- Customer authentication or self-registration
- Staff / UserAccount / Role administration (API-03)
- Membership purchase or membership lifecycle (API-05)
- Attendance / walk-in (API-06)
- Billing / payment (API-08)
- Notifications (API-10)
- File binary upload/download (object-storage vertical / IC-06)
- Family membership graphs
- Customer merge, bulk import, or hard DELETE

The physical customer schema **already exists** in migration `004` (`customer.customer` and related tables). It is **authoritative but incomplete** for primary Facility/Site, which FR-CUS-001 and API-04-006 require and which the current DDL does not type as columns. Implementation needs:

1. Additive Alembic `013` (typed home facility/site, verification status, phone uniqueness) plus permission seed
2. Authoritative ORM mapped to `customer.customer` / `record_id` (quarantine the scaffold `customer.customers` models)
3. HTTP/service/repository on the existing authorization, audit, envelope, and ETag stack

Live numbered handlers today: **none** of the 12. `GET`/`POST /api/v1/customers` currently 404 by design (`tests/api/test_contract_registry.py`). Do not add 501 skeletons. Register routes only when implemented.

### Frozen implementation decisions (no longer open)

| Topic | Frozen rule |
| --- | --- |
| Paths / methods / counts | Registry + `NUMBERED_OPERATIONS`. Exactly 12. Search and GET-by-id **are** in the 12; do not add DELETE, login, booking, payment, or nested `/organizations/{id}/customers`. |
| Operation IDs | `make_operation_id()` in `catalog.py`. Draft YAML IDs are void. |
| HTTP success | Registry: 201 for 001; **200** for 002–012, including documents and emergency-contacts. Collection 201/202 variants are superseded. |
| Error codes | `app/api/error_codes.py` only. Collection `CUSTOMER_*_001` codes are void. |
| 403 / 401 / 404 | `AUTHORIZATION_DENIED` / `AUTHENTICATION_FAILED` / `RESOURCE_NOT_FOUND` (generic message). Cross-tenant and out-of-scope objects → **404**, not 403. |
| Tenant headers | Untrusted. `X-Organization-ID` / `X-Facility-ID` / `X-Site-ID` never grant access. |
| Authorization loader | `load_authorized_principal` + `require_permission(..., loader=...)`. JWT permission lists are not the source of truth. |
| Permission **values** | Domain registry `CUSTOMER_PERMISSION_CODES` (see §17). Not `API04_PERMISSION_CODES`. |
| If-Match | Registry: PATCH only (002). Collection If-Match on lifecycle POSTs is superseded. |
| Idempotency | Registry POST `TBD` + catalog `IDEMPOTENCY_REQUIRED_IDS` (API-04 absent) → **NOT_REQUIRED**. Uniqueness constraints provide retry safety. No idempotency table. |
| Pagination | OFFSET for 004 and 012. Default page size 20, max 100. Collection cursor option for history is deferred. |
| HTTP module | `app/modules/customer/` (package exists; `routes.py` is empty and **not** mounted). |
| Customer vs Identity | No `identity.user_account` row is created or required. `created_by` / `updated_by` are actor UserAccount IDs, not Customer identity. |
| Ownership | Customer belongs to **exactly one Organization** (`organization_id` NOT NULL). Primary Facility is required. Primary Site is required when the Facility has sites; otherwise optional. PATCH cannot change org/facility/site; site moves use API-04-006. |
| Home facility/site storage | **Typed columns**, not `profile_payload` JSON. Additive migration `013`. |
| Duplicate | Organization-scoped. Primary duplicate key is **normalized `primary_phone`**. Email is not unique. `customer_code` unique per org (already in DDL). No duplicate-override numbered API. |
| Lifecycle | `ACTIVE` (register default), `SUSPENDED`, `ARCHIVED`. PATCH must not change status. Dedicated POSTs only. No `PROSPECT` / `BLOCKED` / `INACTIVE` / `CLOSED` in v1. |
| Archive | Set `customer_status = ARCHIVED` and `deleted_at` / `deleted_by`. Search default excludes archived. No hard DELETE. |
| Membership / attendance / billing | API-04 must **not** mutate those tables. FR “impact display” is deferred to those verticals. |
| Documents | Metadata rows in `customer.customer_document` only. No S3/ClamAV in this vertical. |
| Family | Emergency contacts are `customer.customer_contact` with `is_emergency = true`. No Customer-to-Customer guardian FK. |
| Scaffold ORM | `customer.customers` / `customer_contacts` / `customer_documents` / `customer_preferences` / `customer_identifiers` / `customer_status_history` are **quarantined**. Do not persist API-04 against them. |

---

## 2. Gate Status

```text
API-04 CUSTOMER PRE-IMPLEMENTATION GATE: PASS
```

Blocking decisions: **0**.

Remaining work is implementation (migration `013`, ORM, seed, routes/services/tests), not unresolved product architecture.

---

## 3. Authoritative Sources

Inspected:

| Source | Role |
| --- | --- |
| `docs/architecture/API_CONTRACT_REGISTRY.md` | Frozen 12, paths, methods, status, FACILITY scope, OFFSET, IF_MATCH on PATCH |
| `digitize-services/app/api/contracts/operations.py` | Numbered tuples + FR-CUS-001..012 |
| `digitize-services/app/api/contracts/catalog.py` | `make_operation_id`, `COLLECTION_META["API-04"]`, `OPERATION_AUTHORIZATION` (API-04 still TBD) |
| `database/migrations/004_create_customer_membership_operations_training.sql` | Authoritative customer DDL |
| `database/migrations/007_create_indexes_triggers_seed.sql` | `trg_customer_updated_at` |
| `database/migrations/008_create_remaining_ddl.sql` | Indexes on org/status, email, phone, consent |
| `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md` | Same customer DDL; later `created_by` FK commentary |
| `docs/06_Database_Design/DATABASE_FOUNDATION_FREEZE.md` | Customer ORM gap vs SQL |
| `docs/06_Database_Design/MIGRATION_REVIEW.md` | `customer.customers` MODEL GAP |
| `docs/architecture/API_01_PLATFORM_ADMIN_PREIMPLEMENTATION.md` | Gate pattern, error/auth freeze |
| `docs/architecture/API_03_IDENTITY_USER_ROLE_PREIMPLEMENTATION.md` | Customer ≠ UserAccount already stated |
| `docs/architecture/AUTH_CONTRACT_FREEZE.md` | Staff JWT only |
| `docs/architecture/BACKEND_CODING_STANDARDS.md` | Layers, API-00, ETag, UoW |
| `docs/architecture/NAMING_AUDIT.md` | Permission/audit naming |
| `docs/07_API_Collections/API-04_Customer_Management_Collection.md` | Verbose prose (losing source on codes/If-Match/idempotency) |
| `docs/04_Functional_Requirements/FR-07_Customer_Management.md` | Business intent |
| `docs/09_UI_UX_Design/UX-05_UI_Screens.md` | UI implications; non-canonical permission names |
| Live modules | `platform`, `organization`, `facility`, `identity`, `audit`, `core/access.py` |
| `digitize-services/app/modules/customer/` | Empty router; divergent ORM |
| `digitize-ui/lib/src/pages/customers_page.dart` | Placeholder page, not routed |
| Alembic `010`–`012` | Head is `012_identity_user_role`; next additive is `013` |

Not treated as authority: draft OpenAPI YAML, collection numbered error codes, UX `PUT /customers/{id}` / `customer.read`.

---

## 4. Frozen API-04 Inventory

Authentication: Bearer access JWT required on every operation. Principal: `authenticated_staff` (Platform Admin included via existing loader). Tenant scope metadata: **FACILITY** (catalog `COLLECTION_META`). Pagination: OFFSET on 004 and 012. Concurrency: IF_MATCH on 002 only.

`{customer_id}` = `customer.customer.record_id`.

Permission codes below are the frozen API-04 seed values for `OPERATION_AUTHORIZATION` / `identity.permission`. They are **not** live in `OPERATION_AUTHORIZATION` today (`TBD`). Implementation adds them; it does not invent API-numbered registry names.

| API ID | Method | Path | Operation ID | Success | Scope | Page | Idem | Concurrency | AuthZ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-04-001 | POST | `/api/v1/customers` | `customers_create` | 201 | FACILITY | NA | NOT_REQUIRED | NA | `customer.create` |
| API-04-002 | PATCH | `/api/v1/customers/{customer_id}` | `customers_customer_id_update` | 200 | FACILITY | NA | NOT_REQUIRED | IF_MATCH | `customer.update` |
| API-04-003 | POST | `/api/v1/customers/{customer_id}/verify-identity` | `customers_customer_id_verify_identity` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.identity.verify` |
| API-04-004 | GET | `/api/v1/customers` | `customers_list` | 200 | FACILITY | OFFSET | NOT_REQUIRED | NA | `customer.search` |
| API-04-005 | GET | `/api/v1/customers/{customer_id}` | `customers_customer_id_get` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.view` |
| API-04-006 | POST | `/api/v1/customers/{customer_id}/transfer-site` | `customers_customer_id_transfer_site` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.transfer` |
| API-04-007 | POST | `/api/v1/customers/{customer_id}/suspend` | `customers_customer_id_suspend` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.suspend` |
| API-04-008 | POST | `/api/v1/customers/{customer_id}/reactivate` | `customers_customer_id_reactivate` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.reactivate` |
| API-04-009 | POST | `/api/v1/customers/{customer_id}/archive` | `customers_customer_id_archive` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.archive` |
| API-04-010 | POST | `/api/v1/customers/{customer_id}/documents` | `customers_customer_id_documents` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.documents.manage` |
| API-04-011 | POST | `/api/v1/customers/{customer_id}/emergency-contacts` | `customers_customer_id_emergency_contacts` | 200 | FACILITY | NA | NOT_REQUIRED | NA | `customer.emergency_contacts.manage` |
| API-04-012 | GET | `/api/v1/customers/{customer_id}/history` | `customers_customer_id_history_get` | 200 | FACILITY | OFFSET | NOT_REQUIRED | NA | `customer.history.view` |

FR mapping: `FR-CUS-001` … `FR-CUS-012` in order.

Database entities for all twelve: `customer.customer` plus, as needed, `customer.customer_contact`, `customer.customer_preference`, `customer.customer_consent`, `customer.customer_document`, `customer.customer_history`, `audit.audit_event`.

### Source conflicts resolved by this gate

| Conflict | Losing source | Winning source |
| --- | --- | --- |
| Draft OpenAPI / non-canonical operationIds | Collection YAML | Registry + `make_operation_id()` |
| UX `PUT /customers/{id}` | UX-05 | Registry PATCH 002 |
| UX `customer.read` / `customer.edit` / `customer.restricted_view` | UX-05 / API-23 matrix | Collection §29 dotted codes (table above) |
| FR `/api/v1/customers/duplicate-check` | FR-07 related-API table | Not in the 12; duplicate check is **in-process** on 001/002 |
| FR GET verification / GET status extra routes | FR-07 | Not in the 12 |
| API-04-010/011 HTTP 201 | Collection §29 | Registry 200 |
| API-04-003 HTTP 202 | Collection §29 | Registry 200 |
| `CUSTOMER_DUPLICATE_001` etc. | Collection §16 | Frozen `ErrorCode` |
| Required `Idempotency-Key` | Collection §13/23 | Registry/catalog NOT_REQUIRED |
| If-Match on POSTs | Collection §24 | Registry: PATCH only |
| Cursor pagination for history | Collection §17 | Registry OFFSET |
| Membership cancelled on suspend | Implied by some FR “restriction” prose | FR-CUS-007 Notes: suspend does **not** auto-cancel memberships. API-04 does not write membership rows. |
| Customer login / portal | FR out-of-scope + UX later | Not API-04 |
| Scaffold `customer.customers` ORM | Existing Python models | Migration `004` `customer.customer` |
| Registry compact “SKELETON_CREATED” for API-01..03 | Stale registry table | Live handlers exist for 01–03; API-04 remains unimplemented |

No remaining unresolved conflict that would change a path, method, count, or frozen error identity.

---

## 5. Customer Domain Definition

**Customer** is the Organization’s business relationship record for a person (or later a household contact person) who may purchase memberships, attend services, be billed, or receive operational communications.

Customer is a **master-data entity** in schema `customer`, owned by `tenant.organization`. It is created by **staff**, not by the Customer themselves, in this vertical.

Customer is identified by:

- `record_id` (UUID, system, never reused) — path `{customer_id}`
- `customer_code` (org-unique, system-generated human code)
- Organization membership (`organization_id`)

Customer is **not** a login principal. Customer is **not** a membership. Customer is **not** an attendance event. Customer is **not** an invoice.

---

## 6. Customer vs Identity

| Concept | Authoritative store | Role |
| --- | --- | --- |
| **Customer** | `customer.customer` | Business relationship / PII profile for an Organization’s client |
| **UserAccount** | `identity.user_account` | Authenticated staff (or platform admin) login subject |
| **StaffProfile** | `identity.staff_profile` | Employment/profile row 1:1 with a tenant UserAccount |
| **Role** | `identity.role` | Permission bundle for staff |
| **Principal** | Runtime `Principal` from access JWT + DB assignments | Actor calling API-04 |
| **IdentityAccessScope** | `identity.access_scope` | Staff org/facility/site assignments used to **authorize** Customer access |

Rules:

- API-04 never inserts `identity.user_account` or `identity.staff_profile`.
- A person may be a Customer without ever being a UserAccount.
- A person may be Staff without being a Customer.
- Overlap of the same human as both Staff and Customer, if it occurs in real life, is **two records**. There is no shared PK and no FK between them in v1.
- `created_by` / `updated_by` / `deleted_by` on customer tables are actor UserAccount IDs (staff), not Customer IDs.
- API-04-003 “Verify Customer Identity” means **KYC/document outcome recorded by staff**, not login, MFA, or password.

API-03 already froze: “UserAccount ≠ Customer. API-03 never inserts `customer.customer`.” This gate is the symmetric freeze.

---

## 7. Customer Ownership / Tenancy

Frozen product hierarchy:

```text
Platform → Organization → Facility → Site
```

Do not introduce Branch.

| Question | Frozen answer |
| --- | --- |
| Is Customer owned by Organization? | **Yes.** `customer.customer.organization_id` NOT NULL. One Organization only. |
| Can a Customer be associated with multiple Facilities? | **Not as multiple owners.** One **primary Facility**. Other facilities appear only via later membership/attendance records (API-05/06), not as Customer ownership. |
| Can a Customer exist without a Facility? | **No** for API-04-001. Primary Facility is required at register. |
| Can a Customer belong directly to a Site? | Customer does not replace Facility with Site. Customer has optional/conditional **primary Site** under the primary Facility. |
| Is Site association required? | **Conditional.** Required when the primary Facility has at least one Site; otherwise omitted. Transfer-site (006) requires a target Site in the same Organization, belonging to an eligible Facility. |
| Is the record global to the Organization? | **Yes, as master data.** Facility/Site are home-context columns, not separate customer rows. |
| Same person in multiple Organizations? | **Allowed as separate rows.** Isolation is `organization_id`. No global person registry. |
| Cross-organization leakage? | Queries always constrain `organization_id` from the **authorized object**, never from tenant headers. Out-of-org IDs → 404. |
| Facility Staff principal? | Must have facility (or inherited org) access to the Customer’s **primary Facility**. Otherwise 404. |
| Site-scoped staff? | Must have site access to the Customer’s **primary Site** when the Customer has one; if primary Site is null, facility-level access applies. |
| Platform Admin? | Existing `is_platform_admin` bypass in `app/core/access.py` continues. Still requires `customer.*` permission on the role (Platform Admin seed binds all customer codes). |

Register (001) and search (004) are FACILITY-scoped: the actor’s facility assignment is the authorization boundary. The Customer row remains org-owned.

---

## 8. Database Authority

Physical authority is migration `004` (and indexes in `008`), not the Python scaffold models.

### `customer.customer`

| Attribute | DDL |
| --- | --- |
| Classification | **AUTHORITATIVE BUT INCOMPLETE** |
| PK | `record_id UUID` |
| Organization | `organization_id` NOT NULL → `tenant.organization(record_id)` RESTRICT |
| Facility / Site | **Missing typed columns** (see §24) |
| Status | `customer_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE'` (unconstrained enum) |
| Type | None. No `customer_type` column. Do not invent one. |
| Names | `first_name` NOT NULL, `last_name` nullable |
| DOB | `date_of_birth DATE` nullable |
| Gender | `gender_code VARCHAR(40)` nullable |
| Email | `primary_email CITEXT` nullable |
| Phone | `primary_phone VARCHAR(50)` nullable |
| Address / extras | `profile_payload JSONB NOT NULL DEFAULT '{}'` |
| Timestamps | `created_at`, `updated_at`, `created_by`, `updated_by` |
| Concurrency | `version_number INTEGER NOT NULL DEFAULT 1` |
| Soft delete | `deleted_at`, `deleted_by` |
| Uniqueness | `UNIQUE (organization_id, customer_code)` |
| Indexes (008) | `(organization_id, customer_status)`, `primary_email`, `primary_phone` (non-unique) |

### `customer.customer_contact`

**AUTHORITATIVE AND USABLE.** Org + customer FKs. `contact_type`, `contact_name`, `email`, `phone`, `is_primary`, `is_emergency`, `address_payload`. Emergency contacts (011) persist here with `is_emergency = true`. No unique emergency-contact constraint.

### `customer.customer_preference`

**AUTHORITATIVE AND USABLE.** Unique `(customer_id, preference_key)`. Communication preferences on register live here (e.g. `preference_key = communication`).

### `customer.customer_consent`

**AUTHORITATIVE AND USABLE.** No numbered consent API. Register (001) and profile view (005) may write/read rows. Marketing send remains API-10.

### `customer.customer_document`

**AUTHORITATIVE AND USABLE** for **metadata** (010): `document_type`, `document_name`, `storage_reference`, `document_status`, `metadata`. Binary upload is out of scope.

### `customer.customer_history`

**AUTHORITATIVE AND USABLE** for 012 and mutation history inserts.

### Downstream FKs (not API-04 writes)

SQL `membership.customer_membership.customer_id`, `operations.attendance`, `operations.walkin_visit`, `training.customer_progress`, billing/support references → `customer.customer(record_id)`. **Do not write these from API-04.**

### Quarantined / missing physical tables

| Object | Classification |
| --- | --- |
| `customer.customers` | **Does not exist in DDL.** Scaffold ORM only. **QUARANTINED** |
| `customer.customer_contacts` (plural) | **Does not exist.** **QUARANTINED** |
| `customer.customer_documents` (plural) | **Does not exist.** **QUARANTINED** |
| `customer.customer_preferences` (plural) | **Does not exist.** **QUARANTINED** |
| `customer.customer_identifiers` | **Does not exist.** **QUARANTINED / SPECULATIVE** |
| `customer.customer_status_history` | **Does not exist.** History is `customer.customer_history`. **QUARANTINED** |
| Guardian/family table | **MISSING** and **DEFERRED** |

---

## 9. Existing Customer Implementations

| Artifact | Classification |
| --- | --- |
| `app/modules/customer/routes.py` empty, unmounted | **USABLE skeleton** — keep empty until handlers exist |
| `app/modules/customer/models/customers.py` → `customer.customers.customer_id` | **DIVERGENT / QUARANTINE** |
| `customer_contacts.py`, `customer_documents.py`, `customer_preferences.py`, `customer_identifiers.py`, `customer_status_history.py` | **DIVERGENT / QUARANTINE** (wrong table names, columns, FKs, statuses `INACTIVE`/`CLOSED`) |
| `app/modules/membership/models/memberships.py` FK `customer.customers.customer_id` | **MODEL GAP** (SQL is correct). Align at **API-05**, not this vertical |
| Other modules FKing `customer.customers.customer_id` (attendance, billing, support, training, communication) | **DIVERGENT ORM**; out of API-04 write scope |
| Catalog / operations numbered 12 | **AUTHORITATIVE** |
| `tests/api/test_contract_registry.py` 404 on `/customers` | **USABLE** — must keep 404 until live |
| Flutter `lib/src/pages/customers_page.dart` | **PLACEHOLDER**, not in GoRouter |
| Flutter membership_plan feature | Plans, **not** customer memberships |
| Collection OpenAPI YAML | **NON-AUTHORITATIVE** |

No live Customer HTTP handler exists. No Customer service or repository exists.

---

## 10. Customer Lifecycle

Authoritative v1 states (string values in `customer_status`):

```text
ACTIVE ──suspend──► SUSPENDED ──reactivate──► ACTIVE
   │                     │
   └──archive──► ARCHIVED
                 SUSPENDED ──archive──► ARCHIVED
```

| State | How entered | Who |
| --- | --- | --- |
| `ACTIVE` | API-04-001 default; API-04-008 from `SUSPENDED` | Staff with `customer.create` / `customer.reactivate` |
| `SUSPENDED` | API-04-007 from `ACTIVE` only | `customer.suspend` |
| `ARCHIVED` | API-04-009 from `ACTIVE` or `SUSPENDED` | `customer.archive` |

Rules:

- PATCH 002 **must reject** status changes (`VALIDATION_FAILED` / ignore unknown status field — do not accept `customer_status` on PATCH).
- Suspend of `ARCHIVED` → `INVALID_STATE`.
- Reactivate of `ACTIVE` → `INVALID_STATE` (not a no-op success).
- Reactivate of `ARCHIVED` → `INVALID_STATE` (FR-CUS-008).
- Archive is terminal for v1. No unarchive API in the 12.
- `deleted_at` is set only by archive, not by suspend.
- Default search (004) returns non-archived (`deleted_at IS NULL` and status ≠ `ARCHIVED`) unless an explicit `customer_status=ARCHIVED` filter is authorized.
- Suspend/archive **do not** write membership, attendance, or invoice rows. Downstream verticals read `customer_status` later.
- FR `PROSPECT` / `REGISTERED` / `BLOCKED` / `INACTIVE` / ORM `CLOSED` are **not** v1 API-04 states.

Identity verification is **orthogonal** to lifecycle (`UNVERIFIED` / `VERIFIED` / `REJECTED` on `identity_verification_status`). A Customer may be `ACTIVE` and `UNVERIFIED`. Membership activation gating is **API-05**.

---

## 11. Duplicate / Uniqueness Rules

| Key | Scope | Mechanism |
| --- | --- | --- |
| `record_id` | Global | PK |
| `customer_code` | `(organization_id, customer_code)` | Existing UNIQUE |
| `primary_phone` | Organization, non-archived, non-null | Application check **and** proposed partial unique index (013) |
| `primary_email` | Organization | **Not unique.** Format only. |
| Name + DOB | — | **Not** a uniqueness constraint. Optional search aid only; do not 409. |
| External identifier table | — | Not in DDL. Do not invent. |

Normalization:

- Phone: trim; store E.164 when the value starts with `+`; otherwise store digits-only national form used consistently in the org. Duplicate compare uses the normalized stored form.
- Email: CITEXT already case-insensitive; trim.
- No third-party validation service.

Duplicate on register/update phone → **409 `RESOURCE_CONFLICT`** (not `CUSTOMER_DUPLICATE_001`). Message: existing customer already uses this phone in the organization. Do **not** return the other customer’s PII beyond `record_id` / `customer_code` to callers who can `customer.view` that same org; if the match is out of the caller’s facility scope, still 409 without leaking the other profile.

No `customer.duplicate.override` numbered API. Override is **DEFERRED**.

---

## 12. Contact / Profile Rules

### Register (001) application-required fields

Even where DDL is nullable:

- `first_name`
- `primary_phone`
- `date_of_birth`
- `gender_code` (allow-list from configured values; unknown → 422)
- `primary_facility_id` (must be ACTIVE facility in the same org and in actor scope)
- emergency contact: name + phone (persisted as `customer_contact` `is_emergency=true`)
- communication consent captured as `customer.customer_consent` row(s)

Optional: `last_name`, `primary_email`, `primary_site_id` (required if facility has sites), address inside `profile_payload.address` or emergency/primary contact `address_payload`.

`customer_code`: system-generated, unique per org (implementation may use a stable prefix + unique suffix; never client-supplied on create).

### Update (002)

Same format/duplicate rules. PATCH **must not** change `organization_id`, `customer_code`, `customer_status`, `primary_facility_id`, or `primary_site_id`. Home Site changes use API-04-006 only. There is **no** numbered facility-transfer API; changing primary Facility is **DEFERRED**.

### Privacy / logs

Do not log phone, email, DOB, document storage references, or authorization headers. Reuse existing logging interceptor redaction. Responses never include passwords/tokens (none exist on Customer).

---

## 13. Family / Guardian Boundary

`customer.customer_contact` can store an emergency contact (`is_emergency`) and, if needed, `contact_type = GUARDIAN` as a **contact person**, not as another Customer row.

There is **no** Customer↔Customer relationship table.

**Family Membership ≠ Customer family graph.** Family membership is API-05. Do not model dependents as nested Customers in API-04.

**DEFERRED:** guardian-of-customer FK, parental consent workflows beyond contact + document metadata.

---

## 14. Customer / Membership Boundary

| Customer | Membership |
| --- | --- |
| Person/org relationship | Commercial entitlement |
| `customer.customer` | `membership.customer_membership` |
| Status ACTIVE/SUSPENDED/ARCHIVED | Separate membership_status |
| API-04 | API-05 |

API-04 responses **must not** embed membership plan, expiry, freeze, or payment status except perhaps a non-authoritative count later (not in v1). Create Customer does not create a membership.

FR-CUS-008 Notes: reactivation does not resume frozen/cancelled memberships. Honor that.

---

## 15. Customer / Attendance Boundary

Attendance is `operations.attendance` / walk-in (API-06). Customer APIs must not insert attendance. Search/view do not imply check-in.

API-06-008 `GET /customers/{id}/attendance-history` is **not** API-04.

---

## 16. Customer / Billing Boundary

Invoices/payments are API-08. Customer APIs must not create financial rows. `invoice_id` on membership is irrelevant here.

---

## 17. Authorization Model

Reuse:

- `load_authorized_principal`
- `require_permission(..., loader=...)`
- `app/core/access.py` (`require_organization_access`, `require_facility_access`, `require_site_access`)
- `IdentityAccessScope` already loaded onto `Principal.access_assignments`

Canonical namespace: **`customer.*`**

```text
CUSTOMER_PERMISSION_CODES = (
    "customer.create",
    "customer.update",
    "customer.identity.verify",
    "customer.search",
    "customer.view",
    "customer.transfer",
    "customer.suspend",
    "customer.reactivate",
    "customer.archive",
    "customer.documents.manage",
    "customer.emergency_contacts.manage",
    "customer.history.view",
)
```

Seed in `013` and bind to `PLATFORM_ADMIN`. Org-scoped standard roles (Organization Admin, Facility Manager, Reception) may receive subsets **via existing API-03 role-permission machinery**, not a new API. Default implementation seed: bind **all twelve** to `PLATFORM_ADMIN` only; additional role bindings are data, not new endpoints.

Do not create `customer.restricted_view` in v1. Field-level masking is **DEFERRED**; v1 authorized viewers see the profile fields in the contract.

Evaluation:

1. Permission code required (missing → 403 `AUTHORIZATION_DENIED`).
2. Object in actor’s org/facility/site assignments (missing → 404 `RESOURCE_NOT_FOUND`).
3. Platform Admin: existing access helpers.

JWT claims never grant Customer access by themselves.

---

## 18. Object Isolation

| Actor vs object | Result |
| --- | --- |
| Same org, primary facility in actor’s facility scopes | Allow if permission holds |
| Same org, different facility, facility-scoped staff | **404** |
| Same facility, different site, site-scoped staff, customer has other primary site | **404** |
| Different organization | **404** |
| Platform Admin with permission | Allow |
| Missing permission, object would be in scope | **403** |
| Unauthenticated | **401** |

Search (004) returns only Customers whose primary facility/site is inside the principal’s assignments (Platform Admin: all orgs they are authorized to see; typically all). Never use tenant headers to widen that set.

---

## 19. Concurrency

Version source: `customer.customer.version_number`.

ETag: existing `etag_for_version` / `etag_matches` from `app.modules.platform.service` (already used by API-01/02/03). Do not create a second helper.

| Operation | If-Match |
| --- | --- |
| 002 PATCH | **Required.** Missing → 428 `CONCURRENCY_CONFLICT`. Stale → 412 `CONCURRENCY_CONFLICT`. Success increments `version_number`. |
| All other API-04 ops | **Not required** (registry). |

`customer_contact` / `customer_document` have no `version_number` in DDL. 010/011 do not use If-Match.

---

## 20. Audit

Use `record_audit_event` in the **same UoW** as the mutation. Flush, never commit in repository. Failed mutation rolls back audit.

`organization_id` on `audit.audit_event` **must** be the Customer’s organization.

Canonical `action` / payload `event` names (dotted, matching API-02/03):

| API | Audit action |
| --- | --- |
| 001 | `customer.created` |
| 002 | `customer.updated` |
| 003 | `customer.identity.verified` |
| 006 | `customer.transferred` |
| 007 | `customer.suspended` |
| 008 | `customer.reactivated` |
| 009 | `customer.archived` |
| 010 | `customer.document.updated` |
| 011 | `customer.emergency_contact.updated` |

No audit rows for GET 004/005/012 (collection `CUSTOMER_SEARCHED` / `CUSTOMER_PROFILE_VIEWED` superseded).

Also insert `customer.customer_history` for mutations (history_type matching the event). GET 012 reads that table, not `audit.audit_event`.

Facility/site IDs belong in `event_payload`, not as extra audit columns (audit schema has `organization_id` only).

---

## 21. Error Model

Raise `DigitizeError` subclasses. No `HTTPException` in services.

| Condition | Code | HTTP |
| --- | --- | --- |
| Unauthenticated | `AUTHENTICATION_FAILED` | 401 |
| Missing permission | `AUTHORIZATION_DENIED` | 403 |
| Unknown / out-of-scope customer, facility, or site | `RESOURCE_NOT_FOUND` | 404 |
| Duplicate phone / customer_code | `RESOURCE_CONFLICT` | 409 |
| Illegal lifecycle transition | `INVALID_STATE` | 409 |
| Missing/stale If-Match | `CONCURRENCY_CONFLICT` | 428 / 412 |
| Schema/field validation | `VALIDATION_FAILED` | 422 |
| Unexpected | `INTERNAL_ERROR` | 500 |

Do **not** add `CUSTOMER_NOT_FOUND`, `CUSTOMER_DUPLICATE`, or numbered `CUSTOMER_*_001`. Collection §16 is void.

---

## 22. Service / Repository / Route Architecture

```text
Routes (app/modules/customer/routes.py)
  → CustomerService / CustomerDocumentService / CustomerContactService
    → CustomerRepository (+ contact/document/history repositories)
      → ORM mapped to customer.customer* (004)
      → PostgreSQL
```

Expected files (create at implementation, not this gate):

```text
app/modules/customer/constants.py      # CUSTOMER_PERMISSION_CODES
app/modules/customer/schemas.py        # APIModel DTOs
app/modules/customer/repository.py
app/modules/customer/service.py
app/modules/customer/routes.py         # thin; mount in api/v1/routes.py when live
app/modules/customer/models/customer.py          # map customer.customer
app/modules/customer/models/customer_contact.py
app/modules/customer/models/customer_preference.py
app/modules/customer/models/customer_consent.py
app/modules/customer/models/customer_document.py
app/modules/customer/models/customer_history.py
```

Routes: `require_permission`, `load_authorized_principal`, API-00 `success_response`, no SQL, no commit, no business rules, no `HTTPException`.

Services: validation beyond schema, lifecycle, duplicate, object isolation via `app.core.access`, audit + history, transaction (UoW), ETag for 002.

Repositories: queries/persistence, `flush`, unique-violation mapping to domain errors. No commit, no envelopes, no HTTP.

---

## 23. ORM Alignment

| Model to implement | Maps |
| --- | --- |
| Authoritative `Customer` | `customer.customer`, PK `record_id`, columns from 004 **plus** 013 additions |
| Authoritative contact/preference/consent/document/history | singular table names from 004 |

| Existing file | Status |
| --- | --- |
| `models/customers.py` (`__tablename__ = "customers"`) | **quarantine** — do not use |
| sibling plural scaffold models | **quarantine** — do not use |

Implementation replaces mappings; do not dual-write. Do not “fix” membership/attendance ORM FKs in this vertical except if SQLAlchemy mapper configuration requires the authoritative Customer class to exist (membership gap stays API-05).

Follow API-02/03 style: `APIModel` schemas; `version_number` on Customer.

---

## 24. Migration Requirements

**Required: additive Alembic `013_customer_master` (name exact at implementation, parent `012_identity_user_role`).**

Do not edit `001`–`012`.

### Purpose

1. Seed `CUSTOMER_PERMISSION_CODES` and bind to `PLATFORM_ADMIN`.
2. Complete Customer home context and verification state that 004 omitted.

### Proposed additive columns on `customer.customer`

| Column | Type | Notes |
| --- | --- | --- |
| `primary_facility_id` | UUID NOT NULL FK `tenant.facility(record_id)` RESTRICT | Required home facility |
| `primary_site_id` | UUID NULL FK `tenant.site(record_id)` RESTRICT | Conditional home site |
| `identity_verification_status` | VARCHAR(40) NOT NULL DEFAULT `'UNVERIFIED'` | `UNVERIFIED` \| `VERIFIED` \| `REJECTED` |

Empty table today: NOT NULL facility is compatible (no backfill).

### Proposed indexes / uniqueness

- Index `(organization_id, primary_facility_id)`
- Index `(organization_id, primary_site_id)` where site not null
- Partial unique: `(organization_id, primary_phone)` WHERE `deleted_at IS NULL AND primary_phone IS NOT NULL`

Application still validates facility belongs to customer org and site belongs to that facility (no cross-table CHECK).

### Rollback

Drop added indexes/columns; delete seeded permission rows. Non-destructive relative to 004 data.

### Explicitly not in 013

- New customer tables
- Family/guardian graph
- Unique email
- Membership/attendance schema
- Rewriting scaffold ORM tables into existence

SQL twin under `database/migrations/` if repository convention requires it (as 012).

---

## 25. Test Strategy

### Existing

| Test | Class |
| --- | --- |
| `test_unimplemented_numbered_api_is_not_registered` GET `/customers` 404 | **USABLE** until routes mount; then replace with contract tests |
| Membership/subscription tests asserting SaaS ≠ customer membership | **USABLE**, unrelated |
| No Customer API/service tests | **MISSING** |
| Flutter Customer tests | **MISSING** (placeholder page only) |

### Required at implementation (PostgreSQL live)

- FK: org/facility/site invalid → 404/422 as specified
- Unique phone and customer_code → 409
- UoW: failed audit/history rolls back customer insert
- Isolation: org A cannot read org B (404); facility staff cannot read other facility (404)
- 403 vs 404 split
- If-Match missing/stale/success on 002
- Lifecycle matrix (suspend/reactivate/archive illegal transitions)
- Register creates history + audit + emergency contact + consent
- Search OFFSET, default excludes archived
- 010 does not require object storage
- PII absent from logs
- OpenAPI operation IDs match `make_operation_id`
- Registry count remains 222; API-04 live count 12
- Regression: API-01/02/03 and auth

Do not use SQLite for uniqueness, CITEXT, partial unique indexes, or FK tests.

---

## 26. Flutter Integration Implications

Do **not** implement Flutter in the API-04 backend task. Implications only:

- Shared `DigitizeApiClient` already handles API-00, cookies, ETag/`If-Match`. **No second HTTP client.**
- `CustomersPage` is an unrouted placeholder. Do not treat it as a contract.
- UX-05 assumes list/get (those **are** in the 12). Nested org URLs and `PUT` are invalid.
- Do not persist refresh tokens. Staff login remains AUTH.
- Client-side permissions are presentation-only; backend remains authoritative.
- Development mock vs production remote: follow existing `AppEnvironment` split when UI is later wired.
- Search (004) is the list API. There is no separate “directory” path.

---

## 27. Open Decisions

### DECISION REQUIRED

None.

### DEFERRED (non-blocking)

| Item | Notes |
| --- | --- |
| Customer portal / login / UserAccount link | Separate authentication vertical |
| Duplicate-override permission/API | Not in the 12 |
| `PROSPECT` / `REGISTERED` / `BLOCKED` states | Not in registry lifecycle POSTs |
| Field-level `customer.restricted_view` masking | UX-05; not in 12 |
| Family membership / Customer-to-Customer guardian | API-05 / later |
| Membership/attendance/billing side effects of suspend | Those verticals read `customer_status` |
| Notifications on register/suspend | API-10 |
| Object-storage upload/scan | IC-06 / file baseline |
| Consent numbered APIs | Write on register; no extra path |
| Align membership/attendance ORM FKs to `customer.customer.record_id` | API-05/06 |
| Change of primary Facility after register | No numbered facility-transfer API; PATCH cannot change `primary_facility_id` |
| Role seed for Reception / Facility Manager customer permissions | Data via API-03; not new inventory |
| Cursor pagination for history | Registry OFFSET |
| Idempotency table | Frozen NOT_REQUIRED |

---

## 28. Implementation Sequence

1. Additive Alembic `013` + SQL twin: columns, indexes, `CUSTOMER_PERMISSION_CODES` seed + `PLATFORM_ADMIN` bind.
2. Authoritative ORM for `customer.customer` and 004 child tables; leave scaffold files unused (do not mount them).
3. Constants + catalog `OPERATION_AUTHORIZATION` for the 12 (implementation change to catalog is allowed; do **not** change the 222 inventory identity).
4. Repository (flush-only) + service (rules, access, audit, history, ETag).
5. Thin routes; mount `customer` router in `app/api/v1/routes.py`.
6. PostgreSQL contract tests (isolation, uniqueness, lifecycle, concurrency, audit atomicity).
7. Confirm registry count 222, API-01/02/03 regression, unimplemented extras still 404.
8. Flutter Customer integration is a **later** gate after backend CERTIFIED for this vertical.

---

## 29. Final Gate Checklist

| Item | Status |
| --- | --- |
| API contract frozen | **PASS** |
| 12 APIs verified | **PASS** |
| Database authority resolved | **PASS** |
| Customer identity boundary resolved | **PASS** |
| Tenancy resolved | **PASS** |
| Lifecycle resolved | **PASS** |
| Duplicate rules resolved | **PASS** |
| Authorization resolved | **PASS** |
| Isolation resolved | **PASS** |
| Concurrency resolved | **PASS** |
| Audit resolved | **PASS** |
| Error model resolved | **PASS** |
| ORM authority resolved | **PASS** (quarantine + replace) |
| Migration impact resolved | **PASS** (documented 013 only) |
| Test strategy resolved | **PASS** |
| Flutter implications resolved | **PASS** |
| No speculative API additions | **PASS** |
| No conflicting architecture left silent | **PASS** |
| No blocking decisions | **PASS** |

---

## 30. Final Recommendation

**Implementation should begin** after explicit review of this document.

Do not start until this gate is approved. When approved, implement exactly the 12 frozen routes against `customer.customer` (plus 013 additive columns), using the existing Principal / permission / audit / ETag / API-00 stack. Do not merge Customer into Identity. Do not implement API-05 or later.

---

## Appendix A — Request/response expectations (implementation DTO sketch)

Not new APIs. Fields for `APIModel` schemas at implementation. Snake_case.

**001 Register** request (illustrative): `first_name`, `last_name?`, `primary_phone`, `primary_email?`, `date_of_birth`, `gender_code`, `primary_facility_id`, `primary_site_id?`, `profile_payload?`, `emergency_contact { contact_name, phone, relationship? }`, `consents [{ consent_type, consent_status, channel_type? }]`.

**001/002/005 response:** `record_id`, `organization_id`, `customer_code`, names, status, verification status, phone/email, DOB, gender, primary facility/site, `version_number`, timestamps. Nested emergency contacts / consents on GET 005.

**006 request:** `target_site_id`, `reason?`.

**007/008/009 request:** `reason` required (FR).

**003 request:** `identity_verification_status` (`VERIFIED` \| `REJECTED`), `reason?`, `document_id?`.

**010 request:** `document_type`, `document_name`, `storage_reference`, `metadata?`.

**011 request:** `contact_name`, `phone`, `email?`, `relationship?`, `address_payload?`. Optional `record_id` to update.

**004 query:** `q?`, `customer_status?`, `facility_id?`, `site_id?`, `primary_phone?`, `primary_email?`, `page`, `page_size`. Actor scope still applied.

Exact JSON remains implementation-time `APIModel` work within this freeze; do not publish a second OpenAPI as contract authority.
