# Razorpay sandbox integration — execution evidence (2026-11-08)

## Scope

Approved **sandbox / test-mode only**. Production (`live` money) remains out of scope.

## Gaps addressed (code + tests)

| Gap | Status after this slice |
| --- | --- |
| GAP-INT-004 | **Partial → INTEGRATION_VERIFIED (mock + sandbox paths)** — `RAZORPAY_MODE` drives mock vs HTTP; dual-path unit tests |
| GAP-API08-006 | **Partial → SANDBOX_CONNECTED** — facility `POST /payments/online` uses settings-backed gateway; Flutter live SDK path when `mock_checkout=false` |
| GAP-API09-003 | **Partial → SANDBOX_CONNECTED** — SaaS path unchanged; shared webhook delegates to facility billing when order is not SaaS |
| GAP-JRN-008 (live pay) | **Partial → SANDBOX_CONNECTED** — outstanding panel + facility checkout + SaaS checkout share `CheckoutGateway` |

## Files changed

### digitize-services

- `app/modules/billing/constants.py` — `GATEWAY_RAZORPAY_SANDBOX`
- `app/modules/billing/facility_razorpay_gateway.py` — settings-backed mock/sandbox/live adapter
- `app/modules/billing/online_payment_service.py` — settings injection, `key_id`, webhook settlement helper
- `app/modules/billing/schemas.py` — optional `key_id` on `OnlinePaymentOut`
- `app/modules/billing/routes.py` — `get_settings` on online payment route
- `app/modules/subscription/commerce/service.py` — webhook routes unknown SaaS orders to facility settlement
- `tests/billing/test_facility_razorpay_gateway.py` — mock + sandbox HTTP tests

### digitize-ui

- `lib/features/organization/domain/facility_online_payment.dart` — `keyId`
- `lib/features/organization/presentation/widgets/facility_outstanding_statements_panel.dart` — sandbox checkout via `createCheckoutGateway()`; mock dialog preserved

## APIs connected

| API | Behavior |
| --- | --- |
| `POST /api/v1/payments/online` | Initiate: Razorpay order from `RAZORPAY_*` + `mock_checkout` / `key_id` / `gateway` |
| Same (verify body) | HMAC checkout verify; settlement unchanged |
| `POST /api/v1/webhooks/razorpay` | Idempotent events; facility invoice payments settled when order matches `billing.payments` |
| SaaS commerce (existing) | Orders, verify, webhook — unchanged contract |

## Tests executed

| Suite | Result |
| --- | --- |
| `tests/billing/test_facility_razorpay_gateway.py` | **2 passed** |
| `tests/billing/test_billing_api08_m2_routes.py` + `test_razorpay_hmac.py` + `test_saas_commerce_service.py` | **28 passed** |
| Flutter `facility_outstanding_statements_controller_test.dart` + `checkout_gateway_test.dart` | **18 passed** |

## PostgreSQL integration (`digitize` localhost)

Commands (all `ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost`, no `DATABASE_URL`):

```bash
DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1 poetry run pytest \
  tests/billing/test_billing_m2_http_digitize_postgres.py -q

DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1 poetry run pytest \
  tests/billing/test_billing_credit_receipt_recon_http_digitize_postgres.py -q

DIGITIZE_TXN004_PG_TEST=1 poetry run pytest \
  tests/subscription/test_saas_webhook_concurrency_postgres.py -q

poetry run pytest tests/billing/test_facility_razorpay_gateway.py \
  tests/billing/test_billing_api08_m2_routes.py tests/subscription/test_razorpay_hmac.py -q
```

| Result | What was verified on PG |
| --- | --- |
| M2 HTTP IV **1 passed** | Mock order create (`GATEWAY_RAZORPAY_MOCK`, `payment_transactions`), client verify + bad signature, **facility webhook settle** (invoice `PAID`, payment `SUCCESS`), duplicate webhook (`duplicate`), invalid webhook signature (422), amount mismatch (`mismatch`) |
| Credit/receipt/recon IV **1 passed** | Billing regression unchanged |
| SaaS webhook concurrency **3 passed** | SaaS webhook idempotency unchanged |
| Unit **14 passed** | Gateway + route registry + HMAC |

PG harness sets `app.state.settings` with `RAZORPAY_MODE=mock` for the test duration so IV never calls Razorpay HTTP even when local `.env` uses test/live keys.

**Defects fixed in this IV slice:** test-only — M2 PG forced mock settings; extended assertions + webhook scenarios in `test_billing_m2_http_digitize_postgres.py`. No production settlement logic change required for green PG IV.

## Manual sandbox end-to-end (2026-11-08)

### Preflight

