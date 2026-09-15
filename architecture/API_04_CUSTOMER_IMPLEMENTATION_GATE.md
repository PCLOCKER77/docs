# API-04 CUSTOMER IMPLEMENTATION GATE

**Date:** 2026-09-12  
**Pre-implementation gate:** `docs/architecture/API_04_CUSTOMER_PREIMPLEMENTATION.md` (PASS, approved)

---

## 1. Status

```text
API-04 CUSTOMER IMPLEMENTATION GATE: PASS
```

---

## 2. Scope

Backend-only implementation of the frozen 12 API-04 Customer operations.

Implemented:

- Additive Alembic `013_customer_master` (typed home facility/site, verification status, org-scoped phone uniqueness, `CUSTOMER_PERMISSION_CODES` seed bound to `PLATFORM_ADMIN`)
- Authoritative ORM for `customer.customer` / `customer_contact` / `customer_preference` / `customer_consent` / `customer_document` / `customer_history`
- Route → service → repository stack in `app/modules/customer/`
- Catalog `OPERATION_AUTHORIZATION` + `IMPLEMENTED_NUMBERED_KEYS` for the 12
- Mount of the customer router in `app/api/v1/routes.py`
- PostgreSQL live contract tests

Not implemented (out of scope):

- Flutter
- API-05 Membership
- Attendance, billing, notifications
- Customer authentication / UserAccount creation
- Family/guardian graph
- File binary upload
- Customer DELETE / merge / import / extra search APIs

---

## 3. API Inventory

| API ID | Method | Path | Operation ID | Status |
| --- | --- | --- | --- | --- |
| API-04-001 | POST | `/api/v1/customers` | `customers_create` | **201 live** |
| API-04-002 | PATCH | `/api/v1/customers/{customer_id}` | `customers_customer_id_update` | **200 live, If-Match** |
| API-04-003 | POST | `/api/v1/customers/{customer_id}/verify-identity` | `customers_customer_id_verify_identity` | **200 live** |
| API-04-004 | GET | `/api/v1/customers` | `customers_list` | **200 live, OFFSET** |
| API-04-005 | GET | `/api/v1/customers/{customer_id}` | `customers_customer_id_get` | **200 live** |
| API-04-006 | POST | `/api/v1/customers/{customer_id}/transfer-site` | `customers_customer_id_transfer_site` | **200 live** |
| API-04-007 | POST | `/api/v1/customers/{customer_id}/suspend` | `customers_customer_id_suspend` | **200 live** |
| API-04-008 | POST | `/api/v1/customers/{customer_id}/reactivate` | `customers_customer_id_reactivate` | **200 live** |
| API-04-009 | POST | `/api/v1/customers/{customer_id}/archive` | `customers_customer_id_archive` | **200 live** |
| API-04-010 | POST | `/api/v1/customers/{customer_id}/documents` | `customers_customer_id_documents` | **200 live** |
| API-04-011 | POST | `/api/v1/customers/{customer_id}/emergency-contacts` | `customers_customer_id_emergency_contacts` | **200 live** |
| API-04-012 | GET | `/api/v1/customers/{customer_id}/history` | `customers_customer_id_history_get` | **200 live, OFFSET** |

Product inventory remains **222**. OpenAPI exposes exactly these 12 Customer operation IDs. No extra Customer paths.

---

## 4. Database Changes

**Migration:** `013_customer_master`  
**Parent:** `012_identity_user_role`  
**SQL twin:** `database/migrations/013_customer_master.sql`  
**Alembic head after upgrade:** `013_customer_master`

Existing `customer.customer` row count before upgrade: **0**. No duplicate-phone data. Unique index applied safely. No customer rows were deleted or rewritten.

Additive columns on `customer.customer`:

| Column | Type | Notes |
| --- | --- | --- |
| `primary_facility_id` | UUID NOT NULL FK `tenant.facility` | Home facility |
| `primary_site_id` | UUID NULL FK `tenant.site` | Home site |
| `identity_verification_status` | VARCHAR(40) NOT NULL DEFAULT `UNVERIFIED` | Staff-recorded KYC outcome |

Indexes:

- `idx_customer_org_facility (organization_id, primary_facility_id)`
- `idx_customer_org_site (organization_id, primary_site_id)` WHERE site not null
- Partial unique `uq_customer_org_phone_active (organization_id, primary_phone)` WHERE `deleted_at IS NULL AND primary_phone IS NOT NULL`

