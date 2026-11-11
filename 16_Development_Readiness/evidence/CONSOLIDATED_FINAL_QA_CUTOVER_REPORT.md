# Consolidated final QA cutover report

**Date:** 2026-11-09  
**Success condition (user):** Authorized QA deployed, security + smoke gates passed, WhatsApp verified or safely disabled, tester handover ready.

## Executive summary

| Gate | Status |
|------|--------|
| **QA environment deployed** | **FAIL** — no ECR/ECS/Terraform apply |
| **Security verification** | **CONDITIONAL PASS** — local PG evidence; dependency CVE backlog documented |
| **PostgreSQL / migrations** | **PARTIAL** — dev `digitize` @ **088**; `digitize_test` @ **083** (TEST-13) |
| **WhatsApp** | **SAFE OFF** — webhook code tested; `WHATSAPP_PROVIDER=none` for QA |
| **Terraform** | **READY TO PLAN** — validate OK; apply awaiting approval |
| **Smoke tests on QA URL** | **NOT RUN** |
| **Basic testing handover** | **DRAFT** — blocked on deploy URLs and build digest |

**Overall cutover:** **NOT COMPLETE** — execute authorization block below, then deploy + migrate + smoke.

---

## Repository refs (local)

| Repo | Short SHA |
|------|-----------|
| digitize-services | `07cd920` (+ uncommitted cutover fixes) |
| digitize-infrastructure | `f028342` (+ IAM count fix uncommitted) |

---

## Security status

See [FINAL_SECURITY_VERIFICATION_REPORT.md](./FINAL_SECURITY_VERIFICATION_REPORT.md).

- **pip-audit:** 153 vulns / 12 packages; **FastAPI PYSEC-2024-38** → need ≥0.109.1 or QA risk acceptance.
- **Auth PG:** 7 passed including durable security events.
- **Audit / platform admin PG:** 8 + 32 passed in targeted batches.
- **Penetration test:** not performed.

---

## PostgreSQL verification

| Check | Result |
|-------|--------|
| Local `digitize` Alembic | **088_security_event_schema_align** |
| Mig 088 legacy alignment | Applied |
| Auth refresh / login security events | Persist after commit-order + tz fixes |
| `digitize_test` EQ-011 preflight | **NOT READY** (083 vs required ≥084 / head 088) |

---

## WhatsApp

See [FINAL_WHATSAPP_INTEGRATION_REPORT.md](./FINAL_WHATSAPP_INTEGRATION_REPORT.md).

**Live status:** **Disabled.** Webhook unit tests pass.

---

## Terraform / ECR / ECS

See [FINAL_QA_DEPLOYMENT_REPORT.md](./FINAL_QA_DEPLOYMENT_REPORT.md).

**Plan:** 7 add, 1 change, 1 destroy (ECS task definition replace).  
**Apply / deploy:** not executed.

---

## Application smoke tests

**Not executed** (no QA endpoint).

---

## Tester handover

See [BASIC_QA_TESTING_HANDOVER.md](./BASIC_QA_TESTING_HANDOVER.md) (updated for mig **088** and deploy blockers).

---

## Consolidated authorization request (single)

Approve the following in one action for cutover completion:

### A. QA database migration (TEST-13 / GAP-QA-001)

- **Target:** QA RDS database + shared `digitize_test` as applicable per ops runbook.
- **Action:** `alembic upgrade head` through **`088_security_event_schema_align`** (includes **085–087**).
- **Pre-checks:** RDS snapshot; confirm app user DDL rights; confirm no destructive DDL beyond 088 legacy rename.
- **Current `digitize_test`:** revision **083** — upgrade required before EQ-011 regression on shared env.
- **Not authorized:** production DB, ad-hoc superuser, or bypass of TEST-13.

### B. AWS Terraform apply (QA only)

- **Path:** `digitize-infrastructure/environments/qa`
- **Action:** `terraform plan` review → approved `terraform apply`
- **Notable changes:** new KMS key, blind-index secret, ECS task IAM, **ECS task definition replacement**
- **Cost impact:** KMS + Secrets Manager + unchanged RDS on-demand model; review full plan output before apply.
- **Destructive:** 1 ECS task definition replace (rolling deploy expected; not data loss).

### C. Application deploy

- Build/push `digitize-services` image to QA ECR.
- Update ECS service to new digest.
- Configure Secrets Manager (JWT, DB, Razorpay sandbox, `WHATSAPP_PROVIDER=none`).
- Set `ENVIRONMENT=qa`, `AUTH_DEV_BYPASS=false`.

### D. Meta WhatsApp (optional parallel track)

- Business onboarding, tokens, webhook URL — **not required** for first QA pass with WhatsApp off.

### E. Credentials / access required

- AWS role with ECS, ECR, Secrets Manager, RDS connect (migration runner).
- QA DNS/TLS already in stack or updated per plan.
- No new secrets in git.

---

## Remaining external dependencies

1. TEST-13 sign-off for QA RDS + `digitize_test` migration to **088**.  
2. Terraform apply + ECS deploy approval.  
3. FastAPI / dependency upgrade decision for CVE backlog.  
4. Meta WhatsApp onboarding (deferred).  
5. Flutter `flutter test` on CI or local before UI QA.  
6. Live QA smoke after deploy.

---

## Evidence index

| Document |
|----------|
| [FINAL_SECURITY_VERIFICATION_REPORT.md](./FINAL_SECURITY_VERIFICATION_REPORT.md) |
| [FINAL_WHATSAPP_INTEGRATION_REPORT.md](./FINAL_WHATSAPP_INTEGRATION_REPORT.md) |
| [FINAL_QA_DEPLOYMENT_REPORT.md](./FINAL_QA_DEPLOYMENT_REPORT.md) |
| [BASIC_QA_TESTING_HANDOVER.md](./BASIC_QA_TESTING_HANDOVER.md) |
| [MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md](./MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md) |
