# DR-023 Hierarchy Migration Plan (Proposed)

> **Status:** Accepted with DR-023 for **development** work.  
> Additive schema may be applied to confirmed local development databases only.  
> Do not auto-map `digitize_test`, QA, or production. Do not deploy or merge to `main`.

| Field | Value |
|---|---|
| Document | DR-023 Hierarchy Migration Plan |
| Related decision | [DR-023](../99_Decision_Records/DR-023_Company_Branch_Site_Facility_Hierarchy.md) — **Accepted (development)** |
| Live hierarchy (authoritative today) | [DR-004](../99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md), DEC-003 for QA/production until cutover |
| Last updated | 2026-10-16 |
| Execution state | Development implementation in progress; local `digitize` still at Alembic 027 until 028 phone uniqueness is resolved |

---

## 1. Purpose, scope, status, and dependencies

### Purpose

Describe how Digitize would invert tenant parentage from **Organization → Facility → Site** to **Company/Organization → Site/Branch → Facility → Staff**, without losing identifiers, subscriptions, or least-privilege access.

### Scope

In scope (development):

- Cardinality inversion (`tenant.site.facility_id` required today → `tenant.facility.site_id` required in the target).
- Company Admin managing Sites and Facilities; **no** Site Admin / Branch Admin in the target role model.
- Facility-scoped SaaS billing remaining the commercial unit.
- Staged API and Flutter compatibility.
- Preflight, reconciliation, rollback, and release gates.

Out of scope:

- QA/production database changes, deploy, merge to `main`, or commit/push.
- Auto-mapping `digitize_test` fixture Facilities/Sites/Site Admins.
- Renumbering APIs.
- Inventing prices, refunds, or Site Admin → Company Admin mappings.
- Implementing DR-022 (Customer Data Protection + Customer Module).

### Status

**Accepted for development.** QA/production remain on DR-004 until a separate cutover:

1. Formal **Accept** of DR-023 for development is recorded (2026-10-16).
2. Q1/Q2 remain blocking for any environment that still has Facilities, Sites, or Site Admins.
3. Local `digitize` had 0 Sites / 0 Facilities / 0 Site Admins / 0 subscriptions, so no per-record mapping is required there.
4. Alembic 029 is additive and must not be applied until 028 (unique identifiers) can apply or a separately approved local path exists. Do not silently delete duplicate phones.

### Dependencies and boundaries

| Artifact | Boundary |
|---|---|
| DR-004 / DEC-003 | Live hierarchy: Platform → Organization → Facility → Site. Remains authoritative. |
| DR-019 / access freeze | Live roles include Site Admin. Target of DR-023 removes that role; freeze stays in force until DR-023 is Accepted **and** identity mapping is approved. |
| DR-021 | Onboarding/PA boundary and “hierarchy unchanged” clause. Only the hierarchy clause is intended for later supersession. Terms ≠ SaaS activation stays. |
| DR-022 | Reserved for Customer Data Protection + Customer Module. Do not reuse this ID. Customer/membership operational data must still be **inventoried** during preflight because they hang off Facility/Site. |
| API-02 registry | Frozen numbers and live parentage. Compatibility changes require a later contract amendment, not this plan. |
| API-09 | Facility-scoped subscription/license. Commercial unit does not move to Site. |
| AUTH freeze / tenant isolation | Must not weaken. |

---

## 2. Current versus target model

### 2.1 Current (live — source-confirmed)

Confirmed in `digitize-services` models (`app/modules/facility/models/facilities.py`, `sites.py`):

```text
Platform → Organization → Facility → Site
```

| Entity | Owner-facing name | Table | Parent today |
|---|---|---|---|
| Organization | Company | `tenant.organization` | Platform |
| Facility | Facility | `tenant.facility` | `organization_id` NOT NULL; **no** `site_id` |
| Site | Branch (UI label in some Flutter code) | `tenant.site` | `organization_id` NOT NULL **and** `facility_id` NOT NULL |

Cardinality today:

- One Organization → many Facilities.
- One Facility → many Sites (`tenant.site.facility_id`).
- Site code uniqueness: `uq_site_code_facility` on `(facility_id, site_code)`.
- Facility code uniqueness: `uq_facility_code_org` on `(organization_id, facility_code)`.
- Site create/list APIs are **facility-scoped** (API-02-011, API-02-019). Facility create has **no parent site** (API-02-007).

Flutter contradiction (do not treat names as the data model):

- `lib/features/branch` maps a “Branch” from **Site JSON including required `facility_id`** (`branch_mapper.dart`).
- `RemoteSiteRepository` sends `facility_id` on create/list.
- `CurrentSiteContext` is Site Admin / Staff **session context**, not a Company → Site tree.

