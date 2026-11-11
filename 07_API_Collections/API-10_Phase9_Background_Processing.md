# API-10 Phase 9 — Background Processing

## Summary

`app/modules/communication/notification_worker.py` implements one durable tick:

1. Claim due `communication.queued_messages` (`FOR UPDATE SKIP LOCKED`) and deliver/retry via `NotificationService` under a SYSTEM principal.
2. Launch due `campaign.campaign_schedule` rows (status `SCHEDULED`, `scheduled_at <= now`) via `CampaignService.launch`.

## Operations

Run locally (requires DB + applied migrations):

```bash
python3 scripts/run_notification_worker.py
```

Poll interval, deployment, and process supervision are **external** (cron, ECS task, etc.) — not deployed in this task.

## Verification

Worker logic covered by unit-style tests where mocked; **not** verified against PostgreSQL or QA/production runtime.
