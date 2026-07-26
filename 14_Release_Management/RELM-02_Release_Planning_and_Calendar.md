# RELM-02 Release Planning and Calendar

> Release calendar, milestones, scheduling, ownership, dependency planning, and change-freeze governance for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | RELM-02 |
| Document Name | Release Planning and Calendar |
| Folder | 14_Release_Management |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Release Management |
| Reviewers | Product, DevOps, QA, Operations, Support, Security, Backend Engineering |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines release planning and calendar governance for Digitize.

It ensures releases are scheduled, milestone-driven, dependency-aware, change-freeze controlled, and coordinated across Product, Engineering, Deployment, Testing, Operations, Support, and Release Notes.

---

# 2. Scope

This document covers:

- Release calendar.
- Release milestones.
- Release scheduling.
- Ownership.
- Dependency tracking.
- Change-freeze coordination.
- Release readiness timeline.
- Calendar exceptions.

---

# 3. Out of Scope

This document does not define:

- Sprint planning.
- Deployment execution windows in detail.
- Test execution schedules in detail.
- Operations incident schedules.
- Release-note content.

---

# 4. Governing Standard

This document inherits `RELM-00_Release_Management_Standards.md`.

It shall not redefine Deployment, Testing, Operations, or Release Notes ownership.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| RELM-00 | Release lifecycle, planning, ownership, and decision governance |
| Product Foundation | Roadmap and release intent |
| Deployment | Deployment window and readiness timing |
| Testing | Test plan, execution, completion, and UAT timing |
| Operations | Support readiness and operational handover timing |
| Release Notes | Communication preparation and publication timing |

---

# 6. Release Calendar

The release calendar shall define:

- Release name.
- Release type.
- Target release date.
- Planning start date.
- Scope freeze date.
- Code freeze date where applicable.
- Release candidate date.
- Test completion target.
- Operations readiness target.
- Go / No-Go meeting date.
- Cutover window.
- Observation window.
- Closure date.

Calendar dates remain `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` until approved for a specific release.

---

# 7. Milestone Model

Release milestones may include:

- Release initiated.
- Release scope proposed.
- Release scope approved.
- Change freeze active.
- Release candidate created.
- Deployment readiness available.
- Testing recommendation available.
- Operations readiness available.
- Go / No-Go completed.
- Cutover completed.
- Post-release observation completed.
- Release closed.
- Release Notes published.

Milestones shall identify owner, target date, actual date, and status.

---

# 8. Dependency Planning

Release planning shall identify dependencies on:

- Product decisions.
- Business approval.
- Architecture readiness.
- Database migration readiness.
- API readiness.
- Integration/provider readiness.
- UI/UX readiness.
- Backend release readiness.
- Deployment readiness.
- Testing completion.
- Operations readiness.
- Release communication readiness.

Blocked dependencies shall be visible before Go / No-Go.

---

# 9. Change Freeze

Change-freeze governance shall define:

- Freeze start.
- Freeze scope.
- Allowed changes.
- Blocked changes.
- Exception process.
- Approver.
- Evidence requirement.
- Impact on release candidate.

Changes after freeze require Release Management approval.

---

# 10. Calendar Exceptions

Calendar exceptions shall define:

- Exception reason.
- Impacted milestone.
- New target date.
- Risk impact.
- Approval owner.
- Communication dependency.
- Release decision impact.

Release postponement or cancellation shall be governed by RELM-04 and RELM-06.

---

# 11. Evidence

Planning evidence shall include:

- Release calendar.
- Milestone status.
- Dependency status.
- Freeze approval.
- Exception approvals.
- Schedule change history.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Calendar fields are defined.
- Milestone model is documented.
- Dependency planning is covered.
- Change-freeze rules are defined.
- Calendar exceptions are documented.
- Evidence requirements are defined.
- No rule contradicts `RELM-00`.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `RELM-00` is reviewed and release calendar ownership is accepted by Release Management.
