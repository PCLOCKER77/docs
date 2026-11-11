# API-05 Membership Plan — Product Decision Brief

**Status:** READY FOR PRODUCT APPROVAL  
**Date:** 16 September 2026  
**Type:** Documentation-only analysis  
**Does not:** implement API-05, change the 228 inventory, assign catalog IDs, or freeze product choices

Recommendations in this brief are **recommendations**. They are **not** frozen decisions until product/architecture records an explicit approval (DR-020 is **Proposed**, not Accepted).

**Inputs**

- Contract review: `docs/architecture/API-05_MEMBERSHIP_PLAN_CONTRACT_REVIEW.md` (BLOCKED)
- Access freeze: `docs/architecture/ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md` / DR-019
- Inventory: `docs/architecture/API_CONTRACT_REGISTRY.md`, `operations.py` API-05-001…012
- Collection: `docs/07_API_Collections/API-05_Membership_Management_Collection.md`
- FR-08, PF-01 §§9.4–9.5 / 9.18–9.19
- API-04 implementation gate; API-08 collection (payments)
- Physical model notes: `membership.membership_plan`, `customer_membership` (read-only in this task)

---

## 1. Executive summary

API-05 is blocked because **two different products** are using one collection name:

1. **Frozen numbered inventory:** 12 **customer Membership** lifecycle operations.
2. **Product/UI/glossary/SQL:** **Membership Plan** configuration (no numbered HTTP).

Those must stay **separate resources**. The open P0 is whether API-05 **means** (A) memberships only, (B) plans only, or (C) both as two resources.

**Recommendation (not frozen):** Approve **Option C as the intended API-05 collection** (plan catalog + membership instances, separate routes/permissions/lifecycles). Approve **Option A as the only first implementation slice** that does not change the 228. Plan HTTP remains **blocked until a separately approved inventory change**. Do **not** choose Option B.

P1 items below are analyzed with recommended options. Several P1s still **block contract approval** of a plan-inclusive API-05; they do **not** all block a membership-lifecycle-only slice.

---

## 2. Current API-05 state

| Layer | What exists | Status |
| --- | --- | --- |
| Official inventory (228) | API-05-001…012 on `/api/v1/memberships` | Frozen catalog metadata; **not implemented** |
| Semantic IDs | `memberships_create`, `memberships_activate`, … `memberships_history_list` | Derived; not reopened |
| Collection doc §8 | Also lists `/membership-plans` and rules | **Not numbered** |
| Registry Flutter note | `membership_plan` feature | Contradicts numbered paths |
| SQL | `membership_plan` + `customer_membership` | Tables exist; plan HTTP does not |
| Flutter | Plan list/create/update repository | Explicitly **unavailable** / not frozen |
| FR-08 | FR-MEM-001…012 membership **instances** | No FR-MEM for “create plan” |

No new catalog IDs are proposed in this brief.

---

## 3. Confirmed architecture constraints

These are **already frozen**. This brief does not reopen them.

| Constraint | Authority |
| --- | --- |
| Platform → Organization → Facility → Site | DR-004, DR-019 |
| Roles: Platform Admin, Organization Admin, Site Admin, Staff | DR-019 |
| No Manager role | DR-019 |
| Platform Admin: platform-wide via Platform Admin application | DR-019 |
| Customer ≠ Participant | DR-019 |
| SaaS: Organization → Digitize/OreeOn (API-09) | DR-019 |
| Facility commerce: Customer → Facility | DR-019 |
| Customer mobile: Phase 2 | DR-019 |
| Guardian/minor UX: deferred | DR-019 |
| Runtime identity: semantic `operation_id`; `catalog_id` is metadata | Operation-ID freeze |
| Inventory count 228 unless a **separate** inventory approval exists | Registry |
| API-00: envelopes, `DigitizeError`, audit in same UoW, no route HTTPException | Engineering standards |
| `customer.customer` is the API-04 identity | API-04 implementation gate |

---

## 4. P0 decision: API-05 scope

**ID:** P0-001  
**Question:** What does API-05 contain?

### Option A — Membership lifecycle only

API-05 remains the existing 12 operations. Plan configuration is elsewhere or deferred.

