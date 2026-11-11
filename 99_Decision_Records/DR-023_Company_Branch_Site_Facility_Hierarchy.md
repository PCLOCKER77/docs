# DR-023 Company → Branch/Site → Facility Hierarchy

> Accepted target hierarchy for Digitize tenant structure. Development
> implementation is authorized. Deployment, merge to `main`, and QA/production
> database changes are **not** authorized by this record.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-023 |
| Document Name | Company → Branch/Site → Facility Hierarchy |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Product / Architecture Governance |
| Reviewers | Product, Business Analysis, Architecture, Database, Backend Engineering, API, Identity, UI/UX, Operations |
| Version | 1.2 |
| Last Updated | 2026-10-16 |
| Related Source | `00_Project_Management/Decision_Log.md` DEC-003 (current live hierarchy); DR-004 |
| Identifier assignment | Next unused `99_Decision_Records` ID after DR-021. **DR-022 is reserved** for Customer Data Protection + Customer Module (`docs/architecture/DR-022_TRANSITION_FROM_DR-021.md`) and must not be reused. |
| Intended supersession (when Accepted) | DR-004 hierarchy outcome; DEC-003 hierarchy outcome; DR-019 Site Admin as a required role; DR-021 “hierarchy unchanged” clause only |
| Does not supersede | Authentication/session security; tenant isolation; Platform Admin governance (DR-021 remainder); credential provisioning; facility-scoped SaaS billing (DR-019 commerce split); API catalog numbering unless a later contract change is approved |
| Supersedes today | Hierarchy clauses of DR-004 / DEC-003 / DR-021 **for development implementation only**. Live QA/production remain Organization → Facility → Site until a separately authorized cutover |
| Superseded By | None |

---

# 1. Decision Summary

The **target** tenant hierarchy is:

```text
Platform
    ↓
Company / Organization
    ↓
Branch / Site
    ↓
Facility
    ↓
Staff
```

- Company continues as `tenant.organization`. Company is the owner-facing term.
- Branch is the owner-facing name for Site (`tenant.site`). No separate Branch table unless a later explicit decision requires a distinct entity.
- A Company may have multiple Sites. Each Site may contain multiple Facilities of mixed types (for example swimming pool, gym, yoga center, or other supported facility types).
- Each Facility must belong to exactly one Site in the **target** model (`tenant.facility.site_id`).
- Company Admin manages the Company’s Sites, Facilities, authorized staff, and subscriptions, subject to permissions and subscription eligibility. There is **no Site Admin or Branch Admin** in the target role model.
- Staff remain subject to explicit least-privilege permissions and authorized access scopes. Company-wide access is not assumed.
- Each Facility remains independently billable. The Site/Company is not the SaaS commercial unit.
- Company terms acceptance enables onboarding/setup; it does not activate SaaS subscription or permit staff creation / operational use.
- Staff creation and operational access remain gated by company subscription eligibility, evaluated authoritatively on the backend.
- Flutter navigation is not a security boundary.
- Hierarchy, role, and access-scope migration must be traceable and recoverable. Cardinality inversion is not a mechanical FK rename. Silent Site assignment, auto-picking among multiple Sites, and automatic Site Admin → Company Admin promotion are prohibited.

**This record authorizes development implementation only.** It does not authorize deployment, merge to `main`, or QA/production database changes. Local development may use the additive Company → Site → Facility schema. QA/production runtime remains Organization → Facility → Site until a separately authorized cutover. Q1–Q4 remain cutover gates for environments that still hold legacy rows.

---

# 2. Context

The implemented and documented model is:

```text
Platform → Organization → Facility → Site
```

That model is recorded in DR-004, DEC-003, API-02, identity staff types (`SITE_ADMINISTRATOR`), and Flutter/API code. `tenant.site.facility_id` is mandatory. Subscription and license rows are facility-scoped. Site create requires an active parent facility.

Product has approved a **direction change**: Branch/Site is the location layer under the company; Facility is the operational/billable unit under that branch; Receptionist-style staff sit under facility; Site Admin is not required.

This is an architectural change, not a terminology-only rename. Terminology mapping is:

| Owner-facing | Canonical schema name |
|---|---|
| Company | Organization (`tenant.organization`) |
| Branch | Site (`tenant.site`) |
| Facility | Facility (`tenant.facility`) |

