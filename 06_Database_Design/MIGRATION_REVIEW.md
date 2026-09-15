# DIGITIZE Migration Review — DB-11 Alignment

**Document ID:** MIGRATION_REVIEW  
**Product:** Digitize  
**Date:** 2026-09-11  
**Model-layer status:** MODEL READY WITH DEFERRED ITEMS  
**Physical source of truth:** `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md` and `database/migrations/001`–`008`  
**Application representation:** SQLAlchemy 2.0 models in `digitize-services`

This review does not autogenerate Alembic revisions and does not invent schema.

**Physical freeze:** see `DATABASE_FOUNDATION_FREEZE.md`. Decision: **DATABASE FOUNDATION FROZEN WITH DEFERRED ITEMS**.

**Alembic reset (2026-09-11, explicit approval):** the 117-revision chain was deleted. Alembic now contains only `db11_foundation_baseline`, a stamp that requires SQL 001–008 to have been applied.

---

## 1. Executive Summary

Digitize currently has **two independent migration systems**. They do not describe the same database.

| Path | Location | What it creates | Used by |
| ---- | -------- | --------------- | ------- |
| **Approved physical CreateDB (SQL)** | `database/migrations/001`–`008` | `platform`, `tenant`, `commercial`, `membership`, … per DB-11 | `scripts/run_migrations_local.sh`, `.github/workflows/db-migrations-verify.yml` |
| **Alembic scaffold (obsolete)** | `digitize-services/migrations/versions/` (117 linear revisions) | `organization.*`, `facility.*`, `subscription.*`, old platform/membership shapes | Manual `alembic upgrade head` only. Not used by CI. |

The SQL path **already implements the approved core architecture** (Platform → Organization → Facility → Site, Platform-owned SaaS plans, Facility-scoped SaaS subscriptions, separate membership domain).

The Alembic path **does not**. Applying Alembic would recreate the pre-review domain (org-owned SaaS plans, customer subscriptions, Site unique-by-org, no `tenant`/`commercial` schemas).

Alembic history has **not** been applied by CI and reads as pre-production scaffold (placeholder README, empty duplicate revisions, one-table-per-file create chain). DB-12 requires immutable production history; it does **not** authorize rewriting applied production revisions. A clean Alembic reset is appropriate **only after explicit approval**. This review does not execute that reset.

**SQL path defect (fixed in this review):** `008_create_remaining_ddl.sql` previously issued `ALTER TABLE` against communication/support tables that `006` never creates. Those ALTERs are now skipped when the table does not exist. An empty-database apply can complete 008 seeds and indexes.

Remaining items (status vocabulary, extra ORM models, Alembic reset, Site Add-ons, DB-05 vs DB-11 extras) are deferred and non-blocking for core table creation.

---

## 2. Current Migration Inventory

### 2.1 SQL CreateDB chain (authoritative physical path)

Applied in order by `scripts/run_migrations_local.sh`:

| File | Purpose |
| ---- | ------- |
| `001_create_extensions_and_schemas.sql` | `pgcrypto`, `citext`; schemas `platform`, `tenant`, `identity`, `customer`, `membership`, `operations`, `training`, `commercial`, `communication`, `reporting`, `support`, `audit`, `security`, `integration` |
| `002_create_core_platform_tenant_tables.sql` | Platform master data + tenant org/facility/site |
| `003_create_identity_security_tables.sql` | Identity and security |
| `004_create_customer_membership_operations_training.sql` | Customer, membership, operations, training |
| `005_create_commercial_tables.sql` | Pricing, billing, SaaS subscription, license, entitlement |
| `006_create_comm_reporting_support_audit_integration.sql` | Communication, reporting, support, audit, integration |
| `007_create_indexes_triggers_seed.sql` | Selected indexes, `updated_at` triggers, provenance FK loop, **minimal** seed (`SWIMMING_POOL` only) |
| `008_create_remaining_ddl.sql` | Metadata ALTERs, extra indexes, **full** DB-11 §14 seed |
| `verify_schema.sql` | Diagnostic SELECTs (does **not** RAISE on findings) |

