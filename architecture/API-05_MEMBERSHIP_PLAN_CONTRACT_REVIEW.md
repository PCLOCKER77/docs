# API-05 Membership — Slice 1 Contract Finalization

**Document version:** 2.0  
**Status:** CONTRACT READY (Slice 1 specification)  
**Date:** 16 September 2026  
**Supersedes:** this file’s 1.x contract **review** (blocked on P0/P1). Product decisions are **DR-020 Accepted**.  
**Scope:** Documentation only. **Does not implement** API-05.  
**Inventory:** **228** numbered APIs unchanged. API-05 remains **12** operations. No new catalog IDs. Semantic `operation_id` unchanged.

**Authoritative product record:** `docs/99_Decision_Records/DR-020_API-05_Membership_Plan_and_Membership_Scope.md`

**Next gate:** API-05 **implementation-readiness review** (not coding).

This document is the Slice 1 **Membership** HTTP contract. It is not a Membership Plan HTTP contract.

---

## 0. Frozen inventory paths

Official numbered paths include `{membership_id}` (registry / `operations.py` / DR-020). Those paths are **not** rewritten here. Catalog IDs remain metadata; runtime identity is `operation_id`.

| Catalog ID | Method | Path | operation_id |
| --- | --- | --- | --- |
| API-05-001 | POST | `/api/v1/memberships` | `memberships_create` |
| API-05-002 | POST | `/api/v1/memberships/{membership_id}/activate` | `memberships_activate` |
| API-05-003 | POST | `/api/v1/memberships/{membership_id}/renewals` | `memberships_renewals_create` |
| API-05-004 | POST | `/api/v1/memberships/{membership_id}/upgrade` | `memberships_upgrade` |
| API-05-005 | POST | `/api/v1/memberships/{membership_id}/downgrade` | `memberships_downgrade` |
| API-05-006 | POST | `/api/v1/memberships/{membership_id}/freeze` | `memberships_freeze` |
| API-05-007 | POST | `/api/v1/memberships/{membership_id}/resume` | `memberships_resume` |
| API-05-008 | POST | `/api/v1/memberships/{membership_id}/transfer` | `memberships_transfer` |
| API-05-009 | POST | `/api/v1/memberships/{membership_id}/cancel` | `memberships_cancel` |
| API-05-010 | POST | `/api/v1/memberships/{membership_id}/expire` | `memberships_expire` |
| API-05-011 | GET | `/api/v1/memberships/{membership_id}` | `memberships_get` |
| API-05-012 | GET | `/api/v1/memberships/{membership_id}/history` | `memberships_history_list` |

**Not in this contract / not in 228:** `GET /api/v1/memberships` (`memberships_list`). DR-020: future requirement; inventory decision still required. Do not implement.

---

## 1. Resource boundaries

```text
Membership Plan ≠ Membership
Customer ≠ Participant
Plan status ≠ Membership status
```

| Resource | Owner | Meaning |
| --- | --- | --- |
| Membership Plan | Facility (Organization parent) | Catalog product. Status: `DRAFT` / `ACTIVE` / `ARCHIVED` (DR-020). **No HTTP in 228.** |
| Membership | Customer | Purchased/lifecycle instance. Slice 1 HTTP. |
| Payment | API-08 | Money movement. API-05 may **reference** only. |
| SaaS | API-09 | Organization → Digitize/OreeOn. Out of API-05. |

Hierarchy: Platform → Organization → Facility → Site. Roles: Platform Admin, Organization Admin, Site Admin, Staff. **No Manager.**

---

## 2. Domain model

### 2.1 Membership Plan (dependency, not HTTP)

| Status | Meaning (DR-020) |
| --- | --- |
| `DRAFT` | Configured; **not** available for new sale |
| `ACTIVE` | **Available for new sale** |
| `ARCHIVED` | **Not** available for new sale; retained historically |

