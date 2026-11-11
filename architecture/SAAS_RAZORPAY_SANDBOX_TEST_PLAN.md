# SaaS Razorpay sandbox test plan

**Status:** Preparation checklist — **no sandbox transaction has been executed** as part of authoring this document.  
**Date:** 2026-10-20  
**Companion:** `SAAS_INVOICE_READINESS_DECISION_REGISTRY.md`  
**Scope:** Organization → Digitize SaaS (`RAZORPAY_MODE`, extra-catalog commerce routes, Flutter `saas_checkout`).

---

## 1. Configuration (secure)

| Item | Where | Notes |
| --- | --- | --- |
| `RAZORPAY_MODE` | `digitize-services` env | `mock` for CI/automated tests; **`live`** for Razorpay **test mode** API (test `key_id` / `key_secret` from dashboard). Invalid values fail production-like startup (`Settings._missing_razorpay_live_settings`). |
| `RAZORPAY_KEY_ID` | Server env + returned to client on order create | Public Checkout key; safe to pass to Flutter/web SDK. **Never** commit. |
| `RAZORPAY_KEY_SECRET` | Server env only | `repr=False` on `Settings`; used for Orders API and checkout HMAC. **Never** in Flutter or git. |
| `RAZORPAY_WEBHOOK_SECRET` | Server env only | Webhook HMAC; required when `RAZORPAY_MODE=live` in production-like environments. Mock mode allows empty secret with fallback `"mock"` for `_webhook_secret` only in mock gateway paths. |
| Production-like guard | `settings.py` | `staging`/`production` with `RAZORPAY_MODE=live` **refuses boot** if any Razorpay secret missing. |

Reference: `digitize-services/.env.example` (comments only; no real values).

**Logging:** Do not log `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET`, raw webhook bodies containing card data, or full `razorpay_signature`. Prefer `record_id`, `provider_order_id`, event id, and status fields in audit/commerce logs.

---

## 2. Automated tests already completed (no Razorpay account)

These run in CI/local with `RAZORPAY_MODE=mock` and do **not** call Razorpay APIs.

| Case | Evidence |
| --- | --- |
| Mock order create returns `mock: true`, synthetic `order_mock_*` id | `test_saas_mock_checkout_lifecycle.py` |
| Checkout verify with `mock_ok` → `VERIFIED`, activation once | `test_mock_lifecycle_quote_accept_verify_activates_once` |
| Repeat verify idempotent | same file |
| Invalid checkout signature → no activation | `test_invalid_signature_does_not_activate` |
| Live mode rejects `mock_ok` shortcut | `test_live_mode_rejects_mock_ok_shortcut` |
| Webhook invalid signature | `test_webhook_invalid_signature` |
| Duplicate webhook event | `test_duplicate_webhook_is_idempotent` |
| Amount mismatch | `test_webhook_amount_mismatch_does_not_verify` |
| Live webhook without secret | `test_live_webhook_without_secret_is_rejected` |
| HMAC unit tests | `test_razorpay_hmac.py` |
| Platform Admin denied checkout | `test_platform_admin_cannot_verify_checkout`, lifecycle auth tests |
| Client amount tampering rejected | `test_client_amount_tampering_rejected` |
| Flutter: mock host still requires server verify | `saas_checkout_controller_test.dart`, `checkout_gateway_test.dart` |
| Invoice issuance blocked (statutory) | `test_saas_subscription_invoice_lifecycle.py`, cold issue tests |

---

## 3. Manual sandbox tests (require credentials + browser/device)

**Prerequisites:** Approved ops run; Razorpay **test** keys; non-production DB; tenant user with `PERM_SUBSCRIPTION_CREATE`; active discount/tax/quote policies; `RAZORPAY_MODE=live` on API; HTTPS webhook URL reachable (e.g. ngrok) with `RAZORPAY_WEBHOOK_SECRET` matching dashboard.