Permission seed: 12 `customer.*` codes inserted into `identity.permission` and bound to `PLATFORM_ADMIN` (12 `role_permission` rows verified).

Migrations `001`–`012` were **not** modified.

---

## 5. ORM

Authoritative mappings (used by API-04):

| Class | Table | PK |
| --- | --- | --- |
| `Customer` | `customer.customer` | `record_id` |
| `CustomerContact` | `customer.customer_contact` | `record_id` |
| `CustomerPreference` | `customer.customer_preference` | `record_id` |
| `CustomerConsent` | `customer.customer_consent` | `record_id` |
| `CustomerDocument` | `customer.customer_document` | `record_id` |
| `CustomerHistory` | `customer.customer_history` | `record_id` |

Quarantined scaffold (`customer.customers`, PK `customer_id`, and sibling plural models) is **not imported** by the Customer service/repository/routes.

---

## 6. Authorization

`load_authorized_principal` + `require_permission(..., loader=...)`. Tenant headers remain untrusted.

`CUSTOMER_PERMISSION_CODES` in `app/modules/customer/constants.py` (not `API04_PERMISSION_CODES`).

Wired in `OPERATION_AUTHORIZATION`. Seeded and bound to `PLATFORM_ADMIN`.

Object isolation:

- Organization ownership: `customer.customer.organization_id`
- Facility/site access: `primary_facility_id` / `primary_site_id` via `require_facility_access` / `require_site_access`
- Platform Admin: existing platform assignment bypass plus `customer.*` permissions
- Missing permission: **403 `AUTHORIZATION_DENIED`**
- Out-of-scope object: **404 `RESOURCE_NOT_FOUND`**

---

## 7. Lifecycle

| From | Operation | To |
| --- | --- | --- |
| (create) | API-04-001 | `ACTIVE` |
| `ACTIVE` | suspend | `SUSPENDED` |
| `SUSPENDED` | reactivate | `ACTIVE` |
| `ACTIVE` or `SUSPENDED` | archive | `ARCHIVED` (`deleted_at` set) |

Invalid transitions return **409 `INVALID_STATE`**. PATCH cannot change `customer_status`, `organization_id`, `primary_facility_id`, or `primary_site_id`. Archive is terminal. Search default excludes archived.

---

## 8. Duplicate Rules

**Phone canonicalization review (2026-09-12): OPTION A — accept current design.**

Uniqueness applies to the **normalized supplied representation**, not inferred real-world telephone identity.

`app/modules/customer/phone.py`:

- Trim whitespace; drop spaces, parentheses, hyphens, dots
- If the caller supplied a leading `+`, store `+` plus digits (E.164-shaped)
- Otherwise store digits only (national form)
- Require 8–15 digits
- No third-party library
- **Do not** guess a country or convert national digits to E.164

The Customer HTTP contract has `primary_phone` only. It does not include country, numbering-plan, or phone-type. Optional `tenant.organization.country_code` is not Customer phone context and is not used. Silently mapping `9876543210` → `+919876543210` would be an India-shaped guess and is rejected for an international platform.

Equivalent formatting of the **same supplied form** collides (org-scoped, non-archived). A national form and an international form remain distinct until a future contract adds authoritative country context. The same normalized phone may exist in different Organizations. An archived Customer does not block reuse of that phone.

Duplicate → **409 `RESOURCE_CONFLICT`**. Email is not unique. `(organization_id, customer_code)` remains unique.

---

## 9. Concurrency

PATCH 002 only. Reuses `etag_for_version` / `etag_matches`.

- Missing If-Match → 428 `CONCURRENCY_CONFLICT`
- Stale If-Match → 412 `CONCURRENCY_CONFLICT`
- Success increments `version_number` and returns `ETag`

Lifecycle/transfer/document POSTs do **not** require If-Match (registry).

---

## 10. Audit

`record_audit_event` in the same UoW as the mutation. Live convention is uppercase actions (matching API-01/02/03), not the pre-implementation dotted names:

