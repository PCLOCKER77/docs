# GAP-TXN-002 — `get_session` override inventory (2026-11-03)

| Location | Class | Lifecycle | Action |
| --- | --- | --- | --- |
| `scripts/reports_certification_evidence.py` | C — certification | Production `get_session` (no override) | Fixed GAP-API11-003; doc → `asgi_session_helpers` |
| `tests/reports/test_reports_export_http_digitize.py` | A — integration | Production `get_session` | Explicit `clear_get_session_override` |
| `tests/billing/test_billing_invoices_revenue_live_digitize.py` | A — integration | Production (no `get_session` override) | No change |
| `tests/reports/test_reporting_routes.py` | B — unit HTTP | `install_unit_test_session_stub` | Standardized |
| `tests/attendance/test_otp_lifecycle.py` | B — unit HTTP | stub | Standardized |
| `tests/attendance/test_access_token_lifecycle.py` | B — unit HTTP | stub | Standardized |
| `tests/subscription/test_subscription_plan_bulk_create.py` | B — unit HTTP | stub | Standardized |
| `tests/api/test_saas_plan_price_versions.py` | B — unit HTTP | stub + `get_platform_session` stub | Standardized |

Shared helper: `tests/api/asgi_session_helpers.py`  
Regression: `tests/infrastructure/test_get_session_uow_lifecycle.py`  
Reuse: `tests/reports/test_reports_export_http_digitize.py` (API-11 run→export)
