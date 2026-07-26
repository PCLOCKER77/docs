# <!--
# FROZEN: FREEZE-2026-07-26-sample-release
# Freeze date (UTC): 2026-07-26
# Freeze owner: release-manager@example.com
# Do not edit without an unfreeze PR referencing this freeze ID.
# -->

# DEP-06 Backend Deployment Runbook

> Controlled backend deployment procedure for Digitize API, workers, schedulers, outbox processors, and deployment handover.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEP-06 |
| Document Name | Backend Deployment Runbook |
| Folder | 11_Deployment |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Backend Engineering / DevOps |
| Reviewers | Architecture, Database Engineering, Security, QA, Operations |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the controlled backend deployment procedure for Digitize.

It covers artifact verification, migration coordination, process startup, worker and outbox-processor activation, health and readiness verification, smoke testing, rollback initiation, observation, and deployment handover.

---

# 2. Scope

This document covers deployment of:

- Backend API runtime.
- Background workers.
- Scheduled jobs.
- Outbox processors.
- Webhook processors.
- Reconciliation jobs.
- Report workers.
- Backend runtime configuration.
- Backend health, readiness, and smoke verification.

---

# 3. Out of Scope

This document does not define:

- Backend business logic.
- FastAPI source structure.
- API endpoint contracts.
- Database schema definitions.
- Infrastructure topology.
- Long-term production operations.
- Incident-management procedures.

Continuous backend operation after handover is owned by Operations.

---

# 4. Governing Standard

This document inherits `DEP-00_Deployment_Standards.md`.

`DEP-06` ends when deployment verification, post-deployment observation, and operational handover are completed.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| DEP-00 | Backend deployment, worker sequencing, evidence, observation, rollback, and handover standards |
| DEP-01 | Target environment readiness |
| DEP-02 | Backend runtime placement |
| DEP-03 | Pipeline artifact and deployment execution |
| DEP-04 | Backend configuration and secret references |
| DEP-05 | Migration sequencing and verification |
| Backend Engineering | Backend implementation, health, worker, outbox, testing, and release readiness |
| API Collections | Approved API behavior and smoke expectations |
| Integration Contracts | Outbox, provider, webhook, retry, event, and file behavior |
| Operations | Handover acceptance and production monitoring readiness |

---

# 6. Required Inputs

Backend deployment shall not begin until required inputs are available.

| Input | Requirement |
|---|---|
| Release Identifier | Required |
| Backend Artifact Reference | Required |
| Source Revision | Required |
| Build Pipeline Run | Required |
| Artifact Digest or Checksum | Required where supported |
| Configuration Set | Required |
| Secret References | Required |
| Migration Plan | Required where applicable |
| Worker Activation Plan | Required |
| Smoke-Test Plan | Required |
| Rollback or Recovery Decision | Required |
| Observation Window | Required for production |
| Handover Owner | Required for production |

---

# 7. Pre-Deployment Checks

Before backend deployment:

- Confirm environment readiness.
- Confirm artifact provenance.
- Confirm artifact version and digest.
- Confirm required configuration exists.
- Confirm required secret references resolve.
- Confirm database connectivity.
- Confirm migration readiness.
- Confirm API and integration compatibility.
- Confirm worker, scheduler, and outbox sequencing.
- Confirm deployment window and approvals.
- Confirm rollback, roll-forward, or recovery decision.
- Confirm observability readiness.

Failure of a mandatory check shall block deployment.

---

# 8. Deployment Procedure

The standard backend deployment sequence is:

```text
Verify artifact
  ↓
Validate configuration and secrets
  ↓
Prepare database migration path
  ↓
Pause or gate incompatible workers where required
  ↓
Deploy backend API runtime
  ↓
Run or verify migrations as sequenced
  ↓
Verify API health and readiness
  ↓
Activate compatible workers and schedulers
  ↓
Activate outbox and webhook processors
  ↓
Run smoke checks
  ↓
Observe production signals
  ↓
Complete handover
```

The sequence may vary only when approved compatibility and rollback controls exist.

---

# 9. Runtime Process Sequencing

