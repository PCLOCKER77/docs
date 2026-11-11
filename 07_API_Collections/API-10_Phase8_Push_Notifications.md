# API-10 Phase 8 — Push Notifications

## Summary

Push delivery uses `PushNotificationDeliveryProvider` with:

| `PUSH_PROVIDER` | Behavior |
|-----------------|----------|
| *(test env default)* | In-memory `provider_accepted` via full mock routing in `ENVIRONMENT=test` |
| `memory` | In-memory acceptance in non-test environments |
| `fcm` | **FCM HTTP v1** via `app/infrastructure/push/fcm_v1.py` |
| `none` / unset | Structured `PROVIDER_NOT_CONFIGURED` failure |

Legacy `FCM_SERVER_KEY` is not used for HTTP v1.

## FCM HTTP v1 configuration

| Setting | Purpose |
|---------|---------|
| `PUSH_PROVIDER=fcm` | Enable live sender |
| `FCM_PROJECT_ID` | Firebase project ID |
| `FCM_SERVICE_ACCOUNT_FILE` | Path to service account JSON (server-only) |
| `GOOGLE_APPLICATION_CREDENTIALS` | Alternative file path (standard ADC) |
| `FCM_REQUEST_TIMEOUT_SECONDS` | HTTP timeout (default 20) |

Authentication: OAuth2 access token from the service account with scope `https://www.googleapis.com/auth/firebase.messaging`.

Do **not** commit service account JSON. QA/production should mount credentials via existing secret delivery (e.g. Secrets Manager) and set `FCM_SERVICE_ACCOUNT_FILE` or `GOOGLE_APPLICATION_CREDENTIALS`.

## Delivery contract

- Success → `lifecycle=provider_accepted` (not device display or read).
- FCM `UNREGISTERED` / invalid token → `TOKEN_UNREGISTERED` (permanent); `DeviceTokenService.mark_token_unregistered` revokes matching DB rows when possible.
- 401/403 → `AUTH_FAILED` (permanent).
- 429 → `RATE_LIMITED` (transient).
- 5xx / timeout → transient `PROVIDER_ERROR` / `NETWORK_ERROR`.
- Worker retry policy unchanged (existing `next_attempt_at` / max attempts).

Optional FCM **data** keys forwarded from queued message payload when present: `navigation_entity_type`, `navigation_entity_id`, `navigation_event` (same semantics as in-app inbox).

## Device tokens

Migration **068** adds `communication.user_device_tokens`. Registration extras **PUSH-001** / **PUSH-002**.

Each PUSH delivery attempt targets **one** `recipient_value` (FCM device token). Tenant isolation: tokens are registered per authenticated user; broadcasts are not performed.

## Flutter

See `digitize-ui/docs/FCM_INTEGRATION.md`.

## Live verification

**Not verified in this task.** Mocked unit tests in `tests/communication/test_fcm_push_delivery.py`. Authorized QA requires Firebase project, service account, APNs (iOS), and a real device smoke test.

## Tests

```bash
poetry run pytest tests/communication/test_fcm_push_delivery.py -q
```
