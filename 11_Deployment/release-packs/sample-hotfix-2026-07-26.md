
# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# Release Pack: sample-hotfix-2026-07-26

> Populated from `RELEASE_PACK_TEMPLATE.md` for an expedited hotfix example.

- Release Name: sample-hotfix-2026-07-26
- Release Version: 1.0.1-hotfix
- Release Type: Hotfix
- Target Environment: production
- Release Manager: oncall.release@example.com
- Deployment Window: 2026-07-26 ASAP (emergency)
- Change Reference: HF-2026-0001
- Emergency / Hotfix Reference: HF-2026-0001

---

## Evidence Sections (fill during release execution)

### Environment Approval
- Status: [ ]
- Evidence: Emergency change approval HF-2026-0001

### Environment Parity Gaps
- Status: [ ]
- Evidence: N/A

### Deployment Window Approval
- Status: [ ]
- Evidence: Emergency approval recorded

### Infrastructure Availability
- Status: [ ]
- Evidence: Prod cluster available for emergency deploy

### Compute Responsibilities / Ownership
- Status: [ ]
- Evidence: Oncall DevOps and Backend Eng contacts

### Pipeline Artifacts Produced
- Status: [ ]
- Evidence: Hotfix image: `ghcr.io/orieon/digitize-backend:1.0.1-hotfix` — pipeline run: https://ci.example.org/runs/hf-5678

### Concurrency & Locks
- Status: [ ]
- Evidence: Emergency lock acquired

### Artifact Provenance Verified
- Status: [ ]
- Evidence: Commit and digest attached

### Artifact Retention
- Status: [ ]
- Evidence: Retained per policy

### Configuration Validation
- Status: [ ]
- Evidence: Minimal config review for hotfix

### Secret References Available
- Status: [ ]
- Evidence: Vault access confirmed

### Secret Rotation Impact Reviewed
- Status: [ ]
- Evidence: Not applicable

### Migrations Approved & Sequenced
- Status: [ ]
- Evidence: Hotfix avoids migrations where possible; if required, emergency migration plan attached

### Migration Concurrency / Backup
- Status: [ ]
- Evidence: Backup if migration performed

### Backend Deployment Readiness
- Status: [ ]
- Evidence: Helm chart and image ready

### Worker / Scheduler / Outbox Sequencing
- Status: [ ]
- Evidence: Workers handled per hotfix plan

### Web Deployment & Cache Invalidation
- Status: [ ]
- Evidence: CDN purge plan if web assets included

### Mobile Compatibility & Rollout Strategy
- Status: [ ]
- Evidence: Hotfix for server-side only

### API Compatibility Checks
- Status: [ ]
- Evidence: Contract tests run for hotfix

### Integration Compatibility
- Status: [ ]
- Evidence: Provider quick-checks performed

### Security Checks
- Status: [ ]
- Evidence: Minimal security review for emergency (must be followed by full review)

### Supply-Chain Controls
- Status: [ ]
- Evidence: SBOM attached where possible

### Feature Flag Governance
- Status: [ ]
- Evidence: N/A

### Test Evidence
- Status: [ ]
- Evidence: Hotfix smoke tests and quick regression

### Observability (Dashboards / Alerts)
- Status: [ ]
- Evidence: Dashboard link and emergency alerting

### Diagnostics Availability
- Status: [ ]
- Evidence: Emergency diagnostic steps attached

### Rollback / Recovery Decision
- Status: [ ]
- Evidence: Rollback plan for hotfix

### Partial-Failure Behavior
- Status: [ ]
- Evidence: Hotfix partial-failure guidance

### Provider Mitigation
- Status: [ ]
- Evidence: Provider fallback if applicable

### Operational Handover Evidence
- Status: [ ]
- Evidence: Operations acceptance after hotfix

### Emergency / Hotfix Governance
- Status: [ ]
- Evidence: Emergency approval and contact list

---

## Usage
- Use this pack for emergency hotfix promotions. Attach evidence to the emergency change ticket.