| Check | Result |
| --- | --- |
| `RAZORPAY_MODE=sandbox` in committed dev `.env` | **No** — `.env` has `live` (Razorpay test keys still use `rzp_test_` prefix; not production) |
| Test `key_id` / server secrets present | **Yes** (values not logged) |
| Production `rzp_live_` keys | **No** |
| Flutter uses server `key_id` | **Yes** — `checkout_web.dart` / facility panel when `mock_checkout=false` |
| Public Razorpay → localhost webhook URL | **Not verified** (dashboard/ngrok not confirmed in this run) |
| API + Flutter running for UI checkout | **No** — API was started for probe only; Flutter not launched |

**Conclusion:** Full manual checkout per test plan **not started** until `RAZORPAY_MODE=sandbox` is set in dev config (or agreed `live`+test-key convention), app stack is up, and webhook URL is reachable.

### Executed in this session (partial provider probe)

Runtime: `RAZORPAY_MODE=sandbox` **session override** (not `.env`).

| Step | Outcome |
| --- | --- |
| Facility sandbox order via `FacilityRazorpayGateway` | **Success** — `GATEWAY_RAZORPAY_SANDBOX`, real Razorpay `order_*` id, `mock=false` |
| Razorpay test payment via REST (`/v1/payments`, netbanking HDFC) | **Failed** — HTTP 401 Authentication failed (orders API OK with same credentials → **Checkout UI path required**) |
| Digitize initiate → pay → verify → settle on PG | **Not run** (no payment id; no Flutter) |
| Inbound webhook from Razorpay dashboard | **Not delivered** |

### Negative / server-authoritative scenarios

| Scenario | How verified |
| --- | --- |
| Invalid checkout / webhook signature, duplicate webhook, amount mismatch | PostgreSQL M2 IV (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) — mock Razorpay |
| Client success without server verify | Design + PG/client-verify tests (unchanged) |
| SaaS webhook unaffected by facility branch | `DIGITIZE_TXN004_PG_TEST=1` — **3 passed** |

### Actual sandbox card checkout (2026-11-08 continued)

| Layer | Status |
| --- | --- |
| Code verified | **Yes** (prior slices) |
| PostgreSQL integration verified | **Yes** (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) |
| **Actual sandbox order (Digitize → Razorpay API)** | **Yes** — `RAZORPAY_MODE=sandbox` in dev `.env`; `mock_checkout=false`, `gateway=RAZORPAY_SANDBOX`; Razorpay Orders API 200 |
| **Checkout.js / Test Mode UI** | **Yes** — harness `var/razorpay_sandbox_checkout.html` (same SDK path as Flutter web); Razorpay modal showed **Test Mode** |
| **Actual sandbox payment captured** | **No** — `GET /v1/orders/{id}/payments` **count=0**; card entry blocked in cross-origin checkout iframe in automated browser |
| **Server verify + invoice PAID** | **No** — no `razorpay_payment_id` / signature from Checkout |
| **Webhook delivered by Razorpay** | **No** — `ngrok` / `cloudflared` not installed; no public URL |
| **Local HMAC webhook after payment** | **Not run** — depends on successful payment |
| **Flutter app E2E** | **Not run** — Flutter web not started; harness substitutes Checkout.js only |

**Tooling added:** `scripts/razorpay_sandbox_facility_e2e.py` (`DIGITIZE_RAZORPAY_SANDBOX_E2E=1` or `DIGITIZE_RAZORPAY_SANDBOX_RETRY=1`) — **engineering-only** direct Checkout.js + verify; **not** the full Digitize journey (staff must choose Online vs Offline in Flutter first). Retry mode reuses latest PENDING order without creating a fourth order.

**Config change:** dev `.env` `RAZORPAY_MODE` set from `live` → **`sandbox`** (test `key_id` unchanged; secrets not logged).

**Blockers for full E2E:**
1. Complete payment inside Razorpay Checkout (human in browser or approved automation on iframe).
2. Public webhook tunnel + dashboard URL (optional for verify-only path; webhook path needs tunnel for Razorpay-originated events).
3. Flutter `flutter run -d chrome` against `http://127.0.0.1:8000` for true UI journey (optional if Checkout.js path accepted for provider proof).

## Device verification run (2026-11-08, session 2)

API: `uvicorn` on `http://127.0.0.1:8000` (`RAZORPAY_MODE=sandbox`, test `key_id` prefix only in logs). Harness: `DIGITIZE_RAZORPAY_SANDBOX_E2E=1` + Checkout.js page on port 8800 (same options as Flutter `razorpayStandardCheckoutOptions` after harness align).

