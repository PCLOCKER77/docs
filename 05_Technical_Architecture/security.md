# Security Integration Notes

This document provides concise integration-level security guidance for Digitize and complements the Product Foundation security checklist ([PF-06_Security_Compliance_Checklist.md](../01_Product_Foundation/PF-06_Security_Compliance_Checklist.md)). It is intended for architects, integration engineers, DevOps, and security reviewers preparing interfaces, provider integrations, and operational controls required for Design Freeze.

## Purpose

Provide required security controls, verification steps, and integration checklist items for external providers, identity choices, secret management, telemetry, and auditability to ensure platform readiness for production.

## Scope

Covers integration-level security concerns: authentication and authorization patterns, provider callback verification, transport and data protection, secrets handling, telemetry and audit requirements, and provider onboarding checks. This document does not replace the full compliance checklist in PF-06; it highlights integration specifics that must be validated during design and implementation.

## Authentication and Identity

- Preferred pattern: adopt an external Identity Provider (IdP) for user-facing authentication where feasible (OpenID Connect / OAuth2) and use short-lived service-to-service tokens for internal communication.
- For internal service identities use mTLS or token-based service principals with limited scopes.
- Document the chosen IdP, token formats, claim mappings, session lifetime, and refresh behavior as part of TA-05 review (see TA-05_Security_Identity_Architecture.md).

## Authorization

- Apply centralized authorization checks via a shared authorization service or library that enforces RBAC and tenant-scope before domain execution (see ADR-020, ADR-021).
- Ensure admin and privileged actions are audited and require elevated approval workflows.

## Provider Callbacks and Webhooks

- Verify provider callbacks using one or more of: HMAC signatures, mutual TLS, or provider-supplied verification tokens. Never trust unauthenticated callbacks.
- Implement idempotency and replay protection for external callbacks; log and audit all callback processing results.

## Transport and Data Protection

- Enforce TLS 1.2+ for all external and internal endpoints; disable weak ciphers.
- Encrypt sensitive configuration and secrets at rest using environment-supported key management (KMS) and enable encryption-in-transit for persistence where supported.

## Secrets and Key Management

- Externalize all secrets from code and configuration repositories. Use a dedicated secrets manager (vault, cloud KMS) and rotate keys per policy.
- Limit secret scope and provide least-privilege service identities for provider integrations.

## Sensitive Data Handling (PCI / PII)

- Avoid direct storage or processing of raw payment card data; prefer PCI-compliant gateways and tokenization (see ADR-010 / ADR-030).
- Classify personal data per PF-06; apply masking and retention controls in data flows. Ensure logging avoids persisting sensitive payloads.

## Telemetry, Audit, and Logging

- Capture audit events for privileged configuration changes, provider onboarding actions, maintenance mode toggles, and security-relevant events (see TA-07 and TA-10 audit specifications).
- Mask sensitive fields in logs and traces. Correlate audit events with request and correlation IDs for end-to-end investigation.

## Provider Onboarding Checklist

For each external provider (payment gateway, SMS, email, WhatsApp, marketplace) require:

- Security contact and designated support SLA.
- Callback verification method and example signed payloads.
- Data residency and retention terms.
- Required scopes, credentials, and secret rotation process.
- Test vectors for failure and retry behavior.
- Confirmation of encryption and transport security.

## Deployment and Operational Controls

- Validate runtime secrets access by environment (dev / staging / prod) with strict separation.
- Require security review sign-off for any provider that will handle PCI/PII data before enabling in production.

## Traceability and References

- Trace all security-relevant decisions to TA-10 ADRs and the Product Foundation checklist: [PF-06_Security_Compliance_Checklist.md](../01_Product_Foundation/PF-06_Security_Compliance_Checklist.md).
- Link to `TA-05_Security_Identity_Architecture.md` for identity decisions and `TA-07_Observability_Operations_Architecture.md` for telemetry/audit mappings.

## Remaining Decisions (Require Human Approval)

- Choice of external IdP vs internal authn service (TA-05-QST-001).
- MFA policy for platform administrators (TA-05-QST-002).
- Final selection of secrets manager / KMS provider (TA-06-QST-001).

### KMS / Secrets Manager Proposed Options (proposal — requires approval)

Owner: DevOps / Security

- Option A (Recommended): Use cloud-provider KMS and managed secrets (AWS KMS + AWS Secrets Manager, or equivalent in GCP/Azure). Rationale: deep cloud integration, IAM-backed access, simplified rotation APIs, audit logs. Impact: ties secrets lifecycle to cloud provider; rollback: implement vault abstraction layer and provider-agnostic secret access library.
- Option B (Recommended for multi-cloud or on-prem flexibility): HashiCorp Vault (self-managed or managed HCP). Rationale: central control, hardware-backed keys, multi-cloud support, dynamic secrets. Impact: operational overhead and provisioning; rollback: fallback to encrypted parameter store and rotate keys.
- Option C (Alternative): Use cloud KMS for key management and a lightweight secrets store for application-level secrets (e.g., SOPS + GitOps for configuration) for reduced operational complexity in initial release.

Acceptance: KMS choice must support key rotation, audit logging, environment separation, and least-privilege access models. Approval should be recorded and traced to TA-06 and security ADRs.

### KMS decision — Approval applied (ADR-046)

- Decision: Use AWS KMS and AWS Secrets Manager for key management and secrets storage in the initial release. Rationale: aligns with chosen AWS infrastructure, simplifies rotation and audit, and integrates with IAM for least-privilege access. Implementation: secrets access library should abstract provider calls to allow future migration; enforce rotation and audit logging.

## Acceptance Criteria (for Freeze)

1. All provider integrations have documented callback verification and onboarding checklist completed.
2. Authentication and authorization model is documented and linked to TA-05 with a chosen IdP or internal design.
3. Secrets management approach is documented with rotation and environment separation.
4. Audit events and telemetry required for security investigations are mapped to TA-07 and TA-10.

---

Last updated: July 2026
