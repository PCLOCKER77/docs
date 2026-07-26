
# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# Release Pack: sample-release-dev-2026-07-26

> Populated from `RELEASE_PACK_TEMPLATE.md` as a development-target example.

- Release Name: sample-release-dev-2026-07-26
- Release Version: 1.0.0-dev
- Release Type: Development
- Target Environment: development
- Release Manager: dev.release@example.com
- Deployment Window: 2026-07-26 01:00-02:00 UTC
- Change Reference: CHG-2026-DEV-0001
- Emergency / Hotfix Reference: N/A

---

## Evidence Sections (fill during release execution)

### Environment Approval
- Status: [ ]
- Evidence: Dev environment onboarding ticket

### Environment Parity Gaps
- Status: [ ]
- Evidence: Parity gaps: lower scale; prod feature flags disabled

### Deployment Window Approval
- Status: [ ]
- Evidence: Dev calendar invite

### Infrastructure Availability
- Status: [ ]
- Evidence: Cluster `dev-cluster` available

### Compute Responsibilities / Ownership
- Status: [ ]
- Evidence: DevOps contact listed in ticket

### Pipeline Artifacts Produced
- Status: [ ]
- Evidence: Image: `ghcr.io/orieon/digitize-backend:1.0.0-dev` — pipeline run: https://ci.example.org/runs/dev-123

### Concurrency & Locks
- Status: [ ]
- Evidence: Dev environment lock (optional)

### Artifact Provenance Verified
- Status: [ ]
- Evidence: Commit `abcdefdev123` and digest attached

### Artifact Retention
- Status: [ ]
- Evidence: Dev retention policy applied

### Configuration Validation
- Status: [ ]
- Evidence: Config validation report link

### Secret References Available
- Status: [ ]
- Evidence: Vault path: `secret/data/digitize/development/backend` — access validated

### Secret Rotation Impact Reviewed
- Status: [ ]
- Evidence: No rotation planned

### Migrations Approved & Sequenced
- Status: [ ]
- Evidence: Migration IDs documented for dev testing

### Migration Concurrency / Backup
- Status: [ ]
- Evidence: Backup/restore test confirmed

### Backend Deployment Readiness
- Status: [ ]
- Evidence: Chart and image references ready

### Worker / Scheduler / Outbox Sequencing
- Status: [ ]
- Evidence: Workers scaled appropriately for dev

### Web Deployment & Cache Invalidation
- Status: [ ]
- Evidence: Dev CDN settings (if applicable)

### Mobile Compatibility & Rollout Strategy
- Status: [ ]
- Evidence: Not applicable

### API Compatibility Checks
- Status: [ ]
- Evidence: Contract tests passed (dev run)

### Integration Compatibility
- Status: [ ]
- Evidence: Integration test run links

### Security Checks
- Status: [ ]
- Evidence: Dev-level scans completed

### Supply-Chain Controls
- Status: [ ]
- Evidence: SBOM attached (dev)

### Feature Flag Governance
- Status: [ ]
- Evidence: Feature flags enabled in dev only

### Test Evidence
- Status: [ ]
- Evidence: Test run links

### Observability (Dashboards / Alerts)
- Status: [ ]
- Evidence: Dev dashboard link

### Diagnostics Availability
- Status: [ ]
- Evidence: Runbooks available

### Rollback / Recovery Decision
- Status: [ ]
- Evidence: Dev rollback plan

### Partial-Failure Behavior
- Status: [ ]
- Evidence: Partial failure docs

### Provider Mitigation
- Status: [ ]
- Evidence: Dev provider fallback

### Operational Handover Evidence
- Status: [ ]
- Evidence: Not required for dev

### Emergency / Hotfix Governance
- Status: [ ]
- Evidence: Not applicable

---

## Usage
- Use this pack for development promotions and testing. It is not sufficient for staging or production promotions without review and confirmation.
