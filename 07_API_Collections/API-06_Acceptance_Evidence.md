# API-06 Attendance & Walk-in — Acceptance Evidence

**Document ID:** API-06-EVIDENCE  
**Last updated:** 2026-11-03  
**Registry:** 15/15 numbered operations **BACKEND_IMPLEMENTED**.

## Legend

Same as API-05 evidence doc.

## Operation coverage

Desk check-in/out, eligibility, session alias, reports (API-06-009), walk-in identify/charge/pay path, audit extras — see `test_contract_registry.py`. Flutter attendance desk + reports + walk-in **Implemented** / **Tested** (mock/fake repos).

## PostgreSQL integration (local `digitize`)

| Gap | Command | Result |
|-----|---------|--------|
| GAP-API06-003 | `DIGITIZE_ATTENDANCE_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost pytest tests/attendance/test_attendance_desk_digitize_postgres.py -q` | **PASS** (2026-11-03) |

**Workflow verified:** active membership (via shared bootstrap) → eligibility → check-in → duplicate check-in **409** → reports `counts_by_status` → check-out → walk-in identify (site created/activated in test).

**Guard:** `tests/attendance/attendance_digitize_pg_guard.py`. Legacy env `DIGITIZE_API06_PG_TEST=1` still accepted.

## Blocked / deferred

| Item | Status |
|------|--------|
| GAP-API06-004 OTP/QR provider QA | **Blocked** (live SMS/provider) |
| Session remarks historical read | **Documented** — operational notes not on read APIs |

## Regression

```bash
cd digitize-services
python3 -m pytest tests/attendance/ -q

cd digitize-ui
flutter test test/features/attendance/ -r compact
# 111 passed (2026-11-03 run)
```

## Module status

**15/15 backend live**; desk Flutter **Tested**. **Integration-verified** for GAP-API06-003 desk/report/identify path on local `digitize`. **Not** full provider OTP/QR certification.
