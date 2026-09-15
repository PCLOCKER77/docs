# DIGITIZE Database Foundation Freeze — PostgreSQL / DB-11

**Document ID:** DATABASE_FOUNDATION_FREEZE  
**Product:** Digitize  
**Date:** 2026-09-11  
**Model-layer status:** MODEL READY WITH DEFERRED ITEMS  
**Migration-layer status:** MIGRATION READY WITH DEFERRED ITEMS  
**Physical source of truth:** `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md` and `database/migrations/001`–`008`

This freeze is based on a clean empty-database apply of the SQL CreateDB path. It does not autogenerate Alembic revisions and does not invent schema.

**Alembic reset (2026-09-11):** the 117-revision pre-production chain was removed. Alembic now has a single stamp revision `db11_foundation_baseline`. Physical DDL remains `database/migrations/001`–`008`.

---

## 1. Executive Summary

The approved SQL migration path can provision the DB-11 core database from an empty PostgreSQL database.

```text
DATABASE FOUNDATION FROZEN WITH DEFERRED ITEMS
```

Physical validation proved:

- Platform → Organization → Facility → Site
- Platform-owned SaaS subscription plans
- Facility-scoped SaaS subscriptions
- Separate customer membership domain
- Approved seeds, constraints, JSONB types, and the 008 missing-table guard

Deferred product and ORM-alignment items remain. They do not block treating `database/migrations/001`–`008` as the frozen physical foundation for subsequent backend work.

---

## 2. Physical Source of Truth

Priority order used for this freeze:

1. `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md`
2. `database/migrations/001`–`008`
3. `database/migrations/verify_core_contract.sql`
4. SQLAlchemy core models under `digitize-services/app` (consume the schema; do not create it)

SQLAlchemy extra models are **not** sources of truth. The obsolete 117-revision Alembic chain has been removed.

---

## 3. Migration Architecture

| Path | Role | Freeze status |
| ---- | ---- | ------------- |
| `database/migrations/001`–`008` via `scripts/run_migrations_local.sh` | Approved physical provisioning | **Authoritative** |
| `digitize-services/migrations/versions/` (117 revisions) | Obsolete pre-production scaffold (`organization.*` / `facility.*` / `subscription.*`) | **Isolated. Do not apply.** |

```text
DO NOT RUN ALEMBIC FOR DB-11 PROVISIONING
DO NOT RUN ALEMBIC AUTOGENERATE
```

The ORM must not call `Base.metadata.create_all()` against a DIGITIZE database.

---

## 4. PostgreSQL Environment

A dedicated empty cluster was created for this freeze. The existing listener on port 5432 was **not** used (credentials unknown; no credential discovery). Docker was not available on the validation host.

| Item | Value |
| ---- | ----- |
| Engine | PostgreSQL 14.19 (Homebrew) |
| Bind | `127.0.0.1:55432` (ephemeral cluster, not the unknown :5432 instance) |
| Databases | `digitize_foundation_a`, `digitize_foundation_b`, `digitize_foundation_pytest` |
| Pre-migration application schemas | none (`platform`/`tenant`/`commercial`/`membership` count = 0) |
| Alembic | not executed |

Credentials are not recorded in this document.

The runner now requires an explicit `PGDATABASE` and refuses to apply when DIGITIZE application schemas already exist unless `DIGITIZE_ALLOW_EXISTING_DB=1`.

---

## 5. Empty Database Migration Result

| Run | Database | Start state | Result |
| --- | -------- | ----------- | ------ |
| 1 | `digitize_foundation_a` | empty | **PASS** — 001→008, `verify_core_contract.sql` RAISE path succeeded |
| 2 | `digitize_foundation_b` | empty | **PASS** — identical catalog to run 1 (2528 catalog rows, zero diff) |
| 3 | `digitize_foundation_pytest` | empty | **PASS** — applied by pytest fixture |

Re-apply on `digitize_foundation_a` was refused by the runner (expected). 007 indexes are first-run only; empty-database reproducibility is the approved contract, not in-place re-apply.

008 completed: metadata ALTER DO block, audit-trigger DO block, indexes, and seed inserts (`INSERT 0 13/5/5/14/8/1`).

---

## 6. Schema Validation

Created schemas: `platform`, `tenant`, `identity`, `customer`, `membership`, `operations`, `training`, `commercial`, `communication`, `reporting`, `support`, `audit`, `security`, `integration`.

Required core schemas **present:** `platform`, `tenant`, `commercial`, `membership`.

Obsolete schemas **absent:** `organization`, `facility`, `subscription`.

`public.alembic_version` **absent.**

Additional schemas (`identity`, `customer`, billing tables inside `commercial`, operations, etc.) come from DB-11 files 003–006. They are outside the 30-table freeze core and were not invented in this task.

---

## 7. Core Table Validation

