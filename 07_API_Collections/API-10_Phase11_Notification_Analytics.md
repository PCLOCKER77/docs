# API-10 Phase 11 — Notification Analytics

## Summary

**API-10-023** `GET /api/v1/notifications/reports` returns org-scoped aggregates from `queued_messages` and `message_delivery_attempts`.

## Metric semantics

| Metric | Definition |
|--------|------------|
| `logical_notifications_queued` | Rows created in period |
| `provider_accepted_attempts` | Attempts with status `SENT` after provider acceptance |
| `suppressed_recipients` | Attempts with `error_code=RECIPIENT_SUPPRESSED` |
| `by_channel_queued` | Queued messages grouped by channel |

Retries are not counted as new logical notifications. SMTP/push/SMS acceptance is **not** confirmed delivery.

## Authorization

Requires `view.notification.reports` and organization access; Platform Admin does not receive tenant data through this route.
