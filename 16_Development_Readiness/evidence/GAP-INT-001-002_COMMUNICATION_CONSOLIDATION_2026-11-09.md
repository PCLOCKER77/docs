# GAP-INT-001 / GAP-INT-002 — Communication channels consolidated implementation

**Date:** 2026-11-09  
**Status:** **Application boundary implemented** — live provider delivery remains **external dependency**

## 1. Central Communication Service

| Component | Path | Role |
|-----------|------|------|
| Facade | `app/modules/communication/communication_service.py` | `CommunicationService.deliver_outbound` — consent, tenant context, provider routing |
| Provider registry | `app/modules/communication/delivery.py` | `get_notification_delivery_provider()` — unchanged entry for worker + notifications |
| Channel router | `app/modules/communication/channel_routing.py` | **Reused** — no cross-channel fallback on failure |
| Notification lifecycle | `app/modules/communication/notification_service.py` | **Reused** — now passes `organization_id` in `delivery_context` |

Business modules should prefer `CommunicationService` or existing `NotificationService` / pending queues (email, WhatsApp flush) — not direct provider SDKs.

## 2. Channel status

| Channel | In code | Production send | Notes |
|---------|---------|-----------------|-------|
| **Email SMTP / Mailpit** | **Unchanged + regression tested** | Dev Mailpit when `EMAIL_PROVIDER=smtp` + host/from | `SmtpNotificationDeliveryProvider`, `SmtpReportNotifier`, `HeldReportNotifier` preserved |
| **Email SES** | **Adapter implemented** | **Blocked** — needs `EMAIL_PROVIDER=ses`, `EMAIL_FROM`, `AWS_REGION`, IAM/domain verification | `SesNotificationDeliveryProvider` |
| **SMS** | **Boundary only** | **Deferred (product)** — OTP not activated | `memory`/`none` unchanged; `Msg91SmsNotificationDeliveryProvider` fails with `PROVIDER_NOT_IMPLEMENTED` until vendor sign-off |
| **WhatsApp** | **Hybrid sender resolution** | **Blocked** — Meta business account, templates, secrets | `resolve_whatsapp_sender`; org settings via existing `organizations_settings_update` |

## 3. WhatsApp hybrid sender (org vs central)

Organization settings (existing API **API-02** `organizations_settings_update`):

| Key | Purpose |
|-----|---------|
| `organization.communication.whatsapp.sender_mode` | `CENTRAL` (default) or `ORGANIZATION` |
| `organization.communication.whatsapp.org_sender` | `phone_number_id` + `credential_secret_ref` (no plaintext secrets) |
| `organization.communication.whatsapp.fallback_policy` | `NONE` (default) or explicit `ALLOW_CENTRAL` |

Rules implemented:

- No silent switch to central when org sender is selected and unavailable.
- Fallback only when `ALLOW_CENTRAL` is set (auditable via org setting update).
- Financial alerts pass `organization_id` on `PendingWhatsApp` for flush-time resolution.

## 4. Reused (not duplicated)

- Notification queue, templates, rules, worker, PII encryption, eligibility/consent
- SMTP identity mail + report attachment delivery
- API-10 operations (no new numbered APIs)
- Platform settings pattern (email/SMS/WhatsApp remain env-driven for platform credentials)

## 5. Provider dependencies (not claimed complete)

| Provider | Onboarding / credentials | Legal / consent |
|----------|-------------------------|-----------------|
| **SES** | AWS account, domain/DKIM, IAM or instance role | Production FROM domain approval |
| **MSG91** | API key, DLT/India compliance TBD | Vendor verification pending — HTTP client not implemented |
| **Meta WhatsApp** | Cloud API token, phone number ID, approved templates | Opt-in / messaging window per Meta policy |

## 6. Tests

```text
poetry run pytest tests/communication/test_communication_service_consolidated.py \
  tests/communication/test_smtp_email_delivery.py -q
# 14 passed
```

Covers: SES configured check, SES mocked send, MSG91 fail-closed, org setting validation, no silent WhatsApp fallback, service routing, SMTP regression suite.

**Not claimed:** live SES/MSG91/Meta delivery, production OTP/SMS.

## 7. Product decisions still open

- MSG91 vs Gupshup selection and DLT template registration
- Production email tier approval (Mailpit vs SES) — GAP-INT-002
- SMS/OTP in first release — **remain deferred** (GAP-INT-001)
- Proposed PA platform UI for central WhatsApp defaults (optional; env sufficient today)

## 8. Final channel verdict

| Channel | App status | Blocker |
|---------|------------|---------|
| Email (SMTP) | **Ready in dev** | Production tier approval |
| Email (SES) | **Prepared** | AWS + domain |
| SMS | **Prepared boundary** | Product deferral + vendor |
| WhatsApp | **Prepared hybrid policy** | Meta onboarding + secrets |
