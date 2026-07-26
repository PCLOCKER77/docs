# DB-11 Database DDL / DML Scripts

**Document ID:** DB-11  
**Document Name:** Database DDL / DML Scripts  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Database Implementation Script Baseline  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Implementation Draft  
**Business Owner:** Product Architecture  
**Technical Owner:** Data Architecture / Engineering  
**Prepared By:** Data Architecture Team  
**Reviewed By:** Database Review Board  
**Approved By:** Product Architecture / Solution Architecture  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Document State:** Implementation Draft  
**Release:** Foundation Implementation Baseline  
**Dependencies:** DB-00 to DB-10, TA-03, TA-05, TA-06, TA-10, FR-02 to FR-21  
**Supersedes:** Not Applicable  
**Superseded By:** Not Applicable  
**Last Updated:** July 2026  
**Database Review:** Ready for Review

---

# Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 0.1 | July 2026 | Data Architecture Team | Initial PostgreSQL DDL/DML implementation baseline |
| 0.2 | 2026-07-26 | Data Architecture Team | Freeze preparation edits: marked provisional tenancy assumption; utility function completion; standardized review status |

---

# 1. Introduction

## 1.1 Purpose

This document provides the PostgreSQL implementation baseline for creating the Digitize database schemas, tables, columns, relationships, constraints, indexes, and initial seed data.

DB-11 is an implementation artifact derived from the approved database design documents. It does not replace DB-01 through DB-10. DB-01 through DB-10 remain the source of truth for conceptual, logical, physical, tenancy, domain, lifecycle, traceability, and data dictionary decisions.

## 1.2 Objectives

- Provide executable PostgreSQL DDL for the initial Digitize database baseline.
- Provide PostgreSQL DML for initial reference, platform, role, permission, and configuration data.
- Preserve tenant-aware database design with Organization as the tenant root.
- Preserve Facility as the primary commercial subscription and licensing unit.
- Preserve Site as the physical operating location.
- Support relational integrity using primary keys, foreign keys, uniqueness constraints, check constraints, and indexes.
- Support auditability, reporting, support, notification, billing, membership, attendance, and commercial traceability.
- Provide a baseline that can later be split into migration files for deployment pipelines.

## 1.3 Scope

This document covers:

- PostgreSQL extensions.
- PostgreSQL schemas.
- Core platform tables.
- Tenant hierarchy tables.
- Identity and RBAC tables.
- Customer tables.
- Membership tables.
- Attendance and operations tables.
- Trainer, activity, batch, class, and personal training tables.
- Billing, invoice, payment, refund, subscription, license, and entitlement tables.
- Campaign, notification, reporting, support, audit, security, and compliance tables.
- Foreign key relationships.
- Indexes.
- Initial seed DML.

## 1.4 Out of Scope

- Application source code.
- ORM mappings.
- Stored business workflows.
- Database product alternatives.
- Production environment sizing.
- Cloud managed database provisioning.
- CI/CD pipeline scripts.
- Tenant data migration from existing customer systems.

---

# 2. PostgreSQL Implementation Assumptions

| Assumption ID | Assumption | Decision |
|---|---|---|
| DB-11-ASM-001 | Database engine | PostgreSQL |
| DB-11-ASM-002 | Primary key strategy | UUID primary keys using `record_id UUID PRIMARY KEY DEFAULT gen_random_uuid()` |
| DB-11-ASM-003 | Tenant strategy | Shared database, shared schema namespace model with explicit `organization_id` tenant root columns |

-- NOTE: This tenancy assumption is PROVISIONAL and MUST be confirmed by an ADR before migrations are promoted to production. If an alternative tenancy pattern is approved (schema-per-tenant or database-per-tenant), migration artifacts and indexes will require changes. See DB-03 for alignment guidance.
Refer to [ADR-048 Tenancy Model](../99_Decision_Records/ADR-048_Tenancy_Model.md) for the formal tenancy decision proposal and impact analysis. Do not promote migration artifacts until the ADR is approved.
| DB-11-ASM-004 | Configuration payloads | `JSONB` is used for controlled configuration data |
| DB-11-ASM-005 | Monetary values | `NUMERIC(14,2)` is used for business money values |
| DB-11-ASM-006 | Timestamps | `TIMESTAMPTZ` is used for all business timestamps |
| DB-11-ASM-007 | Lifecycle states | Text status columns are used instead of PostgreSQL enum types to preserve configurability |
| DB-11-ASM-008 | Soft deletion | Mutable business tables may use `deleted_at` and `deleted_by`; audit tables remain append-only |
| DB-11-ASM-009 | Files and documents | Tables store metadata only; binary content shall be stored outside the relational database |
| DB-11-ASM-010 | Payment card data | Raw cardholder data shall not be stored in Digitize |
| DB-11-ASM-011 | Metadata fields | Applicable tables shall include `metadata JSONB NOT NULL DEFAULT '{}'::jsonb` for controlled extension attributes |

---

# 3. Execution Order

| Step | Script Area | Purpose |
|---|---|---|
| 1 | Extensions | Enable required PostgreSQL extensions |
| 2 | Schemas | Create logical namespaces |
| 3 | Utility Functions | Create reusable timestamp and append-only trigger functions |
| 4 | Platform and Tenant Foundation | Create platform, organization, facility, and site tables |
| 5 | Identity and Security Foundation | Create user, role, permission, policy, session, and security tables |
| 6 | Operational Domains | Create customer, membership, attendance, walk-in, trainer, activity, batch, and training tables |
| 7 | Commercial Domains | Create pricing, invoice, payment, refund, subscription, license, and entitlement tables |
| 8 | Communication, Reporting, Support, Audit | Create campaign, notification, report, support, audit, compliance, and investigation tables |
| 9 | Metadata Alignment | Add standard `metadata` JSONB columns where required |
| 10 | Indexes | Create tenant, lookup, lifecycle, reporting, and operational indexes |
| 11 | DML Seed Data | Insert initial reference, permission, role, and configuration data |

---

# 4. PostgreSQL Extension and Schema Scripts

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS citext;

CREATE SCHEMA IF NOT EXISTS platform;
CREATE SCHEMA IF NOT EXISTS tenant;
CREATE SCHEMA IF NOT EXISTS identity;
CREATE SCHEMA IF NOT EXISTS customer;
CREATE SCHEMA IF NOT EXISTS membership;
CREATE SCHEMA IF NOT EXISTS operations;
CREATE SCHEMA IF NOT EXISTS training;
CREATE SCHEMA IF NOT EXISTS commercial;
CREATE SCHEMA IF NOT EXISTS communication;
CREATE SCHEMA IF NOT EXISTS reporting;
CREATE SCHEMA IF NOT EXISTS support;
CREATE SCHEMA IF NOT EXISTS audit;
CREATE SCHEMA IF NOT EXISTS security;
CREATE SCHEMA IF NOT EXISTS integration;
```

---

# 5. Utility Function Scripts

```sql
CREATE OR REPLACE FUNCTION platform.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION audit.prevent_audit_mutation()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'Audit and compliance records are append-only and cannot be updated or deleted.';
END;
$$ LANGUAGE plpgsql;
```

---

# 6. Core Platform and Tenant DDL

```sql
CREATE TABLE platform.global_master_data (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    reference_group VARCHAR(100) NOT NULL,
    reference_code VARCHAR(100) NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    display_order INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_global_master_data_group_code UNIQUE (reference_group, reference_code)
);

