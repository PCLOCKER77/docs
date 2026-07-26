# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# Release Pack Template (DEP-10 helper)

> Template and example release pack entries to populate `DEP-10` readiness checklist.


## Sample Release (Example)

- Release Name: sample-release-2026-07-26
- Release Version: 1.0.0
- Release Type: Standard
- Target Environment: staging
- Release Manager: release.manager@example.com
- Deployment Window: 2026-07-26 02:00-03:00 UTC
- Change Reference: CHG-2026-0001
- Emergency / Hotfix Reference: N/A

---

## Evidence Sections

Fill each evidence item below with links to pipeline runs, artifact URLs, runbook logs, or short text evidence. CI should update these anchors for each release.

### Environment Approval
- Status: [ ]
- Evidence: 

### Environment Parity Gaps
- Status: [ ]
- Evidence: 

### Deployment Window Approval
- Status: [ ]
- Evidence: 

### Infrastructure Availability
- Status: [ ]
- Evidence: 

### Compute Responsibilities / Ownership
- Status: [ ]
- Evidence: 

### Pipeline Artifacts Produced
- Status: [ ]
- Evidence: Artifact URLs / registry references

### Concurrency & Locks
- Status: [ ]
- Evidence: Environment lock ID or pipeline run

### Artifact Provenance Verified
- Status: [ ]
- Evidence: Build ID, commit, checksum

### Artifact Retention
- Status: [ ]
- Evidence: Artifact storage path and retention policy

### Configuration Validation
- Status: [ ]
- Evidence: Config diff or validation report

### Secret References Available
- Status: [ ]
- Evidence: Vault path(s) and access check result

### Secret Rotation Impact Reviewed
- Status: [ ]
- Evidence: Rotation plan or risk note

### Migrations Approved & Sequenced
- Status: [ ]
- Evidence: Migration IDs and sequencing plan

### Migration Concurrency / Backup
- Status: [ ]
- Evidence: Backup confirmation and lock

### Backend Deployment Readiness
- Status: [ ]
- Evidence: Artifact image, checksum, and deployment plan

### Worker / Scheduler / Outbox Sequencing
- Status: [ ]
- Evidence: Worker activation plan

### Web Deployment & Cache Invalidation
- Status: [ ]
- Evidence: CDN purge plan or cache-control headers

### Mobile Compatibility & Rollout Strategy
- Status: [ ]
- Evidence: Store submission plan and supported versions

### API Compatibility Checks
- Status: [ ]
- Evidence: Contract tests or OpenAPI validation

### Integration Compatibility
- Status: [ ]
- Evidence: Provider coordination notes

### Security Checks
- Status: [ ]
- Evidence: Vulnerability scan / security review

### Supply-Chain Controls
- Status: [ ]
- Evidence: SBOM, dependency-scan report

### Feature Flag Governance
- Status: [ ]
- Evidence: Flag owner and activation plan

### Test Evidence
- Status: [ ]
- Evidence: Test run links

### Observability (Dashboards / Alerts)
- Status: [ ]
- Evidence: Dashboard links and alert definitions

### Diagnostics Availability
- Status: [ ]
- Evidence: Diagnostic runbook links or logs

### Rollback / Recovery Decision
- Status: [ ]
- Evidence: Rollback plan or recovery decision

### Partial-Failure Behavior
- Status: [ ]
- Evidence: Partial-failure plan

### Provider Mitigation
- Status: [ ]
- Evidence: Provider fallback or reconciliation plan

### Operational Handover Evidence
- Status: [ ]
- Evidence: Handover checklist completed by Operations

### Emergency / Hotfix Governance
- Status: [ ]
- Evidence: Emergency approval and expedited pipeline run

---

## Template Usage

- Copy this file into a release-specific path (suggested: `docs/11_Deployment/release-packs/<release-name>.md`) and populate the Evidence fields with links to pipeline runs, artifact URLs, and runbook logs.
- `DEP-10` checklist items should link to the corresponding evidence anchors in the release pack.
