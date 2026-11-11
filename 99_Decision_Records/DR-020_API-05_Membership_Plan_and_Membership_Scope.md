# DR-020 API-05 Membership Plan and Membership Scope

> Accepted product/architecture decision for API-05 resource split, Slice 1 vs Slice 2, plan ownership, authority, plan status vocabulary, sold-plan versioning, archive behavior, and membership list as a future inventory item. This record does **not** implement APIs, change the 228 inventory, or assign catalog IDs.

---

# 1. Decision Record Metadata

| Field | Value |
| --- | --- |
| Document ID | DR-020 |
| Document Name | API-05 Membership Plan and Membership Scope |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | **Accepted** |
| Owner | Architecture / Product |
| Reviewers | Architecture, Product, Backend, Identity, Commercial |
| Version | 2.0 |
| Last Updated | 2026-09-16 |
| Relates to | DR-004 (hierarchy); DR-019 (roles, commerce, Customer ≠ Participant); API-04 Customer identity |
| Does not supersede | DR-019; API-01…API-04 and API-09 implementation freezes; operation-ID freeze |
| Implementation | **Not started** |
| Product approval | Explicitly approved in the API-05 product decision gate. |

**Companions**

- `docs/architecture/API-05_MEMBERSHIP_PLAN_CONTRACT_REVIEW.md`
- `docs/architecture/API-05_MEMBERSHIP_PLAN_PRODUCT_DECISION_BRIEF.md`

**Next gate:** API-05 **Contract Finalization** (not implementation).

---

# 2. Context

The Access / Mobile / Commerce architecture is frozen (DR-019). Contract review found that “API-05 Membership Plan” in product/UI language is not the same resource as the frozen numbered API-05 inventory (customer Membership lifecycle).

The API-05 Product Approval Gate recorded explicit approval of P0-001 and P1-001, P1-003, P1-004, P1-005, P1-006, P1-009, and P1-012. This version of DR-020 **accepts** those decisions.

Physical tables already exist for `membership.membership_plan` and `membership.customer_membership`. Flutter Membership Plan HTTP remains unavailable until Slice 2 plus an inventory decision. Membership routes remain an empty skeleton. **No implementation in this record.**

---

# 2a. Product Approval Gate (recorded)

**Product approval:** Explicitly approved in the API-05 product decision gate.

Inherited and **not reopened** (DR-019 / inventory freeze / API-00 / API-04): hierarchy; four roles and no Manager; Customer ≠ Participant; API-08 facility payments; API-09 SaaS; semantic `operation_id`; 228 numbered APIs; API-05 remains 12 operations.

| ID | Decision | Record |
| --- | --- | --- |
| P0-001 | Option C; Slice 1 = 12 membership ops; Slice 2 = plan HTTP later; Option B rejected | **APPROVED** |
| P1-001 | Facility-owned plan; Organization parent; sold through facility | **APPROVED** |
| P1-003 | OA configures/approves plans; Site Admin not org-wide plan config; Staff cannot configure plans | **APPROVED** |
| P1-004 | Plan status = `DRAFT` / `ACTIVE` / `ARCHIVED` | **APPROVED** |
| P1-005 | No silent rewrite of sold commercial terms; revision/clone later | **APPROVED** |
| P1-006 | Archive/deactivate: no new sales; existing memberships not auto-terminated | **APPROVED** |
| P1-009 | Membership list is a future API requirement; **not** added to 228 | **APPROVED** — future inventory decision still required before implementation |
| P1-012 | Align membership FK to API-04 `customer.customer` before writes | **APPROVED AS IMPLEMENTATION PREREQUISITE** |

---

# 3. Problem Statement

Without an explicit split of Membership Plan (catalog) and Membership (instance), implementation would retcon the 12 numbered operations into plan CRUD (Option B — **rejected**), ship enrollment with no governed catalog, or invent catalog IDs outside the 228.

The 228 inventory remains unchanged in this record.

---

# 4. Authoritative Existing API-05 Inventory

**Count:** 12 numbered operations. **Official product total:** **228** (unchanged).