CREATE TABLE platform.platform_setting (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    setting_key VARCHAR(150) NOT NULL,
    setting_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    setting_type VARCHAR(50) NOT NULL DEFAULT 'CONFIGURATION',
    scope_type VARCHAR(30) NOT NULL DEFAULT 'PLATFORM',
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_platform_setting_key_scope UNIQUE (setting_key, scope_type),
    CONSTRAINT ck_platform_setting_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE platform.feature_flag (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    feature_code VARCHAR(120) NOT NULL,
    feature_name VARCHAR(200) NOT NULL,
    description TEXT,
    scope_type VARCHAR(30) NOT NULL DEFAULT 'PLATFORM',
    scope_id UUID,
    is_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    rollout_percentage INTEGER NOT NULL DEFAULT 0,
    rule_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_feature_flag_scope UNIQUE (feature_code, scope_type, scope_id),
    CONSTRAINT ck_feature_flag_rollout CHECK (rollout_percentage BETWEEN 0 AND 100),
    CONSTRAINT ck_feature_flag_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE platform.maintenance_window (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    window_code VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'SCHEDULED',
    impact_level VARCHAR(40) NOT NULL DEFAULT 'LOW',
    notification_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_maintenance_window_code UNIQUE (window_code),
    CONSTRAINT ck_maintenance_window_dates CHECK (ends_at > starts_at)
);

CREATE TABLE platform.release_record (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    release_code VARCHAR(100) NOT NULL,
    release_name VARCHAR(200) NOT NULL,
    release_version VARCHAR(50) NOT NULL,
    release_status VARCHAR(40) NOT NULL DEFAULT 'PLANNED',
    release_notes TEXT,
    deployed_at TIMESTAMPTZ,
    rollback_reference VARCHAR(200),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_release_record_code UNIQUE (release_code)
);

CREATE TABLE tenant.organization (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_code VARCHAR(100) NOT NULL,
    legal_name VARCHAR(250) NOT NULL,
    display_name VARCHAR(250) NOT NULL,
    business_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    tax_identifier VARCHAR(100),
    primary_email CITEXT,
    primary_phone VARCHAR(50),
    country_code VARCHAR(10),
    timezone VARCHAR(80),
    locale_code VARCHAR(20),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    CONSTRAINT uq_organization_code UNIQUE (organization_code),
    CONSTRAINT uq_organization_legal_name UNIQUE (legal_name)
);

CREATE TABLE tenant.organization_setting (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    setting_key VARCHAR(150) NOT NULL,
    setting_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    setting_type VARCHAR(50) NOT NULL DEFAULT 'CONFIGURATION',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_org_setting_key UNIQUE (organization_id, setting_key),
    CONSTRAINT ck_org_setting_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE tenant.organization_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    policy_code VARCHAR(120) NOT NULL,
    policy_name VARCHAR(200) NOT NULL,
    policy_type VARCHAR(60) NOT NULL,
    policy_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_org_policy_code UNIQUE (organization_id, policy_code),
    CONSTRAINT ck_org_policy_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE tenant.organization_document (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    document_type VARCHAR(80) NOT NULL,
    document_name VARCHAR(250) NOT NULL,
    storage_reference VARCHAR(500) NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    uploaded_by UUID,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE tenant.facility_type (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    facility_type_code VARCHAR(100) NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_facility_type_code UNIQUE (facility_type_code)
);

CREATE TABLE tenant.facility (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_type_id UUID NOT NULL REFERENCES tenant.facility_type(record_id) ON DELETE RESTRICT,
    facility_code VARCHAR(100) NOT NULL,
    facility_name VARCHAR(250) NOT NULL,
    facility_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    subscription_scope_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    timezone VARCHAR(80),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    CONSTRAINT uq_facility_code_org UNIQUE (organization_id, facility_code)
);

CREATE TABLE tenant.facility_setting (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    setting_key VARCHAR(150) NOT NULL,
    setting_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    setting_type VARCHAR(50) NOT NULL DEFAULT 'CONFIGURATION',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_facility_setting_key UNIQUE (facility_id, setting_key)
);

CREATE TABLE tenant.facility_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    policy_code VARCHAR(120) NOT NULL,
    policy_name VARCHAR(200) NOT NULL,
    policy_type VARCHAR(60) NOT NULL,
    policy_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_facility_policy_code UNIQUE (facility_id, policy_code),
    CONSTRAINT ck_facility_policy_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE tenant.site (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_code VARCHAR(100) NOT NULL,
    location_name VARCHAR(250) NOT NULL,
    site_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    address_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    CONSTRAINT uq_site_code_facility UNIQUE (facility_id, site_code)
);

CREATE TABLE tenant.site_setting (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID NOT NULL REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    setting_key VARCHAR(150) NOT NULL,
    setting_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    setting_type VARCHAR(50) NOT NULL DEFAULT 'CONFIGURATION',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_site_setting_key UNIQUE (site_id, setting_key)
);

CREATE TABLE tenant.site_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID NOT NULL REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    policy_code VARCHAR(120) NOT NULL,
    policy_name VARCHAR(200) NOT NULL,
    policy_type VARCHAR(60) NOT NULL,
    policy_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_site_policy_code UNIQUE (site_id, policy_code),
    CONSTRAINT ck_site_policy_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);
```

---

# 7. Identity and Security DDL

```sql
CREATE TABLE identity.user_account (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    login_identifier CITEXT NOT NULL,
    display_name VARCHAR(250) NOT NULL,
    account_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    user_type VARCHAR(60) NOT NULL DEFAULT 'TENANT_USER',
    password_hash TEXT,
    mfa_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    last_login_at TIMESTAMPTZ,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    CONSTRAINT uq_user_account_login UNIQUE (login_identifier)
);

CREATE TABLE identity.staff_profile (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    user_account_id UUID NOT NULL REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    staff_code VARCHAR(100) NOT NULL,
    staff_type VARCHAR(80) NOT NULL,
    employment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    profile_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_staff_profile_code UNIQUE (organization_id, staff_code),
    CONSTRAINT uq_staff_profile_user UNIQUE (user_account_id)
);

CREATE TABLE identity.role (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    role_code VARCHAR(120) NOT NULL,
    role_name VARCHAR(200) NOT NULL,
    role_scope VARCHAR(40) NOT NULL DEFAULT 'ORGANIZATION',
    role_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    is_system_role BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_role_code_scope UNIQUE (organization_id, role_code)
);

CREATE TABLE identity.permission (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permission_code VARCHAR(150) NOT NULL,
    permission_name VARCHAR(250) NOT NULL,
    module_code VARCHAR(100) NOT NULL,
    capability_code VARCHAR(150) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_permission_code UNIQUE (permission_code)
);

CREATE TABLE identity.role_permission (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    role_id UUID NOT NULL REFERENCES identity.role(record_id) ON DELETE CASCADE,
    permission_id UUID NOT NULL REFERENCES identity.permission(record_id) ON DELETE RESTRICT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT uq_role_permission UNIQUE (role_id, permission_id)
);

CREATE TABLE identity.access_scope (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    scope_level VARCHAR(40) NOT NULL,
    scope_name VARCHAR(200) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE identity.role_assignment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    user_account_id UUID NOT NULL REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    role_id UUID NOT NULL REFERENCES identity.role(record_id) ON DELETE RESTRICT,
    access_scope_id UUID REFERENCES identity.access_scope(record_id) ON DELETE RESTRICT,
    assignment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_role_assignment_active UNIQUE (user_account_id, role_id, access_scope_id),
    CONSTRAINT ck_role_assignment_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE identity.user_session (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    user_account_id UUID NOT NULL REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    session_token_hash TEXT NOT NULL,
    session_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    ip_address INET,
    user_agent TEXT,
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMPTZ NOT NULL,
    ended_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_user_session_token UNIQUE (session_token_hash),
    CONSTRAINT ck_user_session_dates CHECK (expires_at > started_at)
);

CREATE TABLE security.security_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    policy_code VARCHAR(120) NOT NULL,
    policy_name VARCHAR(200) NOT NULL,
    policy_type VARCHAR(80) NOT NULL,
    policy_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_security_policy_code UNIQUE (organization_id, policy_code)
);

CREATE TABLE security.password_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    security_policy_id UUID NOT NULL REFERENCES security.security_policy(record_id) ON DELETE CASCADE,
    min_length INTEGER NOT NULL DEFAULT 8,
    require_uppercase BOOLEAN NOT NULL DEFAULT TRUE,
    require_lowercase BOOLEAN NOT NULL DEFAULT TRUE,
    require_number BOOLEAN NOT NULL DEFAULT TRUE,
    require_special_character BOOLEAN NOT NULL DEFAULT TRUE,
    password_expiry_days INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ,
    CONSTRAINT ck_password_policy_min_length CHECK (min_length >= 8)
);

CREATE TABLE security.session_policy (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    security_policy_id UUID NOT NULL REFERENCES security.security_policy(record_id) ON DELETE CASCADE,
    idle_timeout_minutes INTEGER NOT NULL DEFAULT 30,
    max_session_minutes INTEGER NOT NULL DEFAULT 480,
    concurrent_session_limit INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ,
    CONSTRAINT ck_session_policy_timeout CHECK (idle_timeout_minutes > 0 AND max_session_minutes >= idle_timeout_minutes)
);

CREATE TABLE security.authentication_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    user_account_id UUID REFERENCES identity.user_account(record_id) ON DELETE SET NULL,
    event_type VARCHAR(80) NOT NULL,
    event_status VARCHAR(40) NOT NULL,
    ip_address INET,
    user_agent TEXT,
    failure_reason TEXT,
    correlation_id VARCHAR(150),
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE security.security_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    user_account_id UUID REFERENCES identity.user_account(record_id) ON DELETE SET NULL,
    event_type VARCHAR(100) NOT NULL,
    severity VARCHAR(40) NOT NULL DEFAULT 'LOW',
    event_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    event_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    correlation_id VARCHAR(150),
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

---

# 8. Customer, Membership, Attendance, and Training DDL

```sql
CREATE TABLE customer.customer (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_code VARCHAR(100) NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150),
    date_of_birth DATE,
    gender_code VARCHAR(40),
    customer_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    primary_email CITEXT,
    primary_phone VARCHAR(50),
    profile_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    deleted_at TIMESTAMPTZ,
    deleted_by UUID,
    CONSTRAINT uq_customer_code_org UNIQUE (organization_id, customer_code)
);

CREATE TABLE customer.customer_contact (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    contact_type VARCHAR(60) NOT NULL,
    contact_name VARCHAR(200),
    email CITEXT,
    phone VARCHAR(50),
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    is_emergency BOOLEAN NOT NULL DEFAULT FALSE,
    address_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE customer.customer_preference (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    preference_key VARCHAR(120) NOT NULL,
    preference_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_customer_preference_key UNIQUE (customer_id, preference_key)
);

CREATE TABLE customer.customer_consent (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    consent_type VARCHAR(80) NOT NULL,
    consent_status VARCHAR(40) NOT NULL,
    channel_type VARCHAR(40),
    captured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    captured_by UUID,
    source_reference VARCHAR(200),
    consent_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE customer.customer_document (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    document_type VARCHAR(80) NOT NULL,
    document_name VARCHAR(250) NOT NULL,
    storage_reference VARCHAR(500) NOT NULL,
    document_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    uploaded_by UUID,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE customer.customer_history (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    history_type VARCHAR(80) NOT NULL,
    history_summary TEXT NOT NULL,
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE membership.membership_plan (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    plan_code VARCHAR(100) NOT NULL,
    plan_name VARCHAR(250) NOT NULL,
    plan_type VARCHAR(80) NOT NULL,
    plan_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    duration_days INTEGER,
    price_amount NUMERIC(14,2),
    currency_code VARCHAR(10),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_membership_plan_code UNIQUE (facility_id, plan_code),
    CONSTRAINT ck_membership_plan_duration CHECK (duration_days IS NULL OR duration_days > 0),
    CONSTRAINT ck_membership_plan_price CHECK (price_amount IS NULL OR price_amount >= 0)
);

CREATE TABLE membership.membership_plan_rule (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    membership_plan_id UUID NOT NULL REFERENCES membership.membership_plan(record_id) ON DELETE CASCADE,
    rule_code VARCHAR(120) NOT NULL,
    rule_type VARCHAR(80) NOT NULL,
    rule_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_membership_plan_rule_code UNIQUE (membership_plan_id, rule_code)
);

CREATE TABLE membership.customer_membership (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    membership_plan_id UUID NOT NULL REFERENCES membership.membership_plan(record_id) ON DELETE RESTRICT,
    membership_number VARCHAR(120) NOT NULL,
    membership_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ,
    invoice_id UUID,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_customer_membership_number UNIQUE (organization_id, membership_number),
    CONSTRAINT ck_customer_membership_dates CHECK (ends_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE membership.membership_lifecycle_history (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_membership_id UUID NOT NULL REFERENCES membership.customer_membership(record_id) ON DELETE RESTRICT,
    from_status VARCHAR(40),
    to_status VARCHAR(40) NOT NULL,
    transition_reason TEXT,
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    changed_by UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE membership.membership_freeze (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_membership_id UUID NOT NULL REFERENCES membership.customer_membership(record_id) ON DELETE RESTRICT,
    freeze_status VARCHAR(40) NOT NULL DEFAULT 'REQUESTED',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ,
    reason TEXT,
    approved_by UUID,
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_membership_freeze_dates CHECK (ends_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE membership.membership_renewal (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_membership_id UUID NOT NULL REFERENCES membership.customer_membership(record_id) ON DELETE RESTRICT,
    renewal_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    renewal_from TIMESTAMPTZ NOT NULL,
    renewal_to TIMESTAMPTZ,
    invoice_id UUID,
    payment_id UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_membership_renewal_dates CHECK (renewal_to IS NULL OR renewal_to >= renewal_from)
);

CREATE TABLE operations.walkin_visit (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    visit_number VARCHAR(120) NOT NULL,
    visit_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    visit_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    amount_reference UUID,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_walkin_visit_number UNIQUE (organization_id, visit_number)
);

CREATE TABLE operations.attendance (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    membership_id UUID REFERENCES membership.customer_membership(record_id) ON DELETE RESTRICT,
    walkin_visit_id UUID REFERENCES operations.walkin_visit(record_id) ON DELETE RESTRICT,
    attendance_reference VARCHAR(120) NOT NULL,
    attendance_status VARCHAR(40) NOT NULL DEFAULT 'RECORDED',
    source_type VARCHAR(60) NOT NULL,
    check_in_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    check_out_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_attendance_reference UNIQUE (organization_id, attendance_reference),
    CONSTRAINT ck_attendance_checkout CHECK (check_out_at IS NULL OR check_out_at >= check_in_at)
);

CREATE TABLE operations.attendance_eligibility (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    attendance_id UUID NOT NULL REFERENCES operations.attendance(record_id) ON DELETE CASCADE,
    eligibility_status VARCHAR(40) NOT NULL,
    rule_code VARCHAR(120),
    decision_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE operations.entry_exit_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    attendance_id UUID NOT NULL REFERENCES operations.attendance(record_id) ON DELETE CASCADE,
    event_type VARCHAR(40) NOT NULL,
    event_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    recorded_by UUID,
    source_reference VARCHAR(200),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE operations.operational_note (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    note_text TEXT NOT NULL,
    visibility_scope VARCHAR(50) NOT NULL DEFAULT 'INTERNAL',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE operations.operational_attachment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    attachment_name VARCHAR(250) NOT NULL,
    storage_reference VARCHAR(500) NOT NULL,
    attachment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE training.trainer (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    staff_profile_id UUID REFERENCES identity.staff_profile(record_id) ON DELETE RESTRICT,
    trainer_code VARCHAR(100) NOT NULL,
    trainer_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    specialization_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_trainer_code UNIQUE (organization_id, trainer_code)
);

CREATE TABLE training.activity (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    activity_code VARCHAR(100) NOT NULL,
    activity_name VARCHAR(250) NOT NULL,
    activity_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    capacity_limit INTEGER,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_activity_code UNIQUE (facility_id, activity_code),
    CONSTRAINT ck_activity_capacity CHECK (capacity_limit IS NULL OR capacity_limit > 0)
);

CREATE TABLE training.activity_rule (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    activity_id UUID NOT NULL REFERENCES training.activity(record_id) ON DELETE CASCADE,
    rule_code VARCHAR(120) NOT NULL,
    rule_type VARCHAR(80) NOT NULL,
    rule_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_activity_rule_code UNIQUE (activity_id, rule_code)
);

CREATE TABLE training.batch (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    activity_id UUID NOT NULL REFERENCES training.activity(record_id) ON DELETE RESTRICT,
    batch_code VARCHAR(100) NOT NULL,
    batch_name VARCHAR(250) NOT NULL,
    batch_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    capacity_limit INTEGER,
    starts_at TIMESTAMPTZ,
    ends_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_batch_code UNIQUE (facility_id, batch_code),
    CONSTRAINT ck_batch_dates CHECK (ends_at IS NULL OR starts_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE training.class_session (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    batch_id UUID NOT NULL REFERENCES training.batch(record_id) ON DELETE RESTRICT,
    trainer_id UUID REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    session_code VARCHAR(120) NOT NULL,
    session_status VARCHAR(40) NOT NULL DEFAULT 'SCHEDULED',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_class_session_code UNIQUE (organization_id, session_code),
    CONSTRAINT ck_class_session_dates CHECK (ends_at > starts_at)
);

CREATE TABLE training.batch_enrollment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    batch_id UUID NOT NULL REFERENCES training.batch(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    enrollment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    enrolled_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_batch_customer_enrollment UNIQUE (batch_id, customer_id)
);

CREATE TABLE training.trainer_assignment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    trainer_id UUID NOT NULL REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    batch_id UUID REFERENCES training.batch(record_id) ON DELETE RESTRICT,
    assignment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_trainer_assignment_dates CHECK (expires_at IS NULL OR effective_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE training.trainer_availability (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    trainer_id UUID NOT NULL REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    availability_status VARCHAR(40) NOT NULL DEFAULT 'AVAILABLE',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_trainer_availability_dates CHECK (ends_at > starts_at)
);

CREATE TABLE training.trainer_schedule (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    trainer_id UUID NOT NULL REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    schedule_status VARCHAR(40) NOT NULL DEFAULT 'SCHEDULED',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_trainer_schedule_dates CHECK (ends_at > starts_at)
);

CREATE TABLE training.personal_training_package (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    package_code VARCHAR(120) NOT NULL,
    package_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    total_sessions INTEGER NOT NULL,
    consumed_sessions INTEGER NOT NULL DEFAULT 0,
    commercial_reference_id UUID,
    starts_at TIMESTAMPTZ,
    ends_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_training_package_code UNIQUE (organization_id, package_code),
    CONSTRAINT ck_training_package_sessions CHECK (total_sessions > 0 AND consumed_sessions >= 0 AND consumed_sessions <= total_sessions)
);

CREATE TABLE training.personal_training_session (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    package_id UUID REFERENCES training.personal_training_package(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    trainer_id UUID NOT NULL REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    session_status VARCHAR(40) NOT NULL DEFAULT 'SCHEDULED',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_personal_training_session_dates CHECK (ends_at > starts_at)
);

CREATE TABLE training.training_note (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    trainer_id UUID REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    session_id UUID REFERENCES training.personal_training_session(record_id) ON DELETE RESTRICT,
    note_text TEXT NOT NULL,
    visibility_scope VARCHAR(50) NOT NULL DEFAULT 'RESTRICTED',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE training.customer_progress (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID NOT NULL REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    trainer_id UUID REFERENCES training.trainer(record_id) ON DELETE RESTRICT,
    progress_type VARCHAR(80) NOT NULL,
    progress_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);
```

---

# 9. Commercial, Billing, Subscription, and License DDL

```sql
CREATE TABLE commercial.pricing (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    pricing_code VARCHAR(120) NOT NULL,
    pricing_name VARCHAR(250) NOT NULL,
    pricing_type VARCHAR(80) NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_pricing_code UNIQUE (organization_id, facility_id, pricing_code)
);

CREATE TABLE commercial.price_version (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pricing_id UUID NOT NULL REFERENCES commercial.pricing(record_id) ON DELETE RESTRICT,
    amount NUMERIC(14,2) NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    effective_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT ck_price_version_amount CHECK (amount >= 0),
    CONSTRAINT ck_price_version_dates CHECK (expires_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE commercial.discount (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    discount_code VARCHAR(120) NOT NULL,
    discount_name VARCHAR(250) NOT NULL,
    discount_type VARCHAR(80) NOT NULL,
    discount_value NUMERIC(14,2) NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_discount_code UNIQUE (organization_id, discount_code),
    CONSTRAINT ck_discount_value CHECK (discount_value >= 0)
);

CREATE TABLE commercial.promotion (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    promotion_code VARCHAR(120) NOT NULL,
    promotion_name VARCHAR(250) NOT NULL,
    promotion_status VARCHAR(40) NOT NULL DEFAULT 'DRAFT',
    promotion_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_promotion_code UNIQUE (organization_id, promotion_code)
);

CREATE TABLE commercial.tax (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    tax_code VARCHAR(120) NOT NULL,
    tax_name VARCHAR(250) NOT NULL,
    tax_rate NUMERIC(8,4) NOT NULL,
    tax_type VARCHAR(80) NOT NULL,
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_tax_code UNIQUE (organization_id, tax_code),
    CONSTRAINT ck_tax_rate CHECK (tax_rate >= 0)
);

CREATE TABLE commercial.billing_account (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    billing_account_number VARCHAR(120) NOT NULL,
    billing_name VARCHAR(250) NOT NULL,
    billing_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    billing_address_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_billing_account_number UNIQUE (organization_id, billing_account_number)
);

CREATE TABLE commercial.invoice (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    billing_account_id UUID NOT NULL REFERENCES commercial.billing_account(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    invoice_number VARCHAR(120) NOT NULL,
    invoice_status VARCHAR(40) NOT NULL DEFAULT 'DRAFT',
    invoice_date DATE NOT NULL,
    due_date DATE,
    subtotal_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    discount_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    tax_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    total_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    currency_code VARCHAR(10) NOT NULL,
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_invoice_number UNIQUE (organization_id, invoice_number),
    CONSTRAINT ck_invoice_amounts CHECK (subtotal_amount >= 0 AND discount_amount >= 0 AND tax_amount >= 0 AND total_amount >= 0)
);

CREATE TABLE commercial.invoice_item (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    invoice_id UUID NOT NULL REFERENCES commercial.invoice(record_id) ON DELETE CASCADE,
    item_sequence INTEGER NOT NULL,
    item_type VARCHAR(80) NOT NULL,
    item_description TEXT NOT NULL,
    quantity NUMERIC(12,2) NOT NULL DEFAULT 1,
    unit_amount NUMERIC(14,2) NOT NULL,
    discount_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    tax_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    line_total_amount NUMERIC(14,2) NOT NULL,
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT uq_invoice_item_sequence UNIQUE (invoice_id, item_sequence),
    CONSTRAINT ck_invoice_item_amounts CHECK (quantity > 0 AND unit_amount >= 0 AND discount_amount >= 0 AND tax_amount >= 0 AND line_total_amount >= 0)
);

CREATE TABLE commercial.billing_adjustment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    invoice_id UUID REFERENCES commercial.invoice(record_id) ON DELETE RESTRICT,
    adjustment_type VARCHAR(80) NOT NULL,
    adjustment_amount NUMERIC(14,2) NOT NULL,
    adjustment_reason TEXT NOT NULL,
    adjustment_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    approved_by UUID,
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT ck_billing_adjustment_amount CHECK (adjustment_amount <> 0)
);

CREATE TABLE commercial.payment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    invoice_id UUID REFERENCES commercial.invoice(record_id) ON DELETE RESTRICT,
    billing_account_id UUID REFERENCES commercial.billing_account(record_id) ON DELETE RESTRICT,
    payment_number VARCHAR(120) NOT NULL,
    payment_status VARCHAR(40) NOT NULL DEFAULT 'INITIATED',
    payment_method VARCHAR(80),
    amount NUMERIC(14,2) NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    provider_code VARCHAR(100),
    provider_reference VARCHAR(250),
    paid_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_payment_number UNIQUE (organization_id, payment_number),
    CONSTRAINT ck_payment_amount CHECK (amount >= 0)
);

CREATE TABLE commercial.payment_attempt (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    payment_id UUID NOT NULL REFERENCES commercial.payment(record_id) ON DELETE RESTRICT,
    provider_code VARCHAR(100) NOT NULL,
    provider_reference VARCHAR(250),
    idempotency_key VARCHAR(250) NOT NULL,
    attempt_status VARCHAR(40) NOT NULL DEFAULT 'INITIATED',
    request_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    response_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    attempted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_payment_attempt_idempotency UNIQUE (organization_id, provider_code, idempotency_key)
);

CREATE TABLE commercial.payment_method_reference (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    billing_account_id UUID REFERENCES commercial.billing_account(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    provider_code VARCHAR(100) NOT NULL,
    provider_customer_reference VARCHAR(250),
    provider_payment_method_reference VARCHAR(250) NOT NULL,
    method_type VARCHAR(80),
    masked_display VARCHAR(100),
    status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_payment_method_reference UNIQUE (organization_id, provider_code, provider_payment_method_reference)
);

CREATE TABLE commercial.receipt (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    payment_id UUID NOT NULL REFERENCES commercial.payment(record_id) ON DELETE RESTRICT,
    receipt_number VARCHAR(120) NOT NULL,
    receipt_status VARCHAR(40) NOT NULL DEFAULT 'ISSUED',
    issued_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT uq_receipt_number UNIQUE (organization_id, receipt_number)
);

CREATE TABLE commercial.refund (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    payment_id UUID NOT NULL REFERENCES commercial.payment(record_id) ON DELETE RESTRICT,
    refund_number VARCHAR(120) NOT NULL,
    refund_status VARCHAR(40) NOT NULL DEFAULT 'REQUESTED',
    amount NUMERIC(14,2) NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    reason TEXT,
    provider_reference VARCHAR(250),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_refund_number UNIQUE (organization_id, refund_number),
    CONSTRAINT ck_refund_amount CHECK (amount > 0)
);

CREATE TABLE commercial.refund_attempt (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    refund_id UUID NOT NULL REFERENCES commercial.refund(record_id) ON DELETE RESTRICT,
    provider_code VARCHAR(100) NOT NULL,
    provider_reference VARCHAR(250),
    idempotency_key VARCHAR(250) NOT NULL,
    attempt_status VARCHAR(40) NOT NULL DEFAULT 'INITIATED',
    request_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    response_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    attempted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_refund_attempt_idempotency UNIQUE (organization_id, provider_code, idempotency_key)
);

CREATE TABLE commercial.settlement (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    provider_code VARCHAR(100) NOT NULL,
    settlement_reference VARCHAR(250) NOT NULL,
    settlement_status VARCHAR(40) NOT NULL DEFAULT 'RECEIVED',
    gross_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    fee_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    net_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    currency_code VARCHAR(10) NOT NULL,
    settled_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT uq_settlement_reference UNIQUE (provider_code, settlement_reference)
);

CREATE TABLE commercial.reconciliation (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    payment_id UUID REFERENCES commercial.payment(record_id) ON DELETE RESTRICT,
    settlement_id UUID REFERENCES commercial.settlement(record_id) ON DELETE RESTRICT,
    reconciliation_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    internal_reference VARCHAR(250),
    provider_reference VARCHAR(250),
    variance_amount NUMERIC(14,2) NOT NULL DEFAULT 0,
    reconciled_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE commercial.subscription_plan (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    plan_code VARCHAR(120) NOT NULL,
    plan_name VARCHAR(250) NOT NULL,
    plan_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    plan_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    base_price_amount NUMERIC(14,2),
    currency_code VARCHAR(10),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_subscription_plan_code UNIQUE (plan_code)
);

CREATE TABLE commercial.subscription (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    subscription_plan_id UUID NOT NULL REFERENCES commercial.subscription_plan(record_id) ON DELETE RESTRICT,
    subscription_number VARCHAR(120) NOT NULL,
    subscription_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_subscription_number UNIQUE (organization_id, subscription_number),
    CONSTRAINT ck_subscription_dates CHECK (ends_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE commercial.subscription_term (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    subscription_id UUID NOT NULL REFERENCES commercial.subscription(record_id) ON DELETE RESTRICT,
    term_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ,
    invoice_id UUID REFERENCES commercial.invoice(record_id) ON DELETE RESTRICT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    CONSTRAINT ck_subscription_term_dates CHECK (ends_at IS NULL OR ends_at >= starts_at)
);

CREATE TABLE commercial.subscription_lifecycle_history (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    subscription_id UUID NOT NULL REFERENCES commercial.subscription(record_id) ON DELETE RESTRICT,
    from_status VARCHAR(40),
    to_status VARCHAR(40) NOT NULL,
    transition_reason TEXT,
    changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    changed_by UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE commercial.license (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    subscription_id UUID REFERENCES commercial.subscription(record_id) ON DELETE RESTRICT,
    license_number VARCHAR(120) NOT NULL,
    license_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_license_number UNIQUE (organization_id, license_number),
    CONSTRAINT ck_license_dates CHECK (expires_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE commercial.license_assignment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    license_id UUID NOT NULL REFERENCES commercial.license(record_id) ON DELETE RESTRICT,
    assignment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_license_assignment UNIQUE (facility_id, license_id, effective_at),
    CONSTRAINT ck_license_assignment_dates CHECK (expires_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE commercial.license_capability (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    capability_code VARCHAR(150) NOT NULL,
    capability_name VARCHAR(250) NOT NULL,
    module_code VARCHAR(100) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_license_capability_code UNIQUE (capability_code)
);

CREATE TABLE commercial.entitlement (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    license_id UUID NOT NULL REFERENCES commercial.license(record_id) ON DELETE RESTRICT,
    capability_id UUID NOT NULL REFERENCES commercial.license_capability(record_id) ON DELETE RESTRICT,
    entitlement_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    effective_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_entitlement_capability UNIQUE (facility_id, license_id, capability_id),
    CONSTRAINT ck_entitlement_dates CHECK (expires_at IS NULL OR expires_at >= effective_at)
);

CREATE TABLE commercial.feature_access (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID NOT NULL REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    capability_id UUID NOT NULL REFERENCES commercial.license_capability(record_id) ON DELETE RESTRICT,
    access_status VARCHAR(40) NOT NULL DEFAULT 'ENABLED',
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    effective_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ,
    CONSTRAINT uq_feature_access_capability UNIQUE (facility_id, capability_id, source_entity_type, source_entity_id)
);

CREATE TABLE commercial.commercial_audit_history (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    action_type VARCHAR(100) NOT NULL,
    action_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

ALTER TABLE membership.customer_membership
ADD CONSTRAINT fk_customer_membership_invoice
FOREIGN KEY (invoice_id) REFERENCES commercial.invoice(record_id) ON DELETE RESTRICT;

ALTER TABLE membership.membership_renewal
ADD CONSTRAINT fk_membership_renewal_invoice
FOREIGN KEY (invoice_id) REFERENCES commercial.invoice(record_id) ON DELETE RESTRICT;

ALTER TABLE membership.membership_renewal
ADD CONSTRAINT fk_membership_renewal_payment
FOREIGN KEY (payment_id) REFERENCES commercial.payment(record_id) ON DELETE RESTRICT;

-- Additional safe referential integrity: link common audit actor columns to identity.user_account
-- Use ON DELETE SET NULL to avoid accidental cascading deletes.
ALTER TABLE tenant.organization
ADD CONSTRAINT fk_organization_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE tenant.organization
ADD CONSTRAINT fk_organization_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE identity.user_account
ADD CONSTRAINT fk_user_account_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE identity.user_account
ADD CONSTRAINT fk_user_account_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE customer.customer
ADD CONSTRAINT fk_customer_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE customer.customer
ADD CONSTRAINT fk_customer_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE membership.customer_membership
ADD CONSTRAINT fk_customer_membership_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE membership.customer_membership
ADD CONSTRAINT fk_customer_membership_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE operations.attendance
ADD CONSTRAINT fk_attendance_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE operations.attendance
ADD CONSTRAINT fk_attendance_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE commercial.invoice
ADD CONSTRAINT fk_invoice_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE commercial.invoice
ADD CONSTRAINT fk_invoice_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;

ALTER TABLE commercial.payment
ADD CONSTRAINT fk_payment_created_by_user FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
ALTER TABLE commercial.payment
ADD CONSTRAINT fk_payment_updated_by_user FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;
```

---

# 10. Communication, Reporting, Support, Audit, and Compliance DDL

```sql
CREATE TABLE communication.advertisement_campaign (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    campaign_code VARCHAR(120) NOT NULL,
    campaign_name VARCHAR(250) NOT NULL,
    campaign_status VARCHAR(40) NOT NULL DEFAULT 'DRAFT',
    campaign_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    starts_at TIMESTAMPTZ,
    ends_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_campaign_code UNIQUE (organization_id, campaign_code)
);

CREATE TABLE communication.campaign_audience (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    campaign_id UUID NOT NULL REFERENCES communication.advertisement_campaign(record_id) ON DELETE CASCADE,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    audience_rule_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    audience_status VARCHAR(40) NOT NULL DEFAULT 'SELECTED',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE communication.campaign_schedule (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    campaign_id UUID NOT NULL REFERENCES communication.advertisement_campaign(record_id) ON DELETE CASCADE,
    schedule_status VARCHAR(40) NOT NULL DEFAULT 'SCHEDULED',
    scheduled_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE communication.campaign_delivery (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    campaign_id UUID NOT NULL REFERENCES communication.advertisement_campaign(record_id) ON DELETE CASCADE,
    delivery_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    channel_type VARCHAR(40) NOT NULL,
    provider_code VARCHAR(100),
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE communication.campaign_result (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    campaign_id UUID NOT NULL REFERENCES communication.advertisement_campaign(record_id) ON DELETE CASCADE,
    metric_code VARCHAR(120) NOT NULL,
    metric_value NUMERIC(18,4) NOT NULL DEFAULT 0,
    measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE communication.notification_template (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    template_code VARCHAR(120) NOT NULL,
    template_name VARCHAR(250) NOT NULL,
    channel_type VARCHAR(40) NOT NULL,
    subject_template TEXT,
    body_template TEXT NOT NULL,
    template_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_notification_template_code UNIQUE (organization_id, template_code, channel_type)
);

CREATE TABLE communication.notification_preference (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    user_account_id UUID REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    channel_type VARCHAR(40) NOT NULL,
    preference_status VARCHAR(40) NOT NULL DEFAULT 'ENABLED',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_notification_preference UNIQUE (organization_id, customer_id, user_account_id, channel_type)
);

CREATE TABLE communication.communication_consent (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    channel_type VARCHAR(40) NOT NULL,
    consent_status VARCHAR(40) NOT NULL,
    captured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    captured_by UUID,
    source_reference VARCHAR(250),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE communication.notification (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    template_id UUID REFERENCES communication.notification_template(record_id) ON DELETE RESTRICT,
    notification_type VARCHAR(80) NOT NULL,
    notification_status VARCHAR(40) NOT NULL DEFAULT 'CREATED',
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    correlation_id VARCHAR(150),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE communication.notification_recipient (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    notification_id UUID NOT NULL REFERENCES communication.notification(record_id) ON DELETE CASCADE,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    user_account_id UUID REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    recipient_address VARCHAR(300),
    recipient_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE communication.notification_delivery (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    notification_recipient_id UUID NOT NULL REFERENCES communication.notification_recipient(record_id) ON DELETE CASCADE,
    channel_type VARCHAR(40) NOT NULL,
    provider_code VARCHAR(100),
    provider_reference VARCHAR(250),
    delivery_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    delivered_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ
);

CREATE TABLE communication.notification_attempt (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    notification_delivery_id UUID NOT NULL REFERENCES communication.notification_delivery(record_id) ON DELETE CASCADE,
    attempt_number INTEGER NOT NULL DEFAULT 1,
    attempt_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    provider_response JSONB NOT NULL DEFAULT '{}'::jsonb,
    attempted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE communication.notification_failure (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    notification_delivery_id UUID NOT NULL REFERENCES communication.notification_delivery(record_id) ON DELETE CASCADE,
    failure_code VARCHAR(120),
    failure_message TEXT,
    failure_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE reporting.report_definition (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    report_code VARCHAR(120) NOT NULL,
    report_name VARCHAR(250) NOT NULL,
    report_domain VARCHAR(100) NOT NULL,
    report_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    definition_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_report_definition_code UNIQUE (organization_id, report_code)
);

CREATE TABLE reporting.report_parameter (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_definition_id UUID NOT NULL REFERENCES reporting.report_definition(record_id) ON DELETE CASCADE,
    parameter_code VARCHAR(120) NOT NULL,
    parameter_name VARCHAR(250) NOT NULL,
    parameter_type VARCHAR(80) NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT FALSE,
    default_value JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_report_parameter_code UNIQUE (report_definition_id, parameter_code)
);

CREATE TABLE reporting.report_schedule (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    report_definition_id UUID NOT NULL REFERENCES reporting.report_definition(record_id) ON DELETE CASCADE,
    schedule_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    schedule_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    next_run_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE reporting.report_execution (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    report_definition_id UUID NOT NULL REFERENCES reporting.report_definition(record_id) ON DELETE RESTRICT,
    execution_status VARCHAR(40) NOT NULL DEFAULT 'QUEUED',
    parameter_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    row_count INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE reporting.report_export (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    report_execution_id UUID NOT NULL REFERENCES reporting.report_execution(record_id) ON DELETE RESTRICT,
    export_format VARCHAR(40) NOT NULL,
    export_status VARCHAR(40) NOT NULL DEFAULT 'CREATED',
    storage_reference VARCHAR(500),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE reporting.dashboard_configuration (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    user_account_id UUID REFERENCES identity.user_account(record_id) ON DELETE RESTRICT,
    dashboard_code VARCHAR(120) NOT NULL,
    dashboard_name VARCHAR(250) NOT NULL,
    configuration_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE reporting.kpi_definition (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    kpi_code VARCHAR(120) NOT NULL,
    kpi_name VARCHAR(250) NOT NULL,
    kpi_domain VARCHAR(100) NOT NULL,
    definition_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_kpi_definition_code UNIQUE (organization_id, kpi_code)
);

CREATE TABLE reporting.kpi_snapshot (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    kpi_definition_id UUID NOT NULL REFERENCES reporting.kpi_definition(record_id) ON DELETE RESTRICT,
    scope_type VARCHAR(40) NOT NULL,
    scope_id UUID,
    kpi_value NUMERIC(18,4) NOT NULL,
    measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE reporting.reporting_projection (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    projection_code VARCHAR(150) NOT NULL,
    source_entity_type VARCHAR(100) NOT NULL,
    source_entity_id UUID NOT NULL,
    projection_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    refreshed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE reporting.analytical_aggregate (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    aggregate_code VARCHAR(150) NOT NULL,
    aggregate_scope VARCHAR(100) NOT NULL,
    aggregate_value NUMERIC(18,4) NOT NULL DEFAULT 0,
    measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE reporting.historical_snapshot (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    snapshot_code VARCHAR(150) NOT NULL,
    snapshot_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    snapshot_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE support.ticket_category (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    category_code VARCHAR(120) NOT NULL,
    category_name VARCHAR(250) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_ticket_category_code UNIQUE (organization_id, category_code)
);

CREATE TABLE support.ticket_priority (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    priority_code VARCHAR(120) NOT NULL,
    priority_name VARCHAR(250) NOT NULL,
    sla_minutes INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_ticket_priority_code UNIQUE (organization_id, priority_code)
);

CREATE TABLE support.support_ticket (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    customer_id UUID REFERENCES customer.customer(record_id) ON DELETE RESTRICT,
    created_by_user_id UUID REFERENCES identity.user_account(record_id) ON DELETE SET NULL,
    category_id UUID REFERENCES support.ticket_category(record_id) ON DELETE RESTRICT,
    priority_id UUID REFERENCES support.ticket_priority(record_id) ON DELETE RESTRICT,
    ticket_number VARCHAR(120) NOT NULL,
    ticket_subject VARCHAR(300) NOT NULL,
    ticket_description TEXT,
    ticket_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    severity VARCHAR(40) NOT NULL DEFAULT 'MEDIUM',
    source_entity_type VARCHAR(100),
    source_entity_id UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT uq_support_ticket_number UNIQUE (organization_id, ticket_number)
);

CREATE TABLE support.ticket_assignment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    support_ticket_id UUID NOT NULL REFERENCES support.support_ticket(record_id) ON DELETE CASCADE,
    assigned_to_user_id UUID REFERENCES identity.user_account(record_id) ON DELETE SET NULL,
    assignment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    assigned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    assigned_by UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE support.ticket_comment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    support_ticket_id UUID NOT NULL REFERENCES support.support_ticket(record_id) ON DELETE CASCADE,
    comment_text TEXT NOT NULL,
    visibility_scope VARCHAR(40) NOT NULL DEFAULT 'INTERNAL',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID
);

CREATE TABLE support.ticket_attachment (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    support_ticket_id UUID NOT NULL REFERENCES support.support_ticket(record_id) ON DELETE CASCADE,
    attachment_name VARCHAR(250) NOT NULL,
    storage_reference VARCHAR(500) NOT NULL,
    attachment_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE support.ticket_escalation (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    support_ticket_id UUID NOT NULL REFERENCES support.support_ticket(record_id) ON DELETE CASCADE,
    escalation_reason TEXT NOT NULL,
    escalation_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    escalated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    escalated_by UUID,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE support.sla_tracking (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    support_ticket_id UUID NOT NULL REFERENCES support.support_ticket(record_id) ON DELETE CASCADE,
    sla_status VARCHAR(40) NOT NULL DEFAULT 'ACTIVE',
    response_due_at TIMESTAMPTZ,
    resolution_due_at TIMESTAMPTZ,
    responded_at TIMESTAMPTZ,
    resolved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ
);

CREATE TABLE audit.audit_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    actor_id UUID,
    action VARCHAR(150) NOT NULL,
    entity_type VARCHAR(120) NOT NULL,
    entity_id UUID,
    event_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    ip_address INET,
    user_agent TEXT,
    correlation_id VARCHAR(150),
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE audit.audit_entity_reference (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    audit_event_id UUID NOT NULL REFERENCES audit.audit_event(record_id) ON DELETE CASCADE,
    entity_type VARCHAR(120) NOT NULL,
    entity_id UUID NOT NULL,
    relationship_type VARCHAR(80),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE audit.compliance_record (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    compliance_code VARCHAR(120) NOT NULL,
    compliance_type VARCHAR(100) NOT NULL,
    compliance_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    evidence_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE audit.data_export_record (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    export_scope JSONB NOT NULL DEFAULT '{}'::jsonb,
    export_status VARCHAR(40) NOT NULL DEFAULT 'REQUESTED',
    requested_by UUID NOT NULL,
    requested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    storage_reference VARCHAR(500),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE audit.investigation_record (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    investigation_number VARCHAR(120) NOT NULL,
    investigation_type VARCHAR(100) NOT NULL,
    investigation_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    summary TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_at TIMESTAMPTZ,
    updated_by UUID,
    CONSTRAINT uq_investigation_number UNIQUE (organization_id, investigation_number)
);

CREATE TABLE audit.security_investigation (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    security_event_id UUID REFERENCES security.security_event(record_id) ON DELETE RESTRICT,
    investigation_record_id UUID REFERENCES audit.investigation_record(record_id) ON DELETE RESTRICT,
    investigation_status VARCHAR(40) NOT NULL DEFAULT 'OPEN',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE audit.administrative_access_record (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    actor_id UUID NOT NULL,
    access_reason TEXT NOT NULL,
    access_scope JSONB NOT NULL DEFAULT '{}'::jsonb,
    accessed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    correlation_id VARCHAR(150),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

---

# 10.1 Integration Outbox and Inbox DDL

The integration schema stores durable asynchronous integration records.

PostgreSQL is the source of truth for outbox publication state. Queue, worker, broker, and provider systems may process these records, but they shall not replace the durable outbox state.

```sql
CREATE TABLE integration.outbox_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    facility_id UUID REFERENCES tenant.facility(record_id) ON DELETE RESTRICT,
    site_id UUID REFERENCES tenant.site(record_id) ON DELETE RESTRICT,
    source_module VARCHAR(80) NOT NULL,
    aggregate_type VARCHAR(120) NOT NULL,
    aggregate_id UUID,
    event_type VARCHAR(160) NOT NULL,
    event_version INTEGER NOT NULL DEFAULT 1,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    headers JSONB NOT NULL DEFAULT '{}'::jsonb,
    publication_status VARCHAR(40) NOT NULL DEFAULT 'PENDING',
    retry_count INTEGER NOT NULL DEFAULT 0,
    max_retry_count INTEGER NOT NULL DEFAULT 5,
    next_attempt_at TIMESTAMPTZ,
    locked_at TIMESTAMPTZ,
    locked_by VARCHAR(150),
    published_at TIMESTAMPTZ,
    failed_at TIMESTAMPTZ,
    failure_code VARCHAR(120),
    failure_message TEXT,
    correlation_id VARCHAR(150),
    request_id VARCHAR(150),
    idempotency_key VARCHAR(200),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID,
    updated_by UUID,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    CONSTRAINT chk_outbox_retry_count_non_negative CHECK (retry_count >= 0),
    CONSTRAINT chk_outbox_max_retry_count_non_negative CHECK (max_retry_count >= 0),
    CONSTRAINT chk_outbox_status CHECK (publication_status IN ('PENDING', 'CLAIMED', 'PUBLISHED', 'FAILED', 'DEAD_LETTER', 'CANCELLED'))
);

CREATE INDEX idx_outbox_event_status_next_attempt
    ON integration.outbox_event (publication_status, next_attempt_at, created_at);

CREATE INDEX idx_outbox_event_tenant_status
    ON integration.outbox_event (organization_id, facility_id, site_id, publication_status);

CREATE INDEX idx_outbox_event_type_created
    ON integration.outbox_event (event_type, created_at);

CREATE INDEX idx_outbox_event_correlation
    ON integration.outbox_event (correlation_id);

CREATE UNIQUE INDEX uq_outbox_event_idempotency
    ON integration.outbox_event (idempotency_key)
    WHERE idempotency_key IS NOT NULL;

CREATE TRIGGER trg_outbox_event_updated_at
BEFORE UPDATE ON integration.outbox_event
FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();

CREATE TABLE integration.inbox_event (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES tenant.organization(record_id) ON DELETE RESTRICT,
    provider_name VARCHAR(120),
    external_event_id VARCHAR(200),
    event_type VARCHAR(160) NOT NULL,
    received_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    received_headers JSONB NOT NULL DEFAULT '{}'::jsonb,
    processing_status VARCHAR(40) NOT NULL DEFAULT 'RECEIVED',
    retry_count INTEGER NOT NULL DEFAULT 0,
    processed_at TIMESTAMPTZ,
    failed_at TIMESTAMPTZ,
    failure_code VARCHAR(120),
    failure_message TEXT,
    correlation_id VARCHAR(150),
    request_id VARCHAR(150),
    idempotency_key VARCHAR(200),
    received_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    CONSTRAINT chk_inbox_retry_count_non_negative CHECK (retry_count >= 0),
    CONSTRAINT chk_inbox_status CHECK (processing_status IN ('RECEIVED', 'VALIDATED', 'PROCESSING', 'PROCESSED', 'FAILED', 'IGNORED', 'DEAD_LETTER'))
);

CREATE INDEX idx_inbox_event_status_received
    ON integration.inbox_event (processing_status, received_at);

CREATE INDEX idx_inbox_event_provider_external
    ON integration.inbox_event (provider_name, external_event_id);

CREATE INDEX idx_inbox_event_correlation
    ON integration.inbox_event (correlation_id);

CREATE UNIQUE INDEX uq_inbox_event_idempotency
    ON integration.inbox_event (idempotency_key)
    WHERE idempotency_key IS NOT NULL;

CREATE TRIGGER trg_inbox_event_updated_at
BEFORE UPDATE ON integration.inbox_event
FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
```

---

# 10.2 Metadata JSONB Column Alignment Scripts

The following scripts ensure applicable tables include a standard `metadata` column for controlled extension attributes, integration hints, non-authoritative contextual data, operational annotations, and future-proofing requirements.

The `metadata` column shall not be used to bypass normalized columns, required relationships, lifecycle states, financial values, tenant identifiers, security controls, audit evidence, or approved business rules.

```sql
ALTER TABLE platform.platform_setting ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE platform.feature_flag ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE platform.maintenance_window ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.organization_setting ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.organization_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.facility_setting ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.facility_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.site_setting ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE tenant.site_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.staff_profile ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.role ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.permission ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.role_permission ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.access_scope ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.role_assignment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE identity.user_session ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE security.security_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE security.password_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE security.session_policy ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE security.authentication_event ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE security.security_event ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE customer.customer ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE customer.customer_contact ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE customer.customer_preference ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE customer.customer_consent ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE customer.customer_history ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE membership.membership_plan_rule ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE membership.membership_lifecycle_history ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE membership.membership_freeze ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE membership.membership_renewal ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.walkin_visit ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.attendance ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.attendance_eligibility ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.entry_exit_event ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.operational_note ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE operations.operational_attachment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.trainer ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.activity_rule ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.batch ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.class_session ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.batch_enrollment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.trainer_assignment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.trainer_availability ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.trainer_schedule ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.personal_training_package ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.personal_training_session ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.training_note ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE training.customer_progress ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.pricing ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.price_version ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.discount ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.promotion ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.tax ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.billing_account ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.invoice ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.invoice_item ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.billing_adjustment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.payment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.payment_attempt ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.payment_method_reference ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.receipt ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.refund ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.refund_attempt ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.settlement ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.reconciliation ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.subscription_plan ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.subscription ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.subscription_term ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.subscription_lifecycle_history ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.license ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.license_assignment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.license_capability ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.entitlement ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.feature_access ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE commercial.commercial_audit_history ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.advertisement_campaign ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.campaign_audience ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.campaign_schedule ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.campaign_delivery ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.campaign_result ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_template ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_preference ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.communication_consent ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_recipient ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_delivery ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_attempt ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE communication.notification_failure ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.report_definition ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.report_parameter ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.report_schedule ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.report_execution ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.report_export ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.dashboard_configuration ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.kpi_definition ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.kpi_snapshot ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.reporting_projection ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.analytical_aggregate ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE reporting.historical_snapshot ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_category ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_priority ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.support_ticket ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_assignment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_comment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_attachment ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.ticket_escalation ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE support.sla_tracking ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.audit_event ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.audit_entity_reference ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.compliance_record ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.data_export_record ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.investigation_record ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.security_investigation ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE audit.administrative_access_record ADD COLUMN IF NOT EXISTS metadata JSONB NOT NULL DEFAULT '{}'::jsonb;

-- 10.3 Provenance Columns (created_by / updated_by)
-- Add nullable provenance columns to all relevant tenant and platform tables and establish
-- safe FK links to `identity.user_account(record_id)` using ON DELETE SET NULL. This block
-- uses dynamic SQL to avoid needing to update every CREATE TABLE statement in-place.

DO $$
DECLARE
    r RECORD;
    fkname TEXT;
BEGIN
    FOR r IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema IN (
            'platform','tenant','identity','customer','membership','operations','training',
            'commercial','communication','reporting','support','audit','security','integration'
        )
        AND table_type='BASE TABLE'
    LOOP
        EXECUTE format('ALTER TABLE %I.%I ADD COLUMN IF NOT EXISTS created_by UUID;', r.table_schema, r.table_name);
        EXECUTE format('ALTER TABLE %I.%I ADD COLUMN IF NOT EXISTS updated_by UUID;', r.table_schema, r.table_name);

        fkname := format('fk_%s_%s_created_by_user', r.table_schema, r.table_name);
        IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = fkname) THEN
            EXECUTE format('ALTER TABLE %I.%I ADD CONSTRAINT %I FOREIGN KEY (created_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;', r.table_schema, r.table_name, fkname);
        END IF;

        fkname := format('fk_%s_%s_updated_by_user', r.table_schema, r.table_name);
        IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = fkname) THEN
            EXECUTE format('ALTER TABLE %I.%I ADD CONSTRAINT %I FOREIGN KEY (updated_by) REFERENCES identity.user_account(record_id) ON DELETE SET NULL;', r.table_schema, r.table_name, fkname);
        END IF;
    END LOOP;
