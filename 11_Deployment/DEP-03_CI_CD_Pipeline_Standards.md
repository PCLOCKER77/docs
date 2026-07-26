# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# DEP-03 CI CD Pipeline Standards

> CI/CD pipeline standards for build, validation, artifact creation, promotion, deployment, and evidence.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEP-03 |
| Document Name | CI CD Pipeline Standards |
| Folder | 11_Deployment |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | DevOps / Platform Engineering |
| Reviewers | Architecture, Backend Engineering, Frontend / Mobile Engineering, Database, Security, QA, Operations |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines CI/CD pipeline standards for Digitize deployment.

It governs how source state becomes validated, traceable, immutable artifacts that are promoted through controlled environments.

---

# 2. Scope

This document covers:

- Pipeline trigger expectations.
- Build and validation stages.
- Artifact provenance.
- Supply-chain controls.
- Approval gates.
- Environment promotion.
- Deployment concurrency.
- Production No-Go handling.
- Evidence retention.

---

# 3. Out of Scope

This document does not define:

- Specific CI/CD vendor tooling.
- Source-code implementation.
- Test strategy ownership.
- Provider-specific hosting topology.
- Production incident management.

Tool selection remains governed by approved architecture decisions.

---

# 4. Governing Standard

This document inherits `DEP-00_Deployment_Standards.md`.

It shall not redefine common supply-chain, artifact, approval, evidence, or deployment-concurrency rules already governed by `DEP-00`.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| DEP-00 | Artifact, provenance, supply-chain, gate, concurrency, and evidence standards |
| DEP-01 | Environment promotion path and readiness |
| DEP-02 | Deployment units and runtime placement |
| Backend Engineering | Backend packaging, tests, migrations, workers, health, and release readiness |
| API Collections | API contract validation and OpenAPI readiness |
| Integration Contracts | Contract, provider, outbox, webhook, and file readiness |
| Database Design | Migration validation and recovery readiness |
| Security | Access, secret scanning, artifact integrity, and exception governance |
| QA | Quality evidence and deployment verification support |

---

# 6. Pipeline Model

Digitize pipelines shall use controlled stages.

```text
Source
  ↓
Validate
  ↓
Build
  ↓
Package
  ↓
Security and Supply-Chain Checks
  ↓
Artifact Publish
  ↓
Environment Promotion
  ↓
Deployment
  ↓
Post-Deployment Verification
  ↓
Evidence Capture
```

Stages may be split by component, but production promotion shall preserve artifact provenance and gate evidence.

---

# 7. Trigger Standard

Pipeline triggers shall define:

- Source branch or release reference.
- Manual or automated trigger.
- Required approvals.
- Target environment.
- Target deployment units.
- Release identifier.
- Artifact versioning rule.
- Superseded-release behavior.

Production deployment triggers shall require explicit approval.

---

# 8. Build and Validation Standard

Pipelines shall execute applicable validation before artifact promotion.

Expected validation includes:

- Source validation.
- Dependency lock verification.
- Static analysis where applicable.
- Unit tests where applicable.
- API contract checks where applicable.
- Integration contract checks where applicable.
- Migration checks where applicable.
- Security checks where applicable.
- Artifact digest generation where supported.
- Build provenance capture.

Mandatory validation failures shall block promotion unless an approved exception exists.

---

# 9. Artifact Publication

Artifacts published by the pipeline shall include:

- Artifact name.
- Artifact type.
- Version.
- Source repository.
- Source revision or commit.
- Build pipeline run.
- Dependency lock reference where applicable.
- Build toolchain version where applicable.
- Checksum or digest.
- SBOM reference where required.
- Signature reference where signing is enabled.

Artifacts whose provenance cannot be verified shall not be promoted to production.

---

# 10. Supply-Chain Controls

Pipeline supply-chain controls shall support approved security architecture.

Controls may include:

- Dependency lock verification.
- Vulnerability scanning.
- License-policy checks.
- Secret scanning.
- Artifact digest verification.
- Container-image scanning.
- SBOM generation.
- Artifact signing.
- Signature verification.
- Build provenance capture.

