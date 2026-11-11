# GAP-ROLE-003 — Platform Admin scoped audit reads

**Date:** 2026-11-08

## Permissions verified

| Operation | Permission | Org scope |
| --- | --- | --- |
| `audit_events_list` | `report.view` | `organization_id` query (governance) |
| `audit_events_export_create` | `report.view` | same |
| `audit_analytics_list` | `report.view` | same |

Platform Admin requires an active **PLATFORM** role assignment **and** `report.view`. Org-scoped query is required; repository always filters `audit.audit_event.organization_id`.

Governance access uses `require_governance_organization_access` (not tenant operational deny). Tenant operational APIs (e.g. `GET /billing/history`) remain **403** for PA (DR-021).

## Defects found and fixed

No authorization logic bug in audit reads. Clarified governance path:

- `app/core/access.py` — `require_governance_organization_access` documents DR-021 split.
- `app/modules/audit/read_service.py` — uses governance helper for list, analytics, export.

## PostgreSQL integration

| Command | Result |
| --- | --- |
| `DIGITIZE_AUDIT_PG_TEST=1 … pytest tests/audit/test_audit_reads_digitize_postgres.py tests/audit/test_audit_platform_admin_digitize_postgres.py -q` | **8 passed** |

New file: `tests/audit/test_audit_platform_admin_digitize_postgres.py` (PA with `report.view`, PA without, unassigned JWT, tenant billing denial, export/analytics, row org filter on export).

## Regression

| Suite | Result |
| --- | --- |
| `pytest tests/audit/ -q` | **11 passed**, 8 skipped (opt-in PG off) |
| `pytest tests/security/test_dr021_tenant_operational_access.py tests/security/test_platform_admin_security_regression.py -q` | **25 passed** |

## Status

**GAP-ROLE-003:** **INTEGRATION_VERIFIED** (local `digitize`, 2026-11-08). Flutter nav work remains **Implemented / Tested** from 2026-11-03.