| Lens | Analysis |
| --- | --- |
| Product completeness | Staff can enroll against plans only if plans exist as **data** (seed/admin SQL) or another collection. Flutter plan admin stays mock/unavailable. |
| Catalog consistency | **Highest.** Matches 228 exactly. |
| API-04 | Create membership needs a live Customer. No change to API-04 inventory. |
| API-08 | Activation/payment still a P1; money stays API-08. |
| API-06 / API-07 | Attendance/scheduling consume **membership entitlement**, not plan CRUD. |
| Flutter | Membership-plan feature cannot go live. Operational enrollment UI is closer to UX-MEM lifecycle screens. |
| Inventory | **No change.** |
| Mix risk | Low if plans are not HTTP. Operational risk: selling without a governed plan catalog. |

### Option B — Membership Plan only

Redefine API-05 as plan configuration; move the 12 membership ops elsewhere.

| Lens | Analysis |
| --- | --- |
| Product completeness | Matches Flutter plan feature; **breaks** FR-08 and numbered inventory meaning. |
| Catalog consistency | **Lowest.** Would retcon API-05-001…012. Forbidden without inventory rewrite. |
| API-04 / 06 / 08 | Membership issuance has no home in 228. |
| Flutter | Plan feature unblocked **after new IDs**; membership purchase still missing. |
| Inventory | Requires moving 12 IDs and adding plan IDs — **not this task**. |
| Mix risk | Avoids mixing resources but **destroys** frozen catalog semantics. |

### Option C — Two-resource API-05

API-05 contains (1) plan configuration and (2) customer membership lifecycle as **separate** resources, routes, permissions, schemas, and lifecycles.

| Lens | Analysis |
| --- | --- |
| Product completeness | **Highest** vs glossary, collection §8, SQL, Flutter + FR-08. |
| Catalog consistency | **Incomplete today:** memberships numbered; plans not. C is a **target**, not a current inventory fact. |
| API-04 | Memberships reference Customer; plans do not create customers. |
| API-08 | Memberships reference payments; plans hold list price only. |
| API-06 / API-07 | Use membership (and later plan rules), not plan HTTP. |
| Flutter | Plan feature can map to plan resource **after** inventory approval; membership screens map to 001–012. |
| Inventory | Plan HTTP needs a **future approved** expansion. This brief does not add IDs. |
| Mix risk | **Acceptable only if** resources stay split. Dangerous if one DTO/lifecycle is used for both. |

### P0 recommendation (not frozen)

**Recommend Option C as the intended collection shape**, with **delivery sequencing:**

1. **Slice 1 (no inventory change):** Option A — implement or contract-freeze the **existing 12** only, with plans as **read-only dependency** (must exist in DB).
2. **Slice 2 (requires inventory approval):** add Membership Plan HTTP as a **second resource inside API-05**, not a Manager role, not API-09, not mixed URLs.

**Recommend rejecting Option B.**

**Blocks contract approval:** Yes. Until product picks A, B, or C (and if C, whether Slice 2 is in the same approval), API-05 cannot be marked implementation-ready as “Membership Plan.”

---

## 5. P1 decision analyses

Legend: **Blocks plan-inclusive contract?** vs **Blocks membership-slice contract?**

### P1-001 — Plan ownership

**Evidence:** Glossary §9.4 / §9.18: owned by Facility, configured by Organization Admin. SQL: `organization_id` + `facility_id` NOT NULL, unique `(facility_id, plan_code)`. Collection §12: plan belongs to Facility. Tests: facility-owned offering, not SaaS.

| Option | Comment |
| --- | --- |
| Organization-owned | Contradicts SQL uniqueness and glossary |
| Facility-owned | Matches schema and PF-01 |
| Site-owned | No `site_id` on plan; would be a new hierarchy of ownership |
| Facility-owned + optional Site applicability | Matches glossary “available across selected Sites” without Site owning the product |

**Recommendation (not frozen):** Facility-owned with optional Site applicability (see P1-002). Organization is parent tenant, not plan owner. Site is not the owner.

**Consequences:** All plan HTTP (if approved) is facility-scoped; Platform Admin may still administer across facilities.

**Blocks approval:** Ownership itself is **strongly evidenced**; treating it as still-open is unnecessary for a membership-only slice. For plan HTTP, product should **confirm** this recommendation. **Does not block** Slice 1 if plans are seeded per facility.