---

# 3. Decision

We will (development implementation authorized; QA/production cutover is not):

1. Treat **Company** as `tenant.organization`. Do not add a company table.
2. Treat **Branch** as the owner-facing label for **Site**. Do not add `tenant.branch` unless a later decision proves a distinct domain entity.
3. Invert parentage so **Site belongs to Organization** and **Facility belongs to one Site** (plus organization for isolation). Each facility has exactly one valid parent branch/site.
4. Associate **Staff** with the company and authorized site/facility scopes. Receptionist is a facility-scoped staff assignment, not a new hierarchy table. Existing `STAFF` may remain the type unless a later identity decision introduces a dedicated receptionist code.
5. **Remove Site Admin** from the new role model. Do not introduce Branch Admin. Existing `SITE_ADMINISTRATOR` (and any Site-scoped admin) assignments require an explicit, auditable inventory and disposition before retirement. Never automatically promote all Site Admins to Company Admins. Never silently broaden permissions. Ambiguous assignments block the affected cutover.
6. Keep **subscription billing facility-scoped**. Each Facility has its own subscription lifecycle. Applicable pricing follows facility type and approved backend commercial configuration. Adding another Facility adds another independently billable unit. Cancelling one Facility subscription must not automatically cancel others. Preserve approved proration, payment, grace-period, cheque-bounce, suspension, and reactivation rules at subscription/facility scope. While a subscription is suspended, preserve approved limited Company Admin access for billing, payment, support, and account recovery. Pricing, invoice calculation, eligibility, and payment confirmation remain backend-authoritative. This record invents no prices, discounts, cancellation penalties, billing dates, or refunds.
7. Keep DR-021 onboarding semantics that do not conflict: terms acceptance ≠ subscription activation; staff create and operational modules require eligible active SaaS.
8. Keep backend authorization authoritative.
9. Require preflight, rollback/recovery, and reconciliation evidence before any data migration. Facilities with exactly one Site may be eligible for deterministic mapping only after operational-data validation. Facilities with zero or multiple Sites are reconciliation exceptions and require explicit approved mapping. A 1:1 Site count does not prove a safe migration.
10. Prefer a staged, backward-compatible API transition. Keep existing API numbers. Do not rewrite frozen contracts in this record. Dual-write, if used, must have one authoritative representation, transactional consistency or equivalent safeguards, reconciliation, and an explicit removal gate. Do not remove `tenant.site.facility_id` until dependent consumers have migrated and removal is separately approved.

We will not, under this Accepted development record:

- Apply Alembic migrations or production/QA data changes.
- Renumber or rewrite live API-02/API-03 contracts.
- Deploy, merge to `main`, or treat Flutter Branch-as-child-of-Facility screens as the target model.
- Silently drop companies, facilities, sites, invoices, subscriptions, or staff assignments.
- Auto-pick a Site when a Facility has multiple Sites, silently assign a Facility that has none, or delete/merge/split/synthesize Sites or Facilities without explicit approval.
- Change Facility IDs or subscription ownership without an approved migration requirement.
- Treat proposed rules as live runtime behavior.

### 3.1 Legacy cardinality

Live schema: `tenant.site.facility_id` is **required**; one Facility may have many Sites; a Facility has no `site_id`. Target schema: `tenant.facility.site_id` required; one Site has many Facilities. This is a **cardinality inversion**.

Prohibited without explicit, reviewed mapping:

- Automatically choosing one Site among several.
- Silently assigning a Facility with no Site.
- Deleting, merging, splitting, or synthesizing Sites or Facilities.
- Changing Facility IDs or moving subscription rows to a different Facility ID unless a later approved requirement says otherwise. Preserve stable identifiers and keep facility subscriptions keyed to the same Facility ID wherever feasible.

### 3.2 Company Admin and staff