No Alembic revision IDs. No PostgreSQL ENUM types. Status/lifecycle values are VARCHAR + defaults.

### 2.2 Alembic chain (obsolete relative to DB-11)

- **117 files**, single linear chain
- **Root:** `1ab74092df84` (`identity.users`)
- **Head:** `3e86e411c717` (`campaign.campaign_status_history`)
- **Schemas created:** `identity`, `organization`, `facility`, `platform`, `subscription`, `billing`, `customer`, `staff`, `membership`, `training`, `attendance`, `communication`, `support`, `analytics`, `audit`, `campaign`
- **Not created:** `tenant`, `commercial`, `operations`, `reporting`, `security`, `integration`
- **Seed data:** none
- **Enums:** none (check constraints instead)
- **Empty revisions:** `f9dd94d85786`, `d03526c80cd2` (`pass`)
- `env.py` imports all `app.modules.*.models` with `include_schemas=True` — **autogenerate would emit extra models and drop/rename against whichever database it is pointed at**

### 2.3 Alembic objects that conflict with DB-11

| Alembic object | Conflict |
| -------------- | -------- |
| `organization.organizations` | Target is `tenant.organization` (`record_id`, `legal_name`, `business_status`) |
| `facility.facility_types` / `facility.facilities` / `facility.sites` | Target is `tenant.facility_type` / `facility` / `site` |
| `subscription.subscription_plans` (org-owned, TIME/QUOTA/UNLIMITED) | Target is platform-owned `commercial.subscription_plan` |
| `subscription.subscriptions` (`customer_id`, `plan_version_id`) | Target is facility-scoped `commercial.subscription` |
| `subscription.products`, `subscription_plan_versions`, `subscription_plan_features`, `subscription_price_points` | Not in DB-11 |
| `membership.memberships` FK to SaaS plan versions | Target is `membership.customer_membership` → `membership.membership_plan` |
| `platform.platform_settings` / `platform_feature_flags` / `platform_configuration` / `platform_modules` / `platform_announcements` | Target names are singular `platform_setting`, `feature_flag`; configuration/modules/announcements are not DB-11 tables |

---

## 3. Target DB-11 Architecture

```text
platform
  global_master_data
  platform_setting
  feature_flag
  maintenance_window
  release_record

tenant
  organization
    organization_setting / organization_policy / organization_document
    facility_type                    # platform-owned catalog living in tenant schema
    facility                         # organization_id + facility_type_id NOT NULL
      facility_setting / facility_policy
      site                           # organization_id + facility_id NOT NULL
        site_setting / site_policy

commercial
  subscription_plan                  # platform catalog, no tenant FK
  subscription                       # organization_id + facility_id + plan_id NOT NULL
    subscription_term
    subscription_lifecycle_history
    license                          # facility-scoped, subscription_id optional
      license_assignment
      entitlement → license_capability
      feature_access
  pricing / price_version

membership
  membership_plan                    # facility-owned customer offering
    membership_plan_rule
  customer_membership
```

Hierarchy remains **Platform → Organization → Facility → Site**. No Branch. Site is not between Organization and Facility. SaaS and membership stay separate schemas.

---

## 4. Migration → Model Reconciliation

Classification key: **ALIGNED** | **MIGRATION GAP** | **MODEL GAP** | **MODEL/DDL CONFLICT** | **DEFERRED** | **OBSOLETE**

“SQL” = `database/migrations`. “Alembic” = `digitize-services/migrations`.

