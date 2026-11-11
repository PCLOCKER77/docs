# Final WhatsApp integration report — QA cutover

**Date:** 2026-11-09  
**Architecture:** Hybrid sender (central Digitize default; org-owned WABA supported) — **preserved**, no silent central fallback.

---

## 1. Implementation status

| Capability | Status |
|--------------|--------|
| Provider abstraction | Present (`WHATSAPP_PROVIDER` setting) |
| Meta Cloud API outbound | Code paths exist; **live credentials not verified** |
| Credential / template resolution | Per-tenant settings; no QA secrets applied |
| Consent enforcement | Existing communication module rules preserved |
| Webhook challenge (`GET`) | **Implemented** — `WHATSAPP_WEBHOOK_VERIFY_TOKEN` |
| Webhook HMAC (`POST`) | **Implemented** — `WHATSAPP_APP_SECRET` |
| In-memory idempotency / replay | **Implemented** (process-local; not durable cross-instance) |
| Durable provider message ID / delivery status in DB | **Not implemented** (future hardening) |
| Live Meta delivery test | **Not run** |

**QA configuration (required):** `WHATSAPP_PROVIDER=none` (or empty) until Meta Business onboarding and webhook URL registration on the QA ALB are complete.

---

## 2. Routes

- `GET /api/v1/webhooks/whatsapp` — Meta hub verification.
- `POST /api/v1/webhooks/whatsapp` — Signed status callbacks; rejects missing/invalid signature.

---

## 3. Tests

```bash
cd digitize-services
poetry run pytest tests/communication/test_whatsapp_webhook.py -q
```

**Result:** **Pass** (included in security regression batch).

---

## 4. Meta onboarding checklist (external)

Operations must supply:

1. Meta Business Manager + WABA for QA (or org-owned sender per tenant policy).
2. `WHATSAPP_PHONE_NUMBER_ID`, long-lived token in Secrets Manager (never in repo).
3. App secret for HMAC + verify token for challenge.
4. Public HTTPS webhook URL on QA ALB (`/api/v1/webhooks/whatsapp`).
5. Template approval for financial/transactional use cases (if used).

Until then: **do not claim live WhatsApp in QA handover scenarios.**

---

## 5. Verdict

| Environment | WhatsApp |
|-------------|----------|
| Local dev | Safe off (`WHATSAPP_PROVIDER` unset) |
| QA target | **Disabled by configuration** |
| Production | Blocked on onboarding + durable delivery audit |
