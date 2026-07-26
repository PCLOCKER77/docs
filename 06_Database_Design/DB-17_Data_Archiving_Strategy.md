# DB-17 Data Archiving Strategy

**Document ID:** DB-17  
**Document Name:** Data Archiving Strategy  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Data Lifecycle Strategy  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the Digitize data archiving strategy for PostgreSQL and related storage layers.

Archiving ensures operational tables remain performant while preserving historical, financial, audit, reporting, and compliance records for approved retention periods.

---

# 2. Archiving Principles

| Principle | Requirement |
|---|---|
| Preserve business history | Archiving shall not break historical reporting or audit needs |
| Protect compliance data | Audit and financial records shall follow stricter retention |
| Tenant-aware archival | Archive jobs shall preserve tenant scope |
| No silent deletion | Purging shall be controlled, approved, and auditable |
| Readability after archive | Archived data shall remain accessible through approved reporting/support processes |

---

# 3. Candidate Data for Archiving

| Data Area | Candidate Tables | Archival Trigger |
|---|---|---|
| Attendance history | `operations.attendance`, `operations.entry_exit_event` | Age and reporting cutoff |
| Notification history | `communication.notification_delivery`, `communication.notification_attempt` | Age and delivery closure |
| Report executions | `reporting.report_execution`, `reporting.report_export` | Age and export expiry |
| Support tickets | `support.support_ticket`, related child tables | Closed and retention threshold met |
| Security events | `security.authentication_event`, `security.security_event` | Age and investigation closure |
| Audit records | `audit.audit_event` | Compliance retention policy only |

---

# 4. Archive Storage Options

| Option | Use Case |
|---|---|
| Archive tables | Queryable historical data inside PostgreSQL |
| Separate archive schema | Clear separation from operational data |
| Object storage export | Long-term cold storage |
| Data warehouse | Historical analytics and BI |

Recommended initial pattern:

- Keep operational tables for current workloads.
- Use reporting projections for dashboards.
- Use archive schema or object storage for cold historical records after retention thresholds.

---

# 5. Archive Job Design

Archive jobs shall:

- Run in batches.
- Filter by tenant and date.
- Preserve source record identifiers.
- Preserve correlation IDs.
- Preserve audit references.
- Validate counts before and after movement.
- Produce audit evidence.
- Avoid locking operational tables for long periods.

---

# 6. Purging Strategy

Purging may occur only when:

- Retention period has expired.
- Legal/compliance hold does not exist.
- Business owner approval is recorded.
- Archive validation is complete where applicable.
- Purge action is audited.

Audit records shall not be purged except under formally approved compliance policy.

---

# 7. Historical Reporting

Historical reporting shall use:

- Reporting projections.
- Archive-aware reporting views.
- Data warehouse/analytics structures where approved.
- Controlled access to archived datasets.

Operational screens should not directly query cold archive data unless specifically designed for that purpose.

---

# 8. Archival Review Checklist

| Review Area | Required |
|---|---|
| Retention class identified | Yes |
| Tenant scope preserved | Yes |
| Business owner approved | Yes |
| Archive validation query defined | Yes |
| Reporting impact assessed | Yes |
| Support access assessed | Yes |
| Audit event generated | Yes |

---

# 9. Summary

DB-17 defines how Digitize data shall move from operational storage to archive storage while preserving performance, reporting, supportability, compliance, and auditability.
