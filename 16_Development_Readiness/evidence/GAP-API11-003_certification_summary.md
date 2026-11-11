# GAP-API11-003 — API-11 reporting certification summary

**Run date:** 2026-11-03 (updated after API-11-009 404 investigation)  
**Environment:** Local PostgreSQL `digitize` (development), Alembic `072_platform_terms_document`, loopback only  
**Application access:** FastAPI via `ASGITransport` with production `get_session` (UnitOfWork commit)  
**Harness:** `scripts/reports_certification_evidence.py` with `DIGITIZE_REPORTS_CERTIFICATION=1` (legacy `DIGITIZE_API11_CERTIFICATION=1`)  
**Raw evidence:** `docs/16_Development_Readiness/evidence/GAP-API11-003_certification_run_2026-11-03.jsonl`

## API-11-009 HTTP 404 — root cause (2026-11-03 follow-up)

**Classification:** Test-harness defect — **not** a product/backend bug.

The initial certification run overrode `get_session` with a generator that **yielded a session but never committed** (`UnitOfWork.commit()` in `app.api.deps.get_session` was bypassed). Each report run flushed an `execution_id` into the HTTP response, then **rolled back** when the request ended. The subsequent export request correctly looked up `ReportExecution` by id, found nothing, and returned **404 RESOURCE_NOT_FOUND**.

**Fix:** Remove the `get_session` override from the certification harness; only override `load_authorized_principal`. **Regression:** `tests/reports/test_reports_export_http_digitize.py` (`DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1`; legacy `DIGITIZE_API11_EXPORT_HTTP_TEST=1`).

**After fix:** HTTP export returns **403** (Advanced Reporting not enabled on Acme) — execution is found; entitlement gate works. PDF export returns **422** (`That export format is not available for this report.`).

## Environments not used (blockers)

| Target | Blocker |
| --- | --- |
| Deployed QA/staging HTTP API | No reachable `/health` on localhost:8000/8080; services not started (per execution rules) |
| `digitize_test` + `DIGITIZE_API_TEST=1` | Alembic at **036** (head **071** required); EQ-011 preflight **NOT READY** |
| Flutter → live API E2E | Not executed; UI covered by widget tests only (GAP-API11-002) |
| Export **byte** success (200 + attachment) | Acme org has **no** active `advanced_reporting` entitlement — not modified without authorization |

## Scenario results (latest run)

| ID | Status | Notes |
| --- | --- | --- |
| ENV-001 | pass | `advanced_reporting_active=False` on Acme |
| A-001, A-002 | pass | Catalogue |
| C-001, C-002 | pass | Run + date validation |
| D-001…D-003 | **blocked** | HTTP export **403** entitlement (execution found) |
| D-004 | pass | PDF → **422** validation |
| B-001 | blocked | Unknown org → 404 |
| B-002, E-001 | pass | Facility revenue; permission gate |
| SVC-D-001, SVC-D-004 | pass | Service-layer entitlement + PDF rejection |

**Tally:** pass 10 · blocked 4 · fail 0

## Supplementary automated evidence

| Suite | Count | Label |
| --- | ---: | --- |
| `test_reports_export_http_digitize.py` | 4 passed | HTTP run→export regression (real `get_session`) |
| `test_reporting_routes.py` + rules + decisions | 33 passed | Route/auth unit |
| `DIGITIZE_REPORTING_SQL_TEST=1` | 14 passed | Read-only SQL integration |
| `digitize-ui` reporting widget tests | 21 passed | Widget only |

## Integration-verification label

- **API integration verified (exports):** Catalogue, run, validation, permissions, facility scope, HTTP export bytes with entitlement fixture — local `digitize` + ASGI (`test_reports_export_http_digitize.py` **5 passed** Phase 9 re-run).
- **Not verified:** Deployed QA; `digitize_test` live suite; Flutter E2E against deployed API.

## Phase 9 — scheduled delivery (2026-11-07)

| Item | Status |
| --- | --- |
| Schedule worker + delivery rows | **TESTED** — `test_report_schedule_worker.py` |
| GAP-API11-001 external email | **BLOCKED (provider)** — `HeldReportNotifier` |
| Consolidated evidence | `docs/07_API_Collections/API-11_Acceptance_Evidence.md` |

## Follow-up

1. Authorize production SMTP/SES notifier to replace `HeldReportNotifier` (GAP-API11-001 / GAP-INT-002).
2. Optional QA deploy + Flutter E2E when environment is available.