Company Admin (CA Admin) manages Sites, Facilities, authorized staff, and subscriptions for the Company, subject to permissions and subscription eligibility. Staff receive only authorized operational scopes. A new Site/Branch Admin role requires separate evidence and a separate approved decision.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Terminology only | Owner UI says Company / Branch / Facility; keep Facility → Site FKs | Rejected as the target. Insufficient for Branch-above-Facility operations |
| New Branch table | Separate `tenant.branch` besides `tenant.site` | Rejected unless a later decision proves Site cannot represent Branch |
| Keep Site Admin | Retain `SITE_ADMINISTRATOR` in the new model | Rejected for the target role model; migration mapping still required |
| Bill at branch | Move commercial.subscription to site_id | Rejected; facility remains the billable unit |
| Implement immediately on QA/production | Apply hierarchy cutover there | Rejected; development only until a separate cutover authorization |
| Auto-map multi-site facilities | Pick first/active Site | Rejected (Q1); exceptions require explicit mapping |
| Auto-promote Site Admins | Map every `SITE_ADMINISTRATOR` to Company Admin | Rejected (Q2); inventory-first, no silent elevation |

---

# 5. Rationale

Companies operate locations (branches/sites) that each host one or more activity facilities. Receptionist and similar staff work a facility, not a separate site-admin layer. Facility-level SaaS billing already matches how licenses and proration work; putting facilities under a branch must not collapse billing to the branch.

Reserving DR-022 for the planned Customer module avoids identifier collision (DR-00: IDs are stable and not reused).

---

# 6. Consequences

## Positive Consequences

- Owner language (Company, Branch, Facility) can match the real parent/child order.
- Site Admin is not required for day-to-day facility staffing.
- Facility commercial independence is preserved.

## Tradeoffs

- Schema, API-02 parent rules, identity packs, access scopes, and Flutter navigation must change together.
- Current Branch UI that treats Site as a child of Facility is being replaced in development; QA/production cutover remains a separate gate.

## Risks

- Data loss if `facility_id` is dropped from site without assigning `site_id` on every facility.
- Privilege widening if Site Admin is removed without a mapped replacement scope, or if all Site Admins are promoted to Company Admin.
- Operational breakage if customers, memberships, attendance, billing, staff, or authorization scopes are not checked alongside cardinality.
- Dual-write divergence if two independent parentage sources of truth exist without an authority and reconciliation gate.
- Contract drift if API-02 paths change without a numbered inventory update.

## QA/production cutover is not authorized

Required later (out of scope for this development authorization): QA/production Alembic application; merge to `main`; live API freeze rewrite; unresolved Q1/Q2 handling in environments that still hold Facilities, Sites, or Site Admins.

---

# 7. Affected Documentation and Contracts

Live artifacts stay in force until a contract-change approval. This record flags conflict, it does not rewrite them.

| Artifact | Conflict with target | Action until Accepted + go-ahead |
|---|---|---|
| DR-004, DEC-003 | Org → Facility → Site | Remain authoritative for runtime |
| DR-019 / access freeze | Site Admin is first-class | Remain authoritative for runtime |
| DR-021 “hierarchy unchanged” | Hierarchy clause only | Onboarding, PA boundary, credentials unchanged |
| API-02 (`API_CONTRACT_REGISTRY.md`, collection) | Site create/list scoped to facility; facility has no parent site | Inventory annotated as current live; no endpoint renumber in this record |
| API-03 identity | `SITE_ADMINISTRATOR` staff type / role seed | Unchanged until mapping is approved |
| API-09 subscription/license | Facility-scoped commercial rows | **Keep** as non-conflicting |
| AUTH freeze, tenant isolation, PA governance | None intended | Remain in force |
| `06_Database_Design`, `07_API_Collections`, `09_UI_UX_Design`, `10_Backend_Engineering` | Must be updated only with the migration plan | No schema or API rewrite in this record |
| DR-022 reservation | None | Customer module keeps DR-022 |

### Current live API-02 parentage (unchanged)

- `POST /api/v1/sites` — facility-scoped create (API-02-011)
- `GET /api/v1/sites` — requires facility context (API-02-019)
- `POST /api/v1/facilities` — organization-scoped; no parent site (API-02-007)

Target (future contract change, not registered here): site listed/created under organization; facility created with required `site_id`. Prefer staged compatibility. Dual-write only if required, with one authoritative representation. Proposed migration mechanics: `docs/architecture/DR-023_HIERARCHY_MIGRATION_PLAN.md` (not executed).

---

# 8. Acceptance Criteria (decision)

