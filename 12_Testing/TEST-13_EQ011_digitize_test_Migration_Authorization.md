# TEST-13 EQ-011 — `digitize_test` Migration Authorization Plan

**Document ID:** TEST-13  
**Folder:** `12_Testing`  
**Status:** **Proposal only — Awaiting authorization.** Not an approved migration. **Do not apply** until explicitly authorized.  
**Related:** [DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md), [TEST-12](TEST-12_Engineering_Quality_QA_Readiness_Review_2026-11-02.md) (EQ-011 finding)  
**Scope:** PostgreSQL database `digitize_test` on the local development host only.  
**Out of scope:** `digitize`, `digitize_mig_cold`, QA RDS, any production database.

EQ-011 remains **Blocked** / **Awaiting authorization** and is **not** integration-verified.

## 1. Confirmed read-only preflight (2026-11-02, re-verified)

Commands used (no writes):

```bash
DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run python scripts/eq011_digitize_test_preflight.py
DB_NAME=digitize_test PGDATABASE=digitize_test poetry run alembic current
poetry run alembic heads
```

| Item | Confirmed value |
| --- | --- |
| Target DB | `digitize_test` @ `localhost` (preflight prints `probing database=digitize_test`) |
| Connection guard | Script refuses unless `DB_NAME`/`PGDATABASE` **and** `Settings.DB_NAME` equal `digitize_test` |
| Current Alembic revision | **`036_facility_feature_values_unique`** |
| Repository head | **`071_support_center_foundation`** (single head) |
| Lineage | `036` is an ancestor of `071` (36 upgrade revisions: `037` … `071`) |
| Twin files | All 36 upgrade steps have matching `migrations/versions/*.py` and `migrations/sql/*.sql` |
| `identity.user_account.display_name_ciphertext` | **Absent** on `digitize_test` |
| Live-guard `SWIMMING_POOL` | Present (count 1) |
| Live-guard `commercial.license_capability` | Present (count 8) |
| `identity.email_outbox` / `password_reset_request` / `tenant.organization` | Present |
| Preflight result | **NOT READY** (exit 1) — expected until authorized upgrade |

Configured application `.env` may still default to `DB_NAME=digitize`. Live EQ-011 **must** override to `digitize_test`. Never point EQ-011 at `digitize`.

## 2. Is migration 043 sufficient?

**No — not for a reliable EQ-011 + current ORM run.**

| Question | Answer |
| --- | --- |
| Column that failed EQ-011 | Added in **`043_identity_staff_pii_encryption`** SQL twin (`ADD COLUMN IF NOT EXISTS display_name_ciphertext`; `display_name` made nullable; default `LEGACY_PLAINTEXT`; **no backfill**) |
| Safe stop at 043? | **Not recommended.** Code under test expects later additive schema through support foundation **`071`**. |
| Recommended authorized target | **`alembic upgrade head`** → `071_support_center_foundation` |

## 3. Migration character (037–071) — confirmed scan

- Read-only scan of all 36 SQL twins for `DROP TABLE`, `TRUNCATE`, `DELETE FROM`, `DROP COLUMN`: **zero hits**.
- Material but expected side effects: additive tables/indexes/columns and permission seed inserts (billing, notifications, support, training, PII ciphertext columns).
- `043` specifically addresses the missing ciphertext column without rewriting existing display names.

Still treat as **irreversible without a restore plan** for `digitize_test`.

## 4. Safe recovery procedure (before/after authorized apply)

1. **Before upgrade (authorized operator):** take a PostgreSQL logical dump of `digitize_test` only, e.g. `pg_dump -Fc digitize_test > digitize_test_pre_eq011.dump`.
2. **Preferred recovery:** restore that dump into `digitize_test` if the upgrade misbehaves.
3. **Not preferred:** `alembic downgrade` — revision `downgrade()` functions exist on sampled migrations (including `043` and `071`) but are **not** the approved recovery path for integration databases.
4. Do not recover by migrating `digitize` or creating a new database without separate authorization.

## 5. Live-test / catalog prerequisites (after upgrade)

From `tests/api/live_db_guard.py`:

1. `DB_NAME=digitize_test` and `PGDATABASE=digitize_test`.
2. `DIGITIZE_API_TEST=1`.
3. `SWIMMING_POOL` facility type — **already present**.
4. `commercial.license_capability` catalog — **already present** (8 rows).
5. Org-type GMD rows — expected from earlier seeds; if missing after upgrade, fail clearly (do not invent seeds here).

## 6. Exact command awaiting authorization

Run **only** after written authorization scoped to **`digitize_test`**:

```bash
cd digitize-services

DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run alembic current
# expect: 036_facility_feature_values_unique

DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run alembic upgrade head

DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run alembic current
# expect: 071_support_center_foundation (head)

DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run python scripts/eq011_digitize_test_preflight.py
# expect: READY
```

**Authorization required:** Explicit approval to apply Alembic revisions `037` through `071` **only** on local PostgreSQL database `digitize_test` (not `digitize`, not QA, not production).

## 7. Verification after authorized upgrade

```bash
cd digitize-services

poetry run pytest tests/organization/test_eq011_onboarding_auth_e2e.py -q
# expect: 1 skipped (without DIGITIZE_API_TEST)

DIGITIZE_API_TEST=1 DB_NAME=digitize_test PGDATABASE=digitize_test \
  poetry run pytest tests/organization/test_eq011_onboarding_auth_e2e.py -q
```

**PASS criteria:** exit 0; **1 passed**; org create → memory setup email → password confirm → login → site/staff blocked while inactive; inventory still **228**.

## 8. Explicit non-actions

- Do not create a new database.
- Do not migrate `digitize` or QA.
- Do not truncate or reseed broadly.
- Do not commit/push/deploy as part of this authorization.
- Do not mark EQ-011 **Integration-verified** until the live test above passes.