| Checkpoint | Status | Notes |
| --- | --- | --- |
| Checkout configuration verified | **Yes** | `mock_checkout=false`, `GATEWAY_RAZORPAY_SANDBOX`, live Razorpay order 201 |
| Flutter Web app E2E (outstanding panel) | **No** | Staff JWT required; **Checkout.js path matches** `checkout_web.dart` SDK + options |
| Checkout.js Test Mode modal | **Yes** | Red “Test Mode” ribbon; merchant title “Digitize facility billing” |
| Desktop **UPI QR** visible | **Yes** | After display `blocks` + `sequence` (UPI first); “Pay via UPI” → QR + UPI ID |
| Card / netbanking / wallet visible | **Yes** | Cards (Visa/MC/RuPay…), Netbanking, Wallet per account |
| **Actual sandbox payment captured** | **No** | Cross-origin checkout iframe blocks automated card/UPI entry; `GET …/orders/{id}/payments` **count=0** |
| Server verify + invoice **PAID** | **No** | Depends on successful Checkout handler (`razorpay_payment_id` + signature) |
| Checkout **cancellation** (harness) | **Yes** | `ondismiss` → callback `cancelled`; harness exit `CHECKOUT_CANCELLED` |
| Live API **invalid webhook** signature | **Yes** | `POST /api/v1/webhooks/razorpay` with bad HMAC → **422** (no tunnel) |
| **Razorpay-originated** webhook | **No** | `ngrok` / `cloudflared` **not installed**; no public URL configured |
| **Local** HMAC webhook after payment | **No** | Harness path ready; not run (no payment id) |
| Android UPI Intent | **No** | `flutter devices`: Chrome + macOS only; **no adb device** |
| Physical collection regression | **Yes** | `test_cheque_bounce_service.py` **2 passed** (unchanged) |

**Flutter Web operator steps (manual, authorized):**

1. API on `:8000`; `flutter run -d chrome` from `digitize-ui` (defaults to `http://127.0.0.1:8000`).
2. Sign in as org staff with `billing.outstanding.view` / online pay permission.
3. Organization → Billing → facility outstanding → **Pay online** on `sbox-e2e` or issued invoice.
4. Complete Razorpay Test Mode payment; confirm verify call and history refresh.

**Android operator steps (manual, authorized):** attach device/emulator, `flutter run`, same billing flow; confirm UPI Intent app picker and return handling.

**Full E2E completion:** **Not claimed** until an actual sandbox capture, server verify, and (optional) inbound webhook all succeed.

## Manual checkout result inspection (2026-11-08)

Authoritative sources: `var/razorpay_sandbox_e2e_result.json`, PostgreSQL `digitize`, Razorpay Orders API (no secrets logged). **Outcome: cancelled — payment journey not complete.**

| # | Check | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Order for correct facility invoice | **Partial** — `sbox-e2e-INV` on facility `de08d511-…5ed7`, amount ₹100; **3** initiate rows (`RAZORPAY_SANDBOX` orders `order_TxYNe59v…`, `order_TxYYCbJ…`, `order_TxYaS4T…`) | DB + checkout HTML |
| 2 | Successful sandbox payment at Razorpay | **No** — every order `status=created`, `amount_paid=0`, `…/payments` **count=0** | Razorpay API |
| 3 | Server signature verify succeeded | **No** — no verify `POST` on live `:8000`; harness `server_verify=false` | Harness result + API logs |
| 4 | Payment persisted as SUCCESS | **No** — all `billing.payments` **PENDING**; txn rows **PENDING** | DB |
| 5 | Invoice / history updated | **No** — invoice **`ISSUED`** (not PAID) | DB |
| 6 | Duplicate settlement | **N/A** — no SUCCESS row to duplicate; multiple **initiate-only** PENDING rows from repeated harness runs | DB |
| 7 | Inbound Razorpay webhook | **No** — `commercial.saas_provider_event` for RAZORPAY **empty**; only agent **invalid** HMAC probe → 422 | DB + logs |

**Diagnosis:** Latest harness run recorded `cancelled: true` (`ondismiss` / harness `CHECKOUT_CANCELLED`). Checkout `<pre id="out">` has **no** `razorpay_payment_id` / signature — modal close or dismiss **without** capture. Closing Checkout is **not** treated as payment success.

**Journey status:** **Incomplete** (unchanged: GAP-JRN-008 / GAP-API08-006 remain partial sandbox, not E2E-complete).

## Remaining external dependencies

- Human completion of Razorpay Checkout in browser or device (iframe automation not authorized in CI/agent)
- Approved public webhook tunnel + dashboard URL → `POST /api/v1/webhooks/razorpay` with `RAZORPAY_WEBHOOK_SECRET` alignment
- Android hardware/emulator for UPI Intent proof
- Production payment enablement (explicitly **not** in scope)

## Security preserved

Tenant isolation, idempotency, server-side verify, webhook HMAC, no client-trusted success without verify/webhook.