### P1-002 — Site applicability

**Evidence:** Glossary: plans available at one or more Sites. SQL: no site column on `membership_plan`. Site Admin must not get org-wide authority (DR-019).

| Option | Comment |
| --- | --- |
| Entire Facility | Simplest; Site Admin of any site of that facility might see all facility plans |
| One Site | Implies ownership or 1:1 site; not in schema |
| Multiple selected Sites | Needs junction/rules table; `membership_plan_rule` could hold site lists in JSON (**weak** unless specified) |

**Recommendation (not frozen):** **v1 assumption:** plan applies to the **entire Facility**. **Future-ready:** selected Sites via an explicit applicability list (not JSON-in-metadata as the long-term model).

**Consequences:** Site Admin permissions for **view** can be “plans of the facility that contains the assigned site.” Configuration remains OA-led (P1-003).

**Blocks approval:** **P1 for plan HTTP and Site Admin matrix.** Membership create already has conditional `site_id` in FR-MEM-001 (operational context), which is **not** the same as plan ownership.

### P1-003 — Plan configuration authority

**Evidence:** Glossary: configured by OA; approval required, approver OA; Site Admin “Operated By” for Membership Plan; Site Admin raises approval requests. Flutter: `membership.plan.create/update`. FR-08: Reception creates **memberships**, not plans. DR-019: Platform Admin platform-wide; Site Admin not org-wide; Staff operational; no Manager.

| Option | Comment |
| --- | --- |
| OA only | Strongest match to “configured by OA” + approval matrix |
| OA + Site Admin (direct edit) | Faster ops; weakens approval matrix |
| Site Admin drafts + OA approval | Matches glossary Draft/Submitted/Approved **if** that lifecycle is chosen (P1-004) |
| Platform Admin override | Required by DR-019; not a replacement for OA |

**Recommendation (not frozen):**

- **Create/edit/price/activate/archive plan:** Organization Admin (normal). Site Admin **may draft or request** if approval workflow is in scope; **must not** publish org-wide or other facilities.
- **Platform Admin:** can administer plans across organizations per platform permissions.
- **Staff:** no plan configuration.

**Blocks approval:** **Yes for plan HTTP.** Membership lifecycle Staff permissions are a separate matrix (P1-011).

### P1-004 — Plan lifecycle / status

**Evidence (conflict):**

| Source | Vocabulary |
| --- | --- |
| Glossary §9.4 | Draft → Submitted → Approved → Published → Active → Expired → Archived |
| SQL | `plan_status` VARCHAR default **`ACTIVE`**, no check constraint |
| Flutter | **`active` / `inactive`** (lowercase); create persists inactive so not live |
| FR-08 | Plan must be **Active** to sell (precondition) |

Proposed product set in the prompt (Draft, Pending Approval, Active, Suspended, Archived) is **another** vocabulary.

**Recommendation (not frozen):** Do **not** finalize a single enum in this brief. For **Slice 1 memberships**, treat “purchasable” as plan_status meaning **Active** (SQL) regardless of Flutter casing. For **plan HTTP**, product must pick one canonical set and a mapping table. Prefer **not** using Suspended (Flutter comment: Suspended is facility/staff, not plan).

**Blocks approval:** **Yes for plan HTTP / Flutter plan admin.** **No** for membership-only if “must be Active to enroll” is accepted.

### P1-005 — Versioning after sales

**Evidence:** Glossary: historical plans cannot be modified after customer purchases; new revisions instead. SQL/Flutter: in-place `version_number` + PATCH. No revision table.

| Option | Comment |
| --- | --- |
| In-place editing | Matches Flutter; violates glossary after sales |
| Immutable revisions | Matches glossary; needs schema/API later |
| Effective-dated revisions | Strongest commercially; not in DB |
| New plan after sales | Operational workaround (clone + new code) |

**Recommendation (not frozen):** **Sold commercial terms** (price, duration, included services) must **not** rewrite history on existing memberships. **Until a revision table exists:** allow in-place edits only while plan has **zero sold memberships**; after first sale, require a **new plan_code** (clone) for material changes. Memberships keep `membership_plan_id` of the sold plan.

**Blocks approval:** **Yes** before plan PATCH goes live. Membership-only slice can freeze plan rows as read-only.

### P1-006 — Deactivation impact

