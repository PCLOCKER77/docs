# GAP-API05-001 — Customer membership list (additive contract)

**Date:** 2026-11-09  
**Status:** **Implemented / Tested / Integration-verified (local `digitize`)**  
**Frozen inventory:** **228** numbered operations unchanged — no new operation IDs.

## Implemented behavior

- `GET /api/v1/customers/{customer_id}/memberships` — paginated list with optional `facility_id` and `status` filters.
- Organization, facility, and site scope enforced via existing customer access and membership repository filters (`MembershipLifecycleService.list_for_customer`).
- Flutter customer profile: list, reload, empty, and error states; tap row to open lifecycle; open-by-ID preserved.

## PostgreSQL integration (2026-11-09 closure)

**Environment (local dev):**

```bash
cd digitize-services
ENVIRONMENT=development \
DB_HOST=localhost DB_PORT=5434 \
DB_USER=digitize_app DB_PASSWORD='***' \
DB_NAME=digitize \
DIGITIZE_MEMBERSHIP_PG_TEST=1 \
python3 -m pytest tests/membership/test_membership_list_by_customer_digitize_postgres.py -q
```

**Result:** **1 passed** — customer create → membership create → list by customer (pagination), facility filter, cross-org denial (`403`/`404` on unknown facility filter).

**Alembic on inspected DB:** `084_cheque_bounce_grace` (head).

## Unit / widget tests

```bash
python3 -m pytest tests/membership/test_membership_list_by_customer.py -q   # 2 passed
cd digitize-ui && flutter test test/features/customer/customer_membership_section_test.dart  # 7 passed
```

## Files (backend / Flutter)

- `app/modules/membership/routes.py`, `lifecycle_service.py`, membership repository
- Flutter: `customer_membership_repository.dart`, `remote_customer_membership_repository.dart`, `customer_membership_section.dart`
- PG IV: `tests/membership/test_membership_list_by_customer_digitize_postgres.py`

## Migrations

None.

## Billing boundary

No invoice or payment APIs added under API-05 listing.
