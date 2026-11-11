# Master — 16 skeleton operations (approved implementation)

**Date:** 2026-11-09  
**Decision authority:** User-approved product decisions (this session)  
**Inventory:** **228/228** `BACKEND_IMPLEMENTED` (`contract_numbered_audit.py`)

---

## Summary

| Module | Promoted | Migrations | Notes |
|--------|----------|------------|-------|
| API-14 | 6 | **085** | GMD seeds, localization, org activity types |
| API-08-005 | 1 | **086** | Facility invoice adjustments + outstanding integration |
| API-13 | 9 | **087** | Governance entities; client trusted ingest **403** |

**Remaining legal/product (not blocking routes):** audit retention day counts; compliance report lifecycle semantics; violation resolution workflow; archive execution destination.

---

## Migrations (apply locally: `alembic upgrade head`)

| Rev | File | Scope |
|-----|------|--------|
| 085 | `085_platform_reference_governance.sql` | GMD seeds, `platform.localization_resource`, `tenant.organization_activity_type` |
| 086 | `086_billing_facility_adjustments.sql` | `billing.facility_invoice_adjustments`, billing adjustment permissions |
| 087 | `087_audit_governance_security.sql` | `security.security_event`, audit governance tables, permissions, default audit policy seed |

---

## Operation status (16/16)

| ID | Status | Backend entry |
|----|--------|---------------|
| API-08-005 | **IMPLEMENTED** | `InvoiceAdjustmentService` + `POST /invoices/{id}/adjustments` |
| API-13-001–003, 004 | **IMPLEMENTED** (server-only) | POST routes call `reject_trusted_client_ingest()` → **403** |
| API-13-006 | **IMPLEMENTED** | `POST /investigations` |
| API-13-007 | **IMPLEMENTED** | `POST /compliance-records/reports` |
| API-13-008 | **IMPLEMENTED** | `POST /audit-events/archive` (non-destructive request record) |
| API-13-010 | **IMPLEMENTED** | `PATCH /audit-policies/{policy_id}` |
| API-13-011 | **IMPLEMENTED** | `GET /compliance-violations` |
| API-14-001–002, 004–005, 007, 012 | **IMPLEMENTED** | `reference/routes.py` list endpoints |

---

## Tests executed

```bash
cd digitize-services
.venv/bin/python scripts/contract_numbered_audit.py
# → BACKEND_IMPLEMENTED: 228

.venv/bin/pytest tests/billing/test_invoice_adjustment_balance.py \
  tests/audit/test_client_ingest_blocked.py \
  tests/api/test_reference_aliases.py \
  tests/api/test_catalog_validation.py -q
# → passed (after GMD catalog test update)

.venv/bin/python -c "from app.main import create_app; create_app()"
# → app ok
```

**PostgreSQL IV:** not run in this session — apply mig **085–087** on local `digitize` before PG integration tests.

---

## QA handover

- **Ready after local migration:** all 16 operations + full **228** numbered inventory.
- **Flutter:** no new screens (reference reads and governance are API-first); existing clients may call new reference lists.
- **Blocked for production DB:** migration apply on QA/prod still requires deployment authorization.

---

## Registers updated

- [API-08 facility billing register](../../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) — API-08-005 approved  
- [API-13 audit product decision](../../architecture/API-13_AUDIT_PRODUCT_DECISION.md) — approved stance  
- [API-14 reference SoT](../../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md) — approved groups  
- DEV-19 / DEV-21 / DEV-23 session entries (2026-11-09 approved implementation)