### 2.2 Target (proposed — not live)

```text
Platform → Company/Organization → Site/Branch → Facility → Staff
```

| Rule | Target |
|---|---|
| Company | Still `tenant.organization` |
| Site/Branch | `tenant.site`; no separate Branch table unless a later decision |
| Company : Site | One to many |
| Site : Facility | One to many; mixed facility types allowed on one Site |
| Facility : Site | Each Facility belongs to **exactly one** Site (`tenant.facility.site_id`) |
| Staff | Company-associated; explicit scopes only |
| Roles | Company Admin manages Sites/Facilities/staff/subscriptions (permissions + eligibility). **No Site Admin. No Branch Admin.** |
| Billing | Facility remains the independent billable unit |

### 2.3 Cardinality inversion

This is **not** renaming `site.facility_id` to `facility.site_id`.

Today a Facility can have 0 (if no sites exist), 1, or N Sites. The target requires every Facility to have exactly one parent Site. N→1 cannot be auto-resolved. 0→1 cannot be fabricated.

---

## 3. Schema migration strategy (proposed, not written)

No migration file is created or executed by this plan.

### 3.1 Additive `tenant.facility.site_id`

Suggested sequence after authorization:

1. Add **nullable** `tenant.facility.site_id` FK → `tenant.site.record_id` (`ON DELETE RESTRICT`), plus index.
2. Keep existing `tenant.site.facility_id` NOT NULL during compatibility.
3. Backfill **only** Facilities that pass preflight (exactly one Site **and** operational-data validation).
4. Stop backfill and fail the environment if any unresolved 0-Site or N-Site Facilities remain.
5. After API consumers write the new parent, application validation requires `site_id` on create/update.
6. Eventual `NOT NULL` on `facility.site_id` only when every row is populated and reconciled.
7. Eventual drop of `tenant.site.facility_id` only after a **separate** removal approval (see §3.5).

### 3.2 Uniqueness and indexes

- **Keep** `uq_facility_code_org`.
- **Site code:** today unique per Facility. Target is organization-scoped uniqueness (`(organization_id, site_code)`), **after** collision inventory.
  - If two Sites in the same Organization share `site_code` under different Facilities, treat as a reconciliation exception. Do not silently rename.
- New index on `facility.site_id`.
- Check org isolation: a Facility’s `site_id` must reference a Site with the same `organization_id`.

### 3.3 Dual-write / compatibility

If dual-write is required:

- Nominate **one** authoritative representation (recommended after cutover: `facility.site_id`).
- Same Unit of Work / transaction (or equivalent) must update both sides while both exist.
- Reconciliation job: every Site.facility_id ↔ Facility.site_id pair must match; mismatches fail the gate.
- Do not maintain two independent sources of truth.

If dual-write is **not** required, prefer expand (nullable column) → backfill → read new → write new → constrain → retire old.

### 3.4 Conditions to remove `tenant.site.facility_id`

All of the following, separately approved:

- Every live Facility has `site_id` NOT NULL to a valid same-org Site.
- No API, report, Flutter, identity scope, or batch job still requires `site.facility_id` as the parent.
- Compatibility period closed; dual-write (if any) retired.
- Rollback window for the drop is understood (column drop is not trivially reversible without backup).

### 3.5 Identifiers and subscriptions

- Preserve `tenant.facility.record_id` and `tenant.site.record_id`.
- `commercial.subscription.facility_id` and licenses stay on the **same** Facility IDs.
- Do not re-key billing to Site or Company.

---

## 4. Preflight inventory and reconciliation

Run **read-only** against a confirmed environment. Do not mutate QA/production during preflight. Generate a reconciliation report **before** any backfill.

### 4.1 Cardinality counts

For each Organization, count Facilities with:

- **0 Sites**
- **exactly 1 Site**
- **2+ Sites**

Also detect:

- Sites whose `facility_id` points at a missing/deleted Facility.
- Facilities whose `organization_id` disagrees with the Site’s `organization_id`.
- Soft-deleted vs active mismatches.

**Gate:** unresolved 0-Site or N-Site Facilities → **preflight fail**. No auto-pick. No synthetic Site.

### 4.2 Deterministic 1:1 candidates

Eligible for mapping **only if** operational checks also pass:

- Customers / customer-facility links
- Memberships and attendance (when those modules exist in the environment)
- Trainers / staff profiles (`staff_profile.facility_id` / `site_id`)
- Identity role assignments and `IdentityAccessScope` (org/facility/site)
- Subscriptions and licenses for that Facility ID
- Reports or aggregates keyed by facility or site

