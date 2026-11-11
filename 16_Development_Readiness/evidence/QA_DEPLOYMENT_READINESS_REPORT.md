# QA deployment readiness

**Date:** 2026-11-09

---

## Application readiness

| Check | Status |
|-------|--------|
| Catalog 228/228 | **Verified** (`contract_numbered_audit.py`) |
| Local migrations through **087** | **Applied** (`alembic current` → head) |
| Security pre-QA gate | **PASS** ([SECURITY_HARDENING_AND_VERIFICATION_REPORT.md](./SECURITY_HARDENING_AND_VERIFICATION_REPORT.md)) |
| New skeleton APIs (085–087) | Unit tests pass; **PG IV for 08/13/14 on digitize** — run with existing guards |

---

## Database authorization

| Target | Status |
|--------|--------|
| Local `digitize` (dev) | **087 applied** this session |
| `digitize_test` (EQ-011) | **AWAITING_AUTHORIZATION** — [TEST-13](../../../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md); remains at **036** until approved upgrade |
| QA RDS | **No migration executed** — requires deployment runbook + explicit approval |

**Procedure when authorized:**

```bash
# QA ECS task or bastion — use approved secret-backed DATABASE_URL only
alembic upgrade head
```

---

## Regression executed (partial)

```bash
cd digitize-services
.venv/bin/pytest \
  tests/authentication/test_auth_api.py \
  tests/communication/test_whatsapp_webhook.py \
  tests/communication/test_communication_service_consolidated.py \
  tests/billing/test_invoice_adjustment_balance.py \
  tests/audit/test_client_ingest_blocked.py \
  tests/api/test_catalog_validation.py -q
```

**31+ passed** in combined targeted runs; **not** full monorepo / Flutter suite this session.

**Pre-existing:** `test_unified_operation_tracking` unmapped extra routes (enrollments list) — unchanged.

---

## AWS QA deployment

| Step | Status |
|------|--------|
| Terraform plan/apply | **Not run** (no CI credentials in agent session) |
| ECR image push | **Not run** |
| ECS deploy | **Not run** |
| Secrets Manager population | **Operator task** |
| Health check smoke | **Pending deploy** |

**Infrastructure repo:** `digitize-infrastructure/environments/qa` — modules for networking, ALB, ECS, RDS, IAM, CloudWatch present.

**Rollback:** Standard ECS previous task definition revision (document in ops runbook — unchanged).

---

## Release gates checklist (§23)

| Gate | Met? |
|------|------|
| Critical security resolved | Yes (none open) |
| High security resolved/accepted | Yes |
| AuthZ tests (targeted) | Yes |
| Tenant isolation (no new defects) | Yes |
| Financial unit integrity | Yes (adjustments) |
| Local migration verified | Yes |
| QA DB migration auth | **No** — TEST-13 |
| Infra security reviewed | Yes (read-only) |
| Backup/recovery documented | RDS module defaults — **confirm in ops** |

**Overall:** **Ready for QA deployment preparation**; **blocked on** EQ-011/`digitize_test` and AWS deploy execution, not on application catalog completeness.

---

## WhatsApp feature gate

**Disabled** until Meta credentials + webhook URL configured ([WHATSAPP_INTEGRATION_IMPLEMENTATION_REPORT.md](./WHATSAPP_INTEGRATION_IMPLEMENTATION_REPORT.md)).
