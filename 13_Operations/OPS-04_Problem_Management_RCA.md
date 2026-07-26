# OPS-04 Problem Management RCA

> Problem management, root-cause analysis, corrective actions, prevention, review, and operational improvement standards for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | OPS-04 |
| Document Name | Problem Management RCA |
| Folder | 13_Operations |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Operations / Support |
| Reviewers | DevOps, Backend Engineering, Database, Security, Product, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines problem management and root-cause analysis standards for Digitize operations.

It ensures recurring or significant operational issues are analyzed, corrected, prevented, and tracked to closure.

---

# 2. Scope

This document covers:

- Problem identification.
- RCA triggers.
- RCA structure.
- Corrective actions.
- Preventive actions.
- Ownership.
- Review cadence.
- Evidence.
- Operational improvement feedback.

---

# 3. Out of Scope

This document does not define:

- Incident triage procedure detail.
- Source-code fixes.
- Deployment procedure changes.
- Product roadmap decisions.
- Customer-facing communication.

Incidents are governed by `OPS-03`. Release decisions are governed by Release Management. Release communication is governed by Release Notes.

---

# 4. Governing Standard

This document inherits `OPS-00_Operations_Standards.md`.

It shall not redefine incident handling, deployment execution, or release-note communication ownership.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| OPS-00 | Problem and RCA standards |
| OPS-03 | Incident records and post-incident review triggers |
| OPS-02 | Monitoring gaps and alert review findings |
| Testing | Known defects and test gaps |
| Backend Engineering | Corrective action support |
| Database Design | Data, performance, backup, or recovery root-cause context |
| Security | Security RCA and audit support where applicable |

---

# 6. Problem Identification

Problem records may be created from:

- Recurring incidents.
- High-severity incidents.
- Repeated support requests.
- Monitoring gaps.
- Capacity bottlenecks.
- Failed operational runbooks.
- Backup or restore validation failures.
- Security findings.
- Known defects with operational impact.

Problem records shall identify owner, impact, and expected review path.

---

# 7. RCA Triggers

RCA should be required for:

- SEV-1 incidents.
- Repeated SEV-2 incidents.
- Data integrity events.
- Tenant isolation events.
- Security-impacting events.
- Repeated provider failures.
- Significant customer-impacting outages.
- Failed recovery procedure.
- Unplanned extended downtime.

RCA may also be requested by Operations, Product, Security, or Release Management.

---

# 8. RCA Structure

RCA shall include:

- Problem identifier.
- Incident or evidence references.
- Impact summary.
- Timeline.
- Root cause.
- Contributing factors.
- Detection gap.
- Response gap.
- Prevention opportunity.
- Corrective actions.
- Preventive actions.
- Owners.
- Due dates.
- Review status.

RCA shall focus on system improvement, not individual blame.

---

# 9. Corrective and Preventive Actions

Actions shall define:

- Action description.
- Owner.
- Priority.
- Target date.
- Validation method.
- Related document or system area.
- Release dependency where applicable.
- Closure evidence.

Actions may feed product backlog, engineering backlog, deployment governance, monitoring improvements, runbook updates, or training.

---

# 10. Review and Closure

Problem closure requires:

- RCA completed where required.
- Corrective actions assigned.
- Preventive actions assigned where applicable.
- Residual risk documented.
- Owner approval.
- Evidence retained.

Problems may remain open while long-running corrective actions are tracked separately.

---

# 11. Evidence

Problem management evidence shall include:

- Problem identifier.
- Related incidents.
- RCA document.
- Corrective actions.
- Preventive actions.
- Owners.
- Due dates.
- Closure evidence.
- Residual risk.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Problem identification is defined.
- RCA triggers are documented.
- RCA structure is defined.
- Corrective and preventive actions are documented.
- Review and closure are defined.
- Evidence requirements are documented.
- No rule contradicts `OPS-00` or Incident Management.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `OPS-00` is reviewed and RCA ownership is accepted by Operations.