| Object | Model | SQL (DB-11 path) | Alembic | Decision |
| ------ | ----- | ---------------- | ------- | -------- |
| `platform.global_master_data` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `platform.platform_setting` | Yes | Yes | Wrong table `platform_settings` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `platform.feature_flag` | Yes | Yes | Wrong table `platform_feature_flags` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `platform.maintenance_window` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `platform.release_record` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `platform.platform_configuration` | Yes (extra) | No | Yes | **MODEL EXISTS / DDL ABSENT** |
| `platform.platform_modules` | Yes (extra) | No | Yes | **MODEL EXISTS / DDL ABSENT** |
| `platform.platform_announcements` | Yes (extra) | No | Yes | **MODEL EXISTS / DDL ABSENT** |
| `tenant.organization` | Yes | Yes | `organization.organizations` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.organization_setting` | Yes | Yes | Wrong shape/schema | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.organization_policy` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `tenant.organization_document` | Yes | Yes | Wrong shape/schema | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `organization.organization_contacts` | Yes (extra) | No | Yes | **MODEL EXISTS / DDL ABSENT** |
| `organization.organization_status_history` | Yes (extra) | No | Yes | **MODEL EXISTS / DDL ABSENT** |
| `tenant.facility_type` | Yes | Yes | `facility.facility_types` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.facility` | Yes | Yes | `facility.facilities` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.facility_setting` | Yes | Yes | Wrong shape | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.facility_policy` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `tenant.site` | Yes | Yes | `facility.sites` unique-by-org | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.site_setting` | Yes | Yes | Wrong shape | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `tenant.site_policy` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| Facility/Site hours, capacity, features, addresses, status history | Yes (extra) | No | Yes | **DB-05 / DB-11 CONFLICT** — do not migrate |
| `commercial.subscription_plan` | Yes | Yes | org-owned `subscription.subscription_plans` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `commercial.subscription` | Yes | Yes | customer-owned `subscription.subscriptions` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `commercial.subscription_term` | Yes; `invoice_id` UUID, no FK | Yes; `invoice_id` **has** FK to `commercial.invoice` | No | SQL **ALIGNED** to DB-11. Model **MODEL GAP** (intentional until billing ORM alignment) |
| `commercial.subscription_lifecycle_history` | Yes | Yes | different `subscription_status_history` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `commercial.license` / `license_assignment` / `license_capability` / `entitlement` / `feature_access` | Yes | Yes | No (old `subscription_entitlements`) | SQL+model **ALIGNED**. Alembic **OBSOLETE** / **MIGRATION GAP** |
| `commercial.pricing` / `price_version` | Yes | Yes | `subscription_price_points` | SQL+model **ALIGNED**. Alembic **OBSOLETE** |
| `subscription.products` / plan versions / plan features / price points | Removed from models | No | Yes | Alembic **OBSOLETE** |
| `membership.membership_plan` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `membership.membership_plan_rule` | Yes | Yes | No | **ALIGNED** (SQL+model). Alembic **MIGRATION GAP** |
| `membership.customer_membership` | Yes; customer FK still `customer.customers.customer_id` | Yes; customer FK `customer.customer.record_id` | `membership.memberships` → SaaS plan versions | SQL **ALIGNED**. Model customer FK **MODEL GAP**. Alembic **OBSOLETE** |
| Site Add-on table | No | No | No | **DEFERRED** |
| One-active-subscription partial unique index | No | No | No | **DEFERRED** (application rule) |

Autogenerate from current ORM metadata would be unsafe: it would try to create extra models and would not produce a clean DB-11 database from the Alembic chain.

---

## 5. Migration → DB-11 Reconciliation

Core platform / tenant / commercial / membership tables in `002` and `005` match DB-11 column lists, PK `record_id`, named uniques, named checks, `ON DELETE RESTRICT` tenant FKs, JSONB defaults, and audit/soft-delete columns.

Known SQL vs DB-11 markdown differences (outside this core scope unless they break apply):

