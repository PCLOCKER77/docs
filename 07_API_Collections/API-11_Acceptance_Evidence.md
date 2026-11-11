# API-11 Reports & Analytics — Acceptance Evidence

**Document ID:** API-11-EVIDENCE  
**Last updated:** 2026-11-07 (Phase 9 — scheduled delivery verification)  
**Status:** PARTIALLY VERIFIED (exports + schedule execution; external email delivery blocked)

## Evidence legend

| Label | Meaning |
|-------|---------|
| **PASS** | Executed tests or live PostgreSQL IV cited below |
| **BLOCKED** | Provider or product gate — see DEV-21 |
| **NOT VERIFIED** | No safe mutating IV for that claim |

## Operation summary (12 numbered)

| Area | Backend | Flutter | Tests | Status |
|------|---------|---------|-------|--------|
| Catalogue / run / export | `ReportingService` + routes | Company reports page | `test_reporting_*`, export HTTP IV | **Implemented** / **Integration-verified** (exports) |
| Schedule CRUD (API-11-010) | `tenant_report_schedule` (mig **039**) | Schedules UI (where wired) | `test_reporting_decisions.py`, SQL IV | **Implemented** / **Tested** |
| Schedule execution | `worker.run_due_schedules` | — | `test_report_schedule_worker.py` + rules in decisions | **Implemented** / **Tested** |
| Schedule email delivery | `HeldReportNotifier` | — | Unit HELD/FAILED/SENT semantics | **BLOCKED** — GAP-API11-001 (SMTP/SES provider) |

**Migration note:** Alembic repository head **082**; tenant scheduling objects from **039_reporting_schedules** (distinct from legacy `reporting.report_schedule`).

## GAP closure map

| Gap ID | Status | Evidence |
|--------|--------|----------|
| GAP-API11-001 | **BLOCKED (provider)** | Worker calculates + records delivery `HELD`; no authorized outbound email |
| GAP-API11-002 | **TESTED** | Flutter PDF limitation UX — 21 widget tests |
| GAP-API11-003 | **INTEGRATION_VERIFIED** | `test_reports_export_http_digitize.py` |
| GAP-API11-004 | **Closed** | Catalog FE metadata |

## Live PostgreSQL (exports — GAP-API11-003)

**Guard:** `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1`, `DB_NAME=digitize`, loopback, production `get_session`.

**Suite:** `tests/reports/test_reports_export_http_digitize.py` — run → export HTML bytes with temporary Advanced Reporting entitlement; cross-org export **404**.

## Scheduled delivery (GAP-API11-001)

| Behavior | Evidence |
|----------|----------|
| Monthly cadence + timezone | `due_action` / `previous_calendar_month` in `test_reporting_decisions.py` |
| Run idempotency (`uq_report_schedule_run_period`) | `worker._run_one` + SQL IV `test_schedule_foundation_relations_exist` |
| Calculation vs delivery separated | Failed calc → `calculation_status=FAILED`; delivery rows independent |
| Default notifier | `HeldReportNotifier` → `delivery_status=HELD` (not SENT) |
| Failed provider | `_deliver` → `delivery_status=FAILED` — `test_report_schedule_worker.py` |
| No duplicate SENT | `delivery_plan("SENT")` → skip — `test_deliver_skips_recipient_when_already_sent` |
| Org scope on schedule CRUD | `ReportingService.create_schedule` / recipient checks — `service.py` |

**Not claimed:** Production email/SES delivery; cron deployment; end-user receives report in inbox.

## Regression commands (Phase 9 — 2026-11-07)

```bash
cd digitize-services
python3 -m pytest tests/reports/ -q

DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1 DB_HOST=localhost DB_PORT=5434 \
  DB_USER=digitize_app DB_NAME=digitize ENVIRONMENT=development \
  python3 -m pytest tests/reports/test_reports_export_http_digitize.py -q

DIGITIZE_REPORTING_SQL_TEST=1 DB_HOST=localhost DB_PORT=5434 \
  DB_USER=digitize_app DB_NAME=digitize ENVIRONMENT=development \
  python3 -m pytest tests/reports/test_reporting_sql_integration.py -q

cd digitize-ui
flutter test test/features/reporting/ -r compact
```

## Security / tenant isolation (test-backed)

| Check | Evidence |
|-------|----------|
| `report.view` / export permissions | `test_reporting_routes.py` |
| Cross-org export | `test_cross_organization_export_is_not_found` |
| Facility scope filters | `test_reporting_rev2a_financial.py`, certification B-002 |
| Schedule org ownership | `schedule.organization_id != scope` → 404 on recipient APIs |
| Advanced entitlement gate | export HTTP **403** without entitlement |

## Out of scope (unchanged)

PDF renderer, new delivery providers, QA/RDS runs, Flutter live E2E against deployed API.
