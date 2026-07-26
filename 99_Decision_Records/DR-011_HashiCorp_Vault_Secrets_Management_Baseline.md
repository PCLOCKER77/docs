# DR-011 HashiCorp Vault Secrets Management Baseline

> Decision record for the Digitize secrets-management baseline.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-011 |
| Document Name | HashiCorp Vault Secrets Management Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Security / DevOps |
| Reviewers | Architecture, Backend Engineering, DevOps, Operations, QA, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

HashiCorp Vault is selected as the secrets-management baseline for Digitize.

Local development may use non-secret templates and local environment files, but shared and production environments shall use controlled secret storage and injection.

---

# 2. Context

Digitize requires secure handling of database credentials, JWT signing material, provider credentials, webhook secrets, encryption keys, API tokens, and operational credentials.

Deployment and backend documents require a concrete secret-management baseline that avoids hardcoded values and repository-stored secrets.

---

# 3. Decision

Digitize shall use HashiCorp Vault as the baseline for:

- Application secrets.
- Database credentials where applicable.
- JWT signing and verification material.
- Provider credentials.
- Webhook secrets.
- Encryption keys or key references.
- CI/CD deployment secrets.
- Runtime secret injection into containerized workloads.

Secrets shall not be committed to the documentation repository or source repository.

Secret access shall be environment-scoped, least-privilege, auditable, and revocable.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| HashiCorp Vault | Provider-neutral enterprise secret manager | Accepted |
| Cloud-provider secret manager | Managed secret store tied to a cloud provider | Deferred until provider selection is approved |
| Kubernetes Secrets only | Native Kubernetes secret objects | Rejected as the sole baseline because enterprise audit and rotation governance need stronger control |
| Environment files | Simple local configuration | Rejected for shared or production environments |

---

# 5. Rationale

Vault provides a provider-neutral baseline with strong access control, auditability, secret rotation support, and integration options for containerized deployments.

It fits the current provider-neutral deployment baseline while leaving room for a future managed cloud secret service decision.

---

# 6. Consequences

## Positive Consequences

- Secret-management ambiguity is removed.
- Security and deployment docs can define concrete controls.
- Provider credentials and signing material have a governed home.
- CI/CD and runtime secret injection can be standardized.

## Tradeoffs

- Vault introduces operational responsibility.
- Teams must manage policies, authentication methods, rotation, and audit logs.

## Risks

- Misconfigured Vault policies could overexpose secrets.
- Vault availability must be considered for runtime startup and incident recovery.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `11_Deployment/DEP-04_Configuration_Secrets_Management.md` | Uses Vault as secrets baseline |
| `10_Backend_Engineering/BE-00_Backend_Engineering_Standards.md` | Defines runtime secret access expectations |
| `08_Integration_Contracts/IC-12_Integration_Security_Contract.md` | Aligns provider credential handling |
| `13_Operations/OPS-07_Security_Access_Operations.md` | Aligns operational access controls |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Secret-management baseline | Security / DevOps |
| Secret policies | Security |
| Runtime injection | DevOps |
| Application consumption | Backend Engineering |
| Future changes | Architecture Governance / Security |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current secrets-management baseline.

It may be frozen after security, deployment, backend, operations, and integration documents align with Vault-based secret handling.