GitHub Actions is the approved CI/CD orchestration baseline per `DR-012_GitHub_Actions_CI_CD_Baseline.md`.

---

# 11. Artifact Retention

Pipeline artifact retention shall define:

- Which artifacts are retained.
- Minimum retained production versions.
- Retention duration.
- Artifact storage owner.
- Integrity-verification expectation.
- Access controls.
- Removal approval.
- Availability for rollback, investigation, and recovery.

Artifacts required for an approved rollback, audit, or investigation window shall not be deleted.

Pipeline artifacts shall be retained for at least 90 days for non-production validation and at least 1 year for production release evidence unless Release Management, Security, or compliance policy requires a longer period.

---

# 12. Environment Promotion

Promotion shall use the same immutable artifact validated in the preceding controlled environment wherever technically possible.

Promotion shall not:

- Recompile from a different source revision.
- Resolve unpinned dependencies again.
- Modify artifact contents.
- Inject environment-specific files into the artifact.
- Replace application binaries manually.
- Bypass approved gates.

Environment differences shall be supplied through approved runtime configuration and secret references.

---

# 13. Deployment Concurrency

Pipeline controls shall prevent conflicting deployments.

Controls shall address:

- Environment locking.
- Concurrent production deployments.
- Concurrent database migrations.
- Multiple pipeline runs for the same release.
- Overlapping rollback and deployment activity.
- Stale approval detection.
- Superseded release cancellation.

Only one approved migration sequence shall modify a target database at a time unless parallel execution has been explicitly designed and validated.

---

# 14. Approval Gates

Production pipelines shall include required gates for:

- Build validation.
- Security validation.
- Migration readiness.
- Contract compatibility.
- Configuration readiness.
- Environment readiness.
- Deployment approval.
- Post-deployment verification.
- Operational handover.
- Go / No-Go decision.

Gate decisions shall be captured as deployment evidence.

---

# 15. Production No-Go Conditions

Pipeline execution shall produce a production No-Go when mandatory controls fail.

No-Go conditions include:

- Unresolved critical security failure.
- Missing artifact provenance.
- Failed mandatory supply-chain control.
- Failed tenant-isolation verification.
- Unreviewed destructive migration.
- Missing production configuration or secret reference.
- Missing rollback, roll-forward, or recovery decision.
- Failed required health, readiness, or smoke validation.
- Unapproved production access.
- Stale approval after source, artifact, migration, or configuration changes.

No-Go exceptions shall follow `DEP-00` and shall not bypass critical security, tenant-isolation, data-integrity, or secret-protection controls.

---

# 16. Emergency and Hotfix Pipeline Path

Emergency and hotfix pipelines may use an expedited process when approved.

The expedited process shall still require:

- Incident or urgent-change reference.
- Defined release scope.
- Risk assessment.
- Minimal mandatory validation.
- Artifact traceability.
- Authorized approval.
- Deployment evidence.
- Post-deployment verification.
- Retrospective review.
- Normalization into the standard release path.

Emergency status shall not bypass tenant-isolation, data-integrity, secret-protection, or critical security controls.

---

# 17. Evidence

Pipeline evidence shall include:

- Pipeline run identifier.
- Source reference.
- Artifact identifiers.
- Validation results.
- Supply-chain results.
- Approval records.
- Environment promotion record.
- Deployment execution result.
- Post-deployment verification result.
- Exception references where applicable.

Evidence shall be retained according to `DEP-00`.

---

# 18. Acceptance Criteria

This document is acceptable when:

- Pipeline stages are defined.
- Trigger and approval expectations are documented.
- Artifact publication and provenance rules are documented.
- Artifact retention expectations are documented.
- Supply-chain controls are defined without mandating a tool.
- Environment promotion rules preserve immutable artifacts.
- Deployment concurrency rules are documented.
- Production No-Go conditions are documented.
- Emergency and hotfix expectations are defined.
- Evidence requirements are documented.
- No pipeline rule contradicts `DEP-00`.

---

# 19. Freeze Rule

This document shall remain `Design Draft` until `DEP-00` is frozen and GitHub Actions workflow gates, artifact retention, environment protections, and release evidence requirements are reviewed.