END$$;
```

---

# 11. Audit Append-Only Trigger Scripts

```sql
CREATE TRIGGER trg_audit_event_prevent_mutation
BEFORE UPDATE OR DELETE ON audit.audit_event
FOR EACH ROW EXECUTE FUNCTION audit.prevent_audit_mutation();

CREATE TRIGGER trg_compliance_record_prevent_mutation
BEFORE UPDATE OR DELETE ON audit.compliance_record
FOR EACH ROW EXECUTE FUNCTION audit.prevent_audit_mutation();

CREATE TRIGGER trg_data_export_record_prevent_mutation
BEFORE UPDATE OR DELETE ON audit.data_export_record
FOR EACH ROW EXECUTE FUNCTION audit.prevent_audit_mutation();

CREATE TRIGGER trg_administrative_access_record_prevent_mutation
BEFORE UPDATE OR DELETE ON audit.administrative_access_record
FOR EACH ROW EXECUTE FUNCTION audit.prevent_audit_mutation();
```

---

# 12. Index Scripts

```sql
CREATE INDEX idx_platform_setting_active ON platform.platform_setting (is_active, setting_key);
CREATE INDEX idx_feature_flag_scope ON platform.feature_flag (feature_code, scope_type, scope_id, is_enabled);

CREATE INDEX idx_organization_status ON tenant.organization (business_status);
CREATE INDEX idx_facility_org_status ON tenant.facility (organization_id, facility_status);
CREATE INDEX idx_site_facility_status ON tenant.site (facility_id, site_status);