`catalog_id` is **product metadata only**. Runtime identity is semantic `operation_id`.

| catalog_id | Method | Path | Purpose | operation_id |
| --- | --- | --- | --- | --- |
| API-05-001 | POST | `/api/v1/memberships` | Create Membership | `memberships_create` |
| API-05-002 | POST | `/api/v1/memberships/{membership_id}/activate` | Activate Membership | `memberships_activate` |
| API-05-003 | POST | `/api/v1/memberships/{membership_id}/renewals` | Renew Membership | `memberships_renewals` |
| API-05-004 | POST | `/api/v1/memberships/{membership_id}/upgrade` | Upgrade Membership | `memberships_upgrade` |
| API-05-005 | POST | `/api/v1/memberships/{membership_id}/downgrade` | Downgrade Membership | `memberships_downgrade` |
| API-05-006 | POST | `/api/v1/memberships/{membership_id}/freeze` | Freeze Membership | `memberships_freeze` |
| API-05-007 | POST | `/api/v1/memberships/{membership_id}/resume` | Resume Membership | `memberships_resume` |
| API-05-008 | POST | `/api/v1/memberships/{membership_id}/transfer` | Transfer Membership | `memberships_transfer` |
| API-05-009 | POST | `/api/v1/memberships/{membership_id}/cancel` | Cancel Membership | `memberships_cancel` |
| API-05-010 | POST | `/api/v1/memberships/{membership_id}/expire` | Expire Membership | `memberships_expire` |
| API-05-011 | GET | `/api/v1/memberships/{membership_id}` | View Membership Details | `memberships_get` |
| API-05-012 | GET | `/api/v1/memberships/{membership_id}/history` | View Membership History | `memberships_history_list` |

There is **no** numbered GET `/api/v1/memberships` list. There are **no** numbered `/api/v1/membership-plans` operations.

FR mapping: FR-MEM-001 … FR-MEM-012 (membership **instances**).

---

# 5. Target Domain Model

```text
Membership Plan ≠ Membership
```

Do **not** combine these into one resource, schema, permission family, or lifecycle.

### Membership Plan

- Facility-owned customer product / catalog definition.
- Organization is the **parent business owner**.
- Sold through the applicable facility (Customer → Facility).
- **Not** SaaS subscription/license configuration (API-09 / Organization → Digitize/OreeOn).

### Membership

- Customer-owned **instance**: the customer’s purchased/lifecycle relationship to a Membership Plan.
- Holder is the **Customer** (API-04). **Customer ≠ Participant.**

```text
Membership Plan  (catalog)  ──sold as──►  Membership (instance)
                                              │
                                              ├── payment refs → API-08
                                              └── attendance → API-06 (Participant may differ)
```

---

# 6. P0 Scope Decision

**Status: APPROVED**

### Target architecture: Option C

API-05 ultimately contains two separate resources:

1. Membership Plan configuration  
2. Customer Membership lifecycle  

Separate routes, permissions, schemas, and lifecycle rules.

**Option B** (convert the existing 12 operations into Plan APIs) is **rejected**.

### Slice 1 — Frozen current scope

The existing **12** numbered membership operations in §4. Catalog IDs and semantic `operation_id` values **must not** be modified.

Slice 1 does **not** include Membership Plan HTTP. Plans may exist as **data** that Slice 1 **reads** when creating a membership.

### Slice 2 — Future scope

Membership Plan HTTP / catalog management.

Requires a **separate API inventory decision** before implementation. **Do not** add plan APIs to the current 228.

```text
228 numbered product APIs remain unchanged.
```

---

# 7. P1 Decision Register

### P1-001 — Plan ownership

**Status: APPROVED**

- Membership Plan is **facility-owned**.
- Organization is the parent business owner.
- Plan is sold through the applicable facility.
- Membership Plan is **not** SaaS subscription/license configuration.

```text
Organization → Digitize/OreeOn     (API-09)
Customer → Facility                (membership commerce + API-08)
```

Not organization-owned as the product entity. Not site-owned. Site-specific plan applicability remains **DEFERRED** (P1-002).

### P1-002 — Site applicability

**Status: DEFERRED**