| Item | SQL files | DB-11 markdown |
| ---- | --------- | -------------- |
| File packaging | 001–008 | Proposed 9-file split in §16 |
| Full seed | Lives in **008** | §14 |
| 007 seed | `SWIMMING_POOL` only | Full seed in §14 |
| Communication campaign / consent tables | **Not created** in 006 | Present in DB-11 |
| Support `ticket_attachment`, `ticket_escalation`, `sla_tracking` | **Not created** in 006 | Present in DB-11 |
| 008 metadata ALTERs | Targets those missing tables | Assumes tables exist |
| `fk_customer_membership_invoice` | Not added | Documented as deferred FK |
| Provenance FKs | 007 dynamic loop `fk_{schema}_{table}_created_by_user` | Named `fk_*_created_by_user` list |
| `subscription_term.invoice_id` | FK to `commercial.invoice` **present** | Present |

**Do not add** the missing campaign/support tables in this workstream.

---

## 6. Schema-by-Schema Review

### platform

| Table | SQL | Notes |
| ----- | --- | ----- |
| `global_master_data` | 002 | Unique `(reference_group, reference_code)`. Seed groups in 008: FACILITY_TYPE, STATUS, CHANNEL_TYPE, CURRENCY |
| `platform_setting` | 002 | Unique `(setting_key, scope_type)`. JSONB `setting_value`. Seed 5 keys in 008 |
| `feature_flag` | 002 | Unique `(feature_code, scope_type, scope_id)`. Rollout 0–100 check. No `module_id` |
| `maintenance_window` | 002 | Unique `window_code`. `ends_at > starts_at` |
| `release_record` | 002 | Unique `release_code`. Platform release governance (FR-PLT-009). Not required for Org/Facility create |

No generic `platform.configuration` table in SQL. Alembic still creates one — do not carry it forward.

### tenant

| Table | SQL | Required constraints |
| ----- | --- | -------------------- |
| `organization` | 002 | Unique `organization_code`, `legal_name`. Soft delete. **No subscription FK**. Default `business_status='ACTIVE'` |
| `organization_setting` | 002 | Unique `(organization_id, setting_key)` |
| `organization_policy` | 002 | Unique `(organization_id, policy_code)` |
| `organization_document` | 002 | Org FK RESTRICT. No `updated_at`/`version_number` in DDL (model matches) |
| `facility_type` | 002 | Unique `facility_type_code`. Platform-owned (no org FK). `is_active` |
| `facility` | 002 | Unique `(organization_id, facility_code)`. Org + type FKs RESTRICT. `subscription_scope_status` default `'PENDING'` |
| `facility_setting` / `facility_policy` | 002 | Key uniqueness on facility |
| `site` | 002 | Unique `(facility_id, site_code)` — **not** org-wide. `address_payload` JSONB |
| `site_setting` / `site_policy` | 002 | Org + facility + site FKs |

Obsolete Alembic fields (`organization_name`, GST/PAN/website, `default_capacity`, logo, Site unique-by-org) are **not** in SQL 002. Do not reintroduce them.

### commercial

SaaS plan has **no** `organization_id` / `facility_id` / `customer_id`. Subscription has **all three** of `organization_id`, `facility_id`, `subscription_plan_id` NOT NULL.

`ck_subscription_dates`: `ends_at IS NULL OR ends_at >= starts_at`.  
No unique-on-active-subscription index (application rule only).

`subscription_term.invoice_id` **does** FK to `commercial.invoice` in SQL 005. The ORM omits that FK until billing models use `commercial.invoice.record_id`. Keep the SQL FK. Do not drop it. Do not invent a different billing FK.

License capability unique `capability_code`. Entitlement unique `(facility_id, license_id, capability_id)`.

Do not recreate `product`, `subscription_plan_version`, `subscription_plan_feature`, `subscription_price_point`.

### membership

`membership_plan` is facility-owned (`organization_id` + `facility_id`, unique `(facility_id, plan_code)`).  
`customer_membership` points at `membership_plan`, not SaaS plan versions.  
`invoice_id` on `customer_membership` has **no** FK in SQL (DB-11 deferred). Correct.

---

## 7. Constraint Review

