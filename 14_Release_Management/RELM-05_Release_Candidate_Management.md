# RELM-05 Release Candidate Management

> Release candidate creation, replacement, validation, supersession, promotion eligibility, and evidence governance for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | RELM-05 |
| Document Name | Release Candidate Management |
| Folder | 14_Release_Management |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Release Management |
| Reviewers | DevOps, QA, Backend Engineering, Database, Security, Operations, Product |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines release candidate management for Digitize.

It governs how release candidates are created, identified, replaced, validated, marked eligible for promotion, superseded, or rejected.

---

# 2. Scope

This document covers:

- Release candidate creation.
- Candidate identifiers.
- Candidate inputs.
- Validation evidence.
- Replacement and supersession.
- Promotion eligibility.
- Candidate rejection.
- Candidate evidence.

---

# 3. Out of Scope

This document does not define:

- Build pipeline implementation.
- Deployment execution.
- Test execution detail.
- Source-code branching strategy.
- Release-note content.

---

# 4. Governing Standard

This document inherits `RELM-00_Release_Management_Standards.md`.

Release candidates shall be governed by Release Management and shall not be promoted based only on artifact existence.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| RELM-00 | Release candidate standards and promotion eligibility |
| Deployment | Artifact identity, deployment readiness, environment validation |
| Testing | Test readiness, test completion, defect status |
| Operations | Support readiness and handover acceptance |
| Backend Engineering | Build and implementation readiness |
| Database Design | Migration compatibility and data-impact readiness |

---

# 6. Candidate Creation

Release candidate creation shall define:

- Release candidate ID.
- Parent release ID.
- Candidate sequence.
- Source revision.
- Build artifact references.
- Build pipeline reference.
- Configuration set reference where applicable.
- Migration reference where applicable.
- Creation owner.
- Creation timestamp.

Candidates without artifact provenance shall not be eligible for production release.

---

# 7. Candidate Validation

Candidate validation shall consume:

- Deployment readiness.
- Test readiness.
- Test execution evidence.
- UAT status where applicable.
- Operations readiness.
- Security readiness.
- Migration readiness.
- API and integration compatibility status.
- Known defects and risks.

Validation evidence shall be attached to the release candidate record.

---

# 8. Candidate Replacement

Candidate replacement shall define:

- Superseded candidate ID.
- Replacement candidate ID.
- Replacement reason.
- Scope change if any.
- Artifact change.
- Test impact.
- Deployment impact.
- Operations impact.
- Approval owner.

Superseded release candidates shall not be promoted without re-approval.

---

# 9. Promotion Eligibility

Promotion eligibility shall require:

- Approved release scope.
- Approved version or candidate identifier.
- Artifact provenance.
- Deployment readiness.
- Testing recommendation.
- Operations readiness.
- Known-risk acceptance where applicable.
- Go / No-Go decision pending or completed.

Promotion eligibility does not equal release approval.

---

# 10. Candidate Rejection

Candidate rejection shall define:

- Candidate ID.
- Rejection reason.
- Failed gate.
- Required corrective action.
- Replacement expectation.
- Impact on release calendar.
- Communication dependency.

Rejected candidates shall not be used in production release decisions.

---

# 11. Evidence

Candidate evidence shall include:

- Candidate record.
- Artifact references.
- Source revision.
- Pipeline run.
- Validation evidence.
- Supersession history.
- Rejection record where applicable.
- Promotion eligibility decision.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Candidate creation is defined.
- Candidate validation is documented.
- Candidate replacement is governed.
- Promotion eligibility is defined.
- Candidate rejection is covered.
- Evidence requirements are documented.
- No rule contradicts `RELM-00`.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `RELM-00` is reviewed and release candidate governance is accepted by Release Management, DevOps, and QA.