A one-to-one **count** is not sufficient.

### 4.3 Constraint collisions

- Duplicate `(organization_id, site_code)` across Facilities.
- Existing unique/check constraints that assume Facility-owned Sites.

### 4.4 Exception handling

Each exception row: Facility ID, Organization ID, Site IDs, evidence, proposed human mapping, approver, date.

Ambiguous rows stay unresolved and **block cutover** for that tenant (or globally, if the release is all-or-nothing — that release shape is a human decision; see §11).

No destructive or automatic resolution.

---

## 5. Site Admin transition

Live identity still seeds `SITE_ADMINISTRATOR` (`app/modules/identity/constants.py`). DR-019 still requires Site Admin. Target DR-023 removes it.

### 5.1 Inventory (required before any mapping policy)

For each assignment:

- User account ID, login identifier (not passwords)
- Organization ID
- Role code / staff type
- Permission set
- Access scopes (`organization_id`, `facility_id`, `site_id`)
- Last activity (if available)
- Whether the user also holds Organization Admin or Staff roles

### 5.2 Audit record per assignment

Required outcome fields:

- `keep_as_staff_with_scopes` | `retire` | `map_to_named_role` | `unresolved`
- Replacement role code (if any)
- Replacement scopes (must not be broader than justified)
- Approver and timestamp
- Evidence link to inventory row

**Prohibited:** automatically promoting all Site Admins to Company/Organization Admin; silently adding permissions.

### 5.3 Cutover block

Any `unresolved` assignment blocks Site Admin retirement and the affected tenant/cutover.

**Q2 mapping policy is not decided in this plan.** Exact replacements wait for inventory.

---

## 6. API and Flutter transition

### 6.1 Affected API-02 operations (registry + code)

Keep IDs stable. Live parentage until a **later** contract amendment:

| ID | Path | Live parentage | Target impact (future) |
|---|---|---|---|
| API-02-007 | `POST /api/v1/facilities` | Organization only | Require `site_id` |
| API-02-008 / 018 | Facility patch/get | No parent site | Return/accept `site_id` |
| API-02-010 | Activate facility | Organization | Unchanged commercial/activation rules except parent context |
| API-02-011 | `POST /api/v1/sites` | **Facility-scoped** | Organization-scoped Site create |
| API-02-012 / 014 / 020 | Site patch / activate / get | Site; create required facility | Parent no longer Facility |
| API-02-017 | `GET /api/v1/facilities` | Organization list | Optional filter by `site_id` |
| API-02-019 | `GET /api/v1/sites` | **Requires facility context** | List by organization (and not require facility) |

Other APIs to inventory from source before implementation (do not assume names):

- API-03 staff/roles/scopes (`facility_id` / `site_id` on profiles and `IdentityAccessScope`)
- API-09 subscription/license (`facility_id` stays)
- Headers `x-facility-id` / `x-site-id` in `app/api/deps.py`
- Staff create gated on org ACTIVE + facility subscription eligibility (keep)

Compatibility: additive response fields first; old query params (`facility_id` on site list) retained until clients migrate; then a dated removal gate.

### 6.2 Flutter (source-confirmed)

| Area | Live coupling | Future work (unauthorized) |
|---|---|---|
| `lib/features/branch` | Branch = Site **under Facility** | Branch/Site under Company; Facility picker is child of Site |
| `remote_site_repository.dart` | Query/body `facility_id` | Organization-scoped list/create |
| Facility forms/list | Org-scoped, no parent site | Required Site on create |
| `current_site_context.dart` | Site Admin/Staff assigned sites | Revisit once Site Admin is gone; Company Admin may still select a working Site without a Site Admin role |
| Company Admin dashboard / staff | Facility subscription gate | Keep facility billing gate |
| Routes | Organization / facility / branch feature modules | Do not invent Site Admin screens |

Do not treat “Branch” in the UI as the target parent until the API parentage actually inverts.

---

## 7. Subscription and billing invariants

Confirmed: `commercial.subscription.facility_id` and facility `subscription_scope_status`.

Must remain true after any future migration:

- Billable unit = **Facility**, not Site or Company.
- Each Facility has an independent subscription lifecycle.
- Pricing from facility type + approved backend commercial configuration (no new prices here).
- Adding a Facility adds another billable unit under existing commercial rules.
- Cancelling one Facility subscription does not auto-cancel others.
- Approved proration, payment, grace, cheque-bounce, suspension, and reactivation stay at subscription/facility scope.
- Suspended subscription: preserve approved limited Company Admin access for billing, payment, support, recovery.
- Backend remains authoritative for price, invoice, eligibility, and payment confirmation.