| Mutation | Audit action |
| --- | --- |
| create | `CUSTOMER_CREATED` |
| update | `CUSTOMER_UPDATED` |
| verify-identity | `CUSTOMER_IDENTITY_VERIFIED` |
| transfer-site | `CUSTOMER_TRANSFERRED` |
| suspend | `CUSTOMER_SUSPENDED` |
| reactivate | `CUSTOMER_REACTIVATED` |
| archive | `CUSTOMER_ARCHIVED` |
| documents | `CUSTOMER_DOCUMENT_UPDATED` |
| emergency-contacts | `CUSTOMER_EMERGENCY_CONTACT_UPDATED` |

`organization_id` is the Customer’s organization. History rows are written to `customer.customer_history`. GET search/view/history are not audited.

Monkeypatched audit failure on create → HTTP 500 and **no** customer row.

---

## 11. Error Model

Existing `DigitizeError` codes only. No numbered `CUSTOMER_*` codes.

| Condition | Code | HTTP |
| --- | --- | --- |
| Unauthenticated | `AUTHENTICATION_FAILED` | 401 |
| Missing permission | `AUTHORIZATION_DENIED` | 403 |
| Unknown / out-of-scope | `RESOURCE_NOT_FOUND` | 404 |
| Duplicate phone/code | `RESOURCE_CONFLICT` | 409 |
| Illegal lifecycle / transfer | `INVALID_STATE` | 409 |
| If-Match | `CONCURRENCY_CONFLICT` | 428 / 412 |
| Field validation | `VALIDATION_FAILED` | 422 |

---

## 12. Isolation

Verified live:

| Case | Result |
| --- | --- |
| Same org / authorized facility | 200 |
| Same org / unauthorized facility | 404 |
| Different organization | 404 |
| Site-scoped staff, other site/facility | 404 |
| Cross-org transfer target | 404 |
| Platform Admin with permissions | 200 |
| Unprivileged platform user | 403 |
| Unauthenticated | 401 |

Search results are filtered to the principal’s assignments.

---

## 13. Test Results

Commands used the project Poetry venv at `~/Library/Caches/pypoetry/virtualenvs/digitize-services-G_7W_USx-py3.13`.

| Gate | Result |
| --- | --- |
| Backend default (`pytest -q`) | **196 passed, 181 skipped** |
| Backend live (`DIGITIZE_API_TEST=1 pytest -q`) | **367 passed, 10 skipped** |
| Ruff (API-04 new files) | **PASS** |
| MyPy (`app/modules/customer`, `app/api/v1/routes.py`) | **PASS** |
| OpenAPI | **PASS** (12 Customer operation IDs, 49 implemented numbered) |
| Migration | **PASS** (`013_customer_master` head, applied cleanly) |
| Registry | **222 APIs**, API-04 **12** |

Previous live baseline (API-03 era): 332 passed / 10 skipped. Current live: 367 passed / 10 skipped. Default passed 191 → 196 from new non-live Customer tests (phone + migration 013). Skip count rose by the new live-gated API-04 tests.

---

## 14. Regression Results

| Vertical | Live suite |
| --- | --- |
| API-01 Platform Admin | **PASS** (included in 367) |
| API-02 Organization / Facility / Site | **PASS** |
| API-03 Identity / User / Role | **PASS** |
| Authentication | **PASS** |

No API-01/02/03 failures.

---

## 15. Known Non-Blocking Issues

- Pre-implementation dotted audit names (`customer.created`) were **not** used. Live API-01/02/03 uppercase actions are the runtime convention; this gate follows them.
- Quarantined scaffold models still exist on disk and fail Ruff if linted as a package glob. They are unused. Not cleaned (out of scope).
- Flutter working tree already had unrelated auth/API-02 changes from prior verticals. This task did not modify Flutter.
- National vs E.164-shaped phone forms remain distinct by **OPTION A**. This is the frozen uniqueness rule, not a defect. Real-world E.164 identity requires a Customer country/numbering-plan field that API-04 does not have.

---

## 16. Deferred Dependencies

- **API-05 Membership** still has divergent ORM FKs to `customer.customers.customer_id`. SQL already FKs `customer.customer.record_id`. Align ORM at API-05.
- **API-06 Attendance** (and walk-in) same ORM gap.
- Billing / support / training / communication ORM FKs to the plural scaffold table — later verticals.
- Customer portal / login / UserAccount link
- Family membership graph
- Object-storage document bytes
- Role seed for Reception / Facility Manager (data via API-03)
- Facility home-transfer API (not in the 12; only site transfer exists)

---

## 17. Final Gate Checklist