CREATE INDEX idx_user_account_org_status ON identity.user_account (organization_id, account_status);
CREATE INDEX idx_role_assignment_user_status ON identity.role_assignment (user_account_id, assignment_status);
CREATE INDEX idx_user_session_user_status ON identity.user_session (user_account_id, session_status, expires_at);

CREATE INDEX idx_customer_org_status ON customer.customer (organization_id, customer_status);
CREATE INDEX idx_customer_email ON customer.customer (primary_email);
CREATE INDEX idx_customer_phone ON customer.customer (primary_phone);
CREATE INDEX idx_customer_consent_customer ON customer.customer_consent (customer_id, consent_type, consent_status);

CREATE INDEX idx_membership_customer_status ON membership.customer_membership (customer_id, membership_status);
CREATE INDEX idx_membership_facility_status ON membership.customer_membership (facility_id, membership_status);
CREATE INDEX idx_membership_plan_facility_status ON membership.membership_plan (facility_id, plan_status);

CREATE INDEX idx_attendance_org_date ON operations.attendance (organization_id, check_in_at);
CREATE INDEX idx_attendance_site_date ON operations.attendance (site_id, check_in_at);
CREATE INDEX idx_attendance_customer_date ON operations.attendance (customer_id, check_in_at);
CREATE INDEX idx_walkin_visit_site_date ON operations.walkin_visit (site_id, visit_at);