---

## 8. Staged implementation sequence

None of these stages are in progress.

1. **Decision acceptance** of DR-023 after Q2 (and any §11) closure — or a superseding record.
2. **Plan review and implementation authorization** (this document, updated with inventory facts).
3. **Baseline backup** of the target environment (disposable local first).
4. **Read-only preflight** and reconciliation report; exception approvals.
5. **Additive schema** (`facility.site_id` nullable) on disposable DB only.
6. **Controlled backfill** of 1:1 validated Facilities only.
7. **API compatibility** (additive fields, dual-read, then dual-write if required) without renumbering.
8. **Authorization/identity** changes only after Site Admin dispositions are signed.
9. **Flutter** client changes against compatible APIs.
10. **Local disposable-database tests** (cardinality, isolation, billing, RBAC).
11. **QA** only after explicit authorization (never as the first write of backfill).
12. **Post-migration reconciliation** vs preflight report.
13. **Rollback drill** on disposable environment.
14. **Main-branch merge** only after approved QA gates.
15. **Separate approval** to drop `site.facility_id`.

---

## 9. Rollback strategy

### Prerequisites

- Snapshot/backup taken immediately before backfill and before NOT NULL / column drop.
- Restore procedure tested on a disposable copy.

### Limits

- After new Facilities are created **only** with `site_id` and clients no longer send `facility_id` on Site create, rollback to old writes requires a dual-write window or a restore.
- Dropping `site.facility_id` is high-risk; restore from backup is the honest rollback.

### Consistency checks

- Every backfilled `facility.site_id` points at a Site that currently has `facility_id` equal to that Facility (during compatibility).
- Subscription `facility_id` set is unchanged vs preflight.
- No new Organization Admin grants that were not in the signed Site Admin disposition file.

### Stop vs unsafe rollback

Stop cutover (leave compatibility dual-read, do not drop columns) when:

- Any cardinality exception appears after backfill.
- Reconciliation mismatches exceed the approved threshold (recommended: **zero**).
- Privilege widening is detected.

Do not “fix forward” by auto-assigning Sites or promoting roles.

---

## 10. Acceptance criteria and release gates

All must be true before calling a future cutover complete:

1. Every in-scope Facility has exactly one valid same-organization parent Site.
2. No unresolved cardinality exceptions.
3. No unresolved Site Admin assignment dispositions.
4. No orphaned subscriptions, licenses, or staff/scope rows relative to preflight.
5. Site-code uniqueness matches the approved organization-scoped policy (collisions resolved by signed mapping, not silent rename).
6. Tenant isolation and RBAC regression tests pass; no unauthorized cross-tenant parentage.
7. Frozen API numbers unchanged; any contract delta is a separately approved amendment.
8. Flutter Company → Site → Facility workflows pass against the authorized API.
9. Facility billing, independent cancellation, eligibility, suspension, limited CA billing access, and reactivation remain correct.
10. Rollback/recovery has been tested on a disposable environment.
11. `tenant.site.facility_id` still present until a separate removal gate passes.

---

## 11. Open questions (human approval)

**Unresolved policy (blocks Accept / cutover):**

1. **Q2 mapping:** After inventory, what is the approved replacement for each class of `SITE_ADMINISTRATOR` assignment? (Not auto Company Admin.)
2. **Release shape:** Fail an entire environment cutover when one tenant has exceptions, or isolate that tenant?
3. **Site-code collisions:** Rename policy, merge policy, or leave blocked until operators choose?
4. **Facilities with zero Sites:** Approved operator action is mapping to an existing Site vs creating a Site — **creation is not allowed without explicit per-row approval** (no synthesized defaults in code).
5. **Dual-write necessity:** Can Flutter and API consumers migrate in one compatibility release, or is a dual-write window mandatory?

**Implementation details (not policy, still not to invent at runtime):**

- Exact Alembic revision IDs (none allocated here).
- Index names beyond the existing `uq_site_code_facility` / `uq_facility_code_org`.
- Length of the compatibility window.
- Job vs SQL for backfill (must be reviewable and reversible on disposable DB).

**Not to be decided in this plan:**

- New commercial prices, discounts, penalties, refunds, or invoice dates.
- Introducing Branch Admin.
- DR-022 customer-module implementation.
- Changing Facility IDs.

---

## 12. Confirmation

This plan has **not** been executed. No schema, API, Flutter, infrastructure, or database change is authorized by publishing this document.