Do not introduce site-specific plan applicability unless a later explicit approval exists. Slice 1 default: facility-level product.

### P1-003 — Plan configuration authority

**Status: APPROVED**

Authoritative roles (DR-019; **no Manager**):

```text
Platform Admin
Organization Admin
Site Admin
Staff
```

**Organization Admin:** organization-level authority to **configure and approve** Membership Plans.

**Site Admin:** remains a **site-scoped** administrative role. Does **not** automatically receive organization-wide Membership Plan configuration authority. This record does **not** invent additional Site Admin permissions.

**Staff:** cannot configure Membership Plans.

**Platform Admin:** platform-wide administration via the Platform Admin application (DR-019), not a substitute for Organization Admin as the normal configurator.

Historical “Facility Manager” / “Site Manager” remain **legacy terminology**, not RBAC roles.

### P1-004 — Membership Plan status

**Status: APPROVED**

Authoritative **Membership Plan** status vocabulary:

```text
DRAFT
ACTIVE
ARCHIVED
```

| Status | Meaning |
| --- | --- |
| **DRAFT** | The plan is being configured and is **not** available for new sale. |
| **ACTIVE** | The plan **is** available for new sale. |
| **ARCHIVED** | The plan is **no longer** available for new sale but is retained for historical/reference purposes. |

**These are Membership Plan statuses, not Membership statuses.**

Do **not** use as Membership Plan statuses: `FROZEN`, `CANCELLED`, `EXPIRED`, `PENDING_PAYMENT`. Those belong to the **Membership** lifecycle where applicable.

SQL default `ACTIVE` and Flutter `active`/`inactive` are **not** silently changed in this record. Reconcile them at the API/data **implementation** gate.

Glossary Submitted / Approved / Published remain an **approval workflow** that can sit on `DRAFT`; they are **not** additional persisted plan statuses.

### Membership lifecycle distinction

```text
Plan status ≠ Membership status
```

Documented **Membership** (instance) lifecycle concepts include:

```text
DRAFT
PENDING_PAYMENT
ACTIVE
FROZEN
CANCELLED
EXPIRED
```

Do not create or modify Membership lifecycle implementation here. Freeze / resume / cancel / expire remain Slice 1 **instance** operations.

### P1-005 — Versioning after sale

**Status: APPROVED**

Once a Membership Plan has been **sold**, its historical commercial terms must **not** be silently rewritten.

Future changes to commercial terms should use **revision/clone** semantics rather than mutating sold historical terms. Existing memberships keep the sold plan identity.

This is a product/architecture decision. **No** revision implementation, database model change, migration, or API is authorized by this record.

### P1-006 — Deactivation / archive behavior

**Status: APPROVED**

When a Membership Plan is no longer available for sale (`ARCHIVED`, or otherwise not `ACTIVE` for new sale):

- it **cannot** be used for **new** sales;
- existing memberships are **not** automatically terminated;
- existing memberships retain their **own** lifecycle state;
- archival/deactivation does **not** retroactively cancel or expire memberships.

Do not implement this behavior in this record.

### P1-007 — Payment relationship

**Status: APPROVED** (DR-019 / collection split)

API-05 owns membership lifecycle. API-08 owns facility payment/money movement. API-05 may reference payment/invoice state. Do not implement payment processing inside API-05. API-09 remains SaaS.

### P1-008 — Customer vs Participant

**Status: APPROVED** (DR-019)

Customer ≠ Participant. Family / guardian / minor: deferred.

### P1-009 — Membership list operation

**Status: APPROVED — FUTURE INVENTORY DECISION REQUIRED**

A Membership collection/list operation is approved as a **future API requirement**.

**Do not add it to the current 228 inventory.** API-05 remains exactly **12** numbered operations. Do **not** create `GET /api/v1/memberships` in this record. A future inventory/contract decision is still required before implementation.

### P1-010 — Concurrency and mutation safety

**Status: APPROVED** (API-00 / live API-04 pattern)

If-Match / `version_number`, idempotency on create and commercial/lifecycle POSTs, state-transition guards, audit in the same UoW.

