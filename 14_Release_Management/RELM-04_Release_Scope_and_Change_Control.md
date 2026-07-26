# RELM-04 Release Scope and Change Control

> Release scope, inclusion, exclusion, deferral, freeze, approval, postponement, cancellation, and change-control governance for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | RELM-04 |
| Document Name | Release Scope and Change Control |
| Folder | 14_Release_Management |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Release Management |
| Reviewers | Product, Business, DevOps, QA, Operations, Security, Backend Engineering |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines release scope and change-control governance for Digitize.

It ensures included, excluded, deferred, frozen, postponed, and cancelled changes are governed by explicit release decision ownership.

---

# 2. Scope

This document covers:

- Release scope definition.
- Change inclusion.
- Change exclusion.
- Change deferral.
- Scope freeze.
- Post-freeze changes.
- Waivers and exceptions.
- Release postponement.
- Release cancellation.

---

# 3. Out of Scope

This document does not define:

- Product backlog prioritization.
- Implementation acceptance.
- Deployment execution.
- Test execution.
- Release-note content.

---

# 4. Governing Standard

This document inherits `RELM-00_Release_Management_Standards.md`.

Release scope is owned by Release Management and Product governance, not Release Notes.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| RELM-00 | Release scope, risk, waiver, and known-risk standards |
| Product Foundation | Roadmap and release intent |
| Functional Requirements | Approved functional behavior |
| Backend Engineering | Implementation readiness and technical constraints |
| Deployment | Deployability and rollback constraints |
| Testing | Test coverage, defect status, UAT, and quality recommendation |
| Operations | Support readiness and operational risks |

---

# 6. Release Scope Fields

Release scope shall define:

- Release ID.
- Included changes.
- Excluded changes.
- Deferred changes.
- Changed modules.
- Affected APIs.
- Affected integrations.
- Affected UI/UX surfaces.
- Affected backend services.
- Affected database migrations.
- Customer or tenant impact.
- Known risks.
- Approval status.

---

# 7. Change Inclusion

Change inclusion shall require:

- Source reference.
- Business or product justification.
- Implementation readiness.
- Deployment readiness impact.
- Testing impact.
- Operations impact.
- Release-note communication impact.
- Approval owner.

Changes without traceable source or approval shall not be included in release scope.

---

# 8. Change Exclusion and Deferral

Excluded or deferred changes shall define:

- Change reference.
- Reason.
- Impact.
- New target release where known.
- Customer or tenant impact.
- Required communication where applicable.
- Approval owner.

Deferred changes shall not be presented as included release functionality.

---

# 9. Scope Freeze

Scope freeze shall define:

- Freeze date.
- Freeze owner.
- Frozen scope.
- Allowed exception types.
- Blocked change types.
- Approval process.
- Release candidate impact.
- Test impact.
- Communication impact.

Post-freeze additions require Release Management approval.

---

# 10. Postponement and Cancellation

Release postponement or cancellation shall define:

- Decision.
- Reason.
- Decision owner.
- Affected release candidate.
- Scope impact.
- Customer impact.
- Deployment impact.
- Testing impact.
- Operations impact.
- Release Notes impact.
- Follow-up action.

Release Notes shall not postpone or cancel releases.

---

# 11. Evidence

Scope and change-control evidence shall include:

- Approved release scope.
- Inclusion decisions.
- Exclusion decisions.
- Deferral decisions.
- Freeze record.
- Exception approvals.
- Postponement or cancellation record.
- Known risks.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Release scope fields are defined.
- Change inclusion is governed.
- Exclusion and deferral are documented.
- Scope freeze is defined.
- Postponement and cancellation are covered.
- Evidence requirements are documented.
- No rule contradicts `RELM-00`.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `RELM-00` is reviewed and release scope ownership is accepted by Release Management and Product.
