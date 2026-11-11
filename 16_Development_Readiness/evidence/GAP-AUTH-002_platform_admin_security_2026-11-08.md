# GAP-AUTH-002 — Platform Admin security regression

**Date:** 2026-11-08  
**Authority:** DR-021, AUTH_CONTRACT_FREEZE, ORGANIZATION_ONBOARDING_PA_BOUNDARY_FREEZE  

## Boundaries verified

| Boundary | Mechanism | Evidence |
| --- | --- | --- |
| Governance-only PA | Flutter `authPermissionProvider` + route policy; API `has_platform_assignment` on governance reads | Flutter **10** passed; backend unit + PG |
| No tenant checkout impersonation | `_deny_platform_impersonation` in SaaS commerce | `test_platform_admin_security_regression.py` |
| No tenant customer CRM | `_deny_platform_tenant_customer_access` (defect fix) | PG `GET /customers` → **403** |
| No tenant facility settings mutation | `deny_platform_admin_tenant_facility_setting_mutation` | existing + regression suite |
| No DEK HTTP surface | Approved API registry scan | no `dek` / `unwrap` paths |
| JWT ≠ assignment | `unprivileged_admin_headers` + `load_platform_principal` DB load | PG + unit |
| Support tickets | `_require_tenant_operator` rejects PA | unit |
| No DEK in catalog extras | Registry static test | unit |

## Defect fixed

**Platform Admin customer search/list** previously succeeded when `organization_id` was supplied because `has_platform_assignment` satisfied `require_organization_access`. Fixed in `CustomerService` with `_deny_platform_tenant_customer_access` (DR-021).

## Tests added

- `tests/security/test_platform_admin_security_regression.py` (unit/service)
- `tests/security/test_platform_admin_security_digitize_postgres.py` (HTTP on local `digitize`)

## Commands and results

| Suite | Result |
| --- | --- |
| `poetry run pytest tests/security/ -q` | **16 passed**, 5 PG skipped without env |
| `DIGITIZE_PLATFORM_ADMIN_PG_TEST=1` … `tests/security/test_platform_admin_security_digitize_postgres.py` + governance supplement | **7 passed** (5 new + 2 existing) |
| `flutter test …/platform_admin_operational_boundary_test.dart` | **10 passed** |
| Bundle: security + media PA + facility authz + inbox + customer PII | **pass** (after PII test fixture fix) |

## GAP status

**Implemented — regression suite + one production defect fixed (customer PA deny).**
