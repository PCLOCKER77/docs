
# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# Release Pack: sample-release-2026-07-26-production

> Populated from `RELEASE_PACK_TEMPLATE.md` as a production-target example.

- Release Name: sample-release-2026-07-26
- Release Version: 1.0.0
- Release Type: Production
- Target Environment: production
- Release Manager: release.manager@example.com
- Deployment Window: 2026-07-26 03:00-04:00 UTC
- Change Reference: CHG-2026-0001-PROD
- Emergency / Hotfix Reference: N/A

---

## Evidence Sections (fill during release execution)

### Environment Approval
- Status: [ ]
- Evidence: Change ticket CHG-2026-0001-PROD, CAB approval

### Environment Parity Gaps
- Status: [ ]
- Evidence: None for production; documented constraints attached

### Deployment Window Approval
- Status: [ ]
- Evidence: Change window approval, communication to business

### Infrastructure Availability
- Status: [ ]
- Evidence: Cluster `prod-cluster` available; node-pool health OK

### Compute Responsibilities / Ownership
- Status: [ ]
- Evidence: DevOps and Ops owners specified in change ticket

### Pipeline Artifacts Produced
- Status: [ ]
- Evidence: Image: `ghcr.io/orieon/digitize-backend:1.0.0` — pipeline run: https://ci.example.org/runs/12345

### Concurrency & Locks
- Status: [ ]
- Evidence: Prod environment lock: lock-id-20260726-prod

### Artifact Provenance Verified
- Status: [ ]
- Evidence: Commit: `abcdef123456`, digest: `sha256:...` (see pipeline run)

### Artifact Retention
- Status: [ ]
- Evidence: Registry retention policy retained artifacts >=1 year

### Configuration Validation
- Status: [ ]
- Evidence: Config validation report attached

### Secret References Available
- Status: [ ]
- Evidence: Vault path: `secret/data/digitize/production/backend` — access validated

### Secret Rotation Impact Reviewed
- Status: [ ]
- Evidence: No rotation during deployment window

### Migrations Approved & Sequenced
- Status: [ ]
- Evidence: Migration IDs and sequence confirmed; backups taken

### Migration Concurrency / Backup
- Status: [ ]
- Evidence: Backup: backup-2026-07-26-prod-01; migration lock acquired

### Backend Deployment Readiness
- Status: [ ]
- Evidence: Helm chart and image references ready

### Worker / Scheduler / Outbox Sequencing
- Status: [ ]
- Evidence: Workers scaled down during migration; activation plan attached

### Web Deployment & Cache Invalidation
- Status: [ ]
- Evidence: CDN purge plan and cache-busting methodology

### Mobile Compatibility & Rollout Strategy
- Status: [ ]
- Evidence: Mobile compatibility window documented (if in scope)

### API Compatibility Checks
- Status: [ ]
- Evidence: Contract tests passed

### Integration Compatibility
- Status: [ ]
- Evidence: Provider coordination and test confirmations

### Security Checks
- Status: [ ]
- Evidence: SAST/DAST and dependency scans attached

### Supply-Chain Controls
- Status: [ ]
- Evidence: SBOM and vulnerability scan links

### Feature Flag Governance
- Status: [ ]
- Evidence: Feature flag owners and default states documented

### Test Evidence
- Status: [ ]
- Evidence: Test run artifacts and summaries

### Observability (Dashboards / Alerts)
- Status: [ ]
- Evidence: Production dashboards and alerting links

### Diagnostics Availability
- Status: [ ]
- Evidence: Diagnostic runbook links

### Rollback / Recovery Decision
- Status: [ ]
- Evidence: Rollback plan and responsible owners

### Partial-Failure Behavior
- Status: [ ]
- Evidence: Partial-failure mitigation plan

### Provider Mitigation
- Status: [ ]
- Evidence: Provider fallback and reconciliation plan

### Operational Handover Evidence
- Status: [ ]
- Evidence: Operations acceptance and handover confirmation

### Emergency / Hotfix Governance
- Status: [ ]
- Evidence: Hotfix process and emergency contacts

---

## Usage
- Copy this pack to `docs/11_Deployment/release-packs/<release-name>-production.md` for production promotions and populate evidence during deployment.