Approved constraints present in SQL 002/005 for core tables:

| Constraint | Object |
| ---------- | ------ |
| `uq_global_master_data_group_code` | global_master_data |
| `uq_platform_setting_key_scope` | platform_setting |
| `uq_feature_flag_scope` | feature_flag |
| `ck_feature_flag_rollout` / `ck_feature_flag_dates` | feature_flag |
| `uq_maintenance_window_code` / `ck_maintenance_window_dates` | maintenance_window |
| `uq_release_record_code` | release_record |
| `uq_organization_code` / `uq_organization_legal_name` | organization |
| `uq_org_setting_key` / `ck_org_setting_dates` | organization_setting |
| `uq_org_policy_code` / `ck_org_policy_dates` | organization_policy |
| `uq_facility_type_code` | facility_type |
| `uq_facility_code_org` | facility |
| `uq_facility_setting_key` | facility_setting |
| `uq_facility_policy_code` / `ck_facility_policy_dates` | facility_policy |
| `uq_site_code_facility` | site |
| `uq_site_setting_key` | site_setting |
| `uq_site_policy_code` / `ck_site_policy_dates` | site_policy |
| `uq_subscription_plan_code` | subscription_plan |
| `uq_subscription_number` / `ck_subscription_dates` | subscription |
| `ck_subscription_term_dates` | subscription_term |
| `uq_license_number` / `ck_license_dates` | license |
| `uq_license_assignment` / `ck_license_assignment_dates` | license_assignment |
| `uq_license_capability_code` | license_capability |
| `uq_entitlement_capability` / `ck_entitlement_dates` | entitlement |
| `uq_feature_access_capability` | feature_access |
| `uq_pricing_code` | pricing |
| `ck_price_version_amount` / `ck_price_version_dates` | price_version |
| `uq_membership_plan_code` / duration + price checks | membership_plan |
| `uq_membership_plan_rule_code` | membership_plan_rule |
| `uq_customer_membership_number` / `ck_customer_membership_dates` | customer_membership |

PK type is UUID `record_id` with `gen_random_uuid()` on all approved core tables.

Alembic invented checks (org onboarding status, facility status enums, plan_type TIME/QUOTA/UNLIMITED, product_type MEMBERSHIP/PASS/ADDON) are **not** in DB-11. Do not port them.

007 indexes (`idx_platform_setting_active`, `idx_feature_flag_scope`, `idx_organization_status`, `idx_facility_org_status`, `idx_site_facility_status`) and 008 commercial/membership indexes match DB-11 selected indexes. They are not `IF NOT EXISTS` (first-run only).

---

## 8. Seed Data Review

### Required (DB-11 §14) — applied in 008 (idempotent `ON CONFLICT DO NOTHING`)

**Facility types** (`tenant.facility_type` and `global_master_data` group `FACILITY_TYPE`):

```text
SWIMMING_POOL
GYM
YOGA_STUDIO
DANCE_STUDIO
SPORTS_ACADEMY
```

**STATUS:** ACTIVE, INACTIVE, SUSPENDED, ARCHIVED  
**CHANNEL_TYPE:** EMAIL, SMS, WHATSAPP, IN_APP  
**CURRENCY:** INR  

**Platform settings:** DEFAULT_LOCALE, DEFAULT_TIMEZONE, DEFAULT_CURRENCY, AUDIT_CAPTURE_ENABLED, NOTIFICATION_DELIVERY_ENABLED  

**SaaS plan:** FOUNDATION / Foundation Plan / ACTIVE / INR / 0.00  

**License capabilities:** CUSTOMER_MANAGEMENT, MEMBERSHIP_MANAGEMENT, ATTENDANCE_MANAGEMENT, BILLING_PAYMENT_MANAGEMENT, NOTIFICATION_MANAGEMENT, REPORTS_ANALYTICS, SUPPORT_TICKET, AUDIT_COMPLIANCE  

