# EQ-011 post-migration test reconciliation — 2026-11-08

**Database:** `digitize_test` @ `localhost`, revision `083_support_ticket_escalation` (preflight **READY**).  
**Continues:** [MASTER_APPROVAL_EXECUTION_REPORT_2026-11-08.md](./MASTER_APPROVAL_EXECUTION_REPORT_2026-11-08.md)

## Failure → root cause → fix

| # | Symptom | Cause class | Root cause | Fix |
| --- | --- | --- | --- | --- |
| 1 | 12× org create 422 | Stale fixture | Org create now requires legal identity at POST (`_require_legal_identity_for_activation`) | `_create_org` supplies GSTIN/PAN/CIN; `_ensure_legal_identity` skips PATCH when masks present |
| 2 | 12× site/subscription 403 | Stale fixture / DR-021 | Platform Admin cannot perform tenant operational routes | `_ready_org_facility` uses `_scoped_headers` with org/facility/site + subscription permissions; API-09 calls use `ctx["tenant_headers"]` |
| 3 | Catalog `== 8` capabilities | Stale expectation | Migration `039` seeds `advanced_reporting` (add-on, not foundation bundle) | `expected_license_capability_codes()` in `catalogs.py`; tests assert full expected set |
| 4 | Entitlements `9 == 8` | Stale expectation | `resolve_capabilities` grants all active catalog rows when plan has no capability list | Test counts `expected_license_capability_codes()` |
| 5 | Expire 409/404 | Test bug | Auto-replace used wrong ctx on expire after `ctx2` flow | `headers=_tenant_headers(ctx2)` on expire |
| 6 | validate-login `valid` | Stale expectation | Tenant with facility but no license: `valid=False` per `LicenseService.validate_login` | Assert `valid is False` for pre-subscription case |
| 7 | Facility types catalog | Integration DB drift | Prior API-09 runs left extra `FT-*` rows; default page omitted approved codes | Paginate facility-types list; assert approved ⊆ codes |

**No backend product-rule changes.** No capability additions or removals in migrations.

## Files changed

- `app/modules/platform/catalogs.py` — `LICENSE_CAPABILITY_MIGRATION_ADDONS`, `expected_license_capability_codes()`
- `tests/api/test_organization_facility_site.py` — org create legal identity, legal identity skip, DR-021-safe helpers
- `tests/api/test_subscription_license.py` — tenant headers, entitlement counts, validate-login, ctx2 expire
- `tests/api/test_platform_catalog.py` — license capabilities + facility-type pagination
- `tests/reports/test_report_mailpit_integration.py` — opt-in Mailpit IV

## Tests executed

```bash
# EQ-011 core (digitize_test)
DIGITIZE_API_TEST=1 DB_NAME=digitize_test DB_HOST=localhost \
  poetry run pytest tests/api/test_subscription_license.py tests/api/test_platform_catalog.py -q
# 73 passed, 1 skipped

# Support escalation regression (digitize)
DIGITIZE_SUPPORT_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  poetry run pytest tests/support/test_support_tickets_digitize_postgres.py tests/support/test_escalation_service.py -q
# 4 passed

# Mailpit report delivery (local)
DIGITIZE_MAILPIT_REPORT_TEST=1 poetry run pytest \
  tests/reports/test_report_mailpit_integration.py tests/reports/test_report_email_delivery.py -q
# 5 passed (Mailpit listening on 127.0.0.1:1025)
```

## Mailpit

| Check | Result |
| --- | --- |
| Listener | **UP** on `127.0.0.1:1025` |
| `SmtpReportNotifier` E2E | **SENT** (opt-in `DIGITIZE_MAILPIT_REPORT_TEST=1`) |
| HELD without SMTP | **Verified** in unit tests |

## Remaining blockers

- **Shared QA certification** (`GAP-API01-002`) — local green does not certify shared RDS/QA.
- **Global product readiness** — unchanged (legal invoice, production providers, etc.).
