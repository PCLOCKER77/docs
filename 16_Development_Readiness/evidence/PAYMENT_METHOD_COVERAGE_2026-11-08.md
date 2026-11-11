# Facility payment method coverage — evidence (2026-11-08)

## Scope

Review of API-08 offline/online flows, Razorpay checkout, Flutter outstanding/history UI. No new permissions, contracts, cheque grace/suspend rules, or physical card-terminal method.

---

## 1. Online (Razorpay)

| Method | Implementation |
| --- | --- |
| Cards | Razorpay Standard Checkout (`checkout_web.dart` / `checkout_io.dart`) |
| Netbanking | Same; enabled in `razorpay_checkout_options.dart` |
| UPI QR (desktop web) | Checkout.js + `method.upi` + display block `upi` |
| UPI Intent (Android) | `razorpay_flutter` with same options map |
| Wallets | `wallet: true` (account-dependent) |
| UPI Collect (deprecated) | **Not implemented** (by design) |

### Why UPI was not prominent in sandbox (investigation)

1. **Checkout opened on Card step first** — Razorpay Standard Checkout defaults to card; UPI is a separate block (now ordered `upi` → `card` → `netbanking` in `razorpay_checkout_options.dart`).
2. **UPI Intent is Android-native** — Flutter web uses Checkout.js (UPI QR / on-page UPI where enabled), not mobile intent.
3. **Account / dashboard** — methods visible only if enabled on the Razorpay test account (provider config, not Digitize business rules).
4. **Offline “UPI” in collect dialog** — records staff-entered UTR/reference via API-08-010; not Razorpay hosted checkout.

---

## 2. Physical collection (API-08-010) — verified existing

| Method | Backend | Lifecycle |
| --- | --- | --- |
| Cash | `APPROVED_OFFLINE_PAYMENT_METHODS` | Immediate SUCCESS + settlement |
| Cheque | `CHEQUE` | PENDING → clear/bounce via `PaymentTransactionService` |
| Bank transfer | `BANK_TRANSFER` | Immediate SUCCESS (staff-verified reference) |
| Physical UPI (counter) | `UPI` offline | SUCCESS with reference (not gateway) |
| Other | `OTHER` | Same pipeline |
| Physical card terminal | **Not in approved set** | **Product blocker** — no `CARD_TERMINAL` without catalog change |

Idempotency: `Idempotency-Key` on offline and online initiate. Cheque bounce: `tests/billing/test_cheque_bounce_service.py`. Online: server verify + webhook (PG IV).

---

## 3. Flutter UX (channel selection — 2026-11-09)

**Journey:** Outstanding invoice → **Collect payment** → **Choose payment channel** (online vs offline at facility) → Razorpay Checkout **or** existing offline collection form.

- `facility_payment_channel_dialog.dart` — online vs offline at facility with method lists.
- Outstanding panel: single **Collect payment** entry; `startOnlinePayment` / Razorpay only after **Online payment** channel.
- Offline: existing `_CollectPaymentDialog` (cash, cheque, bank transfer, counter UPI).
- Razorpay options unchanged (`razorpay_checkout_options.dart`).

**Tests:** `facility_payment_channel_dialog_test.dart`, `facility_outstanding_payment_flow_test.dart`, controller cheque-pending — **passing** (no sandbox capture claimed).

## 3a. Flutter UX (prior changes)

- Outstanding panel: **Pay online** label from `lastOnlineMockCheckout` (mock vs Razorpay).
- **Record cash / cheque / transfer** button + dialog title **Record physical collection** with online vs physical guidance.
- Billing history: `payment_method` already on `FacilityBillingHistoryEntry.summaryLine` (ONLINE vs CASH etc.).

---

## 4. Reporting / reconciliation

- Payment history exposes `payment_method` per row; gateway online payments stored as `ONLINE` with `payment_transactions.gateway` (`RAZORPAY_MOCK` / `RAZORPAY_SANDBOX`).
- Offline channels do not share gateway ids — avoids double-count between offline UPI and Razorpay UPI when staff use correct entry points.
- Reconciliation events: existing API-08-014 PG IV (unchanged).

---

## 5. Tests run

| Suite | Result |
| --- | --- |
| Flutter `razorpay_checkout_options_test.dart` + checkout + outstanding | **19 passed** |
| `test_cheque_bounce_service.py` + gateway + api08 routes | **9 passed** |
| Prior PG IV (M2 HTTP, credit/recon) | unchanged green |

---

## 6. Razorpay E2E status (device verification 2026-11-08)

| Layer | Status |
| --- | --- |
| Code + PG (mock) | Verified (prior; not re-run) |
| Sandbox order | **Verified** (harness + API :8000) |
| Checkout Test Mode + method tiles | **Verified** (UPI QR after Flutter-aligned display blocks) |
| Actual sandbox capture | **Not completed** (2026-11-08 audit: harness **cancelled**, Razorpay payments count **0**) |
| Server verify / invoice PAID | **Not completed** |
| Inbound Razorpay webhook | **Not completed** (no tunnel) |
| Android UPI Intent | **Not completed** (no device) |
| Flutter outstanding UI journey | **Not completed** (auth); SDK path = Checkout.js |

See `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` § Device verification run.

---

## 7. Lifecycle E2E verification

See **`PAYMENT_LIFECYCLE_E2E_2026-11-09.md`** — method matrix, cheque lifecycle, reconciliation rules, test run 2026-11-09. **Live Razorpay capture still not claimed.**

---

## Files touched (this slice)

- `digitize-ui/lib/features/saas_checkout/domain/razorpay_checkout_options.dart`
- `digitize-ui/lib/features/saas_checkout/checkout_io.dart`, `checkout_web.dart`
- `digitize-ui/lib/features/organization/.../facility_outstanding_statements_*`
- `digitize-services/scripts/razorpay_sandbox_facility_e2e.py` (checkout method flags)
