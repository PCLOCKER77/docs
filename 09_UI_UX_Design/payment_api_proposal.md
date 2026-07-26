# Payment & Provider Rules Proposal (API-08 / IC-04) — Draft for Owner Confirmation

Status: Proposed (Product Design drafted) — please confirm with Payments and Finance owners.

Purpose
- Provide concrete webhook samples, refund rules, and UI state mappings for `UI-WLK-002`, `UI-BIL-001`, and `UI-PAY-001`.

1) Payment status model (proposed)

- `PENDING` — payment initiated, awaiting provider callback
- `SUCCESS` — provider confirmed settlement
- `FAILED` — final failure (declined, provider error)
- `TIMEOUT` — no provider response within expected window; needs manual reconciliation
- `RECONCILIATION_REQUIRED` — provider reported mismatch or settlement delay

2) Refund rules (proposed)

- Full refund allowed within 7 days of settlement unless provider policy restricts.
- Partial refunds allowed; UI must collect refund amount and reason.
- Refund fees: provider-specific; UI shows estimated fees when provider returns fee estimate API.

3) Webhook sample (provider → backend)

POST /webhooks/payments

```json
{
  "event": "payment.status.updated",
  "data": {
    "payment_id": "pay_123",
    "status": "SUCCESS",
    "provider_reference": "prov_456",
    "settled_at": "2026-07-26T12:34:56Z"
  }
}
```

- Webhook must be idempotent: include `event_id`; platform should dedupe.

4) Idempotency & reconciliation

- Payment initiation must accept `Idempotency-Key` header to avoid duplicate authorizations.
- Frontend: show `pending` with spinner and poll or rely on push webhook updates.

5) Export / ledger artifact (proposed CSV columns)

- `invoice_number`, `payment_id`, `customer_id`, `amount`, `currency`, `status`, `provider`, `provider_reference`, `settled_at`.
- Mask payment instrument fields (only show last4 and token id).

6) UI mapping (proposed)

- `Pending` → show waiting state and disable actions.
- `Success` → show receipt and enable reconciled actions.
- `Failed/Timeout` → CTA: retry or create reconciliation ticket.
- `Reconciliation_Required` → show special banner linking to reconciliation flow.

7) Request for Payments owner

- Please confirm provider-specific refund windows, fee model, webhook payloads, and idempotency guarantees. Attach OpenAPI or provider docs when possible.

---

Documented-by: Product Design
