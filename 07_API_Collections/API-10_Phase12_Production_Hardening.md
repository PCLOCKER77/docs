# API-10 Phase 12 — Production Hardening

## Security

- Organization scoping preserved on reports, preferences, and notification lifecycle.
- Device tokens bound to authenticated `principal_id`; revoke checks ownership.
- Provider credentials remain in settings/env only; tests use memory mocks.
- Suppression distinguished from provider failure via `lifecycle=suppressed`.

## Reliability

- Per-channel outcomes independent (routing provider).
- Worker uses row locks; campaign schedule marked `SENT` after launch attempt.
- No claim of exactly-once external delivery.

## Migrations (not applied)

| Revision | Depends on | Purpose |
|----------|------------|---------|
| 064–067 | (prior chain) | Phases 1–4 foundation |
| **068** | 067 | PUSH channel, device tokens, report/preference permissions |

## Tests run

```bash
pytest tests/communication tests/campaign -q
```

**Result:** 52 passed (this task).

## Not verified

- Live SMS/WhatsApp/FCM submission
- Worker execution in QA/production
- Migration 068 on PostgreSQL
- Flutter push client