**Permissions:** 14 identity.permission rows (identity domain; required by 008, not this commercial workstream’s product scope)

007 additionally inserts only `FACILITY_TYPE/SWIMMING_POOL`. Harmless duplicate with 008.

No invented plans, tiers, or extra facility types.

---

## 9. Obsolete Migration Objects

Alembic currently creates these and they must **not** be part of the DB-11 target:

**Schemas:** `organization`, `facility` (as domain schema), `subscription`, `billing`, `analytics`, `campaign`, `attendance`, `staff` (as Alembic named them)

**Tables (selected):** `organization.organizations`, contacts, settings, documents, status_history; all 14 `facility.*` tables including operating hours/capacity/features/addresses; `subscription.products`, `subscription_plans`, `subscription_plan_versions`, `subscription_plan_features`, `subscription_price_points`, `subscriptions`, `subscription_entitlements`, `subscription_status_history`; `platform.platform_configuration`, `platform_modules`, `platform_announcements`; `membership.memberships` (SaaS-linked).

**Policy:** treat the 117-revision chain as **historical pre-production scaffold (category B — disposable if explicitly approved)**. Do not rewrite file-by-file in place. Do not `alembic upgrade head` against a DB-11 database. Do not squash/reset without an explicit instruction.

SQL CreateDB does not create those obsolete objects.

---

## 10. Known Conflicts

### 10.1 Status vocabulary — SCHEMA DECISION REQUIRED (non-blocking for VARCHAR columns)

DDL uses VARCHAR without check constraints. Defaults:

| Entity | DB-11 / SQL default | Model server_default | BA / FR vocabulary |
| ------ | ------------------- | -------------------- | ------------------ |
| Organization `business_status` | `ACTIVE` | `ACTIVE` | BA: Pending/Active/Suspended/Archived. FR-03 create = Pending. DB-05-CK: Draft/Active/Suspended/Archived |
| Facility `facility_status` | `ACTIVE` | `ACTIVE` | BA: Draft/Operational/Suspended/Closed. FR-04: Draft → Active |
| Facility `subscription_scope_status` | `PENDING` | `PENDING` | Commercial pending until subscription active |
| Site `site_status` | `ACTIVE` | `ACTIVE` | BA: Planned/Active/Suspended/Closed. FR-05 create = Draft |
| Plan `plan_status` | `ACTIVE` | `ACTIVE` | FR: Active / retired |
| Subscription `subscription_status` | `PENDING` | `PENDING` | Glossary: Draft → Purchased → Active → … |
| License `license_status` | `ACTIVE` | `ACTIVE` | Glossary: Active → Renewed → Expired |
| Global STATUS seed | ACTIVE/INACTIVE/SUSPENDED/ARCHIVED | catalog constants | Does not cover PENDING/DRAFT/CLOSED |

Migration keeps VARCHAR + documented defaults. Application vocabulary is not frozen here.

### 10.2 Facility Type dual catalog — SCHEMA DECISION REQUIRED (keep both)

DB-11 and DB-05 define **both**:

- `tenant.facility_type` — **authoritative normalized entity**. `tenant.facility.facility_type_id` FKs here.
- `platform.global_master_data` (`FACILITY_TYPE`) — **shared reference/display catalog**.

Both are seeded with the same five codes. No sync trigger is approved. Do not delete either. Do not invent synchronization.

### 10.3 DB-05 vs DB-11 extras — DB-05 / DB-11 CONFLICT

DB-05 names `organization_branding`, `facility_operating_hours`, `facility_capacity_rule`. Physical SQL and DB-11 core CREATE set omit them. Extra ORM models exist. **Do not generate migrations for them.**

### 10.4 Dual migration runners

CI applies SQL. Backend README still documents Alembic. That operational conflict is deferred as an Alembic-reset decision. Until then, SQL is the only approved physical apply path.

### 10.5 `008` ALTER on missing tables — fixed

