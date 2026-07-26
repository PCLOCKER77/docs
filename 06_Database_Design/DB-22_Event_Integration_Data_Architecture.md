# DB-22 Event & Integration Data Architecture

**Document ID:** DB-22  
**Document Name:** Event & Integration Data Architecture  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Event and Integration Data Architecture  
**Database Engine:** PostgreSQL  
**Version:** 0.1  
**Status:** Design Draft  
**Classification:** Internal  
**Confidentiality:** Confidential  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the event and integration data architecture for Digitize.

It explains how database-backed integration state, event traceability, provider callbacks, retry handling, outbox patterns, idempotency, and future event-streaming readiness shall be modeled.

---

# 2. Event and Integration Principles

| Principle | Requirement |
|---|---|
| Interface-first | Integrations shall flow through approved service boundaries |
| Idempotency | Provider callbacks and retryable operations shall be idempotent |
| Traceability | Events shall carry correlation and source references |
| Tenant awareness | Tenant context shall be preserved where event data is tenant-specific |
| Reliability | Integration events shall support retry and failure tracking |
| Security | Integration payloads shall not expose secrets or raw payment data |

---

# 3. Event Data Patterns

| Pattern | Purpose |
|---|---|
| Outbox pattern | Reliably publish events after transactional state change |
| Inbox pattern | Idempotently process received events/callbacks |
| Retry queue | Track failed or delayed integration work |
| Dead-letter record | Preserve exhausted failures for investigation |
| Provider reference table | Store external provider identifiers safely |
| Correlation ID | Connect API, event, audit, log, and support records |

---

# 4. Candidate Event Tables

Future event/integration implementation may introduce:

| Table | Purpose |
|---|---|
| integration.integration_provider | Provider registry |
| integration.integration_configuration | Provider configuration metadata |
| integration.integration_outbox | Pending outbound domain events |
| integration.integration_inbox | Received provider callbacks/events |
| integration.integration_attempt | Retry and delivery attempts |
| integration.integration_failure | Failure diagnostics and dead-letter records |
| integration.integration_subscription | External webhook/subscription registrations |

These structures shall be finalized only when implementation architecture confirms integration service boundaries.

---

# 5. Outbox Event Model

Outbox records should include:

| Field | Purpose |
|---|---|
| record_id | Primary identifier |
| organization_id | Tenant scope where applicable |
| event_type | Business event name |
| source_entity_type | Source table/entity |
| source_entity_id | Source record identifier |
| event_payload | Event payload |
| event_status | Pending, published, failed, dead-letter |
| correlation_id | Traceability across systems |
| occurred_at | Business event time |
| published_at | Publish completion time |
| metadata | Controlled extension attributes |

---

# 6. Inbox Event Model

Inbox records should include:

| Field | Purpose |
|---|---|
| record_id | Primary identifier |
| provider_code | External provider |
| provider_event_id | Provider event reference |
| idempotency_key | Duplicate prevention |
| event_type | Provider or integration event type |
| event_payload | Controlled event payload |
| processing_status | Processing lifecycle |
| received_at | Callback receipt time |
| processed_at | Processing completion time |
| correlation_id | Cross-system traceability |
| metadata | Controlled extension attributes |

---

# 7. Integration Events

Initial integration event categories:

- Payment initiated.
- Payment completed.
- Payment failed.
- Refund requested.
- Refund processed.
- Invoice generated.
- Notification requested.
- Notification delivered.
- Notification failed.
- Campaign scheduled.
- Support ticket created.
- Audit event captured.

---

# 8. Idempotency Strategy

Idempotency shall be enforced for:

- Payment attempts.
- Refund attempts.
- Provider callbacks.
- Notification retries.
- Campaign delivery retries.
- Report generation requests where duplicate execution is harmful.

Idempotency keys shall be unique within provider, tenant, and operation scope.

---

# 9. Retry and Failure Strategy

Retry records shall capture:

- Attempt number.
- Attempt status.
- Provider response.
- Failure code.
- Failure message.
- Next retry time.
- Retry exhaustion status.
- Dead-letter reason.

Failures shall be visible to operations and support teams where business impact exists.

---

# 10. CDC and Event Streaming Readiness

Future implementations may evaluate:

- Change Data Capture.
- Kafka or compatible event streaming.
- Webhook subscriptions.
- Event replay.
- Event-driven reporting projections.
- Integration marketplace patterns.

CDC shall not be enabled for sensitive data without security review.

---

# 11. Summary

DB-22 defines the event and integration data architecture foundation required for reliable provider integrations, asynchronous processing, retry handling, and future event-driven expansion.
