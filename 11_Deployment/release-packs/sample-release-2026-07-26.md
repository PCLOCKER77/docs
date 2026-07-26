
# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# Release Pack: sample-release-2026-07-26

> Populated from `RELEASE_PACK_TEMPLATE.md` as a Phase 1 example.

- Release Name: sample-release-2026-07-26
- Release Version: 1.0.0
- Release Type: Standard
- Target Environment: staging
- Release Manager: release.manager@example.com
- Deployment Window: 2026-07-26 02:00-03:00 UTC
- Change Reference: CHG-2026-0001
- Emergency / Hotfix Reference: N/A

---

## Evidence Sections (fill during release execution)

### Environment Approval
- Status: [ ]
- Evidence: Approval ticket / change request CHG-2026-0001

### Environment Parity Gaps
- Status: [ ]
- Evidence: Documented gaps: none for staging

### Deployment Window Approval
- Status: [ ]
- Evidence: Calendar invite and approved change window (CHG-2026-0001)

### Infrastructure Availability
- Status: [ ]
- Evidence: Cluster `staging-cluster` available; node pool healthy

### Compute Responsibilities / Ownership
- Status: [ ]
- Evidence: DevOps oncall and Backend Eng owners listed in change ticket

### Pipeline Artifacts Produced
- Status: [ ]
- Evidence: Image: `ghcr.io/orieon/digitize-backend:1.0.0` — pipeline run: https://ci.example.org/runs/12345

### Concurrency & Locks
- Status: [ ]
- Evidence: Environment lock created: lock-id-20260726-01

### Artifact Provenance Verified
- Status: [ ]
- Evidence: Commit: `abcdef123456`, digest: `sha256:...` (see pipeline run)

### Artifact Retention
- Status: [ ]
- Evidence: Registry retention policy confirmed; artifacts retained 1 year

### Configuration Validation
- Status: [ ]
- Evidence: Config schema validation report: https://ci.example.org/artifacts/config-validate/123

### Secret References Available
- Status: [ ]
- Evidence: Vault path: `secret/data/digitize/staging/backend` — access validated

### Secret Rotation Impact Reviewed
- Status: [ ]
- Evidence: No rotation planned during this window

### Migrations Approved & Sequenced
- Status: [ ]
- Evidence: Migration IDs: 20260726_001 (add column), 20260726_002 (index) — sequencing in ticket

### Migration Concurrency / Backup
- Status: [ ]
- Evidence: Backup taken: backup-2026-07-26-01; migration job lock-id-20260726-mig

### Backend Deployment Readiness
- Status: [ ]
- Evidence: Helm chart `charts/backend`, image `ghcr.io/orieon/digitize-backend:1.0.0`

### Worker / Scheduler / Outbox Sequencing
- Status: [ ]
- Evidence: Workers will be scaled to 0 during migration; activation plan attached

### Web Deployment & Cache Invalidation
- Status: [ ]
- Evidence: CDN purge job scheduled; cache-control version increment

### Mobile Compatibility & Rollout Strategy
- Status: [ ]
- Evidence: Mobile not in scope for this release

### API Compatibility Checks
- Status: [ ]
- Evidence: Contract tests passed in pipeline run 12345

### Integration Compatibility
- Status: [ ]
- Evidence: Provider coordination emails attached

### Security Checks
- Status: [ ]
- Evidence: SAST and dependency scans: https://ci.example.org/scans/12345

### Supply-Chain Controls
- Status: [ ]
- Evidence: SBOM and dependency-scan report attached

### Feature Flag Governance
- Status: [ ]
- Evidence: No new feature flags in this release

### Test Evidence
- Status: [ ]
- Evidence: Test run summary: https://ci.example.org/tests/12345

### Observability (Dashboards / Alerts)
- Status: [ ]
- Evidence: Dashboard: https://grafana.example.org/d/abcd/release-overview

### Diagnostics Availability
- Status: [ ]
- Evidence: Runbook and diagnostic scripts available: docs/runbooks/diagnostics.md

### Rollback / Recovery Decision
- Status: [ ]
- Evidence: Rollback plan in change ticket CHG-2026-0001

### Partial-Failure Behavior
- Status: [ ]
- Evidence: Partial-failure procedure attached

### Provider Mitigation
- Status: [ ]
- Evidence: Provider fallback documented

### Operational Handover Evidence
- Status: [ ]
- Evidence: Operations acceptance email placeholder

### Emergency / Hotfix Governance
- Status: [ ]
- Evidence: Not applicable

---

## Usage
- Use this file as the canonical evidence pack for `sample-release-2026-07-26`.
- Link DEP-10 checklist items to the appropriate evidence rows above.