`ALTER TABLE communication.campaign_schedule` (and peers) fails if the table does not exist. `ADD COLUMN IF NOT EXISTS` does not create the table. 008 now skips ALTERs when the table is absent. Missing campaign/support tables remain a DB-11 packaging gap outside this workstream.

### 10.6 `verify_schema.sql` does not fail the job

It prints diagnostic result sets. `ON_ERROR_STOP` does not treat “rows returned” as failure. CI can report success without asserting core tables exist.

`verify_core_contract.sql` now runs first in `scripts/run_migrations_local.sh` and **does** `RAISE EXCEPTION` if required schemas, core tables, uniqueness/check names, or approved seeds are missing, or if obsolete Alembic tables are present. `verify_schema.sql` remains diagnostic.

---

## 11. Required Forward Migrations

### 11.1 Implemented in this review

Guarded `008` metadata `ALTER TABLE` statements so they run only when the target table exists. Did **not** create the missing campaign/support tables.

Added `database/migrations/verify_core_contract.sql` and wired it into `scripts/run_migrations_local.sh`. This assertion fails the runner if required schemas, core tables, uniqueness/check names, or approved seeds are missing, or if obsolete Alembic tables are present.

### 11.2 Do not implement now

| Change | Reason |
| ------ | ------ |
| Alembic autogenerate | Would drop/create/rename unsafely and emit extra models |
| New Alembic revision on top of 117 | Would stack DB-11 onto obsolete `organization.*` / `subscription.*` |
| Alembic history squash/reset | Requires explicit approval (destructive to revision IDs) |
| Site Add-on table | Deferred schema decision |
| Extra ORM tables | MODEL EXISTS / DDL ABSENT |
| Status check constraints | Vocabulary not frozen |
| Partial unique “one active subscription per facility” | Application rule unless later approved |
| Billing FKs on membership | Explicitly deferred in DB-11 SQL |
| Dropping SQL `subscription_term.invoice_id` FK | DB-11 requires it; `commercial.invoice` already exists in 005 |

### 11.3 Recommended later (explicit approval)

1. Reset Alembic to a single baseline that records “SQL 001–008 already applied” **or** retire Alembic in favor of the SQL CreateDB path.  
2. Add further CI assertions beyond `verify_core_contract.sql` if identity/operations coverage is required.  
3. Align remaining ORM modules (customer, billing) to `customer.customer` / `commercial.invoice`.  
4. Make 007 indexes `IF NOT EXISTS` only if re-apply idempotency is required.

---

## 12. Migration Ordering

SQL CreateDB order already matches FK dependencies:

```text
1. 001 extensions + schemas
2. 002 platform master + tenant org / facility_type / facility / site / settings / policies
3. 003 identity / security   (needed before 007 provenance FKs)
4. 004 customer + membership + operations + training
5. 005 commercial (pricing → invoice → subscription → license → entitlement)
6. 006 communication / reporting / support / audit / integration
7. 007 indexes / triggers / provenance FKs / minimal seed
8. 008 remaining metadata ALTERs / extra indexes / full seed
```

`005` can create `subscription_term.invoice_id` → `commercial.invoice` because invoice is created earlier in the same file.

Do not apply Alembic before or after this chain on the same database.

---

## 13. Migration Test Plan

Physical tests must use PostgreSQL (not SQLite).

1. Empty database; run `scripts/run_migrations_local.sh`.  
2. Required schemas exist.  
3. Approved core tables exist (`platform` 5, `tenant` 11, commercial SaaS/license/pricing 11, membership 3).  
4. Obsolete Alembic tables (`organization.organizations`, `subscription.subscription_plans`, `facility.facilities`, …) are **absent**.  
5. Primary keys are `record_id` UUID.  
6. Foreign keys: Facility→Organization, Facility→FacilityType, Site→Facility, Site→Organization, Subscription→Organization/Facility/Plan, License→Subscription (nullable), Entitlement→Capability.  
7. Unique constraints listed in §7 exist.  
8. Check constraints listed in §7 exist.  
9. Defaults: org/facility/site status, `subscription_scope_status='PENDING'`, `subscription_status='PENDING'`, `plan_status='ACTIVE'`.  
10. Seeds: five facility types, FOUNDATION plan, eight capabilities, master-data groups.  
11. JSONB columns (`metadata`, `plan_payload`, `setting_value`, `address_payload`) are `jsonb`.  
12. `membership.membership_plan` exists and `subscription.subscription_plans` does not.

