# FCM HTTP v1 backend adapter — completion report

**Outcome:** `IMPLEMENTED — MOCKED TESTS PASS; EXTERNAL CONFIGURATION REQUIRED`

## 1. Summary

Implemented Firebase Cloud Messaging **HTTP v1** in `app/infrastructure/push/fcm_v1.py` and wired it into `PushNotificationDeliveryProvider`. The previous stub that always failed with “FCM HTTP v1 adapter is not enabled” is removed. Live delivery is **not** verified.

## 2. Files changed

- `app/infrastructure/push/fcm_v1.py` (new)
- `app/modules/communication/push_delivery.py`
- `app/modules/communication/device_token_service.py` (`mark_token_unregistered`)
- `app/modules/communication/notification_service.py` (revoke on `TOKEN_UNREGISTERED`, pass `delivery_context`)
- `app/modules/communication/delivery.py`, `channel_routing.py`, `smtp_delivery.py`, `mobile_channel_delivery.py` (optional `delivery_context` on provider protocol)
- `app/config/settings.py`, `.env.example`, `pyproject.toml` / lock (`google-auth`)
- `tests/communication/test_fcm_push_delivery.py` (new)
- `docs/07_API_Collections/API-10_Phase8_Push_Notifications.md`

## 3. Provider configuration

- `PUSH_PROVIDER=fcm|memory|none`
- `FCM_PROJECT_ID`, `FCM_SERVICE_ACCOUNT_FILE`, `FCM_REQUEST_TIMEOUT_SECONDS`
- Or `GOOGLE_APPLICATION_CREDENTIALS` for the JSON path

## 4. Credential handling

Server-side only via `google-auth` service account file. Access tokens cached in-process with refresh before expiry. No credentials logged. No AWS changes in this task.

## 5. Device-token lookup and tenant isolation

Delivery uses the FCM token in `recipient_value` for each attempt (one token per attempt). Registrations are user-scoped at registration time. FCM `UNREGISTERED` triggers `mark_token_unregistered` by token fingerprint—no cross-tenant broadcast.

## 6. Delivery and error mapping

| FCM / network | `error_code` | `failure_class` |
|---------------|--------------|-----------------|
| 200 acceptance | *(success)* `provider_accepted` | — |
| UNREGISTERED / 404 token | `TOKEN_UNREGISTERED` | permanent |
| 401/403 | `AUTH_FAILED` | permanent |
| 429 | `RATE_LIMITED` | transient |
| 5xx | `PROVIDER_ERROR` | transient |
| Timeout | `NETWORK_ERROR` | transient |

## 7. Worker integration

Unchanged worker and queue semantics; failures remain `FAILED` with retry scheduling per existing rules. No false success when FCM is unconfigured.

## 8. Tests executed

```bash
poetry run pytest tests/communication tests/campaign -q
```

Record from latest run: **61 passed** (`poetry run pytest tests/communication tests/campaign -q`).

## 9. Remaining Firebase configuration

- Firebase project + service account with Firebase Cloud Messaging API enabled
- JSON key mounted at runtime (Secrets Manager / env path)
- `PUSH_PROVIDER=fcm`, `FCM_PROJECT_ID` set
- iOS APNs key in Firebase for Apple devices

## 10. Remaining QA / live verification

Authorized real-device push smoke test not performed.

## 11. Security findings

- Credentials server-side only; not in Flutter or repo
- Authorization headers and full device tokens not logged
- Bounded HTTP timeout
- Unconfigured provider returns explicit failure, not success

## 12. Safety confirmation

| Action | Occurred? |
|--------|-----------|
| Protected DB mutated | **No** |
| Migrations applied | **No** |
| AWS / Terraform changed | **No** |
| Deploy / commit / push | **No** |
| Real FCM messages sent | **No** |
