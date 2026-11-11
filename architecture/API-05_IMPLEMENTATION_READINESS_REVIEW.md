# API-05 Slice 1 — Implementation-Readiness Review

**Date:** 17 September 2026  
**Scope:** Review only. **No implementation.**  
**Authoritative:** DR-020 (**Accepted**); Slice 1 contract `API-05_MEMBERSHIP_PLAN_CONTRACT_REVIEW.md` v2.0 (**CONTRACT READY**).

Do not reopen DR-019, DR-020, API-02, operation IDs, or the 228 inventory.

**Slice:** the frozen 12 membership operations with `{membership_id}` paths. Membership Plan HTTP remains **out of inventory**.

---

## 1. Verdict

```text
API-05 IMPLEMENTATION READINESS: PASS
API-05 CONTRACT: FROZEN FOR IMPLEMENTATION
API-05 IMPLEMENTATION: AUTHORIZED TO START
228 API INVENTORY: UNCHANGED
```

The 12 operations can be implemented **without guessing deferred commercial rules**, by applying the contract’s conservative boundaries (no proration in API-05, site-within-facility transfer only, payment **reference** via `invoice_id` / unpaid → not `ACTIVE`, Staff denied on mutations the contract marked as a gap).

Items below classified **SAFE DEFERRED** must not be “solved” by inventing product policy. Items classified as **in-scope engineering** (ORM FK, permission seed migration, history table mapping) **are part of Slice 1 implementation**, not separate product gates.

---

## 2. Inventory / path integrity

| catalog_id | Method | Path | operation_id | Registry match |
| --- | --- | --- | --- | --- |
| API-05-001 | POST | `/api/v1/memberships` | `memberships_create` | PASS |
| API-05-002 | POST | `/api/v1/memberships/{membership_id}/activate` | `memberships_activate` | PASS |
| API-05-003 | POST | `/api/v1/memberships/{membership_id}/renewals` | `memberships_renewals_create` | PASS |
| API-05-004 | POST | `/api/v1/memberships/{membership_id}/upgrade` | `memberships_upgrade` | PASS |
| API-05-005 | POST | `/api/v1/memberships/{membership_id}/downgrade` | `memberships_downgrade` | PASS |
| API-05-006 | POST | `/api/v1/memberships/{membership_id}/freeze` | `memberships_freeze` | PASS |
| API-05-007 | POST | `/api/v1/memberships/{membership_id}/resume` | `memberships_resume` | PASS |
| API-05-008 | POST | `/api/v1/memberships/{membership_id}/transfer` | `memberships_transfer` | PASS |
| API-05-009 | POST | `/api/v1/memberships/{membership_id}/cancel` | `memberships_cancel` | PASS |
| API-05-010 | POST | `/api/v1/memberships/{membership_id}/expire` | `memberships_expire` | PASS |
| API-05-011 | GET | `/api/v1/memberships/{membership_id}` | `memberships_get` | PASS |
| API-05-012 | GET | `/api/v1/memberships/{membership_id}/history` | `memberships_history_list` | PASS |

Count **12**. Total numbered inventory **228**. Empty router `app/modules/membership/routes.py` — not mounted. **NOT STARTED.**

---

## 3. Area reviews

### A. Contract integrity — PASS

Slice 1 contract defines envelope (API-00), JWT staff principal, errors (`MEMBERSHIP_*`), history offset pagination, audit+UoW, `Idempotency-Key` on POSTs, If-Match on mutations of existing rows. Matches live API-02/03/04/09 patterns.

Request/response **logical** shapes are specified; Pydantic types are an implementation deliverable (same as prior verticals).

### B. Lifecycle — PASS (deferred rules not used as guesses)