**Evidence:** None stating that deactivation terminates memberships. Glossary separates plan vs membership lifecycles. FR freeze/cancel are **membership** actions.

| Option | Recommendation flag |
| --- | --- |
| Existing memberships continue | **Recommended default** |
| New enrollments blocked | **Recommended** when plan not Active |
| Renewals blocked | **Recommended** unless product wants grandfathering |
| Active memberships terminated | **Not recommended** as automatic |
| Forced migration | **P3 / exception process** |

**Recommendation (not frozen):** Deactivate/archive ⇒ **no new enrollments** (and **no renew onto that plan**). Existing memberships **continue until** their own expire/cancel/freeze rules. Do not auto-terminate.

**Blocks approval:** Should be confirmed before plan status mutations. Membership cancel/expire remain explicit API-05 membership ops.

### P1-007 — Activation and payment

**Evidence:** Collection §4 payment-before-activation; FR-MEM-001 charge calculation + billing references; out of scope refunds; API-08 owns invoices/payments; membership has optional `invoice_id`; SaaS is API-09; BR-SUB-006 is **SaaS**, not facility membership.

| Option | Comment |
| --- | --- |
| Activation requires successful payment | Matches collection narrative |
| API-08 owns payment status | Matches freeze |
| API-05 stores references/snapshots only | Matches `invoice_id` |
| Unpaid can remain pending | FR initial status: Draft, Pending Payment, Active |
| Staff create pending before payment | Reception flow in FR-MEM-001 |

**Recommendation (not frozen):**

- Money movement = **API-08** (facility commerce, not SaaS, not IAP).
- API-05 stores **references** (`invoice_id` and/or payment ids), not PSP payloads.
- **Allow** `memberships_create` to yield **Pending Payment**; `memberships_activate` requires API-08 success **or** an approved offline-recorded payment.
- Do not call API-09 from membership activate.

**Blocks approval:** **Yes** for activate/create contract. Does not require API-08 to be implemented in the same sprint if activate can 409 `MEMBERSHIP_PAYMENT_001` when unpaid.

### P1-008 — Customer and Participant

**Evidence:** DR-019 Customer ≠ Participant. Membership glossary: belongs to Customer. SQL: `customer_id` only. API-04: no guardian graph; family membership ≠ customer family. Flutter `family` plan type. Attendance (API-06) is where participation is recorded.

| Option | Comment |
| --- | --- |
| Customer = holder | **Confirmed direction** |
| Participant = service user | Frozen conceptually; not on membership row |
| Purchase for another participant | Future; needs holder + beneficiary |
| Family now | Type exists; graph does not |
| Guardian deferred | Frozen |

**Recommendation (not frozen):** v1 membership **holder = Customer**. Do not add participant/guardian columns in this gate. Family type may exist on **plan** as a label only. Attendance may later attach participants without equating Customer.

**Blocks approval:** **No** for Slice 1 if product accepts holder-only. **Yes** if family/guardian must work in first membership release.

### P1-009 — Membership list operation

**Evidence:** Inventory has GET-by-id and history, **not** GET `/api/v1/memberships`. API-04 has `customers_list`. Collection §17 mentions offset pagination for membership **lists**. Reception/OA/Site Admin need search in FR/UX.

| Option | Comment |
| --- | --- |
| Required in API-05 | Product-complete; **not in 228** |
| Not required | Get-by-id + customer-nested later |
| Another collection | No natural home; worse |

**Recommendation (not frozen):** A list/search operation is **operationally required** for staff UX. It is **not** in the 228. **Do not add it in this brief.** Product must either (1) accept no list in v1, (2) approve an inventory addition, or (3) expose memberships only via a **future** customer-nested read **without** pretending it is API-05-001–012.

**Blocks approval:** **Yes** for a complete staff membership UI. **No** if Slice 1 is strictly the 12 ops (get-by-id after create).

### P1-010 — Concurrency and mutation safety

**Evidence:** Collection: Idempotency-Key on create/lifecycle; If-Match on lifecycle; audit + history same transaction. Registry: idempotency REQUIRED on 001/003, TBD on others; concurrency column NOT_APPLICABLE (contradicts collection). Tables have `version_number`. API-04 PATCH uses If-Match. Standards: audit in same UoW.