Plan preconditions for **new sale** (create, and target plan on upgrade/downgrade/renew onto a plan):

- Plan exists.
- Plan `facility_id` matches the membership facility.
- Plan `organization_id` matches the tenant.
- Plan status is `ACTIVE`.
- `DRAFT` cannot be sold.
- `ARCHIVED` cannot be newly sold.

Existing memberships on a plan that later becomes `ARCHIVED` **remain valid** under their own lifecycle (DR-020 P1-006).

Sold commercial terms must not be silently rewritten (DR-020 P1-005). Responses that need historical correctness carry a **plan snapshot** (code, name, type, duration_days, list price/currency, plan_id, plan_status_at_sale if stored) — implementation may persist snapshot in membership metadata or history payload; **no schema change in this gate**.

SQL/Flutter plan enums are reconciled at **implementation**, not here.

### 2.2 Membership lifecycle (instance)

Separate from plan status. Documented instance states (FR-08 / DR-020):

```text
DRAFT
PENDING_PAYMENT
ACTIVE
FROZEN
CANCELLED
EXPIRED
```

Do not add extra instance states in this contract. Do not use `FROZEN` / `CANCELLED` / `EXPIRED` / `PENDING_PAYMENT` as **plan** statuses.

---

## 3. Identity, customer, scope

- Membership `customer_id` → API-04 **`customer.customer.record_id`**.
- Legacy ORM `customer.customers` **must be reconciled before writes** (DR-020 P1-012).
- Customer same Organization as membership. Customer ≠ Participant. No guardian/family/participant graph in API-05.
- Facility is required. Site is **conditional** (FR-MEM-001) for operational context.
- Tenant headers / principal org-facility-site as in live API-02/API-04.
- Soft-deleted/archived customers are not valid sale targets (API-04 archive).
- Soft-deleted records are not listed as active (platform rule). History remains readable in scope.

---

## 4. Payment boundary

```text
API-05 = Membership lifecycle
API-08 = Payment / money movement
```

API-05 must **not** process payments, execute refunds, own payment transactions, or create payment methods.

Create **does not** imply payment collected. A membership **may** exist in `PENDING_PAYMENT` (FR-08). Activation requires API-08 success **or** an explicitly recorded **offline** payment according to the API-08 contract.

---

## 5. Cross-cutting HTTP / API-00

- Async services/repos; Pydantic bodies; API-00 envelopes.
- `DigitizeError` in the service layer. **No** route `HTTPException`.
- Correlation / W3C trace IDs; no secrets in logs.
- Mutations: membership change + **audit event** in the **same Unit of Work**.
- Optimistic concurrency on mutations of an existing membership: **If-Match** / `version_number` as API-04 (missing If-Match → 428 `CONCURRENCY_CONFLICT`; stale → 412). Create has no If-Match.
- Idempotency: `Idempotency-Key` required on all Slice 1 **POST** mutations (API-00 / collection). Replay of the same key + same payload returns the original result; conflict → `MEMBERSHIP_IDEMPOTENCY_001`.
- Offset pagination on history (API-05-012). Default exclude inactive/deleted current rows on get (404/`MEMBERSHIP_SCOPE_001` if out of scope).
- Dates: UTC RFC 3339.

### 5.1 Errors (existing families; do not invent numbered codes)

| Situation | Existing code / category |
| --- | --- |
| Unauthenticated | Auth envelope (frozen auth) |
| Forbidden | `MEMBERSHIP_AUTHORIZATION_001` (403) |
| Not found / cross-tenant | `MEMBERSHIP_SCOPE_001` (404) |
| Validation | `MEMBERSHIP_VALIDATION_001` (422) |
| Illegal lifecycle / eligibility | `MEMBERSHIP_ELIGIBILITY_001` (409) |
| Plan not sellable | `MEMBERSHIP_ELIGIBILITY_001` (409) |
| Payment prerequisite | `MEMBERSHIP_PAYMENT_001` (409) |
| Concurrency | `MEMBERSHIP_CONCURRENCY_001` / platform `CONCURRENCY_CONFLICT` (412/428) |
| Idempotency conflict | `MEMBERSHIP_IDEMPOTENCY_001` (409) |
| Infrastructure | Platform 5xx mapping |

