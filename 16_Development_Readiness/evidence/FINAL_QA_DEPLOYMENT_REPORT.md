# Final QA deployment report

**Date:** 2026-11-09  
**Verdict (updated 2026-11-09):** **DEPLOYED via GitHub Actions** — see [QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md](./QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md). Manual Mac ECR push path superseded.

---

## 1. AWS identity

`aws sts get-caller-identity` — **succeeded** (credentials available). No infrastructure mutation performed without explicit apply authorization.

---

## 2. Terraform QA (`digitize-infrastructure/environments/qa`)

```bash
cd digitize-infrastructure/environments/qa
terraform init -backend=false   # local validate path
terraform validate              # Success
terraform plan -input=false
```

**Plan summary (after IAM `count` fix):** **7 add, 1 change, 1 destroy** (replace).

| Resource | Action | Notes |
|----------|--------|-------|
| `module.organization_dek_kms.aws_kms_key` | create | New CMK for org DEK envelope |
| `module.blind_index_secret` | create | Secrets Manager blind-index master |
| `module.iam` ECS task role + KMS/SM policies | create | Crypto access for ECS tasks |
| `module.ecs_task.aws_ecs_task_definition.backend` | **replace** | Task definition revision change |
| `module.ecs_service.aws_ecs_service.backend` | update in-place | Points to new task definition |

**Risk review:** One **destroy/recreate** on ECS task definition (expected for env/crypto IAM wiring). **No** public RDS exposure identified in plan snippet. **KMS + SM** add monthly cost — low but non-zero.

**Code change:** `modules/iam/main.tf` lines 88, 111 — remove ARN emptiness from `count` (fixes “Invalid count argument” when ARNs are `(known after apply)`).

---

## 3. Deployment pipeline (not executed)

| Step | Status |
|------|--------|
| Docker build backend | Not run |
| Push to ECR `digitize-qa` | Not run |
| `terraform apply` (approved plan) | Not run |
| Secrets Manager populate | Not run |
| QA RDS `alembic upgrade head` (**088**) | **Blocked — TEST-13** |
| ECS service deploy | Not run |
| Flutter web QA distribution | Not run |
| TLS/DNS verification | Not run |
| Health `/api/v1/health` on QA URL | Not run |

---

## 4. Database migration state

| Database | Revision | Head required |
|----------|----------|----------------|
| Local `digitize` (dev) | **088_security_event_schema_align** | Applied |
| Local `digitize_test` | **083_support_ticket_escalation** | **NOT READY** — EQ-011 preflight fails |

```bash
DB_NAME=digitize_test ENVIRONMENT=development \
  poetry run python scripts/eq011_digitize_test_preflight.py
```

**Output:** `EQ-011 preflight: NOT READY` — requires authorized upgrade to at least **084**, recommend **088**.

---

## 5. Post-deployment smoke (§6)

**Not executed** — no QA API base URL available.

---

## 6. Rollback

- ECS: revert to previous task definition revision.
- Terraform: stateful resources (KMS, secrets) — **do not destroy** without ops approval.
- DB: forward-only migrations; restore from RDS snapshot if rollback required.

---

## 7. Authorization required (single request)

See consolidated authorization in `CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md` § Authorization.
