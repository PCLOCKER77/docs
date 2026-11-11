# API-14 — Reference data source-of-truth recommendation

**Status:** **Approved (2026-11-09)** — GMD groups COUNTRY, STATE_REGION, LANGUAGE, TIMEZONE, ACTIVITY_TYPE; org activity types; versioned localization (mig **085**).  
**Inventory:** 6/12 **Implemented**. **Recommendation date:** 2026-11-02.  
**Tracker:** [DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md).

## Implemented (do not reinvent)

| ID | Path | Source of truth |
| --- | --- | --- |
| API-14-003 | `/reference/currencies` | `platform.global_master_data` group `CURRENCY` |
| API-14-006 | `/reference/facility-types` | `tenant.facility_type` (alias of `GET /facility-types`) |
| API-14-008 | `/reference/status-values` | GMD group `STATUS` |
| API-14-009 | `/reference/payment-methods` | App constant `APPROVED_OFFLINE_PAYMENT_METHODS` |
| API-14-010 | `/reference/communication-channels` | App constant `APPROVED_CHANNEL_CODES` |
| API-14-011 | `/reference/lookup-values/{group}` | Approved GMD groups only |

Tenant-readable GMD expansion already includes `ORGANIZATION_TYPE`, `CURRENCY`, `STATUS`.

## Remaining (6) — smallest sustainable source

| ID | Path | Recommended source | Migration needed? | Product decision |
| --- | --- | --- | --- | --- |
| API-14-001 | countries | New GMD group `COUNTRY` + approved seed codes | **Yes** (seed + optional expand tenant-readable) | Approve ISO country set / subset |
| API-14-002 | states-regions | New GMD group `STATE_REGION` (country-scoped metadata) **or** defer until country exists | **Yes** | Country FK / parent code rule |
| API-14-004 | languages | New GMD group `LANGUAGE` + BCP-47 / ISO codes | **Yes** | Code list |
| API-14-005 | timezones | **Curated** GMD group `TIMEZONE` of IANA names used by Digitize (not full `zoneinfo` dump) | **Yes** for durability; avoid unbounded stdlib listing without approval | Curated vs full IANA |
| API-14-007 | activity-types | **Not** `facility.activity_program` (tenant ops data). Prefer GMD `ACTIVITY_TYPE` seed **or** declare out of Phase-1 if product means training activities | Likely **Yes** | Which domain owns “activity type”? |
| API-14-012 | localization | **Not** a free-form reference list of `platform_setting` LOCALIZATION without PA governance. Prefer explicit DTO of supported locales/timezones from approved settings keys, or GMD | Maybe | Reference list vs PA settings read |

## Rules

- Do **not** alias facility-types through GMD `FACILITY_TYPE`; FK catalog is `tenant.facility_type`.
- Do **not** invent numbered APIs or arbitrary tables outside Alembic + twin conventions.
- Create/update of GMD remains Platform Admin; tenant reads stay active-only for expanded groups.

## Decision asked of product

Approve (1) country/language/timezone curated GMD seeds, (2) activity-type ownership, (3) localization as settings snapshot vs GMD — then authorize a single additive migration twin for the approved groups only.