| Op | Source → target | Invalid | Idempotency | If-Match | Audit |
| --- | --- | --- | --- | --- | --- |
| create | → `PENDING_PAYMENT` or `ACTIVE` (no payment required) | Plan not `ACTIVE`; bad customer/facility | Key on POST | n/a | Yes |
| activate | `DRAFT`/`PENDING_PAYMENT` → `ACTIVE` | Already terminal / `FROZEN` | Key; no-op if `ACTIVE`+same key | Yes | Yes |
| renew | `ACTIVE` → `ACTIVE` (extended dates) | Plan `ARCHIVED` for **renew onto that plan**; `CANCELLED`/`EXPIRED` | Key | Yes | Yes |
| upgrade/downgrade | `ACTIVE` → `ACTIVE` (new `membership_plan_id`) | Target plan not `ACTIVE`/wrong facility | Key | Yes | Yes |
| freeze | `ACTIVE` → `FROZEN` | Already frozen/cancelled/expired | Key | Yes | Yes |
| resume | `FROZEN` → `ACTIVE` | Not frozen | Key | Yes | Yes |
| transfer | same org, **same facility**, site change | Cross-org; **cross-facility rejected** until addendum | Key | Yes | Yes |
| cancel | non-terminal → `CANCELLED` | Already cancelled/expired | Key; no-op if cancelled+same key | Yes | Yes |
| expire | `ACTIVE`/`FROZEN` → `EXPIRED` | Already expired/cancelled; **not** implied by plan archive | Key | Yes | Yes |
| get / history | n/a | Out of scope → 404 | n/a | n/a | Get/history not audited as writes |

**Effective dates:** `starts_at` required; `ends_at` from plan `duration_days` when present. Fine-grained calendar policy = **SAFE DEFERRED** (derive duration; do not invent fiscal calendars).

**DEFERRED (not BLOCKER):** proration, freeze duration/fees, refund on cancel, expiry **jobs** (expire remains an explicit API).

### C. Authorization — PASS

Roles: Platform Admin, Organization Admin, Site Admin, Staff. **No Manager.**

| Role | Implementation rule |
| --- | --- |
| Platform Admin | Allowed per platform permissions (DR-019) |
| Organization Admin | Org-scoped |
| Site Admin | Assigned site/facility only; **not** org-wide plan admin (N/A for Slice 1 HTTP plans) |
| Staff | Operational: create, activate, renew, freeze, resume, get, history **when** `membership.*` is bound. **Deny** upgrade, downgrade, transfer, cancel, expire until a later permission decision — contract already called this a **gap**; conservative deny is implementable without inventing Staff rights. |

Permission **strings** are contract families (`membership.create`, …). They are **not** in identity seed today. Seeding them in a Slice 1 Alembic (same pattern as `013_customer_master`) is **in-scope implementation**, not a product blocker. Do not seed in this review.

### D. Customer dependency — implementation prerequisite (in-scope)

SQL `004`: `customer_membership.customer_id` → **`customer.customer(record_id)`**.  
ORM `CustomerMembership`: FK **`customer.customers.customer_id`** (wrong).

DR-020 P1-012: align ORM **before writes**. That alignment **is the first engineering step of Slice 1**, not a reason to withhold authorization. Classification: **implementation prerequisite — in scope**. Not a product BLOCKER. Not safely skippable.

Customer ≠ Participant. No family/guardian in Slice 1.

### E. Membership Plan dependency — PASS

New sale requires plan `ACTIVE`. `DRAFT`/`ARCHIVED` cannot be newly sold. Archived plan does not terminate existing memberships. Plan HTTP **not** in 228. Plan status ≠ membership status.

Plan rows may be **seeded/SQL** for tests; no Plan admin API.

SQL/Flutter `active`/`inactive` vs `DRAFT`/`ACTIVE`/`ARCHIVED`: **SAFE DEFERRED** for Flutter (Slice 1 is membership HTTP). Implementation **writes** the frozen three plan statuses when creating test plans; no Flutter enum change required to ship Slice 1.

### F. Payment boundary — SAFE DEFERRED (mapping), PASS (ownership)

API-08 is not live. API-05 must not process payments.

**Implementable boundary (already in contract, not a new mapping):**

- `customer_membership.invoice_id` is optional, **no FK** in 004 (safe to store a reference).
- Paid plan (`price_amount` > 0) without a confirmed reference → create as `PENDING_PAYMENT`; activate without reference → `MEMBERSHIP_PAYMENT_001`.
- `price_amount` null/0 → may create `ACTIVE` (FR complimentary).
- Do **not** call a payment API. Do **not** invent refund/PSP state machines.

Full API-08 status enumeration = **SAFE DEFERRED**.

### G. Concurrency — PASS

