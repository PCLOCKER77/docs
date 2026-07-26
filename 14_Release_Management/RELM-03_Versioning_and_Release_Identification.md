# RELM-03 Versioning and Release Identification

> Versioning, release IDs, release candidate identifiers, build numbers, compatibility identifiers, and release traceability for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | RELM-03 |
| Document Name | Versioning and Release Identification |
| Folder | 14_Release_Management |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Release Management |
| Reviewers | Product, DevOps, Backend Engineering, Mobile Engineering, API Architecture, Integration, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines versioning and release identification standards for Digitize.

It ensures each release, release candidate, build, migration, API compatibility state, integration compatibility state, and mobile release can be traced and communicated consistently.

---

# 2. Scope

This document covers:

- Release IDs.
- Version numbers.
- Release names.
- Release candidate identifiers.
- Build numbers.
- Mobile version identifiers.
- API compatibility identifiers.
- Database migration identifiers.
- Integration compatibility identifiers.
- Release traceability.

---

# 3. Out of Scope

This document does not define:

- Source-control branching strategy.
- Build pipeline implementation.
- API contract contents.
- Database migration implementation.
- Release-note wording.

---

# 4. Governing Standard

This document inherits `RELM-00_Release_Management_Standards.md`.

Version assignment is owned by Release Management and shall not be owned by Release Notes.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| RELM-00 | Version and identification standards |
| Deployment | Artifact identifiers, pipeline run, deployment outcome |
| Backend Engineering | Backend build and release readiness |
| API Collections | API version and compatibility identifiers |
| Integration Contracts | Integration compatibility and provider-impact identifiers |
| Database Design | Migration identifiers |
| UI/UX Design | User-facing release surface identifiers |
| Release Notes | Consumes approved version and release identifiers |

---

# 6. Release Identification Fields

Each release shall define:

- Release ID.
- Release name.
- Release type.
- Version.
- Release candidate identifier.
- Target release date.
- Release owner.
- Product owner.
- Change reference.
- Closure reference.

Unset fields shall use `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` until approved.

---

# 7. Versioning Model

Digitize may use semantic versioning where appropriate.

| Segment | Meaning |
|---|---|
| Major | Significant product, compatibility, or platform change |
| Minor | Backward-compatible feature release |
| Patch | Backward-compatible fix or small change |

Final versioning rules remain `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` until approved by Release Management.

---

# 8. Release Candidate Identification

Release candidates shall define:

- Release candidate ID.
- Parent release ID.
- Candidate sequence.
- Source revision.
- Build artifact references.
- Creation timestamp.
- Superseded status.
- Promotion eligibility.

Superseded release candidates shall not be used for production unless re-approved.

---

# 9. Compatibility Identifiers

Release identification shall include compatibility identifiers where applicable:

- Backend build version.
- API compatibility identifier.
- OpenAPI contract reference.
- Mobile build number.
- Minimum supported mobile version.
- Database migration identifier.
- Integration contract identifier.
- Provider compatibility reference.
- Configuration set reference.

Compatibility identifiers shall be included in Go / No-Go evidence when release risk requires them.

---

# 10. Traceability

Release traceability shall connect:

- Release ID.
- Version.
- Release candidate.
- Source revision.
- Build pipeline run.
- Deployment artifact.
- Test evidence.
- Operations readiness.
- Release decision.
- Release closure.
- Release Notes output.

Release Notes shall consume traceability outputs and shall not assign identifiers independently.

---

# 11. Evidence

Versioning evidence shall include:

- Release identifier record.
- Version assignment record.
- Release candidate record.
- Build and artifact references.
- Compatibility identifiers.
- Approval reference.
- Supersession history.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Release identification fields are defined.
- Versioning model is documented.
- Release candidate identifiers are defined.
- Compatibility identifiers are documented.
- Traceability is defined.
- Evidence requirements are defined.
- No rule contradicts `RELM-00`.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `RELM-00` is reviewed and versioning ownership is accepted by Release Management.