CREATE INDEX idx_trainer_facility_status ON training.trainer (facility_id, trainer_status);
CREATE INDEX idx_class_session_batch_time ON training.class_session (batch_id, starts_at, ends_at);
CREATE INDEX idx_personal_training_customer_time ON training.personal_training_session (customer_id, starts_at);
CREATE INDEX idx_personal_training_trainer_time ON training.personal_training_session (trainer_id, starts_at);

CREATE INDEX idx_invoice_org_status_date ON commercial.invoice (organization_id, invoice_status, invoice_date);
CREATE INDEX idx_invoice_customer ON commercial.invoice (customer_id, invoice_date);
CREATE INDEX idx_payment_org_status ON commercial.payment (organization_id, payment_status, created_at);
CREATE INDEX idx_payment_provider_reference ON commercial.payment (provider_code, provider_reference);
CREATE INDEX idx_refund_org_status ON commercial.refund (organization_id, refund_status, created_at);
CREATE INDEX idx_subscription_facility_status ON commercial.subscription (facility_id, subscription_status);
CREATE INDEX idx_license_facility_status ON commercial.license (facility_id, license_status);
CREATE INDEX idx_entitlement_facility_status ON commercial.entitlement (facility_id, entitlement_status);

CREATE INDEX idx_campaign_org_status ON communication.advertisement_campaign (organization_id, campaign_status);
CREATE INDEX idx_notification_org_status ON communication.notification (organization_id, notification_status, created_at);
CREATE INDEX idx_notification_delivery_status ON communication.notification_delivery (delivery_status, created_at);

