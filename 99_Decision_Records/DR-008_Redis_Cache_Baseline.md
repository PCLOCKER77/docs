# DR-008 Redis Cache Baseline

> Decision record for selecting Redis as the runtime cache baseline.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-008 |
| Document Name | Redis Cache Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Backend Engineering / DevOps |
| Reviewers | Architecture, Backend Engineering, Security, DevOps, Operations, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Redis is selected as the runtime cache baseline for Digitize.

Redis shall be used only for cacheable, reproducible, or short-lived runtime state. PostgreSQL remains the source of truth for business data.

---

# 2. Context

Digitize requires efficient access to frequently used runtime data such as permission lookups, tenant context resolution, short-lived idempotency lookups, rate-limit counters, feature flag snapshots, and safe reference-data caching.

These concerns should not require repeated database reads when cached values can be safely invalidated or regenerated.

---

# 3. Decision

Digitize shall use Redis for:

- Permission and role lookup caching.
- Tenant context lookup caching.
- Short-lived idempotency lookup acceleration.
- Rate limiting counters.
- Feature flag and configuration snapshots where approved.
- Reference-data caching where stale-read tolerance is defined.
- Worker coordination primitives where approved.

Redis shall not store:

- Raw secrets.
- Primary business records.
- Financial source-of-truth records.
- Audit source-of-truth records.
- Tenant data that cannot be regenerated.
- Long-term release, testing, or operations evidence.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Redis | Mature in-memory cache with broad ecosystem support | Accepted |
| PostgreSQL-only caching | Use database reads without runtime cache | Rejected because permission, tenant, and rate-limit paths benefit from fast cache access |
| Memcached | Simple cache service | Rejected because Redis supports broader runtime patterns |
| Application memory only | Per-process cache | Rejected because multi-instance deployments need shared cache behavior |

---

# 5. Rationale

Redis is widely used for FastAPI/Python runtime caching, rate limiting, and short-lived coordination patterns.

It improves performance for repeated reads while keeping PostgreSQL as the durable source of truth.

---

# 6. Consequences

## Positive Consequences

- Cache technology ambiguity is removed.
- Backend tenant and authorization paths can define concrete cache behavior.
- Deployment can include Redis readiness and health checks.
- Operations can monitor cache availability, memory, evictions, and latency.

## Tradeoffs

- Cache invalidation rules must be explicit.
- Redis outage behavior must be defined for each cached concern.

## Risks

- Stale cache values may affect authorization or tenant context if invalidation is weak.
- Teams may misuse Redis as a database unless governance is enforced.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `10_Backend_Engineering/BE-05_Authentication_Authorization_Implementation.md` | Permission and authorization cache behavior |
| `10_Backend_Engineering/BE-06_Tenant_Context_Implementation.md` | Tenant context cache behavior |
| `11_Deployment/DEP-02_Infrastructure_Deployment_Architecture.md` | Redis runtime dependency |
| `13_Operations/OPS-02_Monitoring_Alerting_Operations.md` | Redis monitoring and alerts |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Cache usage policy | Backend Engineering |
| Redis provisioning | DevOps |
| Redis operations | Operations / DevOps |
| Security review | Security |
| Future cache changes | Architecture Governance |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current cache baseline.

It may be frozen after cache usage, invalidation, fallback, monitoring, and deployment behavior are reviewed.