| Schema | Table | Expected | Exists | Result |
| ------ | ----- | -------: | -----: | ------ |
| platform | global_master_data | 1 | 1 | PASS |
| platform | platform_setting | 1 | 1 | PASS |
| platform | feature_flag | 1 | 1 | PASS |
| platform | maintenance_window | 1 | 1 | PASS |
| platform | release_record | 1 | 1 | PASS |
| tenant | organization | 1 | 1 | PASS |
| tenant | organization_setting | 1 | 1 | PASS |
| tenant | organization_policy | 1 | 1 | PASS |
| tenant | organization_document | 1 | 1 | PASS |
| tenant | facility_type | 1 | 1 | PASS |
| tenant | facility | 1 | 1 | PASS |
| tenant | facility_setting | 1 | 1 | PASS |
| tenant | facility_policy | 1 | 1 | PASS |
| tenant | site | 1 | 1 | PASS |
| tenant | site_setting | 1 | 1 | PASS |
| tenant | site_policy | 1 | 1 | PASS |
| commercial | subscription_plan | 1 | 1 | PASS |
| commercial | subscription | 1 | 1 | PASS |
| commercial | subscription_term | 1 | 1 | PASS |
| commercial | subscription_lifecycle_history | 1 | 1 | PASS |
| commercial | license | 1 | 1 | PASS |
| commercial | license_assignment | 1 | 1 | PASS |
| commercial | license_capability | 1 | 1 | PASS |
| commercial | entitlement | 1 | 1 | PASS |
| commercial | feature_access | 1 | 1 | PASS |
| commercial | pricing | 1 | 1 | PASS |
| commercial | price_version | 1 | 1 | PASS |
| membership | membership_plan | 1 | 1 | PASS |
| membership | membership_plan_rule | 1 | 1 | PASS |
| membership | customer_membership | 1 | 1 | PASS |

**30/30.** PK on core tables is `record_id UUID DEFAULT gen_random_uuid()`.

Organization has `organization_code`, `legal_name`, `display_name`, `business_status`, audit columns, and `deleted_at`/`deleted_by`. No SaaS subscription FK.

Facility has `organization_id` and `facility_type_id` NOT NULL. No `default_capacity` or `logo`.

Site uniqueness is `UNIQUE (facility_id, site_code)`, not organization-wide. `address_payload` is JSONB.

SaaS plan has no `organization_id` / `facility_id` / `customer_id`. Subscription has those three FKs NOT NULL and no `customer_id`.

---

## 8. Foreign Key Validation

PostgreSQL `confdeltype`: `r` = RESTRICT, `n` = SET NULL, `c` = CASCADE.

| Source | Target | Source nullability | ON DELETE | Result |
| ------ | ------ | ------------------ | --------- | ------ |
| tenant.facility.organization_id | tenant.organization.record_id | NOT NULL | RESTRICT | PASS |
| tenant.facility.facility_type_id | tenant.facility_type.record_id | NOT NULL | RESTRICT | PASS |
| tenant.site.organization_id | tenant.organization.record_id | NOT NULL | RESTRICT | PASS |
| tenant.site.facility_id | tenant.facility.record_id | NOT NULL | RESTRICT | PASS |
| commercial.subscription.organization_id | tenant.organization.record_id | NOT NULL | RESTRICT | PASS |
| commercial.subscription.facility_id | tenant.facility.record_id | NOT NULL | RESTRICT | PASS |
| commercial.subscription.subscription_plan_id | commercial.subscription_plan.record_id | NOT NULL | RESTRICT | PASS |
| commercial.subscription_term.subscription_id | commercial.subscription.record_id | NOT NULL | RESTRICT | PASS |
| commercial.subscription_term.invoice_id | commercial.invoice.record_id | NULL | RESTRICT | PASS (SQL/DB-11) |
| commercial.license.subscription_id | commercial.subscription.record_id | NULL | RESTRICT | PASS |
| commercial.entitlement.license_id | commercial.license.record_id | NOT NULL | RESTRICT | PASS |
| commercial.entitlement.capability_id | commercial.license_capability.record_id | NOT NULL | RESTRICT | PASS |
| membership.customer_membership.membership_plan_id | membership.membership_plan.record_id | NOT NULL | RESTRICT | PASS |
| membership.customer_membership.customer_id | customer.customer.record_id | NOT NULL | RESTRICT | PASS (SQL/DB-11) |

Provenance FKs `created_by` / `updated_by` → `identity.user_account.record_id` ON DELETE SET NULL were added by 007 and are present.

`membership.membership_plan_rule.membership_plan_id` is ON DELETE CASCADE in 004. Recorded as physical fact; not changed.

Organization has **zero** FKs to `commercial.*`.

---

## 9. Unique Constraint Validation

