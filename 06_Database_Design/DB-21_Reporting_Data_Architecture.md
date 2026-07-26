# DB-21 Reporting Data Architecture

**Document ID:** DB-21  
**Document Name:** Reporting Data Architecture  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Reporting Data Architecture  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the reporting data architecture for Digitize.

It explains how operational, commercial, customer, membership, attendance, notification, support, audit, and security data shall be transformed into reporting-friendly structures without making reporting tables the system of record.

---

# 2. Reporting Principles

| Principle | Requirement |
|---|---|
| Source separation | Reporting structures shall not become authoritative transactional sources |
| Tenant awareness | Reporting data shall preserve tenant, facility, and site scope |
| Performance isolation | Heavy analytics shall not degrade operational workflows |
| Traceability | Reporting records shall identify source entities where practical |
| Security | Sensitive data shall be masked or excluded where not required |
| Rebuildability | Derived reporting structures should be rebuildable from authoritative sources |

---

# 3. Reporting Data Layers

| Layer | Purpose |
|---|---|
| Operational source tables | Authoritative business data |
| Reporting projections | Read-optimized structures for screens and reports |
| KPI snapshots | Time-based metric values |
| Analytical aggregates | Aggregated business measures |
| Historical snapshots | Frozen reporting state for period comparison |
| Export metadata | Audit-friendly report export tracking |

---

# 4. Reporting Schema Scope

Approved reporting tables include:

- `reporting.report_definition`
- `reporting.report_parameter`
- `reporting.report_schedule`
- `reporting.report_execution`
- `reporting.report_export`
- `reporting.dashboard_configuration`
- `reporting.kpi_definition`
- `reporting.kpi_snapshot`
- `reporting.reporting_projection`
- `reporting.analytical_aggregate`
- `reporting.historical_snapshot`

---

# 5. Reporting Projection Strategy

Reporting projections shall:

- Be derived from authoritative source tables.
- Include `organization_id` where tenant-specific.
- Include source entity references where practical.
- Be refreshed synchronously only where business-critical.
- Be refreshed asynchronously for dashboards and analytics where acceptable.
- Include refresh timestamps.

Example projection categories:

| Projection | Source Areas |
|---|---|
| Customer summary | Customer, membership, attendance, billing |
| Membership summary | Membership, customer, payment |
| Attendance summary | Attendance, membership, site |
| Revenue summary | Invoice, payment, refund |
| Support summary | Tickets, SLA, assignments |

---

# 6. KPI Snapshot Strategy

KPI snapshots shall support:

- Daily attendance counts.
- Active membership counts.
- Revenue totals.
- Outstanding invoice totals.
- Payment success rates.
- Campaign delivery results.
- Support SLA compliance.

KPI snapshots shall include measurement time, scope, and metric definition reference.

---

# 7. Materialized View Strategy

Materialized views may be used for expensive reporting queries where:

- Source tables are large.
- Dashboard response time requirements cannot be met through direct queries.
- Refresh frequency is acceptable.
- Refresh job ownership is defined.

Materialized views shall not replace source tables.

---

# 8. Reporting Security

Reporting security shall:

- Enforce organization/facility/site scope.
- Respect RBAC permissions.
- Mask sensitive personal data where not required.
- Restrict export access.
- Audit report exports.
- Prevent unauthorized cross-tenant reporting.

---

# 9. Reporting Refresh Patterns

| Pattern | Usage |
|---|---|
| On-write projection | Critical summaries needed immediately |
| Scheduled refresh | Dashboards and daily KPIs |
| Event-driven refresh | Notifications, payments, support events |
| Manual rebuild | Recovery or correction scenarios |

---

# 10. Reporting Quality Controls

Reporting data shall be validated for:

- Source count reconciliation.
- Tenant scope consistency.
- Financial total accuracy.
- Snapshot timestamp correctness.
- Duplicate projection prevention.
- Export audit creation.

---

# 11. Summary

DB-21 defines how Digitize reporting data shall be structured, refreshed, secured, and governed for enterprise analytics and operational dashboards.
