# DR-016 AWS Cloud Provider Baseline

> Decision record for selecting AWS as the cloud provider baseline for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-016 |
| Document Name | AWS Cloud Provider Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Architecture Governance / DevOps |
| Reviewers | Backend Engineering, Database Engineering, Security, Operations, QA, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

AWS is selected as the cloud provider baseline for Digitize.

---

# 2. Context

Deployment documentation previously used provider-neutral language. Development planning now requires a concrete cloud baseline for database, storage, cache, container registry, deployment targets, secrets, monitoring, and release readiness.

---

# 3. Decision

Digitize shall use AWS as the initial cloud provider baseline.

AWS-aligned services may include:

- Amazon RDS for PostgreSQL.
- Amazon S3 for object storage.
- Amazon ElastiCache for Redis.
- Amazon ECR for container images.
- Amazon EKS or another approved Kubernetes-compatible AWS runtime for production workloads.
- AWS Secrets Manager or HashiCorp Vault integration for secret storage depending on security review.
- Amazon CloudWatch as an AWS-native infrastructure signal source.

OpenTelemetry, Prometheus, Grafana, Loki, and Tempo remain the application observability baseline unless superseded.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| AWS | Broad managed-service ecosystem and strong PostgreSQL, storage, cache, and container support | Accepted |
| Azure | Strong enterprise cloud platform | Rejected for initial baseline |
| Google Cloud | Strong cloud-native services | Rejected for initial baseline |
| Provider-neutral only | Delay provider selection | Rejected because development and deployment need concrete cloud assumptions |

---

# 5. Consequences

## Positive Consequences

- Deployment planning can target real cloud services.
- Database, object storage, cache, and registry decisions become concrete.
- AWS cost, security, IAM, networking, and environment planning can begin.

## Tradeoffs

- Some deployment guidance becomes AWS-specific.
- Future cloud migration would require a superseding decision record and migration plan.

## Risks

- AWS IAM, networking, and secrets configuration can become complex without strong governance.
- Teams may accidentally use AWS-specific features where provider-neutral abstractions are still preferred.

---

# 6. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `11_Deployment/` | AWS becomes the cloud provider baseline |
| `06_Database_Design/` | PostgreSQL production target aligns with Amazon RDS |
| `10_Backend_Engineering/` | Runtime dependencies align with AWS managed services where applicable |
| `13_Operations/` | AWS operations, IAM, monitoring, backup, and recovery become relevant |
| `16_Development_Readiness/` | Development planning targets local parity with AWS services |

---

# 7. Review and Freeze Rule

This decision is `Accepted` for initial development and deployment planning.

It may be frozen after AWS environment strategy, cost ownership, IAM model, networking, secrets, backup, and operational readiness are reviewed.

