# API-01 Platform Administration — Acceptance Evidence

**Document ID:** API-01-EVIDENCE  
**Last updated:** 2026-11-07 (Phase 10 — Platform Admin completion)  
**Status:** PARTIALLY VERIFIED (local governance IV; shared QA certification blocked)

## Gap map

| Gap ID | Status | Evidence |
|--------|--------|----------|
| GAP-API01-001 | **IMPLEMENTED** / **TESTED**; **INTEGRATION_VERIFIED** (local `digitize` governance IV) | Flutter `/platform/console`; `test_platform_admin_governance_digitize_postgres.py` |
| GAP-API01-002 | **BLOCKED** / **AWAITING_AUTHORIZATION** | EQ-011 on `digitize_test` / shared QA — not run in Phase 10 |
| GAP-API01-003 | **Closed** | `test_collection_metadata_drift.py` |

## Workflows verified (Phase 10)

| Workflow | Backend | Flutter / unit |
|----------|---------|----------------|
| PA platform settings/health/ops | `test_platform_admin.py` (opt-in `digitize_test`) | `platform_console_page_test.dart` |
| Org create → PENDING | HTTP IV on `digitize` | Companies create UX |
| OA provision when requested | IV creates admin + credential template | create form tests |
| PA governance summary | HTTP **200** scoped to org | — |
| OA denied platform routes | **403** `AUTHORIZATION_DENIED` | `platform_admin_operational_boundary_test.dart` |
| PA denied tenant billing history | **403** on `/billing/history` | PA operational boundary |
| Onboarding phase rules | `test_onboarding_review.py` | — |

## PostgreSQL integration (local `digitize`)

**Guard:** `DIGITIZE_PLATFORM_ADMIN_PG_TEST=1`, `ENVIRONMENT=development`, `DB_NAME=digitize`, loopback, no `DATABASE_URL`.

**Suite:** `tests/api/test_platform_admin_governance_digitize_postgres.py` — synthetic `digitize-iv-platform-admin-*` org rows; no broad teardown on shared seed data.

**EQ-011 / `digitize_test`:** Documented live API-01 batch remains on `DIGITIZE_API_TEST=1` + `DB_NAME=digitize_test` per `live_db_guard.py` — **not** re-run until TEST-13 authorization.

## Regression commands (2026-11-07)

```bash
cd digitize-services
python3 -m pytest tests/organization/test_onboarding_review.py \
  tests/modules/media/test_authz_platform_admin.py \
  tests/subscription/test_saas_platform_invoice_access.py -q

DIGITIZE_PLATFORM_ADMIN_PG_TEST=1 DB_HOST=localhost DB_PORT=5434 \
  DB_USER=digitize_app DB_NAME=digitize ENVIRONMENT=development \
  python3 -m pytest tests/api/test_platform_admin_governance_digitize_postgres.py -q

cd digitize-ui
flutter test test/features/platform_administration/ \
  test/features/authentication/platform_admin_operational_boundary_test.dart -r compact
```

## Out of scope (unchanged)

Shared QA/RDS, DR-021 rule changes, Platform Admin tenant CRM/billing access, impersonation.
