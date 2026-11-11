# Facility payment lifecycle — verification (2026-11-09)

## Scope

End-to-end **verification** of authorized facility payment lifecycles (online + offline). No contract changes, no new product rules. **Razorpay sandbox capture remains incomplete** (separate from mock/PG verification).

---

## 1. Lifecycle by method

| Method | Initiate / collect | Initial status | Confirmation | Persistence | Invoice | Receipt / history | Audit / idempotency | Automated proof |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Online Razorpay** | `POST /payments/online` initiate → checkout | `PENDING` | Server verify (+ optional webhook) | `payment_transactions` + gateway | PAID on verify (mock/PG) | History `ONLINE`; receipt path via settlement | `Idempotency-Key`; duplicate verify idempotent (PG) | PG M2 **1 passed** 2026-11-09; **live sandbox capture: No** |
| **Cash** | `POST /payments/offline` | `SUCCESS` | Staff + reference | Same | PAID when full | `payment_method` CASH | Idempotency + audit (offline service) | `test_offline_payment_invoice_lock` **6 passed** (subset) |
| **Cheque** | Offline CHEQUE | **`PENDING`** | Clear → SUCCESS; bounce → FAILED | Txn PENDING until clear | **No PAID** until clear | History shows pending cheque | `AUDIT_CHEQUE_*` | Flutter controller cheque **PENDING**; bounce guards **2 passed** |
| **Bank transfer** | Offline BANK_TRANSFER | `SUCCESS` | Staff reference | Same | PAID | BANK_TRANSFER in history | Idempotency | Offline lock subset |
| **Counter UPI / UTR** | Offline UPI | `SUCCESS` | Staff UTR | Same | PAID | UPI offline ≠ Razorpay UPI | Idempotency | Offline lock subset |

**Flutter Collect payment journey:** channel dialog → online (initiate only after selection) or offline form — **25 tests passed** (2026-11-09).

---

## 2. Cheque lifecycle (no invented rules)

| Step | Behavior | Evidence |
| --- | --- | --- |
| Received | `PaymentTransactionService` + `payment_service`: CHEQUE → **`PENDING`**, no invoice finalize | Code + offline API |
| Cleared | `clear_cheque_payment` → SUCCESS + `finalize_successful_payment_collection` | `payment_transaction_service.py` |
| Bounced | `bounce_cheque_payment` → FAILED txn; **no** settlement on receive/bounce | Unit guards `test_cheque_bounce_service.py` |
| Outstanding after bounce | Invoice never PAID from pending cheque; failed payment excluded from SUCCESS totals | Design + reconciliation filters |
| Grace / auto-suspend | **Implemented** (GAP-API09-005, mig 084) | Bounce opens grace; scheduler runs `run_cheque_bounce_grace_worker.py`; facility SaaS suspend on expiry |

---

## 3. Reconciliation

| Rule | Status |
| --- | --- |
| One row per successful collection event | Idempotency + PG duplicate webhook |
| `payment_method` vs gateway channel distinguishable | History + `payment_transactions.gateway` |
| Pending cheques excluded from SUCCESS totals | Cheque PENDING until clear |
| FAILED / bounced not in success rollups | `PAYMENT_STATUS_FAILED` |
| Invoice balance vs confirmed payments | `invoice_effective_outstanding` + settlement helpers |
| API-08-014 reconciliation events | Prior PG `test_billing_credit_receipt_recon_http_digitize_postgres.py` (not re-run) |

---

## 4. Cross-module consistency

| Surface | Online | Offline |
| --- | --- | --- |
| Outstanding | Refresh after verify/collect | Same |
| Billing history | `ONLINE` + status | Method per row |
| Receipts | Settlement path | Receipt generation on SUCCESS offline |
| SaaS billing | Facility webhook branch when order not SaaS; facility payments isolated | N/A |

Facility Razorpay orders do not settle SaaS `saas_commerce` attempts (shared webhook routes to facility billing when order matches facility payment).

---

## 5. Razorpay sandbox (explicitly separate)

| Item | Status |
| --- | --- |
| Mock + PG online lifecycle | **Verified** (2026-11-09 PG M2 re-run **1 passed**) |
| Live Razorpay capture + server verify on `digitize` | **Not complete** (cancelled harness; 3 PENDING orders) |
| Inbound Razorpay webhook | **Not verified** (no tunnel) |
| Engineering harness | Direct Checkout.js only; **not** full channel-selection UX |

---

## 6. Tests executed (this slice)

| Suite | Result |
| --- | --- |
| `test_cheque_bounce_service.py` + API08 M2 routes + gateway + HMAC | **16 passed** |
| `test_offline_payment_invoice_lock.py` (-k offline/cash/cheque) | **6 passed** |
| `test_billing_m2_http_digitize_postgres.py` (PG, mock Razorpay) | **1 passed** |
| Flutter channel + flow + controller + razorpay options | **25 passed** |

No defects found; no code changes required in this slice.

---

## 7. Remaining external dependencies

- Human Razorpay Test Mode capture + verify on reused PENDING order (`DIGITIZE_RAZORPAY_SANDBOX_RETRY=1`).
- Optional: authorized public webhook URL for Razorpay-originated events.
- Dedicated PG test for cheque **clear** happy path (guards exist; full clear IV not added — no contract gap).
