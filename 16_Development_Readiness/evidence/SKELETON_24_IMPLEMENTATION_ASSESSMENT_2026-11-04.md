# Skeleton 24 — Implementation assessment (2026-11-04)

**Task:** Implement all 24 remaining numbered skeleton operations.  
**Canonical registry:** `app/api/contracts/api_registry.py`  
**Result:** **No skeleton promoted to `BACKEND_IMPLEMENTED` in this pass.**  
**Final status:** **COMPLETE WITH APPROVED DEFERRED ITEMS** — every operation reviewed; remaining work is gated by existing product, schema, or authorization decisions documented below. Implementing routes without those gates would violate project rules (no fake 200s, no client audit ingest, no unauthorized DDL).

Regenerate skeleton list:

```bash
cd digitize-services && poetry run python scripts/contract_numbered_audit.py
# Expect: SKELETON_CREATED: 24
```

---

## Summary (dynamic from catalog + decision registers)

| Class | Count |
| --- | ---: |
| Still `SKELETON_CREATED` | **24** |
| Promoted to implemented in this pass | **0** |
| Blocked — schema / migration not authorized | **14** |
| Deferred — product decision (rules undefined) | **9** |
| Awaiting authorization — migration proposal only | **1** (API-12-008) |

---

## API-08 (8) — Facility billing

**Register:** [API-08_FACILITY_BILLING_DECISION_REGISTER.md](../../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md)  
**Summary row:** *None of the 8 remaining as full live ops without approval.*

| ID | operation_id | Status | Blocker |
| --- | --- | --- | --- |
| API-08-002 | billing_charges_calculate_create | DEFERRED_BY_PRODUCT_DECISION | Facility service-charge catalog undefined; no schema |
| API-08-003 | invoices_discounts | DEFERRED_BY_PRODUCT_DECISION | Discount lifecycle / persistence on facility invoices undefined |
| API-08-004 | invoices_taxes_calculate | DEFERRED_BY_PRODUCT_DECISION | Facility tax policy; `BillingSetting.tax_settings` unmigrated |
| API-08-005 | invoices_adjustments | DEFERRED_BY_PRODUCT_DECISION | Adjustment vs credit note vs cancel undefined |
| API-08-007 | invoices_credit_notes | BLOCKED (route) | Schema mig **080** + services live; numbered HTTP **SKELETON** until product promotes |
| API-08-009 | payments_online_create | BLOCKED (schema + provider) | `payment_transactions` unmigrated; Razorpay facility path not authorized live |
| API-08-012 | payments_receipts | BLOCKED (schema) | `billing.receipts` unmigrated |
| API-08-014 | reconciliations_create | DEFERRED_BY_PRODUCT_DECISION | No reconciliation model / ops process |

**DEV-21:** GAP-API08-006, GAP-API08-* family.

---

## API-12 (1) — Support

| ID | operation_id | Status | Blocker |
| --- | --- | --- | --- |
| API-12-008 | support_tickets_escalate | AWAITING_AUTHORIZATION | No `support.ticket_escalation` table; migration **072** proposal not authorized ([API-12_008_Escalate_Migration_Proposal.md](../../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md)); no `escalate.ticket` permission |

**Code note:** `app/modules/support/routes.py` explicitly excludes escalate registration.

**DEV-21:** GAP-API12-001.

---

## API-13 (9) — Audit

**Register:** [API-13_AUDIT_PRODUCT_DECISION.md](../../architecture/API-13_AUDIT_PRODUCT_DECISION.md)  
**Recommendation:** Keep API-13-001/002/003 as **server-side side effects only** — do **not** register client POST ingest.

| ID | operation_id | Status | Blocker |
| --- | --- | --- | --- |
| API-13-001 | audit_events_create | DEFERRED_BY_PRODUCT_DECISION | Client-writable audit forbidden by security recommendation |
| API-13-002 | authentication_events_create | DEFERRED_BY_PRODUCT_DECISION | Auth stack already writes `security.authentication_event` |
| API-13-003 | audit_events_configuration_changes_create | DEFERRED_BY_PRODUCT_DECISION | Config changes audited via domain `record_audit_event` |
| API-13-004 | security_events_create | BLOCKED (schema + product) | No `security.security_event` ORM |
| API-13-006 | investigations_create | BLOCKED (schema) | No investigation table |
| API-13-007 | compliance_records_reports_create | DEFERRED_BY_PRODUCT_DECISION | No compliance-record model |
| API-13-008 | audit_events_archive_create | DEFERRED_BY_PRODUCT_DECISION | Archive lifecycle undefined |
| API-13-010 | audit_policies_update | BLOCKED (schema) | Catalog `database_gap` |
| API-13-011 | compliance_violations_list | BLOCKED (schema) | Catalog `database_gap` |

**DEV-21:** GAP-API13-*.

---

## API-14 (6) — Reference / platform GMD

**Register:** [API-14_REFERENCE_SOURCE_OF_TRUTH.md](../../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md)  
**Decision:** Approve GMD seed groups (COUNTRY, LANGUAGE, TIMEZONE, etc.) before routes + migration.

| ID | operation_id | Status | Blocker |
| --- | --- | --- | --- |
| API-14-001 | reference_countries_list | AWAITING_AUTHORIZATION | GMD group `COUNTRY` + seed not approved/migrated |
| API-14-002 | reference_states_regions_list | AWAITING_AUTHORIZATION | Depends on country model |
| API-14-004 | reference_languages_list | AWAITING_AUTHORIZATION | GMD `LANGUAGE` + seed |
| API-14-005 | reference_timezones_list | AWAITING_AUTHORIZATION | Curated GMD `TIMEZONE` policy |
| API-14-007 | reference_activity_types_list | DEFERRED_BY_PRODUCT_DECISION | Activity-type ownership (GMD vs training ops) |
| API-14-012 | reference_localization_list | DEFERRED_BY_PRODUCT_DECISION | Localization as settings snapshot vs GMD |

**DEV-21:** GAP-API14-001…004.

---

## What would unblock work (ordered)

1. **Product sign-off** on API-08 charge/discount/tax/adjustment/reconciliation rules.  
2. **Migration authorization** for billing credit notes, payment transactions, receipts (`API-08` register).  
3. **Migration authorization** for API-12-008 escalation twin (`072_support_ticket_escalation`).  
4. **Product confirmation** API-13 capture POSTs remain non-routes (or explicit alternative).  
5. **Product approval** API-14 GMD seed set + single additive migration.  
6. Then: vertical slice per operation (route, service, PG tests, Flutter where applicable), update `IMPLEMENTED_NUMBERED_KEYS` + contract status only when complete.

---

## Test evidence (inventory unchanged)

```bash
cd digitize-services
poetry run python scripts/contract_numbered_audit.py
# backend_status: {'BACKEND_IMPLEMENTED': 204, 'SKELETON_CREATED': 24}

poetry run pytest tests/api/test_module_routes.py -q -k skeleton
poetry run pytest tests/api/test_api_registry_consolidation.py -q
```

No PostgreSQL schema changes in this pass. No Flutter changes.
