# API-10 Phase 7 — SMS and WhatsApp Delivery

## Summary

SMS and WhatsApp notifications use dedicated providers behind `MultiChannelRoutingNotificationDeliveryProvider`, mirroring the Phase 6 SMTP pattern. Each channel records independent `provider_accepted` attempts; failures do not affect other channels.

## Providers

| Channel | Provider module | Configuration |
|---------|-----------------|---------------|
| SMS | `SmsNotificationDeliveryProvider` | `SMS_PROVIDER=memory` (test/QA) or `none` (disabled) |
| WhatsApp | `WhatsAppNotificationDeliveryProvider` | `WHATSAPP_PROVIDER=memory` or `cloud_api` + Meta credentials |

Phone validation reuses `customer.phone.normalize_phone` digit rules without inferring country.

## Live verification

- **SMS:** No live SMS gateway adapter beyond `memory`; configure a future provider before production SMS.
- **WhatsApp:** Cloud API path calls existing `_send_cloud_api`; not live-verified in this task.

## Tests

`tests/communication/test_mobile_channel_delivery.py` (mocked; no real messages).