CREATE INDEX idx_report_execution_org_status ON reporting.report_execution (organization_id, execution_status, created_at);
CREATE INDEX idx_kpi_snapshot_scope_time ON reporting.kpi_snapshot (scope_type, scope_id, measured_at);
CREATE INDEX idx_reporting_projection_source ON reporting.reporting_projection (source_entity_type, source_entity_id);

CREATE INDEX idx_support_ticket_org_status ON support.support_ticket (organization_id, ticket_status, created_at);
CREATE INDEX idx_support_ticket_customer ON support.support_ticket (customer_id, created_at);
CREATE INDEX idx_sla_tracking_status ON support.sla_tracking (sla_status, response_due_at, resolution_due_at);

CREATE INDEX idx_audit_event_org_time ON audit.audit_event (organization_id, occurred_at);
CREATE INDEX idx_audit_event_entity ON audit.audit_event (entity_type, entity_id);
CREATE INDEX idx_audit_event_correlation ON audit.audit_event (correlation_id);
CREATE INDEX idx_security_event_org_status ON security.security_event (organization_id, event_status, occurred_at);
CREATE INDEX idx_auth_event_user_time ON security.authentication_event (user_account_id, occurred_at);

-- Provisional tenant-aware index recommendations for critical tables
-- These indexes are suggested for the shared-schema tenancy model and are safe additions
-- when `organization_id` scoping is used. They can be reviewed and split into migration files.
CREATE UNIQUE INDEX IF NOT EXISTS uq_user_account_login_org ON identity.user_account (organization_id, login_identifier) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_customer_org_email ON customer.customer (organization_id, primary_email) WHERE primary_email IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_attendance_org_site_checkin ON operations.attendance (organization_id, site_id, check_in_at);
CREATE INDEX IF NOT EXISTS idx_payment_org_provider_reference ON commercial.payment (organization_id, provider_code, provider_reference);
```

---

# 13. Updated Timestamp Trigger Scripts

```sql
CREATE TRIGGER trg_platform_setting_updated_at BEFORE UPDATE ON platform.platform_setting FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_feature_flag_updated_at BEFORE UPDATE ON platform.feature_flag FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_organization_updated_at BEFORE UPDATE ON tenant.organization FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_facility_updated_at BEFORE UPDATE ON tenant.facility FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_site_updated_at BEFORE UPDATE ON tenant.site FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_user_account_updated_at BEFORE UPDATE ON identity.user_account FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_customer_updated_at BEFORE UPDATE ON customer.customer FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_customer_membership_updated_at BEFORE UPDATE ON membership.customer_membership FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_attendance_updated_at BEFORE UPDATE ON operations.attendance FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_trainer_updated_at BEFORE UPDATE ON training.trainer FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_invoice_updated_at BEFORE UPDATE ON commercial.invoice FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_payment_updated_at BEFORE UPDATE ON commercial.payment FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_subscription_updated_at BEFORE UPDATE ON commercial.subscription FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_license_updated_at BEFORE UPDATE ON commercial.license FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_notification_updated_at BEFORE UPDATE ON communication.notification FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
CREATE TRIGGER trg_support_ticket_updated_at BEFORE UPDATE ON support.support_ticket FOR EACH ROW EXECUTE FUNCTION platform.set_updated_at();
```

---

# 14. Seed DML Scripts

```sql
INSERT INTO platform.global_master_data (reference_group, reference_code, name, description, display_order)
VALUES
('FACILITY_TYPE', 'SWIMMING_POOL', 'Swimming Pool', 'Initial supported facility type', 1),
('FACILITY_TYPE', 'GYM', 'Gym', 'Future supported facility type', 2),
('FACILITY_TYPE', 'YOGA_STUDIO', 'Yoga Studio', 'Future supported facility type', 3),
('FACILITY_TYPE', 'DANCE_STUDIO', 'Dance Studio', 'Future supported facility type', 4),
('FACILITY_TYPE', 'SPORTS_ACADEMY', 'Sports Academy', 'Future supported facility type', 5),
('STATUS', 'ACTIVE', 'Active', 'Active lifecycle state', 1),
('STATUS', 'INACTIVE', 'Inactive', 'Inactive lifecycle state', 2),
('STATUS', 'SUSPENDED', 'Suspended', 'Suspended lifecycle state', 3),
('STATUS', 'ARCHIVED', 'Archived', 'Archived lifecycle state', 4),
('CHANNEL_TYPE', 'EMAIL', 'Email', 'Email communication channel', 1),
('CHANNEL_TYPE', 'SMS', 'SMS', 'SMS communication channel', 2),
('CHANNEL_TYPE', 'WHATSAPP', 'WhatsApp', 'WhatsApp communication channel', 3),
('CHANNEL_TYPE', 'IN_APP', 'In-App', 'In-application notification channel', 4),
('CURRENCY', 'INR', 'Indian Rupee', 'Default commercial currency for India', 1)
ON CONFLICT (reference_group, reference_code) DO NOTHING;