### P1-011 — Permission seed

**Status: DEFERRED** to implementation pre-gate (exact codes). Role intent is P1-003. No Manager. Do not seed in this record.

### P1-012 — Customer foreign key

**Status: APPROVED AS IMPLEMENTATION PREREQUISITE**

API-04’s authoritative Customer identity (`customer.customer` / `record_id`) must be used for Membership implementation.

The membership ORM/customer relationship must be aligned to that model **before membership write implementation begins**.

No ORM, schema, or migration changes are authorized in this record.

---

# 8. Role / Authority Model

```text
Platform → Organization → Facility → Site

Platform Admin | Organization Admin | Site Admin | Staff
```

**No Manager role.**

| Actor | Membership instance (Slice 1) | Plan configuration (Slice 2 HTTP later) |
| --- | --- | --- |
| Platform Admin | Platform-wide per platform permissions | Platform-wide per platform permissions |
| Organization Admin | Org facilities | Configure and approve plans |
| Site Admin | Assigned site scope; not org-wide | Not automatic org-wide plan configuration |
| Staff | Operational (e.g. FR-MEM-001 create membership) | Cannot configure plans |

---

# 9. Customer / Participant Boundary

**APPROVED (DR-019):** Customer = commercial holder; Participant = service user; do not collapse. Family/guardian deferred.

---

# 10. Payment Boundary

```text
Facility commerce:  Customer → Facility     (membership + API-08)
Digitize SaaS:      Organization → Digitize/OreeOn   (API-09)
```

---

# 11. API Inventory Boundary

```text
228 numbered product APIs remain unchanged.
API-05 numbered operations remain exactly 12.
No new catalog IDs in this record.
Semantic operation_id remains the runtime identifier.
catalog_id (API-05-001 … API-05-012) remains metadata only.
```

Slice 2 plan HTTP and `memberships_list` are **out of inventory** until separate catalog decisions.

---

# 12. Data Model Dependencies

| Dependency | Notes | This task |
| --- | --- | --- |
| `membership.membership_plan` | Facility catalog; reconcile `plan_status` to DRAFT/ACTIVE/ARCHIVED at implementation | No change |
| `membership.membership_plan_rule` | No HTTP in 228 | No change |
| `membership.customer_membership` | Instance; `invoice_id` reference | No change |
| `customer.customer` | API-04 identity | Align FK at implementation (P1-012) |
| `customer.customers` | Legacy | Not authoritative for new writes |
| API-08 | Payments | Reference only |

---

# 13. Open Questions (non-blocking for this DR)

Still for **later** gates (not reopening accepted P0/P1):

- Slice 2: which plan HTTP operations, after an inventory RFC.
- P1-009: inventory add for list, when that RFC runs.
- Slice 1 implementation: pending vs pay-before-activate **detail** with API-08; If-Match TBD rows; P1-012 ORM work.
- P1-002 site-specific applicability if product later wants it.
- P1-011 exact permission codes.

---

# 14. Consequences / Follow-on Work

1. API-05 Slice 1 remains the existing **12** Membership operations.
2. Membership Plan HTTP APIs require a **future inventory decision**.
3. Plan status vocabulary is frozen as **DRAFT / ACTIVE / ARCHIVED**.
4. Membership lifecycle status remains **separate**.
5. Sold-plan commercial terms cannot be silently rewritten.
6. Archived plans cannot be newly sold.
7. Existing memberships are not automatically terminated by plan archival.
8. API-08 remains responsible for payments.
9. API-04 Customer identity must be reconciled before membership writes.
10. API-05 implementation has **not** started.

Flutter Membership Plan remains unavailable until Slice 2 + inventory approval.

---

# 15. Implementation Gate

```text
API-05 IMPLEMENTATION — NOT STARTED

API-05 CONTRACT — READY FOR CONTRACT FINALIZATION
```

**Do not start API-05 implementation** in this record. Next gate: **API-05 Contract Finalization** for Slice 1 (and inventory RFC only if listing or plan HTTP is in that contract).

---

# 16. Traceability

