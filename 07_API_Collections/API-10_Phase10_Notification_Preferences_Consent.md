# API-10 Phase 10 — Preferences and Consent

## Summary

Consent and channel preferences use existing `customer.customer_preference` rows:

- `notification.promotional.consent` — required for promotional sends (JSON `{ "consented": true, ... }`).
- `notification.channel.{email|sms|whatsapp|push|in_app}` — channel opt-out via `{ "enabled": false }`.

Dispatch-time enforcement in `NotificationService.deliver` records `lifecycle=suppressed` with `RECIPIENT_SUPPRESSED`. Business-event promotional rules require consent instead of the Phase 5 skip.

## API

**API-10-024** `PATCH /api/v1/notification-preferences/{preference_id}` — staff update (`manage.notification.preferences`).

There is no customer login; self-service preference UI depends on a future customer identity flow.

## Defaults

- Operational notifications: channel enabled if preference row missing.
- Promotional: no consent unless explicitly recorded (no backfill of opt-in).