- Hierarchy is documented in this registry entry and cross-linked from the API inventory without pretending live contracts already changed.
- Target: each facility has exactly one valid parent branch/site.
- Facility-level subscription billing and proration remain intact.
- No silent loss of company, facility, site, invoice, subscription, or staff assignment in any future migration.
- Site Admin assignments migrated or retired through an approved mapping; least privilege preserved.
- Tenant isolation and authentication guarantees remain intact.
- Future migration must include preflight, rollback/recovery, and reconciliation evidence.
- No QA/production deployment until a separate cutover authorization.
- Preflight fails on unresolved zero-Site or multi-Site Facilities (Q1).
- Every legacy Site Admin assignment has an auditable disposition before Site Admin retirement (Q2). Mapping policy remains open until inventory.

---

# 9. Ownership

| Concern | Owner |
|---|---|
| Decision ownership | Product / Architecture Governance |
| Identifier / supersession hygiene | Architecture Governance |
| Future migration plan | Database / Backend / Identity |
| API contract amendment | API / Backend |
| Owner-facing UI terms | UI/UX |
| Implementation authorization | Product / Architecture (separate go-ahead) |

---

# 10. Review and Freeze Rule

This record is **Accepted** for development implementation as of 2026-10-16.

Acceptance rationale: product authorized Company → Site → Facility; local development database `digitize` (localhost) had 0 Sites, 0 Facilities, 0 Site Admin assignments, and 0 facility subscriptions. Existing Companies and identities were preserved. Empty local data does **not** prove QA or production are empty. The disposable API-test database `digitize_test` contains fixture Facilities/Sites/Site Admins and must **not** be auto-mapped.

Deployment and merge to `main` remain unauthorized.

It does **not** freeze QA/production runtime. DR-004 / API-02 / DR-019 remain the live hierarchy and role model there until a separately authorized cutover.

Once Accepted and Frozen, outcome changes require a new superseding decision record. DR-004 and conflicting clauses in DR-019 / DR-021 shall then be marked superseded **only for those clauses**, with this ID as successor. Non-conflicting requirements stay in force.

Q2 Site Admin conversion is **not required** for the local development database (`digitize`), which had zero Site Admin assignments. Fixture/QA/production inventories remain a separate cutover gate. This record is **Accepted** for development only.

---

# 11. Proposed answers to open questions

These answers are **proposed**, not Accepted live policy.

## Q1 — Existing Facilities with zero or multiple Sites

- Preflight **must fail** for unresolved cardinality exceptions.
- Each exception needs an explicit, reviewed mapping.
- Never auto-pick a Site or fabricate a mapping.
- Facilities with exactly one Site may be deterministically mapped only after operational-data validation (customers, memberships, attendance, billing, staff, authorization scopes). Count alone is insufficient.

## Q2 — Existing Site Admin assignments

- Site Admin is removed from the **target** role model.
- Existing assignments require an explicit, auditable disposition (user, tenant, role, permissions, access scope, outcome).
- No automatic Company Admin promotion and no silent permission broadening.
- Exact mapping policy is finalized **after** inventorying actual roles, permissions, and scopes.
- Unresolved or ambiguous assignments block the affected migration/cutover.
- Because that mapping policy is not yet evidence-based for QA/production, those environments stay blocked. Development `digitize` had zero Site Admin rows, so Q2 conversion is not required there.

## Q3 — Branch-scoped role

- No Site Admin or Branch Admin role initially.
- Company Admin manages Sites and Facilities (subject to permissions and eligibility).
- Staff receive only authorized operational scopes.
- A new role requires separate evidence and a separate approved decision. Do not introduce Branch Admin in this record.

## Q4 — API transition

- Prefer a staged, backward-compatible migration.
- Keep existing API numbers. Do not rewrite frozen contracts as part of this decision.
- Dual-write only if required, with explicit consistency protections, one authoritative representation, reconciliation, and a defined retirement gate.
- Avoid two independent sources of truth.
- Do not remove `tenant.site.facility_id` until all dependent consumers have migrated and removal is separately approved.

---

# 12. Related proposed plan

Implementation is **not** authorized. The proposed (unexecuted) migration plan is:

`docs/architecture/DR-023_HIERARCHY_MIGRATION_PLAN.md`
