# DB-16 Database Monitoring & Health Guide

**Document ID:** DB-16  
**Document Name:** Database Monitoring & Health Guide  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Database Operations Guide  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the database monitoring, health, alerting, diagnostics, and operational readiness guidance for Digitize PostgreSQL environments.

---

# 2. Monitoring Principles

| Principle | Requirement |
|---|---|
| Detect early | Database health issues shall be detected before business impact where practical |
| Measure tenant impact | Alerts shall support tenant/facility impact analysis |
| Monitor both system and workload | Infrastructure metrics and database workload metrics are both required |
| Alert actionable issues | Alerts shall have owner, severity, threshold, and response playbook |
| Preserve observability safety | Logs shall not expose sensitive personal, payment, or secret data |

---

# 3. Key Metrics

| Metric Area | Metrics |
|---|---|
| Availability | Database up/down, failover state, replication state |
| Connections | Active connections, idle connections, pool saturation |
| Query performance | Slow queries, average latency, p95/p99 latency |
| Locks | Blocking sessions, lock wait duration, deadlocks |
| Storage | Disk usage, table growth, index growth, WAL growth |
| Replication | Replication lag, WAL archive health |
| Maintenance | Vacuum activity, analyze activity, table bloat |
| Errors | Connection failures, query errors, migration errors |

---

# 4. Alert Threshold Guidance

| Alert | Severity | Initial Threshold Guidance |
|---|---|---|
| Database unavailable | Critical | Immediate |
| Connection pool exhausted | High | Sustained saturation |
| Replication lag high | High | Exceeds approved RPO tolerance |
| Disk utilization high | High | Above 80 percent |
| Long-running blocking lock | High | Above approved operational threshold |
| Deadlocks detected | Medium/High | Any repeated occurrence |
| Slow query spike | Medium | Sustained p95 degradation |
| Failed backup | Critical | Any production backup failure |

Thresholds shall be finalized after baseline load testing.

---

# 5. Slow Query Monitoring

Slow query monitoring shall capture:

- Query fingerprint.
- Execution duration.
- Rows scanned/returned.
- Tenant scope where safe.
- Application module.
- Correlation ID where available.
- Execution plan for critical regressions.

Sensitive parameters shall not be logged.

---

# 6. Health Dashboards

Recommended dashboards:

- Database availability.
- Query latency.
- Connection pool.
- Lock and deadlock status.
- Storage growth.
- WAL and backup health.
- Tenant growth trends.
- High-volume table growth.
- Migration execution status.

---

# 7. Operational Runbooks

Runbooks shall exist for:

- Database unavailable.
- Slow queries.
- Connection exhaustion.
- Lock contention.
- Failed migration.
- Failed backup.
- Replication lag.
- Storage pressure.
- Security event investigation.

---

# 8. Monitoring Ownership

| Area | Owner |
|---|---|
| Database metrics | DevOps / Platform Engineering |
| Query performance | Engineering / Data Architecture |
| Security events | Security Architecture |
| Backup alerts | DevOps |
| Business impact assessment | Support / Product Operations |

---

# 9. Summary

DB-16 defines the PostgreSQL monitoring and health baseline required for reliable enterprise SaaS operations.
