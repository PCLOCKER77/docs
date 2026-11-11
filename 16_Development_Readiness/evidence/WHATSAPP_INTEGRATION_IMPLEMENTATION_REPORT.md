# WhatsApp integration — implementation report

**Date:** 2026-11-09  
**Architecture:** Hybrid sender (central vs org-owned) — **unchanged**, per approved product decision.

---

## 1. Existing foundation (preserved)

| Component | Location |
|-----------|----------|
| Sender resolution | `whatsapp_sender_resolution.py` |
| Cloud API send | `infrastructure/whatsapp/cloud_api.py` |
| Delivery provider | `mobile_channel_delivery.py` |
| No silent central fallback | `test_org_whatsapp_sender_fails_without_silent_central_fallback` |
| Plaintext credential rejection | `test_org_whatsapp_setting_rejects_plaintext_secrets` |

---

## 2. Implemented this pass

| # | Capability | Status |
|---|------------|--------|
| 1 | Meta webhook verification (`hub.challenge`) | **IMPLEMENTED** — `GET /api/v1/webhooks/whatsapp` |
| 2 | Signature verification (`X-Hub-Signature-256`) | **IMPLEMENTED** — HMAC-SHA256 with `WHATSAPP_APP_SECRET` |
| 3 | Status event parsing | **IMPLEMENTED** — counts delivered/failed statuses |
| 4 | Idempotent duplicate `wamid` | **IMPLEMENTED** (in-process set; cap 10k) |
| 5 | Settings | `WHATSAPP_APP_SECRET`, `WHATSAPP_WEBHOOK_VERIFY_TOKEN` in `Settings` + `.env.example` |
| 6 | Unit tests | `tests/communication/test_whatsapp_webhook.py` — **3 passed** |

---

## 3. Not live-verified

| Item | Reason |
|------|--------|
| Outbound message to Meta | No QA/production tokens in repo (correct) |
| Webhook callback from Meta | Requires public HTTPS endpoint + App Dashboard config |
| Template sync / WABA onboarding | Operator action in Meta Business Manager |

**QA stance:** Keep `WHATSAPP_PROVIDER=none` or `memory` until credentials and webhook URL are configured.

---

## 4. Meta actions required (exact)

1. Create / confirm WhatsApp Business Account and phone number.  
2. Generate long-lived **Cloud API token** and **Phone number ID**.  
3. Set App **secret** and **verify token** in Secrets Manager (QA).  
4. Register webhook URL: `https://<qa-host>/api/v1/webhooks/whatsapp`.  
5. Subscribe to `messages` status fields.  
6. Run one authorized test message to approved test MSISDN.

---

## 5. Tests

```bash
cd digitize-services
.venv/bin/pytest tests/communication/test_whatsapp_webhook.py \
  tests/communication/test_communication_service_consolidated.py -q
```

---

## 6. Follow-up engineering (non-blocking for core QA)

- Persist provider message IDs and delivery status to `communication.message_delivery_attempts` (or approved table).  
- Replace in-memory webhook dedupe with DB unique constraint on provider message id.

**Feature gate:** WhatsApp **safely disabled** for QA until Meta onboarding completes; does **not** block other QA journeys.
