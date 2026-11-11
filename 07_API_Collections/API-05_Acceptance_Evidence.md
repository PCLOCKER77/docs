# API-05 Membership — Acceptance Evidence

**Document ID:** API-05-EVIDENCE  
**Last updated:** 2026-11-03  
**Registry:** 12/12 numbered operations **BACKEND_IMPLEMENTED** (contract registry).

## Legend

| Label | Meaning |
|-------|---------|
| **PASS** | Automated tests or documented PostgreSQL IV |
| **MOCK** | In-memory / stub session tests |
| **DEFERRED** | Product decision — not a defect |
| **NOT VERIFIED** | No opt-in PG IV for that claim |

## Operation coverage

All API-05-001 … API-05-012 paths registered in `test_contract_registry.py`. Flutter customer membership lifecycle (renew/upgrade/downgrade/freeze/resume/cancel/transfer/expire) **Implemented** / **Tested** (mock repositories).

## PostgreSQL integration (local `digitize`)

| Gap | Command | Result |
|-----|---------|--------|
| GAP-API05-005 | `DIGITIZE_MEMBERSHIP_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost pytest tests/membership/test_membership_lifecycle_digitize_postgres.py -q` | **PASS** (2026-11-03) |

**Workflow verified (HTTP + read-after-write):** customer register → membership create → API-08 membership invoice → offline payment → activate → history → freeze → resume.

**Guard:** `tests/membership/membership_digitize_pg_guard.py` — does **not** use `digitize_test`. Legacy env `DIGITIZE_API05_PG_TEST=1` still accepted.

## Dependency fix (2026-11-03)

| Defect | Fix |
|--------|-----|
| `billing.invoice_items.product_id` ORM FK to missing `subscription.products` caused **500** on membership invoice create (PG IV) | Removed invalid ORM `ForeignKey`; column remains optional UUID matching migration 063 |

## GAP-API05-001 list memberships by customer (2026-11-09)

| Item | Status |
|------|--------|
| Additive `GET /api/v1/customers/{customer_id}/memberships` | **PASS** — unit **2**; PG `test_membership_list_by_customer_digitize_postgres.py` **1** (`DIGITIZE_MEMBERSHIP_PG_TEST=1`, `digitize` @ localhost:5434) |
| Flutter profile list + reload | **PASS** — `customer_membership_section_test.dart` **7** |
| Numbered inventory | **Unchanged** (228) |

Evidence: `docs/16_Development_Readiness/evidence/GAP-API05-001_MEMBERSHIP_LIST_BY_CUSTOMER_2026-11-09.md`

## Deferred (unchanged)

| Item | Status |
|------|--------|
| GAP-API05-004 freeze date-range / billing coupling | **Deferred by product decision** |

## Regression

```bash
cd digitize-services
python3 -m pytest tests/membership/ -q
# 167+ passed (includes PG module skipped without env)

cd digitize-ui
flutter test test/features/customer/customer_membership_lifecycle_controller_test.dart \
  test/features/customer/customer_membership_section_test.dart -r compact
```

## Module status

**Implemented / Tested** for approved Slice 1 + lifecycle Flutter. **Integration-verified** for GAP-API05-005 on local `digitize`. **Not** EQ-011 / full module “complete” while list-by-customer remains deferred.
