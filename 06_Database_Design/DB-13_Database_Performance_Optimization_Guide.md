# DB-13 Database Performance & Optimization Guide

**Document ID:** DB-13  
**Document Name:** Database Performance & Optimization Guide  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Database Engineering Guide  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Business Owner:** Product Architecture  
**Technical Owner:** Data Architecture / Platform Engineering  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines PostgreSQL performance engineering guidance for Digitize.

It expands the operational guidance in DB-09 and explains how indexes, access patterns, statistics, partitioning, maintenance jobs, query reviews, and optimization controls shall be managed for a multi-tenant SaaS platform.

---

# 2. Performance Principles

| Principle | Requirement |
|---|---|
| Tenant-aware access | High-volume queries shall include tenant scope filters |
| Index by access pattern | Indexes shall support documented API, UI, reporting, and operational access patterns |
| Avoid unbounded scans | Production queries shall avoid full-table scans on high-volume tenant-owned tables unless approved |
| Measure before tuning | Optimization shall be based on execution plans and observed metrics |
| Separate reporting load | Reporting projections and aggregates shall reduce pressure on OLTP tables |
| Keep writes efficient | Indexes shall be balanced against write overhead |

---

# 3. Index Strategy

| Index Type | Usage |
|---|---|
| Primary key index | Automatically created on `record_id` |
| Foreign key index | Required for high-volume relational joins |
| Tenant composite index | Required for tenant-scoped operational queries |
| Partial index | Preferred for active/open/high-frequency states |
| GIN index | Used selectively for JSONB metadata/search fields |
| Time-series index | Used for attendance, audit, notification, report execution, and security events |

Example pattern:

```sql
CREATE INDEX idx_customer_active_by_org
ON customer.customer (organization_id, customer_status)
WHERE customer_status = 'ACTIVE';

CREATE INDEX idx_attendance_org_check_in
ON operations.attendance (organization_id, check_in_at);

CREATE INDEX idx_customer_metadata_gin
ON customer.customer USING GIN (metadata);
```

---

# 4. Query Optimization Standards

Queries shall:

- Filter by `organization_id` for tenant-owned tables.
- Use `facility_id` and `site_id` when the business workflow operates at those scopes.
- Avoid selecting unnecessary columns in list screens.
- Avoid joining audit tables into transactional screens unless required.
- Use pagination for list APIs.
- Use date range filters for high-volume time-series data.
- Use reporting projections for dashboards.

---

# 5. Execution Plan Review

The following PostgreSQL commands may be used in lower environments:

```sql
EXPLAIN ANALYZE
SELECT *
FROM operations.attendance
WHERE organization_id = '<organization-uuid>'
  AND check_in_at >= NOW() - INTERVAL '30 days';
```

Execution plans shall be reviewed for:

- Sequential scans on high-volume tables.
- Missing tenant indexes.
- Excessive nested loop joins.
- Poor row estimates.
- Sorts spilling to disk.
- Unused indexes.

---

# 6. Statistics, VACUUM, and ANALYZE

| Activity | Purpose | Frequency Guidance |
|---|---|---|
| AUTOVACUUM | Reclaim dead tuples | Enabled continuously |
| ANALYZE | Refresh planner statistics | Automatic and after large backfills |
| Manual VACUUM | Recover from exceptional write-heavy workloads | Operationally approved |
| REINDEX | Rebuild bloated indexes | Maintenance window where needed |

High-write tables include:

- `operations.attendance`
- `operations.entry_exit_event`
- `communication.notification_delivery`
- `communication.notification_attempt`
- `audit.audit_event`
- `security.authentication_event`
- `security.security_event`

---

# 7. Partitioning Strategy

Partitioning should be evaluated for large time-series or append-heavy tables.

| Candidate Table | Partition Key | Rationale |
|---|---|---|
| operations.attendance | `check_in_at` | High-volume attendance history |
| operations.entry_exit_event | `event_at` | High-volume event data |
| communication.notification_delivery | `created_at` | Delivery tracking volume |
| audit.audit_event | `occurred_at` | Compliance and investigation volume |
| security.authentication_event | `occurred_at` | Login/security event volume |
| reporting.kpi_snapshot | `measured_at` | Time-series reporting |

Partitioning shall be introduced only after volume assumptions are validated.

---

# 8. Fillfactor and HOT Update Strategy

Fillfactor may be considered for write-heavy mutable tables where updates are frequent.

| Table Type | Guidance |
|---|---|
| Immutable audit/event tables | Default fillfactor |
| Mutable status tables | Consider lower fillfactor after measurement |
| High-update support tickets | Evaluate fillfactor if bloat appears |
| Payment/invoice tables | Preserve integrity; tune only after measurement |

---

# 9. Full Text and Search Optimization

Search use cases should avoid expensive wildcard scans.

Recommended approaches:

- Use normalized search columns for frequently searched text.
- Use trigram or full-text search only after approval.
- Use GIN indexes for structured JSONB metadata where justified.
- Use search views for customer, membership, invoice, and support search experiences.

Example search view:

```sql
CREATE VIEW customer.customer_search AS
SELECT
    record_id,
    organization_id,
    customer_code,
    first_name,
    last_name,
    primary_email,
    primary_phone,
    customer_status
FROM customer.customer;
```

---

# 10. Performance Review Checklist

| Review Area | Required |
|---|---|
| Tenant filters validated | Yes |
| Pagination validated | Yes |
| Index usage reviewed | Yes |
| Execution plan reviewed for critical queries | Yes |
| Write overhead assessed | Yes |
| Reporting load separated | Yes |
| Slow query threshold defined | Yes |

---

# 11. Summary

DB-13 defines the PostgreSQL performance engineering approach for Digitize and shall be used by developers, database engineers, QA engineers, and DevOps teams before production implementation.