**Recommendation (not frozen):** Follow **API-00 / live API-04 pattern**, not the incomplete registry column:

- Mutations: optimistic concurrency (`version_number` + If-Match)
- Create and commercial/lifecycle POSTs: Idempotency-Key
- State-transition guards (e.g. cannot freeze cancelled)
- Audit event in the same commit as the membership/plan write

**Blocks approval:** **Should be confirmed** as the API-05 quality bar; it is **not** a new architecture. Registry TBD rows should be filled at implementation pre-gate, not by inventing IDs.

### P1-011 — Permission seed

**Evidence:** Flutter plan: `membership.plan.{list,view,create,update}`. API-03 seeds roles/permissions for other verticals; membership pack not frozen. FR-MEM: Reception creates membership. DR-019 roles only.

**Proposed families (not seeded in this task):**

| Family | PA | OA | Site Admin | Staff |
| --- | --- | --- | --- | --- |
| `membership.plan.view` / `list` | platform perms | org facilities | assigned facility via site | active plans if enrollment duty |
| `membership.plan.create` / `update` / pricing | platform perms | **yes** | draft/request only (if P1-003 approved) | no |
| `membership.plan.activate` / `suspend` / `archive` | platform perms | **yes** | no org-wide publish | no |
| `membership.create` / `activate` / `renew` | platform perms | yes | assigned site/facility | Reception-style yes |
| `membership.transfer` / `cancel` | platform perms | yes | site scope | limited / P2 |
| `membership.history.view` | platform perms | yes | site scope | yes if they can view membership |

**Recommendation (not frozen):** Seed **no Manager**. Bind defaults like other verticals: Platform Admin all; OA org; Site Admin scoped; Staff operational subset. Exact codes at implementation pre-gate.

**Blocks approval:** Permission **names** can wait for pre-gate. **Role intent** for plan config (P1-003) blocks plan HTTP.

### P1-012 — Customer foreign-key model

**Evidence:** API-04 gate: authoritative `customer.customer.record_id`. Quarantined `customer.customers` / `customer_id` **not** used by Customer service. Membership ORM `CustomerMembership.customer_id` FK **`customer.customers.customer_id`**. Gate text: SQL already FKs `customer.customer.record_id`; **align ORM at API-05**.

**Recommendation (not frozen):** Legacy plural table is **not** authoritative. Before membership writes go live, membership ORM/SQL must target **`customer.customer.record_id`**. Compatibility layer should be **temporary at most**, not a dual-write product.

**Blocks approval:** **Yes before membership create implementation.** Does not require inventory change. Schema/migration change is an **implementation dependency**, not this documentation gate.

---

## 6. Cross-API impact analysis

| API | If Option A (slice 1) | If Option C slice 2 (plans) |
| --- | --- | --- |
| API-04 | Memberships reference Customer; no new customer fields required for holder-only | Unchanged; still no family graph |
| API-08 | Activate/create depend on payment **references**; do not implement PSP in API-05 | Plan price is list price only |
| API-06 | Check-in uses active membership entitlement | Plan rules may later constrain eligibility |
| API-07 | PT/class not in API-05 | Plan type `personal_training` is a **label** until API-07 |
| API-09 | No coupling | No coupling |
| API-03 | Need membership permission seed at implement | Plus `membership.plan.*` |
| Flutter | Plan feature stays unavailable; membership screens later | Plan feature can call plan routes **after IDs exist** |
| Inventory | Unchanged 228 | **Requires later approval** to add plan ops |

---

## 7. Recommended target model

**Not frozen.** Proposed picture for product to accept or reject:

```text
Facility-owned Membership Plan  (catalog product)
        │
        │  sold as
        ▼
Customer Membership             (instance / entitlement)
        │
        ├── invoice/payment refs → API-08 (Customer → Facility)
        └── attendance → API-06 (Participant may differ from Customer)

Digitize SaaS remains API-09 (Organization → Digitize/OreeOn).
```

- API-05 **collection intent:** two resources (Option C).
- API-05 **first build:** 12 numbered membership ops (Option A).
- Plan HTTP: second slice, **new IDs only after inventory approval**.
- Site Admin: operational on instances; plan **publish** stays OA unless product overrides P1-003.
- No Manager. No Customer = Participant. No SaaS checkout on staff mobile.