INSERT INTO tenant.facility_type (facility_type_code, name, description)
VALUES
('SWIMMING_POOL', 'Swimming Pool', 'Initial supported activity-based business type'),
('GYM', 'Gym', 'Future activity-based business type'),
('YOGA_STUDIO', 'Yoga Studio', 'Future activity-based business type'),
('DANCE_STUDIO', 'Dance Studio', 'Future activity-based business type'),
('SPORTS_ACADEMY', 'Sports Academy', 'Future activity-based business type')
ON CONFLICT (facility_type_code) DO NOTHING;

INSERT INTO platform.platform_setting (setting_key, setting_value, setting_type, scope_type, description)
VALUES
('DEFAULT_LOCALE', '{"locale":"en-IN"}', 'LOCALIZATION', 'PLATFORM', 'Default platform locale'),
('DEFAULT_TIMEZONE', '{"timezone":"Asia/Kolkata"}', 'LOCALIZATION', 'PLATFORM', 'Default platform timezone'),
('DEFAULT_CURRENCY', '{"currency":"INR"}', 'COMMERCIAL', 'PLATFORM', 'Default platform currency'),
('AUDIT_CAPTURE_ENABLED', '{"enabled":true}', 'AUDIT', 'PLATFORM', 'Audit event capture switch'),
('NOTIFICATION_DELIVERY_ENABLED', '{"enabled":true}', 'COMMUNICATION', 'PLATFORM', 'Notification delivery switch')
ON CONFLICT (setting_key, scope_type) DO NOTHING;