| Constraint | Definition | Result |
| ---------- | ---------- | ------ |
| uq_global_master_data_group_code | (reference_group, reference_code) | PASS |
| uq_platform_setting_key_scope | (setting_key, scope_type) | PASS |
| uq_organization_code | (organization_code) | PASS |
| uq_organization_legal_name | (legal_name) | PASS |
| uq_facility_type_code | (facility_type_code) | PASS |
| uq_facility_code_org | (organization_id, facility_code) | PASS |
| uq_site_code_facility | (facility_id, site_code) | PASS |
| uq_subscription_plan_code | (plan_code) | PASS |
| uq_subscription_number | (organization_id, subscription_number) | PASS |
| uq_license_capability_code | (capability_code) | PASS |
| uq_entitlement_capability | (facility_id, license_id, capability_id) | PASS |
| uq_membership_plan_code | (facility_id, plan_code) | PASS |

No unique-on-active-subscription index (application rule; deferred).

---

## 10. Check Constraint Validation

| Constraint | Expression | Result |
| ---------- | ---------- | ------ |
| ck_subscription_dates | ends_at IS NULL OR ends_at >= starts_at | PASS |
| ck_subscription_term_dates | ends_at IS NULL OR ends_at >= starts_at | PASS |
| ck_customer_membership_dates | ends_at IS NULL OR ends_at >= starts_at | PASS |
| ck_feature_flag_rollout | rollout_percentage BETWEEN 0 AND 100 | PASS |
| ck_maintenance_window_dates | ends_at > starts_at | PASS |

No extra business-rule checks were added in this freeze.

---

## 11. Default Validation

| Column | Database default | Model server_default | Notes |
| ------ | ---------------- | -------------------- | ----- |
| tenant.organization.business_status | ACTIVE | ACTIVE | BA/FR create vocabulary remains deferred |
| tenant.facility.facility_status | ACTIVE | ACTIVE | BA Operational / FR Draft remain deferred |
| tenant.facility.subscription_scope_status | PENDING | PENDING | Aligned |
| tenant.site.site_status | ACTIVE | ACTIVE | BA/FR create vocabulary remains deferred |
| commercial.subscription_plan.plan_status | ACTIVE | ACTIVE | Aligned |
| commercial.subscription.subscription_status | PENDING | PENDING | Aligned |
| commercial.license.license_status | ACTIVE | ACTIVE | Aligned |
| tenant.facility_type.is_active | true | true | Aligned |
| created_at | now() | NOW() | Aligned |

Database defaults were not changed to match application create PENDING/DRAFT behavior.

---

## 12. Data Type Validation

| Column | Physical type | Result |
| ------ | ------------- | ------ |
| *.record_id | uuid + gen_random_uuid() | PASS |
| commercial.subscription_plan.plan_payload | jsonb | PASS |
| platform.platform_setting.setting_value | jsonb | PASS |
| tenant.site.address_payload | jsonb | PASS |
| platform/tenant/membership metadata | jsonb | PASS |
| business/lifecycle statuses | varchar | PASS (no ENUMs) |
| timestamps | timestamptz | PASS |
| commercial.subscription_plan.base_price_amount | numeric | PASS |
| tenant.organization.primary_email | citext | PASS |

---

## 13. Seed Data Validation

| Seed | Physical result |
| ---- | --------------- |
| Facility types | SWIMMING_POOL, GYM, YOGA_STUDIO, DANCE_STUDIO, SPORTS_ACADEMY (5) |
| SaaS plan | FOUNDATION / ACTIVE / INR / 0.00 |
| License capabilities | 8 approved module codes |
| global_master_data groups | FACILITY_TYPE 5, STATUS 4, CHANNEL_TYPE 4, CURRENCY 1 |
| platform_setting | 5 approved keys |

No extra plans, facility types, or capabilities were inserted.

Facility Type dual catalog remains: `tenant.facility_type` (authoritative FK target) and `platform.global_master_data` group `FACILITY_TYPE` (reference/display). Both seeded. No sync trigger.

---

## 14. Migration 008 Guard Validation

| Check | Result |
| ----- | ------ |
| 006 did not create campaign_schedule / campaign_delivery / campaign_result / notification_preference / communication_consent / ticket_attachment / ticket_escalation / sla_tracking | PASS (0 rows) |
| 008 completed against those missing tables | PASS |
| 008 did not invent those tables to satisfy ALTERs | PASS |
| Site add-on / platform.configuration tables absent | PASS |
| Obsolete product / plan-version / plan-feature / price-point tables absent | PASS |

---

## 15. Migration Test Results

| Suite | Result |
| ----- | ------ |
| `poetry run pytest tests/migrations` (flag unset) | 10 skipped |
| `DIGITIZE_MIGRATION_TEST=1 PGDATABASE=digitize_foundation_pytest poetry run pytest tests/migrations` | **10 passed** |
| `poetry run pytest tests` (default) | 35 passed, 10 skipped |