Backend deployment procedures shall define sequencing for:

- API processes.
- Background workers.
- Scheduled jobs.
- Outbox processors.
- Webhook processors.
- Reconciliation jobs.
- Report workers.

Workers that require the new schema or event contract shall not start before compatible migrations and application dependencies are verified.

Old and new workers shall not process incompatible payload versions concurrently unless compatibility is explicitly supported.

---

# 10. Health and Readiness

Backend deployment shall verify:

- API health endpoint availability.
- Readiness endpoint availability.
- Database connectivity.
- Required provider configuration availability where applicable.
- Worker dependency availability.
- Queue or outbox dependency availability.
- Required secret reference availability.
- Logging availability.
- Metrics availability.
- Trace propagation where enabled.

Readiness failure shall block production handover.

---

# 11. Smoke Checks

Smoke checks shall validate the release-critical backend path.

Smoke checks may include:

- Authentication.
- Tenant context resolution.
- Approved API endpoint sample.
- Database read and write where safe.
- Migration compatibility.
- Worker dispatch where safe.
- Outbox record creation where applicable.
- Provider adapter reachability where applicable.
- Error response shape where applicable.

Smoke checks shall avoid unsafe production data changes unless explicitly approved.

---

# 12. Post-Deployment Observation

Production backend deployment shall define an observation period appropriate to release risk.

During observation, the release team shall review:

- Health and readiness.
- Error rates.
- Latency.
- Database performance.
- Worker failures.
- Outbox backlog.
- Provider failures.
- Authentication failures.
- Tenant-context errors.
- Payment or billing failures where affected.
- Business-critical smoke checks.

The release shall not be considered fully handed over until required observation checks are accepted.

---

# 13. Rollback Initiation

Rollback, roll-forward, or mitigation shall be initiated when:

- Required health checks fail.
- Readiness remains failed beyond approved threshold.
- Smoke checks fail.
- Tenant-isolation verification fails.
- Critical security issue is detected.
- Migration incompatibility is detected.
- Worker or outbox failures create unacceptable risk.
- Provider failures create unacceptable release impact.
- Error rate or latency exceeds approved threshold.

Rollback shall follow `DEP-09`.

---

# 14. Partial Backend Deployment Failure

Backend deployment procedures shall define behavior for partial backend failure.

The procedure shall identify:

- Whether API runtime deployment completed.
- Whether migrations completed and were verified.
- Whether workers started.
- Whether schedulers started.
- Whether outbox processors started.
- Whether webhook processors started.
- Whether the release remains API compatible.
- Whether workers or processors must remain disabled.
- Whether traffic should remain on the prior runtime.
- Whether rollback, roll-forward, or mitigation is required.
- Required verification before resuming deployment.

Partial backend deployment failure shall not be handed over as normal operation until risk is accepted and recovery state is documented.

---

# 15. Evidence

Backend deployment evidence shall include:

- Release identifier.
- Backend artifact reference.
- Source revision.
- Pipeline run.
- Configuration set.
- Secret reference validation result.
- Migration verification result.
- Process startup result.
- Worker and scheduler activation result.
- Health and readiness result.
- Smoke-test result.
- Observation result.
- Rollback or mitigation decision.
- Handover confirmation.

---

# 16. Handover

Backend handover to Operations requires:

- Deployment completed.
- Required migrations verified.
- API runtime ready.
- Workers and processors in intended state.
- Smoke checks accepted.
- Observation window accepted.
- Required dashboards and alerts available.
- Known residual risks documented.
- Evidence retained.

Operations owns continuous backend operation after handover is accepted.

---

# 17. Acceptance Criteria

This document is acceptable when:

- Backend deployment inputs are defined.
- Pre-deployment checks are documented.
- Deployment sequence is defined.
- Runtime process sequencing is documented.
- Health, readiness, and smoke checks are defined.
- Observation and rollback initiation are documented.
- Partial backend deployment failure handling is documented.
- Handover criteria are clear.
- No rule contradicts Backend Engineering, Database Design, Integration Contracts, or `DEP-00`.