---

## 8. Decisions requiring product approval

These must be explicit (accept / reject / amend recommendations):

| ID | Decision | Blocks |
| --- | --- | --- |
| P0-001 | A vs B vs C, and slice sequencing | Contract “Membership Plan” naming and implementation start |
| P1-003 | Who configures/publishes plans | Plan HTTP |
| P1-004 | Canonical plan status vocabulary | Plan HTTP / Flutter alignment |
| P1-005 | Edit-after-sale / revision rule | Plan PATCH |
| P1-006 | Deactivate vs existing memberships | Plan status mutations |
| P1-007 | Pending vs pay-before-activate | `memberships_create` / `activate` |
| P1-009 | Whether list is in v1 (inventory or not) | Staff membership UX completeness |
| P1-012 | Confirm ORM/SQL alignment to `customer.customer` before write APIs | Membership create implementation |

P1-001 confirmation of Facility ownership is recommended as a **rubber-stamp** of existing evidence.

---

## 9. Decisions safe to defer

| Topic | Assumption until later |
| --- | --- |
| Guardian/minor UX | Future-ready only |
| Family beneficiary graph | Plan type label only |
| Selected-site applicability table | Entire facility (P1-002 v1 assumption) |
| Display order, T&Cs, capacity, tax on plan | API-08 / later fields |
| Auto-renew billing | Later + API-08 |
| Customer mobile purchase | Phase 2 |
| Option B | Reject; do not design |
| Plan HTTP catalog IDs | No IDs until inventory process |
| Exact permission code strings | Implementation pre-gate |
| Filling every registry TBD cell | Pre-gate, not new architecture |

---

## 10. Risks and dependencies

| Risk | Mitigation |
| --- | --- |
| Implementing Flutter plan CRUD against empty inventory | Keep unavailable repository until Slice 2 approval |
| Renaming API-05-001 to mean “create plan” | Reject Option B |
| Mixing plan DTO with membership DTO | Separate routes/schemas |
| SaaS vs gym membership billing | API-09 vs API-08; no IAP |
| Dual customer tables | Align FK before writes (P1-012) |
| Site Admin org-wide plans | P1-003 |
| Assuming deactivation cancels members | P1-006 |

**Dependencies:** API-04 Customer live; API-02 facility/site; API-03 permission machinery; API-08 for paid activation (or 409 pending); API-06 later for check-in.

---

## 11. Proposed decision-record entries

Suggested **DR-020** (not created as accepted in this task) outline:

```text
DR-020 API-05 Membership vs Membership Plan scope
Status: Proposed — awaiting product approval

P0: Option C intended; Slice 1 = existing 12 membership operations;
    plan HTTP requires later inventory approval. Option B rejected.

P1-001: Facility-owned plans.
P1-002: v1 entire facility; selected sites deferred.
P1-003: OA publishes; Site Admin not org-wide; PA platform-wide; Staff no plan config.
P1-004: Status vocabulary TBD in DR-020 body after product pick.
P1-005: No silent rewrite of sold terms; clone plan after first sale until revision model.
P1-006: Deactivate blocks new sales/renewals; does not auto-terminate.
P1-007: API-08 owns payment; API-05 references; pending membership allowed.
P1-008: Holder = Customer; Participant separate; family/guardian deferred.
P1-009: List not in 228; product must approve inventory or accept omit.
P1-010: If-Match + idempotency + same-UoW audit (API-00).
P1-011: Role matrix as brief; codes at implement.
P1-012: customer.customer.record_id is the membership FK target.
```

Do not treat this subsection as an accepted DR.

---

## 12. Recommended next gate

1. Product/architecture **approves or amends** P0-001 and the P1 list in §8.  
2. Record the result as DR-020 (or equivalent).  
3. **API-05 implementation pre-gate** for **Slice 1 only** (12 membership ops), including P1-007, P1-010, P1-012.  
4. Separate **inventory change request** if/when Membership Plan HTTP is approved (Slice 2).

Do **not** implement API-05 until §8 is explicitly approved.

```text
API-05 PRODUCT DECISION BRIEF

Status: READY FOR PRODUCT APPROVAL

Recommendations are not frozen.

Official inventory: 228 — unchanged.
No catalog IDs added.
No API-05 implementation.
```