`version_number` on `customer_membership`. Use existing If-Match / ETag (API-04). Create: no If-Match.

### H. Idempotency — PASS

Platform `Idempotency-Key` on all Slice 1 POSTs. Sufficient. Do not invent a new key format.

### I. Audit / UoW — PASS

Same as API-04: mutation + `audit.audit_event` (+ history row) in one UoW.

### J. Errors — PASS

Use existing `MEMBERSHIP_*` and platform concurrency codes. `DigitizeError`; no route `HTTPException`. No new numbered error codes required.

### K. History — PASS

SQL `membership.membership_lifecycle_history` matches catalog (`from_status`, `to_status`, `changed_by`, `changed_at`). Offset pagination + newest-first as contracted.

**ORM note:** `MembershipStatusHistory` maps `membership_status_history` (different physical table). Implementation must persist **`membership_lifecycle_history`** (004 / catalog). Dual legacy model = in-scope mapping, not a product blocker.

### L. Database / ORM — PASS with in-scope fixes

| Object | Readiness |
| --- | --- |
| `membership.membership_plan` | Present; facility-owned; `version_number` |
| `membership.customer_membership` | Present; org/facility; `invoice_id`; `version_number`; **no `site_id` column** |
| `membership.membership_lifecycle_history` | Present in 004; use for API-05-012 |
| `membership.membership_renewal` / freeze | Present; optional for renew/freeze rows |
| Customer FK SQL | Correct (`customer.customer`) |
| Customer FK ORM | **Wrong** — fix in Slice 1 |
| Default `membership_status='ACTIVE'` | Override in create; do not rely on default for unpaid |
| Plan `deleted_at` | None; archive via `plan_status` |
| Soft-delete membership | No `deleted_at`; cancel/expire are statuses |

**`site_id`:** not on `customer_membership`. Contract site is conditional. **SAFE DEFERRED** as a column; store operational site in `metadata` for Slice 1 **or** add a column in the Slice 1 migration. Adding `site_id` is allowed as implementation schema **if** required for Site Admin scoping; it is not a product reopen of DR-020. If Site Admin isolation is required on day one, **prefer adding `site_id` in the Slice 1 migration** (engineering), not blocking the gate.

### M. Soft delete / historical integrity — PASS

Plan archive does not CASCADE-delete memberships (`ON DELETE RESTRICT` on plan FK). Snapshot fields on get/history per contract. No schema redesign in this review.

### N. Flutter — INFORMATIONAL (not a blocker)

`UnavailableMembershipPlanRepository` is **Plan** HTTP, Slice 2. There is **no** Flutter customer-membership remote repository for the 12 ops. Architecture does **not** require Flutter for backend Slice 1 (API-04 shipped backend-first). **Not a blocker.**

### O. Minimum test matrix (do not write tests here)

- Happy path: create (unpaid → `PENDING_PAYMENT`; zero-price → `ACTIVE`) → activate → get → history
- Renew / freeze / resume / cancel / expire happy paths
- Upgrade/downgrade to `ACTIVE` same-facility plan
- Transfer same-facility site (or metadata site); reject other facility; reject other org
- Validation: missing fields, date `ends_at < starts_at`
- AuthZ: missing permission; Staff denied on cancel/transfer/upgrade as implemented
- Isolation: org, facility, site (once `site_id` or equivalent exists)
- Plan `DRAFT`/`ARCHIVED` cannot create/upgrade-to
- Archived plan: existing membership get/activate still allowed; renew blocked
- Payment: activate without `invoice_id` on priced plan → `MEMBERSHIP_PAYMENT_001`
- Idempotency replay; If-Match missing/stale
- Audit row + history row same commit; rollback on audit failure
- 404 cross-tenant get
- Customer archived cannot create

---

## 4. Deferred-item classification

