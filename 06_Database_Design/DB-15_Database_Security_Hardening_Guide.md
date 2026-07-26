# DB-15 Database Security Hardening Guide

**Document ID:** DB-15  
**Document Name:** Database Security Hardening Guide  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Database Security Guide  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines PostgreSQL database security hardening guidance for Digitize.

It translates the security architecture, tenant isolation rules, RBAC expectations, audit requirements, and data protection principles into database-level security controls.

---

# 2. Security Principles

| Principle | Requirement |
|---|---|
| Least privilege | Database users shall receive only required permissions |
| Tenant isolation | Tenant-owned records shall be protected by application and database controls |
| No shared admin usage | Applications shall not connect using owner/superuser credentials |
| Secrets isolation | Credentials shall be externalized through approved secret management |
| Auditability | Privileged and sensitive access shall be logged |
| Defense in depth | Database controls shall complement application authorization |

---

# 3. Role and Privilege Model

| Role Type | Purpose |
|---|---|
| Database owner role | Owns schemas and objects; not used by application runtime |
| Migration role | Executes approved migrations |
| Application role | Executes runtime CRUD through approved access paths |
| Read-only reporting role | Reads approved reporting structures only |
| Support read role | Controlled read access for support diagnostics |
| Audit read role | Controlled read access to audit evidence |

Example role pattern:

```sql
CREATE ROLE digitize_app NOLOGIN;
CREATE ROLE digitize_app_user LOGIN PASSWORD '<managed-secret>';
GRANT digitize_app TO digitize_app_user;
```

---

# 4. Row Level Security Strategy

Row Level Security should be evaluated for tenant-owned tables as an additional safeguard.

Example pattern:

```sql
ALTER TABLE customer.customer ENABLE ROW LEVEL SECURITY;

CREATE POLICY customer_tenant_isolation_policy
ON customer.customer
USING (organization_id = current_setting('app.current_organization_id')::uuid);
```

RLS shall not replace application authorization. It shall act as defense in depth.

---

# 5. Secure Connection Requirements

Database connections shall:

- Use TLS/SSL in production.
- Avoid public exposure unless explicitly approved.
- Use private network connectivity where available.
- Use connection pooling with controlled credentials.
- Rotate passwords/secrets through approved processes.
- Disable direct human production access except approved operational roles.

---

# 6. Sensitive Data Controls

| Data Category | Control |
|---|---|
| Customer personal data | Restricted access, masking where appropriate |
| Payment references | Store provider references only; no raw card data |
| Authentication data | Password hashes only; no plaintext credentials |
| Audit data | Append-only and restricted |
| Support comments/attachments | Restricted and classified |
| Metadata JSONB | Must not contain secrets or raw payment data |

---

# 7. PostgreSQL Configuration Hardening

| Area | Guidance |
|---|---|
| `pg_hba.conf` | Restrict hosts, users, and authentication methods |
| SSL | Require encrypted production connections |
| Superuser | Limit to platform/database administration only |
| Extensions | Allow only approved extensions |
| Logging | Enable security-relevant connection and error logging |
| Statement timeout | Configure to reduce runaway query risk |
| Idle timeout | Configure to reduce abandoned sessions |

---

# 8. Audit Logging

Audit logging shall capture:

- Login failures.
- Privileged access.
- Schema changes.
- Role/permission changes.
- Sensitive data export.
- Financial data access changes.
- Cross-tenant support access.

Database-level audit extensions may be evaluated during implementation.

---

# 9. Security Review Checklist

| Review Area | Required |
|---|---|
| Superuser not used by application | Yes |
| Runtime role least privilege | Yes |
| Migration role separated | Yes |
| Tenant tables reviewed for RLS eligibility | Yes |
| Metadata fields reviewed for sensitive data risk | Yes |
| Backup access controlled | Yes |
| Production access audited | Yes |

---

# 10. Summary

DB-15 defines the PostgreSQL hardening baseline required to protect Digitize tenant data, financial data, customer data, and audit evidence.