`verify_core_contract.sql` is the failing assertion for this core contract. `verify_schema.sql` remains diagnostic.

Physical PostgreSQL apply was **not run** in this review: localhost:5432 is reachable, but documented credentials (`postgres` / `postgres`) failed password authentication. Do not guess other credentials. Re-run `scripts/run_migrations_local.sh` against a dedicated empty database when credentials are available, then `DIGITIZE_MIGRATION_TEST=1 PGDATABASE=<dedicated_db> poetry run pytest tests/migrations`.

---

## 14. Deferred Decisions

1. Freeze status vocabularies vs VARCHAR defaults.  
2. Dual Facility Type catalog synchronization.  
3. DB-05 operating hours / capacity / branding tables.  
4. Extra ORM models (contacts, announcements, modules, configuration, feature values, …).  
5. Site Add-on commercialization.  
6. Alembic reset vs retire.  
7. Customer and billing ORM alignment to DB-11 table/PK names.  
8. Represent `subscription_term.invoice_id` FK on the ORM.  
9. One-active-SaaS-subscription-per-facility enforcement (app vs partial unique index).  
10. Missing DB-11 communication campaign / support attachment tables (out of this workstream).  
11. Whether `verify_schema.sql` should also RAISE (core contract is now asserted by `verify_core_contract.sql`).

---

## 15. Final Migration Readiness

```text
MIGRATION READY WITH DEFERRED ITEMS
```

**Meaning:**

- The **SQL CreateDB path** (`database/migrations`) is the approved physical implementation of DB-11 for the Platform / Organization / Facility / Site / SaaS / Membership core.  
- After guarding 008 ALTERs, an empty PostgreSQL database can be provisioned without inventing schema.  
- **Alembic is not ready** and must not be applied or autogenerated until an explicit reset/retire decision.  
- Deferred product/schema decisions in §14 do not block creating the approved core tables.

```text
Migration Review Result
-----------------------

Decision:
MIGRATION READY WITH DEFERRED ITEMS

Core tables aligned:
30

Migration gaps:
8

Model/DDL conflicts:
2

Obsolete migration objects:
117

Deferred schema decisions:
11

Blocking issues:
0

Forward migrations required:
yes (008 ALTER guard + verify_core_contract.sql implemented; Alembic reset still requires explicit approval)

Physical PostgreSQL validation:
not run
```

Core tables aligned = platform 5 + tenant 11 + commercial 11 + membership 3 on the SQL CreateDB path.

Migration gaps = 8 DB-11 communication/support tables named in markdown and 008 ALTERs but never created by 006. They are out of this workstream and no longer block empty-DB apply.

Model/DDL conflicts = `commercial.subscription_term.invoice_id` FK present in SQL, omitted in ORM; `membership.customer_membership` still FKs `customer.customers.customer_id`.

Obsolete migration objects = 117-revision Alembic chain (`organization.*` / `facility.*` / `subscription.*`). Do not apply.

Physical validation was not run: localhost:5432 rejected documented `postgres`/`postgres` credentials. Model-layer pytest: 35 passed, 7 skipped (opt-in PostgreSQL contract tests).

---

## Appendix A — Alembic safety

Do **not** run:

```bash
alembic revision --autogenerate
alembic upgrade head
```

against a DB-11 database or as a way to “catch up” models. Autogenerate will treat extra ORM files as required tables and will treat `tenant.*` / `commercial.*` as unrelated to `organization.*` / `subscription.*`.