---

## 6. Permission families (contract, **not seeded**)

API-03 has no membership permission pack today. Required **families** (dotted, like `customer.create`). Do **not** seed in this gate.

| Family | Typical ops |
| --- | --- |
| `membership.create` | create |
| `membership.activate` | activate |
| `membership.renew` | renewals |
| `membership.upgrade` | upgrade |
| `membership.downgrade` | downgrade |
| `membership.freeze` | freeze |
| `membership.resume` | resume |
| `membership.transfer` | transfer |
| `membership.cancel` | cancel |
| `membership.expire` | expire |
| `membership.view` | get |
| `membership.history.view` | history |

**Gap:** none of these are in `IDENTITY` / customer seed packs. Binding to roles is an **implementation-readiness** item (P1-011 deferred). Until seeded, this matrix is the **intended** allow/deny; it is not live RBAC data.

### 6.1 Authorization matrix

A = allowed in scope · S = allowed, **scope-limited** (assigned org / facility / site) · D = denied · V = allowed only with extra business validation (plan, payment, lifecycle).

| operation_id | Platform Admin | Organization Admin | Site Admin | Staff |
| --- | --- | --- | --- | --- |
| `memberships_create` | A / platform perms | S org | S assigned site/facility | S operational (FR Reception) + V |
| `memberships_activate` | A | S | S | S operational + V (payment) |
| `memberships_renewals_create` | A | S | S | S operational + V |
| `memberships_upgrade` | A | S | S | S if existing ops model allows; else D — **gap** |
| `memberships_downgrade` | A | S | S | same as upgrade — **gap** |
| `memberships_freeze` | A | S | S | S operational + V |
| `memberships_resume` | A | S | S | S operational + V |
| `memberships_transfer` | A | S | S site of source/target | D unless FR assigns Reception — **gap**; OA/SA primary |
| `memberships_cancel` | A | S | S | S limited — **gap** |
| `memberships_expire` | A | S | S | D (administrative/system; Staff not assumed) |
| `memberships_get` | A | S | S | S view |
| `memberships_history_list` | A | S | S | S view |

Site Admin: **not** organization-wide. Staff: **no** plan configuration (DR-020). Do not invent additional Staff permissions beyond FR operational membership actions.

---

## 7. Operation contracts

Unless noted: POST success **200** with resulting membership (create **201**); GET **200**. Bodies snake_case. All mutations: UoW + audit + history row.

### 7.1 `memberships_create`

**Request (logical):** `customer_id` (API-04), `membership_plan_id`, `facility_id`, `site_id` (conditional), `starts_at` (or start date), optional `ends_at` if not derived, optional payment/invoice **references**, remarks.

**Validation:** Customer exists, not archived, same org. Facility active, same org. Plan exists, same facility, status **`ACTIVE`**. Dates consistent. Duplicate policy: **not frozen** — see gaps; until then reject a second **ACTIVE** or **PENDING_PAYMENT** membership for the same customer+plan+facility (`MEMBERSHIP_ELIGIBILITY_001`) as a conservative default **only if** implementation-readiness confirms; otherwise treat as gap.

**Initial state:** Does **not** collect payment. If payment required and not confirmed → `PENDING_PAYMENT`. If payment not required / complimentary policy (FR) or API-08 already confirmed → may be `ACTIVE` without a separate activate, **or** `PENDING_PAYMENT` then activate — FR allows both; **contract:** prefer `PENDING_PAYMENT` then `memberships_activate` when payment is required; allow direct `ACTIVE` only when no payment is required.