- [x] exactly 12 API-04 operations
- [x] API registry remains 222
- [x] migration 013 applied
- [x] migrations 001–012 unchanged
- [x] authoritative Customer ORM
- [x] quarantined ORM unused
- [x] Customer permissions seeded
- [x] authorization enforced
- [x] organization isolation enforced
- [x] facility isolation enforced
- [x] site isolation enforced
- [x] duplicate phone rule enforced
- [x] phone uniqueness is the normalized supplied representation (OPTION A)
- [x] customer code uniqueness enforced
- [x] lifecycle enforced
- [x] transfer rules enforced
- [x] ETag/If-Match enforced where required
- [x] audit implemented
- [x] audit atomicity verified
- [x] semantic errors verified
- [x] PostgreSQL tests passing
- [x] live API tests passing
- [x] API-01 regression passing
- [x] API-02 regression passing
- [x] API-03 regression passing
- [x] OpenAPI validated
- [x] no Flutter changes
- [x] no unrelated cleanup of legacy modules

---

## 18. Final Recommendation

**API-04 backend is ready to freeze.**

Phone uniqueness is frozen as OPTION A (normalized supplied representation). Do not start Flutter API-04 integration until this implementation gate is explicitly reviewed. The next step is a separate **Flutter API-04 Customer Integration Gate**.

---

## 19. Phone Canonicalization Review (2026-09-12)

**Decision: OPTION A — ACCEPT CURRENT DESIGN**

### Rule

Uniqueness applies to the **normalized supplied representation**, not inferred real-world telephone identity.

- Formatting (spaces, parentheses, hyphens, dots) is stripped.
- A leading `+` is preserved: stored form is `+` plus digits (E.164-shaped only when the caller supplied `+`).
- Without `+`, digits are stored as a national form. National digits are **not** converted to E.164.
- Digitize has no authoritative numbering-plan country on the Customer contract. Optional `tenant.organization.country_code` is not used as phone context.
- Therefore `9876543210` and `+919876543210` remain distinct. Treating them as the same number would require guessing a country, which is not internationally valid.
- Duplicate compare remains organization-scoped, non-archived, non-null `primary_phone`.
- The same normalized phone may exist in different Organizations.
- An archived Customer does not block reuse of that phone.

This matches the pre-implementation rule: store E.164-shaped values when the input starts with `+`; otherwise store digits-only national form; duplicate compare uses the normalized stored form.

### Why not OPTION B or OPTION C

- OPTION B (silent E.164 conversion of national numbers) would guess a country. No Customer, facility, site, or required organization numbering-plan field exists. Using optional organization `country_code` would still guess.
- OPTION C (contract change) is not required to freeze API-04. The frozen contract is `primary_phone: str` only. Adding country/phone-type would be a later additive contract, not a freeze blocker. The current dual-form uniqueness is intentional, not an incomplete contract.

### What changed in this review

| Surface | Changed |
| --- | --- |
| Runtime phone behavior | **No** |
| HTTP contract / registry / OpenAPI | **No** |
| Migration 013 / Alembic head | **No** |
| Flutter | **No** |
| `phone.py` docstring | Yes (documents OPTION A; no logic change) |
| Focused unit + live tests | Yes |

### Existing-data / future conversion

Migration 013 was applied against zero Customer rows. OPTION A does not rewrite stored phones. If a later vertical adds authoritative country context and E.164 identity:

- Do not silently rewrite national numbers.
- `+`-prefixed stored values are already E.164-shaped and can be compared as-is.
- National stored values must remain distinct until country is known on the contract.

### Validation (this review)

| Gate | Result |
| --- | --- |
| Focused phone unit (`tests/customer/test_phone.py`) | **5 passed** |
| Backend default (`pytest -q`) | **198 passed, 182 skipped** |
| Backend live (`DIGITIZE_API_TEST=1 pytest -q`) | **370 passed, 10 skipped** |
| OpenAPI | **Unchanged** (12 Customer operation IDs; product inventory 222) |
| Migration | **Unchanged** (`013_customer_master` head) |
| API-01 / API-02 / API-03 / Authentication | **PASS** (included in live 370) |

Default 196 → 198 from two additional phone unit cases. Live 367 → 370 from those unit cases plus one live canonicalization test (formatting duplicate, national vs `+` distinct, org isolation, archive reuse).

**Blocking issues:** 0  
**Freeze recommendation after phone review:** **FREEZE**
