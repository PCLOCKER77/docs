# API-08 Phase 1 — Facility membership billing

**Status:** Implemented in code (2026-10-30). Not registry-certified.

## Live numbered operations

| ID | Method | Path | Scope |
| --- | --- | --- | --- |
| API-08-001 | POST | `/api/v1/invoices` | Membership invoice from `customer_membership_id` + plan snapshot |
| API-08-010 | POST | `/api/v1/payments/offline` | Full offline payment against issued invoice |

## Database

Migration `063_facility_billing_membership` adds `billing` schema (`sellers`, `invoices`, `invoice_items`, `payments`) and billing permissions. **Not applied** during development tasks against protected databases.

## Out of scope (Phase 1)

Facility online gateway, refunds, credit notes, reconciliation, commercial reports, statutory GST/tax rules.

## Membership activation

`POST /memberships/{id}/activate` requires a **paid** facility `invoice_id` for priced plans. Client `offline_payment_confirmed` alone is rejected.