---

# 18. Freeze Rule

This document shall remain `Design Draft` until `DEP-00`, Backend Engineering release readiness, and database migration deployment standards are reviewed together.

---

# 19. Runbook Template (Executable)

This section provides a runnable deployment runbook template aligned to the repository's CI/CD baseline (GitHub Actions per `DR-012`) and Vault-based secrets (per `DR-011`). Replace angle-bracket placeholders before execution.

Variables (replace):

- `<RELEASE_ID>`: release identifier (e.g., sample-release-2026-07-26)
Variables (sample values used in this example):

- `RELEASE_ID`: sample-release-2026-07-26
- `IMAGE`: ghcr.io/orieon/digitize-backend:1.0.0
- `NAMESPACE`: digitize-staging
- `K8S_CONTEXT`: staging-cluster
- `VAULT_PATH`: secret/data/digitize/staging/backend
- `HELM_RELEASE`: digitize-backend
- `MIGRATION_JOB`: db-migrate-sample-release-2026-07-26
- `HEALTH_ENDPOINT`: https://api.staging.orieon.dev/health
- `SMOKE_ENDPOINT`: https://api.staging.orieon.dev/api/v1/health/smoke
- `EXPECTED_REPLICAS`: 3
- `IMAGE_REPOSITORY`: ghcr.io/orieon/digitize-backend
- `IMAGE_TAG`: 1.0.0

Prerequisites:

- `kubectl` configured for the target cluster and context (`<K8S_CONTEXT>`).
- `helm` available if Helm charts are used for deployment.
- `vault` CLI authenticated with an account that has read access to `<VAULT_PATH>`.
- CI artifacts available in container registry (image `<IMAGE>`).
- Migration scripts packaged as a Kubernetes Job or a container-based runner.

High-level Steps (runnable):

1) Verify artifact provenance

```bash
# Verify image exists and print digest
docker pull "<IMAGE>" || exit 1
docker inspect --format='{{index .RepoDigests 0}}' "<IMAGE>" || true
echo "Image verified: <IMAGE>"
```

Expected result: `docker pull` succeeds and digest matches pipeline-recorded checksum.

2) Verify required secrets (Vault)

```bash
# Example: validate Vault keys resolve
vault kv get -format=json "<VAULT_PATH>" >/tmp/vault-secrets.json || { echo "Vault read failed"; exit 1; }
jq . /tmp/vault-secrets.json || true
echo "Secrets resolved from <VAULT_PATH>"
```

Expected result: Vault returns JSON of the required keys; no secret values are printed in logs in production (use CI to redact if needed).

3) Lock environment / Acquire deployment guard (CI-driven)

Use pipeline or coordination mechanism to set an environment lock. Example GitHub Actions approach: use a manual approval job or create a small lock file in an approved storage location. Implementation detail varies by org.

4) Prepare migration path

If migrations are required, create and run a Kubernetes Job that executes migrations. Example using kubectl and a migration image:

```bash
kubectl --context="<K8S_CONTEXT>" -n "<NAMESPACE>" create job "<MIGRATION_JOB>" --image="<IMAGE>" -- /bin/sh -c "./scripts/run_migrations.sh --release <RELEASE_ID>"
kubectl --context="<K8S_CONTEXT>" -n "<NAMESPACE>" wait --for=condition=complete job/"<MIGRATION_JOB>" --timeout=60m || { echo "Migration job failed or timed out"; kubectl logs job/"<MIGRATION_JOB>" -n "<NAMESPACE>"; exit 1; }
echo "Migrations completed"
```

Expected result: Job completes successfully; verification queries (see verification step) confirm schema changes.

5) Pause or gate incompatible workers