Physical tests covered schemas, 30 core tables, obsolete-table absence, FKs, SaaS vs membership separation, JSONB/seeds, Alembic absence, 008 non-invention, and ORM column mapping.

---

## 16. verify_core_contract.sql Result

Executed as part of the runner on databases A, B, and pytest.

**PASS** (PL/pgSQL `DO` completed; RAISE path not taken).

`verify_schema.sql` remains diagnostic SELECTs and does not RAISE on findings.

---

## 17. ORM Smoke Test

Core 30 SQLAlchemy models were imported and checked against `information_schema`.

**PASS:** every core model table exists; every mapped column exists physically.

`Base.metadata.create_all()` was **not** run.

Organization model has no `subscription_id`.

Known ORM-only gaps (not physical blockers):

- `SubscriptionTerm.invoice_id` has no ORM ForeignKey; SQL has FK to `commercial.invoice`
- `CustomerMembership.customer_id` ORM FK still names `customer.customers.customer_id`; SQL FKs `customer.customer.record_id`

Extra ORM models without DDL remain unmapped and were not migrated.

---

## 18. Known Model/DDL Conflicts

| Conflict | Physical | ORM | Blocks freeze? |
| -------- | -------- | --- | -------------- |
| subscription_term.invoice_id | FK to commercial.invoice | UUID, no FK | **No** — keep SQL FK |
| customer_membership.customer_id | FK to customer.customer.record_id | FK to customer.customers.customer_id | **No** — SQL is DB-11; customer ORM alignment deferred |

---

## 19. Deferred Decisions

1. Status vocabulary (ACTIVE vs PENDING/DRAFT/Operational/Closed).
2. Dual Facility Type catalogs (keep both; no sync trigger).
3. DB-05 operating hours / capacity / branding tables.
4. Extra ORM models without DDL.
5. Site Add-ons.
6. Alembic incremental revisions after the stamp baseline (autogenerate remains disabled).
7. Customer and billing ORM table/PK alignment.
8. One-active-subscription-per-facility partial unique index.
9. Remaining communication/support CREATE TABLEs named in DB-11 but absent from 006.
10. Whether `verify_schema.sql` should RAISE.
11. Physical tenancy ADR / RLS.

None of these blocked the empty-database core contract.

---

## 20. Migration-System Decision

```text
Current physical migration path:
database/migrations/001–008

Physical source of truth:
DB-11

Alembic:
single stamp revision db11_foundation_baseline (does not create tables)

ORM:
does not create the production schema
```

Forward application schema changes after this freeze must be designed as SQL forward migrations on this path. Do not autogenerate Alembic from ORM metadata. The 117-revision chain has been removed.

---

## 21. Database Foundation Freeze Decision

```text
DATABASE FOUNDATION FROZEN WITH DEFERRED ITEMS
```

The core physical contract is proven on PostgreSQL. Deferred items do not prevent the next development phase:

```text
Platform Admin Backend Foundation
        ↓
Facility Type Management
        ↓
Digitize SaaS Subscription Plan Management
        ↓
License Capability / Entitlement Management
        ↓
Global Master Data Management
        ↓
Platform Admin APIs
        ↓
Platform Admin Metadata Forms
        ↓
Organization Creation
```

Those features are **not** started by this freeze.

---

## Validation Matrix

| Validation | Result | Evidence |
| ---------- | ------ | -------- |
| Empty DB migration | PASS | Runner 001–008 on `digitize_foundation_a` and `_b` |
| Schemas | PASS | `platform` `tenant` `commercial` `membership` present; obsolete schemas absent |
| 30 core tables | PASS | information_schema 30/30 |
| PKs | PASS | `record_id` uuid + `gen_random_uuid()` |
| FKs | PASS | pg_constraint inventory in §8 |
| Unique constraints | PASS | named uniques in §9 |
| Check constraints | PASS | `ck_subscription_dates` and approved peers |
| Defaults | PASS | ACTIVE/PENDING/is_active/now() as in §11 |
| PostgreSQL data types | PASS | uuid / varchar / jsonb / timestamptz / numeric / citext |
| Seed data | PASS | 5 facility types, FOUNDATION, 8 capabilities, 4 master-data groups |
| 008 guard | PASS | 008 completed; 8 uncreated tables remain absent |
| No invented core schema | PASS | no organization/facility/subscription schemas; no site add-on; no platform.configuration |
| Migration tests | PASS | 10 passed against dedicated pytest database |
| verify_core_contract.sql | PASS | runner DO block on A, B, pytest |
| ORM smoke test | PASS | 30 core models map to existing tables/columns |
| Alembic isolation | PASS | Alembic not run; `alembic_version` absent |
| Reproducibility | PASS | A vs B catalog diff empty (2528 rows) |
