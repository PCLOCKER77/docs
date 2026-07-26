# DR-003 Release Management Folder Addition

> Decision record for adding `14_Release_Management/` between Operations and Release Notes.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-003 |
| Document Name | Release Management Folder Addition |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Release Management / Product Governance |
| Reviewers | Product, DevOps, QA, Operations, Support, Security, Architecture |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

A dedicated `14_Release_Management/` folder shall be added between `13_Operations/` and `15_Release_Notes/`.

Release Notes shall be renumbered to `15_Release_Notes/`.

---

# 2. Context

Deployment defines how an approved build is deployed.

Testing defines whether the product has been verified.

Operations defines whether the deployed product can be supported.

Release Notes communicates what changed in an approved released version.

Before this decision, there was no clear owner for release scope, release calendar, version assignment, release candidate governance, Go / No-Go decisions, cutover coordination, staged rollout, hotfix governance, post-release observation, and release closure.

---

# 3. Decision

The documentation hierarchy shall include:

```text
11_Deployment/
12_Testing/
13_Operations/
14_Release_Management/
15_Release_Notes/
16_Development_Readiness/
99_Decision_Records/
```

Release Management owns:

- Release scope.
- Release calendar.
- Version assignment.
- Release candidate governance.
- Change freeze controls.
- Go / No-Go governance.
- Release approval.
- Cutover coordination.
- Staged rollout decisions.
- Feature activation governance.
- Hotfix and emergency-release governance.
- Release postponement or cancellation.
- Post-release observation.
- Release closure and evidence packaging.

Release Notes consumes approved Release Management closure outputs and communicates what changed.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Keep Release Notes as folder 14 | Release Notes remains immediately after Operations | Rejected because release decision ownership remains unclear |
| Put release governance inside Deployment | Deployment owns release decisions | Rejected because Deployment should execute approved deployment, not decide release scope or Go / No-Go |
| Put release governance inside Testing | Testing owns release decisions | Rejected because Testing provides quality recommendation, not release approval |
| Put release governance inside Operations | Operations owns release decisions | Rejected because Operations supports production and readiness, not release scope and rollout decisions |
| Add Release Management folder | Create explicit release decision governance layer | Accepted |

---

# 5. Rationale

Release approval requires inputs from Deployment, Testing, Operations, Product, Security, Support, and Engineering.

No single execution folder should own the overall release decision.

A dedicated Release Management folder gives the repository a clear governance layer for release decision-making before Release Notes communicates approved outcomes.

---

# 6. Consequences

## Positive Consequences

- Release decision ownership is explicit.
- Deployment, Testing, and Operations boundaries remain clean.
- Release Notes remains lightweight and communication-focused.
- Go / No-Go governance has a clear home.
- Known-risk acceptance and release closure are traceable.

## Tradeoffs

- One additional folder must be maintained.
- Existing references to Release Notes numbering must be updated.

## Risks

- Teams may confuse Release Management with Deployment unless ownership boundaries remain visible in both folders.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `11_Deployment/` | Provides deployment readiness and deployment outcome inputs |
| `12_Testing/` | Provides quality recommendation and known defect inputs |
| `13_Operations/` | Provides operations readiness and support inputs |
| `14_Release_Management/` | Added as release decision governance owner |
| `15_Release_Notes/` | Consumes approved release closure outputs |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Release decision governance | Release Management |
| Deployment execution | DevOps / Deployment |
| Quality recommendation | QA / Testing |
| Production readiness | Operations |
| Release communication | Release Notes / Product |
| Future changes to this decision | Release Management / Product Governance |

---

# 9. Review and Freeze Rule

This decision shall remain `Design Draft` until `14_Release_Management/` and `15_Release_Notes/` are reviewed together.

Once frozen, changes to release governance ownership shall be captured through a superseding decision record.