**Idempotency:** required. **If-Match:** n/a. **Audit:** yes.

### 7.2 `memberships_activate`

**Source states:** `DRAFT`, `PENDING_PAYMENT` (FR-MEM-002). Not `ACTIVE`, `CANCELLED`, `EXPIRED`, `FROZEN`.

**Payment:** API-08 success or recorded offline payment. Else `MEMBERSHIP_PAYMENT_001`. No PSP in API-05.

**Plan:** referenced plan need not still be `ACTIVE` if already sold (P1-006); activation of an already-created instance is not a **new sale**.

**Idempotency:** required (repeat activate on already `ACTIVE` with same key is success/no-op). **If-Match:** required. **Audit:** yes.

### 7.3 `memberships_renewals_create`

**Eligible:** `ACTIVE` (and FR pending-payment renewal paths). Not `CANCELLED` / `EXPIRED`.

**Plan:** renewal continues **current** `membership_plan_id` unless a later rule says otherwise. New sale of a **different** plan is upgrade/downgrade. If current plan is `ARCHIVED`, renewal onto that plan is **blocked** (DR-020 P1-006: no renew onto deactivated plan) → `MEMBERSHIP_ELIGIBILITY_001`.

**Period:** from plan `duration_days` / existing end date — exact calendar math **gap**.

**Payment:** API-08 prerequisite same pattern as activate.

**History:** append renewal record; do not rewrite prior periods. **Idempotency + If-Match + audit.**

### 7.4 `memberships_upgrade` / `memberships_downgrade`

**Source:** typically `ACTIVE`. **Target plan:** exists, **same facility**, status **`ACTIVE`** (new sale of target).

**Effective date:** not frozen (immediate vs next period) — **gap**; do not invent. Until addendum, treat as **immediate** change of `membership_plan_id` only if no proration is required; if a commercial delta is required and API-08 has not confirmed, `MEMBERSHIP_PAYMENT_001`.

**Proration/pricing:** **not frozen**. API-05 does **not** compute proration.

**History:** preserve prior plan via history/snapshot. **Idempotency + If-Match + audit.**

### 7.5 `memberships_freeze` / `memberships_resume`

**Freeze source:** `ACTIVE`, not already `FROZEN` / `CANCELLED` / `EXPIRED` (FR). **Resume source:** `FROZEN`.

**Duration / expiry extension / freeze fees:** **not frozen** — do not invent. Freeze must not become plan archival.

**Payment:** no API-05 money movement. **Idempotency + If-Match + audit.**

### 7.6 `memberships_transfer`

**Organization boundary:** same Organization only (FR-MEM-008 VAL-MEM-TRN-001). Cross-organization **denied**.

**What transfers:** operational assignment of the **same** membership instance (customer ownership unchanged).

**Same facility, different site:** **in contract** (FR site context). Target site active, belongs to membership facility.

**Different facility, same org:** FR lists target facility; DR-020 plan is **facility-owned**. Plan compatibility (“permit target scope or equivalent plan”) is **not fully frozen**. **This contract:** if `target_facility_id` ≠ current `facility_id`, reject `MEMBERSHIP_ELIGIBILITY_001` until a contract addendum defines target plan mapping. Capacity warnings: **gap**.

**Payment:** no processing. **Reason + effective date** required (FR). **Idempotency + If-Match + audit.** Approval workflow in FR is **not** a numbered API — do not add endpoints.

### 7.7 `memberships_cancel`

**States:** not already `CANCELLED` / `EXPIRED` (FR). **Effective date** required. **Reason** required.

**Reversible:** **not frozen**; do not assume uncancel.

**Refunds:** API-08 only; no policy invented. API-05 may store that cancellation occurred.

**Idempotency + If-Match + audit.** Repeat cancel on `CANCELLED` with same key: success/no-op.

### 7.8 `memberships_expire`