| # | Scenario | Steps | Pass criteria (backend records) |
| --- | --- | --- | --- |
| S1 | Create order | `POST /api/v1/saas/payment-orders` after quote accept | `saas_payment_attempt` row; `provider_order_id` matches Razorpay order; amount/currency match obligation; response `key_id` is test key |
| S2 | Successful payment | Complete Checkout (web: Checkout.js; mobile: `razorpay_flutter` via `checkout_io.dart`) then `POST /api/v1/saas/payments/verify` | Attempt `VERIFIED`; obligation `PAID`; subscription activated if `UPFRONT` or `INSTALLMENT_1`; **UI “success” alone insufficient** |
| S3 | Failed / cancelled checkout | Abandon or fail payment in widget | Attempt not `VERIFIED`; no activation; optional `FAILED` via webhook |
| S4 | Invalid verify signature | POST verify with wrong signature | `ValidationFailed`; attempt not verified; `failure_reason` may be `invalid_checkout_signature` |
| S5 | Valid verify signature | Correct HMAC from test secret | Same as S2 |
| S6 | Valid webhook | Razorpay sends `payment.captured` with valid `X-Razorpay-Signature` | `saas_provider_event` `APPLIED`; attempt `VERIFIED` if not already |
| S7 | Invalid webhook signature | Tampered body or signature | `ValidationFailed`; no state change |
| S8 | Duplicate webhook | Replay same `event_id` | Second processing `duplicate` / `already_verified`; single activation |
| S9 | Amount mismatch | Webhook amount ≠ attempt (simulate in test dashboard or crafted payload in controlled env) | Attempt `MISMATCH`; not verified |
| S10 | Currency mismatch | Same as S9 for currency | `MISMATCH` |
| S11 | Unknown order id in webhook | Event for foreign order | Event `REJECTED` / `unknown_order` |
| S12 | Failure after success (out of order) | Verify success, then deliver failed webhook for same payment | Document observed behavior: verified attempt should not downgrade without explicit product rule (current code: failed webhook only sets `FAILED` if not already `VERIFIED`) |
| S13 | Repeat verify | Call verify twice with valid signature | `already_verified: true`; activation count unchanged |
| S14 | Installment 1 success | `INSTALLMENT_60_40` first obligation | Activation runs (`_mark_verified` + `UPFRONT`/`INSTALLMENT_1` kinds) |
| S15 | Installment 2 failure | Pay/fail second obligation | Second obligation may `FAILED`; **no automatic subscription suspend** in current commerce service (activation only on upfront/installment_1) |
| S16 | Client-only “success” | Skip server verify after SDK callback | Subscription remains inactive; invoice unpaid |
| S17 | Invoice reconciliation | After statutory invoice exists (post INV decisions) | `saas_invoice_payment` row; `amount_received` updated — **blocked today** for real tax invoice issue |

**Flutter wiring:** `checkout_host.dart` selects `checkout_web.dart` (web) or `checkout_io.dart` (Android/iOS). Tests use `checkout_stub_factory.dart`. Sandbox exercise must use a **built** web/mobile target, not the stub factory.

---

## 4. Integration readiness (reviewed — not sandbox-run)

| Check | Result |
| --- | --- |
| Mock cannot impersonate live verification | Live mode: `mock_ok` rejected (`test_live_mode_rejects_mock_ok_shortcut`); mock mode uses `is_mock` on gateway |
| Live requires server secrets | `require_secrets_for_live()` on order create; production-like settings validation |
| Backend verify + webhook authoritative | `verify_checkout` / `handle_webhook` → `_mark_verified`; Flutter always calls `repository.verify` after host success |
| No provider secret in Flutter | Only `keyId` from order response; signatures generated by Razorpay SDK |
| No secrets in committed config | `.env.example` placeholders only; `RAZORPAY_KEY_SECRET` `repr=False` |
| Config failures actionable | Missing live settings list field names; commerce `ValidationFailed` with codes for policy gaps |
| Checkout adapters | Web + IO implementations exist; conditional export in `checkout_host.dart` |
| Subscription activation rules unchanged | `_activate_after_payment` only after verified payment for `UPFRONT` / `INSTALLMENT_1` |
| Invoice reconciliation unchanged | `apply_verified_attempt` only when issued invoice exists; statutory issue still blocked |

---

## 5. Statutory invoice issuance (explicitly out of sandbox payment scope)

Sandbox payment tests **do not** require tax invoice issuance. Issuance remains blocked by `ISSUANCE_BLOCKERS` (INV-001/002/003). Preview and blocked-issue paths are covered by automated tests.

---

## 6. Sign-off

| Gate | Status |
| --- | --- |
| Automated mock commerce suite | Ready |
| Razorpay sandbox end-to-end | **Not executed** — awaiting credentials and authorization |
| Production Razorpay | **Not in scope** |
| GST / statutory invoice production | **Blocked** on commercial decisions |
