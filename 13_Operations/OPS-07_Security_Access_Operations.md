# OPS-07 Security Access Operations

> Operational security, access requests, privileged access, access reviews, credential operations, audit support, and security escalation for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | OPS-07 |
| Document Name | Security Access Operations |
| Folder | 13_Operations |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Security / Operations |
| Reviewers | Architecture, DevOps, Backend Engineering, Database, Support, Product |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines security and access operations standards for Digitize.

It governs operational access requests, privileged access, access reviews, credential operations, audit support, and security escalation after production handover.

---

# 2. Scope

This document covers:

- Operational access requests.
- Privileged access.
- Access reviews.
- Account removal.
- Credential and secret rotation coordination.
- Audit evidence.
- Security operational alerts.
- Security escalation.

---

# 3. Out of Scope

This document does not define:

- Security architecture.
- Authentication implementation.
- Authorization model design.
- Penetration testing.
- Secret values.
- Legal incident response.

Security architecture and testing are governed by their respective documentation folders.

---

# 4. Governing Standard

This document inherits `OPS-00_Operations_Standards.md`.

Operational access shall follow least privilege and shall be auditable where practical.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| OPS-00 | Access operations, evidence, and security escalation standards |
| Technical Architecture | Security architecture and trust boundaries |
| Backend Engineering | Authentication, authorization, tenant context, logging, and audit behavior |
| Database Design | Database access, audit, retention, and sensitive data controls |
| Deployment | Secret reference and deployment access boundaries |
| Testing | Security testing and known security risks |

---

# 6. Access Request Standard

Access requests shall define:

- Requester.
- Business reason.
- Target system.
- Requested role.
- Tenant scope where applicable.
- Duration.
- Approver.
- Risk classification.
- Evidence requirement.

Access without a valid owner and approval shall not be granted.

---

# 7. Privileged Access

Privileged access shall define:

- Justification.
- Approver.
- Time limit.
- Scope.
- Required evidence.
- Session logging expectation where available.
- Revocation time.
- Review requirement.

No individual shall approve their own privileged access where separation is practical.

---

# 8. Access Review

Access reviews shall verify:

- Active users.
- Privileged users.
- Service accounts.
- Support accounts.
- Database access.
- Provider access where applicable.
- Dormant accounts.
- Role appropriateness.
- Tenant-scope appropriateness.

Access review cadence remains `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` until approved security commitments are available.

---

# 9. Credential and Secret Operations

Credential and secret operations shall coordinate:

- Rotation owner.
- Rotation window.
- Affected services.
- Overlapping validity where required.
- Provider-side activation order.
- Revocation timing.
- Rollback implications.
- Evidence.

Secret values shall not appear in operational documents, tickets, logs, screenshots, or evidence.

---

# 10. Security Escalation

Security escalation shall occur for:

- Suspected unauthorized access.
- Tenant isolation risk.
- Credential exposure.
- Sensitive data exposure.
- Suspicious authentication behavior.
- Privileged access misuse.
- Critical vulnerability.
- Audit evidence gap.

Security escalation shall protect evidence and limit sensitive detail to approved access.

---

# 11. Evidence

Security and access operations evidence shall include:

- Access request.
- Approval record.
- Privileged access record.
- Access review record.
- Revocation record.
- Credential rotation record.
- Security escalation record.
- Audit support record.

---

# 12. Acceptance Criteria

This document is acceptable when:

- Access request rules are defined.
- Privileged access is documented.
- Access review is defined.
- Credential and secret operations are covered.
- Security escalation is documented.
- Evidence requirements are defined.
- No rule contradicts `OPS-00`, Security Architecture, or Deployment governance.

---

# 12a. Authentication Rate Limiting and Trusted Proxies (P0)

Production-like deployments (`staging` / `production`) must configure:

| Setting | Requirement |
|---|---|
| `RATE_LIMIT_BACKEND` | `redis` (process-local `memory` is rejected at startup) |
| `REDIS_URL` | Private Redis endpoint (`redis://` or `rediss://` with TLS) |
| `REDIS_CONNECT_TIMEOUT_SECONDS` / `REDIS_OPERATION_TIMEOUT_SECONDS` | Bounded timeouts |
| `REDIS_MAX_CONNECTIONS` | Pool ceiling per process |
| `TRUSTED_PROXY_CIDRS` | CIDRs of load balancers / reverse proxies only |

**Redis isolation:** Do not expose Redis publicly. Bind to a private network, require AUTH (and ACL where available), prefer TLS (`rediss://`), and allow only application instances to connect.

**Outage policy:** When `RATE_LIMIT_BACKEND=redis`, authentication and recovery refuse the request with `503 SERVICE_UNAVAILABLE` if Redis is unreachable. They never silently bypass rate-limit enforcement.

**Client IP:** Only peers inside `TRUSTED_PROXY_CIDRS` may supply `X-Forwarded-For`. Untrusted peers cannot spoof client IP. Empty CIDRs (local/dev default) ignore all forwarding headers.

**Keys:** Rate-limit keys hash account identifiers (SHA-256). Raw emails, passwords, and tokens must never be stored in Redis keys or audit payloads.

---

# 13. Freeze Rule

This document shall remain `Design Draft` until `OPS-00` is reviewed and security access operations are accepted by Security and Operations.
