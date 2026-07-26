# DR-009 Celery Background Worker Baseline

> Decision record for selecting Celery as the background worker baseline.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-009 |
| Document Name | Celery Background Worker Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Backend Engineering / DevOps |
| Reviewers | Architecture, Backend Engineering, Integration, DevOps, QA, Operations |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Celery is selected as the Python background worker baseline for Digitize.

Redis is selected as the initial broker for Celery unless production load or reliability review requires a superseding broker decision.

PostgreSQL outbox remains the durable source of truth for integration events and provider dispatch state.

---

# 2. Context

Digitize needs background processing for notifications, reports, outbox processing, exports, provider callbacks, retries, reconciliation, maintenance jobs, and operational automation.

The backend baseline is Python and FastAPI. Background workers must reuse application services without coupling domain behavior to HTTP request handling.

---

# 3. Decision

Digitize shall use:

- Celery for background task execution.
- Redis as the initial Celery broker.
- PostgreSQL outbox tables for durable event publishing state.
- Application services as the shared business-use-case boundary for API and worker execution.

Celery tasks shall be observable, retry-safe, tenant-aware, and idempotent where retry is possible.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Celery with Redis broker | Mature Python worker model that fits FastAPI services | Accepted |
| FastAPI background tasks only | In-process lightweight background tasks | Rejected for durable production workloads |
| APScheduler only | Scheduler-focused approach | Rejected because Digitize needs queue-based asynchronous jobs |
| Cloud-native queue service only | Use provider-specific queue | Deferred to avoid binding deployment to a provider-specific service |

---

# 5. Rationale

Celery is mature, Python-native, compatible with FastAPI application-service reuse, and suitable for queued background jobs.

Using Redis initially keeps the runtime baseline simple while PostgreSQL outbox protects durable integration state.

---

# 6. Consequences

## Positive Consequences

- Worker framework ambiguity is removed.
- Backend job structure can be standardized.
- Deployment can define worker process readiness and scaling.
- Operations can monitor queues, retries, failures, and dead-letter behavior.

## Tradeoffs

- Redis broker durability must be reviewed for high-criticality workloads.
- Task idempotency and retry behavior must be carefully implemented.

## Risks

- Teams may treat Celery queue state as durable business state instead of PostgreSQL outbox state.
- Long-running tasks may affect worker capacity unless timeouts and concurrency are governed.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `10_Backend_Engineering/BE-09_Background_Jobs_Outbox_Implementation.md` | Uses Celery and Redis worker baseline |
| `08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md` | Outbox processor uses worker baseline |
| `11_Deployment/DEP-06_Backend_Deployment_Runbook.md` | Deploys API and worker processes |
| `13_Operations/OPS-02_Monitoring_Alerting_Operations.md` | Monitors worker and queue behavior |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Worker framework | Backend Engineering |
| Broker provisioning | DevOps |
| Task design and idempotency | Backend Engineering |
| Worker operations | Operations / DevOps |
| Future broker changes | Architecture Governance |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current background worker baseline.

It may be frozen after worker execution, retry, idempotency, outbox, monitoring, and deployment behavior are reviewed.

