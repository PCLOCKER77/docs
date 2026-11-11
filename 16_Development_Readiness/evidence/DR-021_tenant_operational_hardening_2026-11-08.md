# DR-021 — Platform Admin tenant operational hardening (residual)

**Date:** 2026-11-08  

## Problem

`has_platform_assignment` made `can_access_organization` / `can_access_facility` / `can_access_site` return true for any tenant scope, allowing PA to reach operational APIs when permissions were seeded broadly (customer CRM fixed in GAP-AUTH-002; same class elsewhere).

## Fix strategy

1. **`app/core/access.py`**
   - `deny_platform_tenant_operational_access`
   - `require_tenant_operational_organization_access` (governance org **get**/lifecycle unchanged)
   - `require_facility_access` / `require_site_access` call deny before scope checks

2. **Operational modules** switched org checks to `require_tenant_operational_organization_access` where appropriate (billing, attendance, membership, facility, identity staff, subscription tenant paths, communication, campaign, support escalation, org tenant update/settings/T&C accept).

3. **`attendance/repository.scope_clause`** returns `false()` for PA (defense in depth).

## Preserved governance

- `require_organization_access` unchanged for PA company **GET**, activate/suspend/archive/restore, governance-summary, platform routes.

## Tests

| Suite | Result |
| --- | --- |
| `tests/security/test_dr021_tenant_operational_access.py` | **7 passed** |
| `tests/security/` (full) | **29 passed** |
| `DIGITIZE_PLATFORM_ADMIN_PG_TEST=1` security + governance PG | **8 passed** |