docker pull "ghcr.io/orieon/digitize-backend:1.0.0" || exit 1
docker inspect --format='{{index .RepoDigests 0}}' "ghcr.io/orieon/digitize-backend:1.0.0" || true
echo "Image verified: ghcr.io/orieon/digitize-backend:1.0.0"
# Example: scale worker deployment to 0
kubectl --context="<K8S_CONTEXT>" -n "<NAMESPACE>" scale deployment worker --replicas=0
```

jq . /tmp/vault-secrets.json || true
echo "Secrets resolved from secret/data/digitize/staging/backend"

6) Deploy API runtime (Helm example)

```bash
jq . /tmp/vault-secrets.json || true
echo "Secrets resolved from secret/data/digitize/staging/backend"
  --namespace "<NAMESPACE>" --set image.repository="<IMAGE%before_colon%>" --set image.tag="<IMAGE_TAG>" --wait --timeout 10m
# Alternate kubectl apply approach for K8s manifests
```

Notes: Replace `<IMAGE%before_colon%>` and `<IMAGE_TAG>` appropriately if image string must be split.

Expected result: Helm completes, new pods reach `READY` and `STATUS=Running`.

7) Verify API health and readiness

```bash
# Wait for pods
kubectl --context="<K8S_CONTEXT>" -n "<NAMESPACE>" rollout status deployment/<HELM_RELEASE> --timeout=5m
# Verify health endpoint
curl -f -sS "<HEALTH_ENDPOINT>" || { echo "Health check failed"; kubectl get pods -n "<NAMESPACE>"; kubectl logs -l app=<HELM_RELEASE> -n "<NAMESPACE>" --tail=200; exit 1; }
echo "Health check OK"
```

Expected result: Health endpoint returns 200 and readiness probes pass.

8) Activate workers and outbox processors

```bash
# Scale workers back up
kubectl --context="<K8S_CONTEXT>" -n "<NAMESPACE>" scale deployment worker --replicas=<EXPECTED_REPLICAS>
# Confirm they are ready
kubectl get pods -n "<NAMESPACE>" -l app=worker
```

Expected result: Worker pods are running and liveness/readiness checks pass.

9) Run smoke tests

```bash
# Minimal smoke test
curl -f -sS "<SMOKE_ENDPOINT>" || { echo "Smoke test failed"; exit 1; }
echo "Smoke test passed"
```

Expected result: Smoke endpoint returns expected content (200, expected JSON fields). Record result in evidence package.

10) Observe production signals during observation window

- Monitor logs, metrics, and alerts for the configured observation period.
- Example quick checks:

```bash
# Check error rate via metrics (example using prometheus query API)
curl -sS 'http://prometheus.example/api/v1/query?query=rate(http_requests_total{job="api",status=~"5.."}[5m])'
# Tail recent logs
kubectl logs -l app=<HELM_RELEASE> -n "<NAMESPACE>" --since=10m --tail=200
```

Expected result: No rising error signals; error rates acceptable and within thresholds.

11) Complete handover

- Capture evidence: artifact digests, pipeline run IDs, migration job logs, smoke test output, health-check result, Vault access check, and observation notes.
- Populate release pack (see `docs/11_Deployment/RELEASE_PACK_TEMPLATE.md`) and mark DEP-10 checklist items as complete.

12) Rollback (if required)

- If rollback is selected, follow `DEP-09` strategy: typically re-promote previous artifact image and restore prior configuration. Example rollback (Helm):

```bash
helm rollback "<HELM_RELEASE>" <REVISION>
kubectl rollout status deployment/<HELM_RELEASE> -n "<NAMESPACE>"
```

Capture rollback evidence and follow with observation.

Runbook notes and safety:

- Do not print secret values in logs. Where a command must show a secret-derived value, mask it or use CI-secret injection.
- Keep migration backups and restore points accessible before running destructive steps.
- Ensure independent approvals for migration and security-sensitive changes per `DEP-00`.
- Retain all runbook logs in the evidence package and reference them in `DEP-10` release pack.

Example quick checklist (to execute manually or via CI):

1. Verify artifact provenance
2. Verify Vault secrets
3. Acquire environment lock
4. Run migrations (if required)
5. Deploy application
6. Wait for readiness and health checks
7. Activate workers
8. Run smoke tests
9. Observe and capture evidence
10. Handover to Operations
helm rollback "digitize-backend" <REVISION>
kubectl rollout status deployment/digitize-backend -n "digitize-staging"

