# DR-002 Governing Document Per Folder

> Decision record for the folder-level governing document model.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-002 |
| Document Name | Governing Document Per Folder |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Architecture Governance / Documentation Governance |
| Reviewers | Product, Architecture, Backend Engineering, DevOps, QA, Operations, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Each major documentation folder shall have exactly one governing standards document using the `00` document pattern where applicable.

---

# 2. Context

The documentation set contains many specialized documents per folder.

Without a governing document, common standards such as scope, boundaries, tenant isolation, security, observability, testing expectations, lifecycle status, and ownership may be repeated inconsistently.

---

# 3. Decision

Each major folder shall define one governing document.

Examples:

| Folder | Governing Document |
|---|---|
| `07_API_Collections/` | `API-00` |
| `08_Integration_Contracts/` | `IC-00_Integration_Standards.md` |
| `09_UI_UX_Design/` | `UI-00_UI_UX_Standards.md` |
| `10_Backend_Engineering/` | `BE-00_Backend_Engineering_Standards.md` |
| `11_Deployment/` | `DEP-00_Deployment_Standards.md` |
| `12_Testing/` | `TEST-00_Testing_Standards.md` |
| `13_Operations/` | `OPS-00_Operations_Standards.md` |
| `14_Release_Management/` | `RELM-00_Release_Management_Standards.md` |
| `15_Release_Notes/` | `RN-00_Release_Notes_Standards.md` |
| `16_Development_Readiness/` | `DEV-00_Development_Readiness_Standards.md` |
| `99_Decision_Records/` | `DR-00_Decision_Record_Standards.md` |

Downstream documents shall inherit common standards from the governing document instead of redefining them.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Repeat standards in every document | Each document includes all common rules | Rejected because it creates drift and review overhead |
| Global-only standards document | One document governs all folders | Rejected because folder-specific concerns need local governance |
| One governing document per folder | Each folder defines local standards once | Accepted |

---

# 5. Rationale

The governing-document model keeps each folder consistent, reduces duplication, and gives reviewers one place to validate common rules.

It also allows downstream documents to focus on their specific topic.

---

# 6. Consequences

## Positive Consequences

- Common standards are easier to maintain.
- Specialized documents are shorter and clearer.
- Review flow is more consistent.
- Freeze rules are easier to enforce.

## Tradeoffs

- Folder-level standards must be written before downstream documents can be finalized.
- Downstream documents must reference the governing document correctly.

## Risks

- If a governing document is incomplete, downstream documents may inherit gaps.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `07_API_Collections/` through `16_Development_Readiness/` | Common standards are centralized in each folder |
| `99_Decision_Records/` | Records and governs the decision model |
| Future folders | Should follow the same `00` standards pattern |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Folder governing document | Respective folder owner |
| Cross-folder consistency | Architecture Governance / Documentation Governance |
| Freeze readiness | Folder owner and reviewers |
| Future changes | Documentation Governance |

---

# 9. Review and Freeze Rule

This decision shall remain `Design Draft` until active folder governing documents are reviewed for consistency.

Once frozen, changes to the folder governance model shall be captured through a superseding decision record.