**Eligible:** `ACTIVE` or `FROZEN` reaching end (FR). Not already `EXPIRED` / `CANCELLED`.

**Who:** Organization Admin / Site Admin / Platform Admin in scope; **system-driven** expiry may exist later. **No background job** is defined in this contract.

**Plan archival** does **not** expire memberships.

**Idempotency + If-Match + audit.**

### 7.9 `memberships_get`

**200** membership projection in caller scope else `MEMBERSHIP_SCOPE_001`.

**Response (logical):** `membership_id`, `customer_id` (no extra PII beyond id/display fields already used in other staff APIs), `membership_plan_id`, plan **snapshot** fields, `facility_id`, `site_id` if set, `membership_status`, `starts_at` / `ends_at`, `invoice_id` / payment refs if present, `created_at` / `updated_at`, `version_number` (ETag).

### 7.10 `memberships_history_list`

Offset pagination (API-00). Order: `created_at` descending unless standard says otherwise.

Each event: action/type, actor, timestamp, prior/current status, reason, references (invoice, target plan/site). Append-only; **must not** require mutating current membership to reconstruct the past.

Authorization: `membership.history.view` in scope.

---

## 8. Future Membership Plan HTTP Contract — OUT OF CURRENT SCOPE

Architecturally recognized (DR-020 Slice 2). **Not** in the 228.

Likely catalog operations (illustrative **only** — **no** catalog IDs, **no** frozen paths, **no** `operation_id` assignment):

- create / get / list / update-or-revision / archive / activate (plan status)

A **separate inventory decision** is required before any Plan HTTP.

---

## 9. Contract gaps / deferred decisions

Accepted DR-020 items are **not** reopened.

| Item | Status |
| --- | --- |
| Exact upgrade/downgrade proration and pricing | **Deferred** — API-08; not guessed |
| Immediate vs next-period plan change | **Deferred** |
| Cross-facility transfer + equivalent plan mapping | **Deferred**; Slice 1 allows **site-within-facility** only |
| Freeze duration, freeze fees, expiry extension | **Deferred** |
| Cancellation refund policy | **Deferred** — API-08 |
| Automatic expiry job | **Deferred** — not in this contract |
| Exact `starts_at` / end-date calendar rules | **Deferred** (derive from `duration_days` at implementation-readiness) |
| Exact API-08 payment-state machine mapping | **Deferred** to API-08 contract; API-05 only references success/offline/unpaid |
| Duplicate concurrent membership policy (beyond conservative note) | **Deferred** |
| Staff allow/deny on upgrade/downgrade/cancel/transfer | **Gap** — FR vs OA/SA; do not invent |
| Permission **seed** / role bindings | **Deferred** (P1-011) |
| Membership list `GET /memberships` | **Future inventory** (P1-009) |
| Membership Plan HTTP inventory | **Future inventory** (Slice 2) |
| P1-012 ORM alignment | **Implementation prerequisite** |
| SQL/Flutter plan status strings vs DRAFT/ACTIVE/ARCHIVED | **Implementation reconciliation** |

These gaps do **not** reopen DR-020. They are insufficient to block **specifying** the 12 operations; they **do** block claiming **implementation readiness**.

---

## 10. Transaction / audit / history integrity

Every mutation: business write + `audit.audit_event` (+ membership history) in one UoW. Failure rolls back all.

Archived plans remain referencable so history does not lose commercial context.

---

## 11. Gate

```text
API-05 CONTRACT FINALIZATION

STATUS: CONTRACT READY

Meaning: Slice 1 HTTP contract is specified for the frozen 12 operations.
Not meaning: ready to code; implementation-readiness is a separate gate.

DR-020: ACCEPTED
API-05 OPERATIONS: 12
TOTAL NUMBERED API INVENTORY: 228
MEMBERSHIP PLAN HTTP: FUTURE — INVENTORY DECISION REQUIRED
IMPLEMENTATION: NOT STARTED
```