| Source | Use |
| --- | --- |
| API-05 Product Approval Gate | Explicit APPROVED records in §2a |
| Contract review / decision brief | Analysis; superseded as the approval authority |
| Registry / `operations.py` | 12 API-05 rows; 228 total |
| API-05 collection / FR-08 | Instance lifecycle |
| DR-019 | Roles, commerce, Customer ≠ Participant |
| PF-01 | Plan vs membership entities |
| API-04 gate | `customer.customer` |
| API-08 / API-09 | Payment vs SaaS |

---

# 17. Approval section

| Decision | Status | Product Approval Required |
| --- | --- | --- |
| P0-001 Option C + Slice 1/2; Option B rejected | **APPROVED** | Recorded |
| 228 inventory unchanged; no new catalog IDs | APPROVED (existing freeze) | No |
| Semantic `operation_id`; catalog_id metadata | APPROVED (existing freeze) | No |
| Hierarchy and four roles; no Manager | APPROVED (DR-019) | No |
| Customer ≠ Participant | APPROVED (DR-019) | No |
| API-09 SaaS vs API-08 facility payments | APPROVED (DR-019) | No |
| P1-001 Facility-owned plan | **APPROVED** | Recorded |
| P1-002 Site-specific plan applicability | DEFERRED | Only if later introduced |
| P1-003 OA / Site Admin / Staff plan authority | **APPROVED** | Recorded |
| P1-004 Plan status DRAFT / ACTIVE / ARCHIVED | **APPROVED** | Recorded |
| P1-005 No silent rewrite of sold terms | **APPROVED** | Recorded |
| P1-006 Archive ≠ terminate existing memberships | **APPROVED** | Recorded |
| P1-007 Payment boundary | APPROVED | No |
| P1-009 Membership list | **APPROVED — future inventory decision required** | Inventory RFC before implement |
| P1-010 Concurrency / audit | APPROVED (API-00) | No |
| P1-011 Exact permission codes | DEFERRED | Implementation pre-gate |
| P1-012 Customer FK | **APPROVED AS IMPLEMENTATION PREREQUISITE** | Engineering before writes |

### Decision matrix

| Decision | Current State | Direction | Status | Blocking this DR? | Next Action |
| --- | --- | --- | --- | --- | --- |
| P0 scope | 12 membership ops; plan HTTP unnumbered | Option C; Slice 1 = 12; Slice 2 later | **APPROVED** | No | Contract finalization |
| Plan HTTP inventory | Not in 228 | Separate catalog decision | **APPROVED** boundary | Slice 2 | Inventory RFC |
| Plan ownership | Glossary + SQL | Facility-owned; org parent | **APPROVED** | No | Implement later |
| Site applicability | No site column | Deferred | DEFERRED | No | Later product if needed |
| Site Admin authority | Role frozen | OA configures; SA not org-wide; Staff no plan config | **APPROVED** | No | No extra SA perms invented |
| Plan status | Glossary/SQL/Flutter conflict | DRAFT / ACTIVE / ARCHIVED | **APPROVED** | No | Reconcile SQL/Flutter at implementation |
| Membership status | FR-08 instance lifecycle | Separate enum | **APPROVED** | No | Slice 1 contract |
| Versioning | — | No silent rewrite; clone/revision later | **APPROVED** | No | No schema now |
| Archive | — | No new sales; keep existing memberships | **APPROVED** | No | No behavior now |
| Payment | DR-019 | API-08 money; API-05 refs | **APPROVED** | No | — |
| Membership list | Not in 12 | Future requirement; not in 228 | **APPROVED** | Inventory before HTTP | Do not create GET list now |
| Customer FK | Legacy ORM | API-04 `customer.customer` | **APPROVED AS IMPLEMENTATION PREREQUISITE** | Writes | Align at implementation |
| Participant | DR-019 | Customer ≠ Participant | **APPROVED** | No | — |

**Product approval:** Explicitly approved in the API-05 product decision gate.

---

```text
DR-020 STATUS: ACCEPTED

API-05 IMPLEMENTATION — NOT STARTED

API-05 CONTRACT — READY FOR CONTRACT FINALIZATION
```