| Item | Class | Why |
| --- | --- | --- |
| Proration | **SAFE DEFERRED** | Upgrade/downgrade change plan_id only; no money math |
| Freeze fees | **SAFE DEFERRED** | Freeze is a status change |
| Refunds | **SAFE DEFERRED** | API-08; cancel does not execute refunds |
| Expiry jobs | **SAFE DEFERRED** | `memberships_expire` is an explicit API |
| API-08 state mapping | **SAFE DEFERRED** | `invoice_id` present/absent is enough |
| Duplicate-membership policy | **SAFE DEFERRED** with contract default | Reject second `ACTIVE`/`PENDING_PAYMENT` for same customer+plan+facility |
| Staff allow/deny on some mutations | **SAFE DEFERRED** | Implement conservative **deny** on upgrade/downgrade/transfer/cancel/expire for Staff |
| Permission seeds | **In-scope engineering** | Alembic seed like API-04; not a product decision |
| Membership list | **SAFE DEFERRED** | Not in 228 |
| Membership Plan HTTP inventory | **SAFE DEFERRED** | Slice 2 |
| ORM customer FK | **In-scope engineering** | Mandatory first step; does not block **authorization to start** |
| SQL/Flutter Plan status strings | **SAFE DEFERRED** (Flutter); **in-scope** (backend tests use DRAFT/ACTIVE/ARCHIVED) | |

None of the above is a **product BLOCKER** that withholds implementation authorization.

---

## 5. Readiness matrix

| Area | Status | Blocker? | Evidence | Required action |
| --- | --- | --- | --- | --- |
| Contract integrity | PASS | No | v2.0 contract + registry 12 ops | Implement against contract |
| Inventory / IDs / paths | PASS | No | `operations.py`; `{membership_id}` | Do not change |
| Lifecycle | PASS | No | Contract §7 | Honor conservative transfer/renew rules |
| Authorization model | PASS | No | DR-019 + contract matrix | Seed `membership.*` in Slice 1 migration |
| Staff mutation gaps | SAFE DEFERRED | No | Contract gap | Deny Staff on listed mutations |
| Customer identity | PASS | No | API-04 live; SQL FK correct | Fix ORM FK in Slice 1 |
| Plan sellability | PASS | No | DR-020 statuses | Enforce on new sale |
| Payment ownership | PASS | No | DR-020 / contract | References only |
| API-08 mapping | SAFE DEFERRED | No | `invoice_id` column | No PSP |
| Concurrency | PASS | No | `version_number`; API-04 If-Match | Apply to mutations |
| Idempotency | PASS | No | API-00 header | All POSTs |
| Audit UoW | PASS | No | API-04 pattern | Same commit |
| Errors | PASS | No | `MEMBERSHIP_*` | No new codes |
| History | PASS | No | `membership_lifecycle_history` | Map ORM to 004 table |
| DB tables | PASS | No | 004 SQL | Use existing |
| site_id column | SAFE DEFERRED / engineering | No | Not on membership table | metadata or Slice 1 column |
| Soft-delete / archive | PASS | No | RESTRICT FKs | Snapshot on get |
| Flutter Slice 1 | INFORMATIONAL | No | No membership instance client | Backend-first OK |
| Plan HTTP | SAFE DEFERRED | No | DR-020 Slice 2 | Do not add IDs |
| List GET | SAFE DEFERRED | No | P1-009 | Do not add |

---

## 6. Implementation start constraints (not blockers)

When implementation **starts**, it **must**:

1. Point `CustomerMembership.customer_id` at `customer.customer.record_id`.
2. Seed contract `membership.*` permissions (not invent new families).
3. Write history to `membership.membership_lifecycle_history`.
4. Not implement Plan HTTP, list GET, IAP, or API-08 processors.
5. Not introduce a Manager role.

---

## 7. Test / auth / isolation reminder

Minimum matrix: §3.O. Organization, facility, and (if `site_id` present) site isolation tests are mandatory. Invalid transitions and plan-status tests are mandatory.

---

## 8. Final decision

```text
API-05 IMPLEMENTATION READINESS:
PASS

API-05 CONTRACT:
FROZEN FOR IMPLEMENTATION

API-05 IMPLEMENTATION:
AUTHORIZED TO START

228 API INVENTORY:
UNCHANGED
```

**Next task:** Slice 1 **implementation** of the 12 operations. Do not open another broad architecture review. Do not implement in **this** document’s task.

```text
API-05 IMPLEMENTATION READINESS: PASS
API-05 IMPLEMENTATION: AUTHORIZED
API-05 OPERATIONS: 12
TOTAL API INVENTORY: 228
DR-020: ACCEPTED
SOURCE/SCHEMA/ROUTE CHANGES: NONE
```
