# DR-017 Modular Monolith Baseline

> Decision record for selecting a modular monolith as the initial backend architecture style.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-017 |
| Document Name | Modular Monolith Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Architecture Governance / Backend Engineering |
| Reviewers | Product, Backend Engineering, Database Engineering, API, Integration, DevOps, QA, Operations |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Digitize shall start as a modular monolith, not microservices.

The architecture shall preserve clear module boundaries so selected modules can be split into services later if scale, ownership, deployment, or operational needs justify it.

---

# 2. Context

Digitize has many business modules, but the initial product needs faster delivery, simpler deployment, consistent transaction handling, and lower operational overhead.

Microservices would introduce service discovery, distributed transactions, network failure handling, independent deployment governance, and operations complexity before the platform has validated module boundaries.

---

# 3. Decision

Digitize backend implementation shall use a modular monolith.

The modular monolith shall:

- Use one deployable backend application initially.
- Keep modules clearly separated by package boundaries.
- Keep domain services independent from FastAPI routes.
- Keep repositories module-owned.
- Avoid cross-module table mutation from unrelated modules.
- Use service boundaries, query contracts, or outbox events for cross-module behavior.
- Preserve API and event contracts so modules can be split later.
- Avoid distributed-service assumptions during initial development.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Modular monolith | Single deployable with strong internal module boundaries | Accepted |
| Microservices from day one | Independently deployed services per domain | Rejected because operational and coordination cost is too high initially |
| Simple layered monolith | Single application without strict module boundaries | Rejected because future service extraction would be harder |
| Serverless per capability | Function-oriented backend | Rejected for initial baseline due to complexity and consistency concerns |

---

# 5. Consequences

## Positive Consequences

- Faster initial development.
- Simpler deployment and testing.
- Easier database transaction management.
- Lower operational overhead.
- Future service extraction remains possible through module boundaries.

## Tradeoffs

- Independent deployment per module is not available initially.
- Strong code-review discipline is required to prevent module boundary erosion.

## Risks

- If modules are not enforced, the monolith can become tightly coupled.
- Later service extraction requires clear contracts, data ownership, and event boundaries.

---

# 6. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `05_Technical_Architecture/` | Runtime architecture starts as modular monolith |
| `10_Backend_Engineering/` | Project structure, domain services, repositories, and outbox use modular boundaries |
| `07_API_Collections/` | API contracts remain module-oriented |
| `08_Integration_Contracts/` | Integration contracts avoid assuming microservice topology |
| `11_Deployment/` | One backend application plus workers is deployed initially |
| `16_Development_Readiness/` | Implementation plan starts with modular monolith structure |

---

# 7. Review and Freeze Rule

This decision is `Accepted` for initial development.

It may be frozen after the first vertical slice proves module boundaries, API boundaries, repository ownership, and outbox/event behavior can be maintained inside one backend deployable.

