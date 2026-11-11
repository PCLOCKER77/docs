# API-10 Phase 6 — Real email delivery (SMTP)

## Selected provider

**SMTP** via existing `EMAIL_PROVIDER` / `SMTP_*` settings (same stack as identity credential email in `app/infrastructure/email/service.py`).

Rationale: configuration and `send_simple_smtp_email` already exist; no new vendor dependency.

## Configuration

| Variable | Purpose |
|----------|---------|
| `EMAIL_PROVIDER` | `smtp`, `memory`, `none`, or empty (env-based default) |
| `EMAIL_FROM` | From address (required for SMTP) |
| `SMTP_HOST` | SMTP server host |
| `SMTP_PORT` | Port (default 587) |
| `SMTP_USE_TLS` | STARTTLS when true |
| `SMTP_USERNAME` / `SMTP_PASSWORD` | Optional auth (secrets via env only) |

**Notification provider selection**

- `ENVIRONMENT=test` → always **mock** (pytest).
- `resolved_email_provider()` → `smtp` in qa/staging/production when unset.
- When SMTP mode and host/from present → `SmtpNotificationDeliveryProvider` for **EMAIL** only.
- SMS/WhatsApp/other channels → mock until later phases.
- SMTP mode but missing host/from → EMAIL deliveries **fail** with `PROVIDER_NOT_CONFIGURED` (not silent mock success).

## Status semantics

| Layer | Meaning |
|-------|---------|
| `queued_messages.status=SENT` | All recipient submission attempts succeeded (provider accepted). |
| `message_delivery_attempts.status=SENT` | Provider accepted submission for that recipient. |
| `lifecycle=provider_accepted` in JSON | **Not** confirmed inbox delivery. |
| `DELIVERED` attempt status | **Not used** without webhook/DSP evidence. |

## Retries

Existing `notifications_retry` + `MAX_DELIVERY_ATTEMPTS` unchanged. Transient SMTP errors classified in `provider_response.failure_class=transient`; permanent errors (invalid recipient, auth) should not succeed on retry without config fix.

**Idempotency:** delivery idempotency keys unchanged. SMTP has no idempotency key — ambiguous timeouts may cause duplicate email if retried after unknown acceptance.

## Files

- `app/infrastructure/email/service.py` — `send_simple_smtp_email`
- `app/modules/communication/smtp_delivery.py` — SMTP adapter + routing
- `app/modules/communication/delivery.py` — provider factory
- `app/modules/communication/notification_service.py` — attempt metadata includes `error_code`

## Migration

None. Uses existing `message_delivery_attempts`.

## Live verification

Automated tests use mocks. **Live SMTP not verified** in this task unless separately tested against MailHog/production SMTP with authorization.

## Next phase

Phase 7 — SMS/WhatsApp providers behind the same abstraction pattern.
