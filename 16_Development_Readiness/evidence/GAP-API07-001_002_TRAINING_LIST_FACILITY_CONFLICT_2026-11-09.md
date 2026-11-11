# GAP-API07-001 / GAP-API07-002 — Batch enrollment list and facility/site schedule conflicts

**Date:** 2026-11-09  
**Status:** **Implemented / Tested / Integration-verified (local `digitize`, sequential facility rules)**  
**Frozen inventory:** **228** numbered operations unchanged — additive `GET` only.

## GAP-API07-001 — Batch enrollment list / reload

### PostgreSQL on `digitize` (extended GAP-API07-004 suite)

```bash
cd digitize-services
ENVIRONMENT=development \
DB_HOST=localhost DB_PORT=5434 \
DB_USER=digitize_app DB_PASSWORD='***' \
DB_NAME=digitize \
DIGITIZE_TRAINING_PG_TEST=1 \
python3 -m pytest tests/training/test_training_programs_digitize_postgres.py -q
```

**Result:** **1 passed** — includes:

| Check | Result |
| --- | --- |
| POST enroll (existing) | PASS |
| GET `/batches/{id}/enrollments` pagination | PASS |
| `status=ACTIVE` filter | PASS |
| `customer_id` filter | PASS |
| Empty filter after remove | PASS |
| Cross-org list denied (`403`/`404`) | PASS |

### Flutter

`BatchDetailPage` — load, refresh, empty/error; mock `listBatchEnrollments`.

## GAP-API07-002 — Facility/site schedule conflict enforcement

### Recorded rule (unchanged)

- Same `organization_id`, `facility_id`, and **matching `site_id`** (`NULL` matches `NULL` only).
- Facility-level (`site_id` null) and site-specific bookings are **separate resources** — no cross-blocking (open product decision if that should change).

### PostgreSQL on `digitize` (sequential, real enforcement path)

In the same GAP-API07-004 run:

| Scenario | Expected | Result |
| --- | --- | --- |
| Facility-level + site-specific overlap (different trainers) | Both `201` | **PASS** |
| Second site-specific overlap | `409` `FACILITY_SCHEDULE_CONFLICT_001` | **PASS** |
| Trainer BR-TRN-008 on same trainer | Preserved (409 if same trainer/time) | **PASS** (isolated with second trainer) |

### Unit tests

```bash
python3 -m pytest \
  tests/training/test_facility_schedule_conflict.py \
  tests/training/test_trainer_schedule_conflict_enforcement.py -q
# 16 passed combined with membership list unit tests in regression slice
```

### Opt-in PostgreSQL **concurrency** (real advisory locks + overlapping PTR)

**Module:** `tests/training/test_facility_schedule_concurrency_postgres.py`  
**Guard:** `DIGITIZE_FACILITY_SCHEDULE_CONCURRENCY_PG_TEST=1`, `DB_NAME=digitize_trainer_concurrency`, loopback only.

**Attempted 2026-11-09:**

```bash
ENVIRONMENT=development DB_HOST=localhost DB_PORT=5434 \
DB_USER=digitize_app DB_NAME=digitize_trainer_concurrency \
DIGITIZE_FACILITY_SCHEDULE_CONCURRENCY_PG_TEST=1 \
python3 -m pytest tests/training/test_facility_schedule_concurrency_postgres.py -v
```

**Blocker (not bypassed):**

1. Database `digitize_trainer_concurrency` **does not exist** on local PostgreSQL (`asyncpg.exceptions.InvalidCatalogNameError`).
2. `CREATE DATABASE digitize_trainer_concurrency` **failed** — `digitize_app` has **permission denied to create database**.

**Conclusion:** Real concurrent transaction / advisory-lock overlap verification is **NOT VERIFIED** in this session. Tests are present and fail-closed on missing disposable DB (same pattern as trainer concurrency).

**To run when authorized:** DBA creates `digitize_trainer_concurrency`, apply Alembic head, optionally clone minimal tenant seed, set:

- `TRAINER_CONCURRENCY_ORG_ID=11c32018-0ca8-458b-9cb1-6d644df879a9`
- `TRAINER_CONCURRENCY_FACILITY_ID=de08d511-7dca-486e-b80c-69e357bd5ed7`
- `TRAINER_CONCURRENCY_TRAINER_ID` / `TRAINER_CONCURRENCY_TRAINER_B_ID` (two active trainers)
- `TRAINER_CONCURRENCY_CUSTOMER_ID`
- `TRAINER_CONCURRENCY_SITE_ID` (for null vs site cross-block test)

## Migrations

None for gap implementation.

## Open product decision

Cross-blocking between facility-level (`site_id` null) and a specific site at the same facility — **not implemented** (by design).
