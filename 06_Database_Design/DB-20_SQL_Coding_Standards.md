# DB-20 SQL Coding Standards

**Document ID:** DB-20  
**Document Name:** SQL Coding Standards  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Database Coding Standard  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines SQL coding standards for Digitize PostgreSQL scripts, migrations, constraints, indexes, triggers, functions, views, seed data, and validation queries.

It ensures all database implementation artifacts remain readable, reviewable, maintainable, secure, and consistent across teams.

---

# 2. General SQL Standards

| Standard | Requirement |
|---|---|
| SQL keywords | Use uppercase SQL keywords |
| Identifiers | Use lowercase snake_case |
| Table names | Use singular or domain-approved table names consistently with DB-03 to DB-11 |
| Schemas | Use approved namespaces only |
| Primary key | Use `record_id` as the standard primary key |
| Foreign keys | Use business-readable names such as `organization_id`, `facility_id`, `customer_id` |
| JSON columns | Use `JSONB` for metadata and controlled payload fields |
| Timestamps | Use `TIMESTAMPTZ` for business timestamps |
| Monetary values | Use `NUMERIC(14,2)` unless approved otherwise |

---

# 3. Naming Standards

| Object | Pattern | Example |
|---|---|---|
| Table | `schema.table_name` | `customer.customer` |
| Primary key column | `record_id` | `record_id` |
| Foreign key column | `{entity}_id` | `customer_id` |
| Unique constraint | `uq_{table}_{columns}` | `uq_customer_code_org` |
| Check constraint | `ck_{table}_{rule}` | `ck_invoice_amounts` |
| Foreign key constraint | `fk_{table}_{referenced_entity}` | `fk_payment_invoice` |
| Index | `idx_{table}_{columns_or_purpose}` | `idx_attendance_org_date` |
| Trigger | `trg_{table}_{purpose}` | `trg_invoice_updated_at` |
| Function | `{schema}.{verb}_{object}` | `platform.set_updated_at` |
| View | `{schema}.{business_view_name}` | `customer.customer_search` |

---

# 4. Migration Coding Standards

Migration scripts shall:

- Be immutable after merge.
- Use approved version naming from DB-12.
- Avoid environment-specific values unless parameterized.
- Be reviewed before execution.
- Include validation queries when risk is material.
- Avoid destructive production changes without approval.
- Be idempotent only where intentionally repeatable.

---

# 5. DDL Standards

DDL scripts shall:

- Create parent tables before child tables where practical.
- Use `record_id UUID PRIMARY KEY DEFAULT gen_random_uuid()`.
- Include tenant scope columns for tenant-owned tables.
- Include audit fields where applicable.
- Include `metadata JSONB NOT NULL DEFAULT '{}'::jsonb` where flexible extension attributes are required.
- Define constraints close to table definitions where practical.
- Add cross-domain foreign keys after dependent tables exist.

---

# 6. DML Standards

Seed DML shall:

- Use stable natural keys for conflict handling.
- Use `ON CONFLICT DO NOTHING` for idempotent seed data where appropriate.
- Avoid hardcoded production tenant data.
- Avoid personal data in seed scripts.
- Avoid secrets, tokens, passwords, or provider credentials.

---

# 7. Query Standards

Production queries shall:

- Filter tenant-owned data by `organization_id`.
- Use `facility_id` and `site_id` when scope is known.
- Use pagination for list operations.
- Avoid `SELECT *` in application queries.
- Avoid unbounded date ranges for high-volume tables.
- Avoid direct operational table queries for dashboard-heavy reporting where projections exist.

---

# 8. JSONB Standards

JSONB fields shall:

- Store flexible extension attributes only.
- Not replace normalized fields required for relationships, reporting, security, financial calculations, or lifecycle control.
- Not store secrets or raw payment data.
- Be documented when used for business-critical payloads.
- Use GIN indexes only where access patterns justify them.

---

# 9. Trigger and Function Standards

Triggers and functions shall:

- Have clear ownership.
- Be named consistently.
- Avoid hidden business workflow behavior unless explicitly approved.
- Be deterministic where possible.
- Be tested through database test cases.
- Be used for technical concerns such as timestamps, audit protection, and controlled database safeguards.

---

# 10. Review Checklist

| Review Area | Required |
|---|---|
| Naming follows standard | Yes |
| Tenant scope present where required | Yes |
| `record_id` primary key used | Yes |
| Constraints are meaningful | Yes |
| Indexes support access patterns | Yes |
| JSONB usage justified | Yes |
| Migration is reviewable | Yes |
| Seed data is safe | Yes |

---

# 11. Summary

DB-20 defines the SQL coding standard required to keep Digitize PostgreSQL implementation artifacts consistent, readable, and enterprise maintainable.