INSERT INTO identity.permission (permission_code, permission_name, module_code, capability_code)
VALUES
('PLATFORM_ADMIN_MANAGE_SETTINGS', 'Manage Platform Settings', 'PLATFORM_ADMINISTRATION', 'MANAGE_SETTINGS'),
('ORG_MANAGE_ORGANIZATION', 'Manage Organization', 'ORGANIZATION_MANAGEMENT', 'MANAGE_ORGANIZATION'),
('FACILITY_MANAGE_FACILITY', 'Manage Facility', 'FACILITY_MANAGEMENT', 'MANAGE_FACILITY'),
('SITE_MANAGE_SITE', 'Manage Site', 'SITE_MANAGEMENT', 'MANAGE_SITE'),
('USER_MANAGE_USERS', 'Manage Users', 'USER_ROLE_MANAGEMENT', 'MANAGE_USERS'),
('ROLE_MANAGE_ROLES', 'Manage Roles', 'USER_ROLE_MANAGEMENT', 'MANAGE_ROLES'),
('CUSTOMER_MANAGE_CUSTOMERS', 'Manage Customers', 'CUSTOMER_MANAGEMENT', 'MANAGE_CUSTOMERS'),
('MEMBERSHIP_MANAGE_MEMBERSHIPS', 'Manage Memberships', 'MEMBERSHIP_MANAGEMENT', 'MANAGE_MEMBERSHIPS'),
('ATTENDANCE_RECORD_ATTENDANCE', 'Record Attendance', 'ATTENDANCE_MANAGEMENT', 'RECORD_ATTENDANCE'),
('BILLING_MANAGE_INVOICES', 'Manage Invoices', 'BILLING_PAYMENT_MANAGEMENT', 'MANAGE_INVOICES'),
('PAYMENT_MANAGE_PAYMENTS', 'Manage Payments', 'BILLING_PAYMENT_MANAGEMENT', 'MANAGE_PAYMENTS'),
('REPORT_VIEW_REPORTS', 'View Reports', 'REPORTS_ANALYTICS', 'VIEW_REPORTS'),
('SUPPORT_MANAGE_TICKETS', 'Manage Support Tickets', 'SUPPORT_TICKET', 'MANAGE_TICKETS'),
('AUDIT_VIEW_AUDIT_LOGS', 'View Audit Logs', 'AUDIT_COMPLIANCE', 'VIEW_AUDIT_LOGS')
ON CONFLICT (permission_code) DO NOTHING;

INSERT INTO commercial.license_capability (capability_code, capability_name, module_code)
VALUES
('CUSTOMER_MANAGEMENT', 'Customer Management', 'CUSTOMER_MANAGEMENT'),
('MEMBERSHIP_MANAGEMENT', 'Membership Management', 'MEMBERSHIP_MANAGEMENT'),
('ATTENDANCE_MANAGEMENT', 'Attendance Management', 'ATTENDANCE_MANAGEMENT'),
('BILLING_PAYMENT_MANAGEMENT', 'Billing and Payment Management', 'BILLING_PAYMENT_MANAGEMENT'),
('NOTIFICATION_MANAGEMENT', 'Notification Management', 'NOTIFICATION_MANAGEMENT'),
('REPORTS_ANALYTICS', 'Reports and Analytics', 'REPORTS_ANALYTICS'),
('SUPPORT_TICKET', 'Support Ticket Management', 'SUPPORT_TICKET'),
('AUDIT_COMPLIANCE', 'Audit and Compliance', 'AUDIT_COMPLIANCE')
ON CONFLICT (capability_code) DO NOTHING;

INSERT INTO commercial.subscription_plan (plan_code, plan_name, plan_status, plan_payload, base_price_amount, currency_code)
VALUES
('FOUNDATION', 'Foundation Plan', 'ACTIVE', '{"description":"Initial commercial SaaS plan baseline"}', 0.00, 'INR')
ON CONFLICT (plan_code) DO NOTHING;
```

---

# 15. Validation Queries

```sql
SELECT schemaname, tablename
FROM pg_catalog.pg_tables
WHERE schemaname IN (
    'platform', 'tenant', 'identity', 'customer', 'membership', 'operations',
    'training', 'commercial', 'communication', 'reporting', 'support', 'audit', 'security'
)
ORDER BY schemaname, tablename;

SELECT conrelid::regclass AS table_name, conname AS constraint_name, contype AS constraint_type
FROM pg_constraint
WHERE connamespace::regnamespace::text IN (
    'platform', 'tenant', 'identity', 'customer', 'membership', 'operations',
    'training', 'commercial', 'communication', 'reporting', 'support', 'audit', 'security'
)
ORDER BY table_name, constraint_name;

SELECT schemaname, tablename, indexname
FROM pg_indexes
WHERE schemaname IN (
    'platform', 'tenant', 'identity', 'customer', 'membership', 'operations',
    'training', 'commercial', 'communication', 'reporting', 'support', 'audit', 'security'
)
ORDER BY schemaname, tablename, indexname;
```

---

# 16. Migration Packaging Recommendation

This document provides a single baseline script for review and implementation clarity.

For engineering execution, the script should later be split into migration files:

```text
database/migrations/
001_create_extensions_and_schemas.sql
002_create_platform_tenant_tables.sql
003_create_identity_security_tables.sql
004_create_customer_membership_operations_tables.sql
005_create_training_tables.sql
006_create_commercial_tables.sql
007_create_communication_reporting_support_audit_tables.sql
008_create_indexes_and_triggers.sql
009_seed_reference_data.sql
```

Each migration should be versioned, reviewed, tested against an empty database, tested against upgrade scenarios, and executed through the approved deployment pipeline.

---

# 17. Rollback Considerations

| Rollback Area | Consideration |
|---|---|
| Empty database deployment | Drop schemas in reverse dependency order if baseline execution fails |
| Production deployment | Prefer forward-only corrective migrations after first production release |
| Seed data | Use idempotent `ON CONFLICT DO NOTHING` where stable natural keys exist |
| Financial records | Do not delete production financial records through rollback scripts |
| Audit records | Do not update or delete audit records |
| Tenant data | Do not run destructive tenant data operations without approved change control |

---

# 18. Traceability

| Source Document | Source Content | DB-11 Implementation |
|---|---|---|
| DB-03 | Physical schemas, tables, relationships, indexes | PostgreSQL schema/table/index baseline |
| DB-04 | Multi-tenancy design | `organization_id`, `facility_id`, and `site_id` scope columns |
| DB-05 | Core platform database design | Platform, tenant, identity, and security DDL |
| DB-06 | Operational database design | Customer, membership, attendance, operations, and training DDL |
| DB-07 | Commercial database design | Billing, invoice, payment, refund, subscription, license, and entitlement DDL |
| DB-08 | Communication, reporting, support, audit, and governance design | Communication, reporting, support, audit, compliance, and security DDL |
| DB-09 | Operations, performance, lifecycle | Indexes, append-only audit behavior, migration packaging, rollback considerations |
| DB-10 | Traceability and data dictionary | Column naming, classification, and source mapping alignment |

---

# 19. Summary

DB-11 provides the PostgreSQL DDL/DML implementation baseline required to create the initial Digitize database.

It converts the approved database design set into executable PostgreSQL structures while preserving tenant isolation, relational integrity, auditability, commercial traceability, operational reporting, and future SaaS extensibility.

DB-11 should be reviewed by Data Architecture, Solution Architecture, Security Architecture, Engineering, DevOps, and QA before being split into executable migration files.
