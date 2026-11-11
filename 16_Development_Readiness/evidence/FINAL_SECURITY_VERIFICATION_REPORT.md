# Final security verification — QA cutover gate

**Date:** 2026-11-09  
**Scope:** `digitize-services` (local `digitize` DB); no independent penetration test.  
**Overall verdict:** **CONDITIONAL PASS** — auth/audit PG IV green after mig **088** + auth commit-order fix; **dependency CVE backlog** requires upgrade plan or documented risk acceptance before production.

---

## 1. Baseline

| Item | Result |
|------|--------|
| Numbered API catalog | **228/228** `BACKEND_IMPLEMENTED` |
| Local Alembic head | **088_security_event_schema_align** |
| Penetration test | **Not performed** (no third-party assessment) |

---

## 2. Defects fixed in this cutover (authorized scope)

| Defect | Fix |
|--------|-----|
| Legacy `security.security_event` schema mismatch (087 `IF NOT EXISTS` skip) | Mig **088** — new table + `security_event_legacy` |
| ORM insert `occurred_at` tz mismatch (asyncpg DataError) | `DateTime(timezone=True)` on `SecurityEvent` |
| Durable events rolled back on failed login/refresh | Commit order: `record_durable_security_event` then `_persist_failure` |
| IAM Terraform plan blocked | `modules/iam` — `count` on crypto policies uses `enable_ecs_crypto_access` only |

---

## 3. Dependency scan (`pip-audit`)

```bash
cd digitize-services && poetry run pip-audit -f columns
```

**Result:** **153 known vulnerabilities in 12 packages** (transitive duplicates in report).

| Package | Installed | Notable ID | Fix versions |
|---------|-----------|------------|--------------|
| **fastapi** | 0.100.1 | PYSEC-2024-38 | ≥ **0.109.1** |
| certifi | 2026.7.22 | PYSEC-2026-4320 | 2026.10.18 |
| h11 | 0.14.0 | PYSEC-2026-348 | 0.16.0 |
| pillow | 11.3.0 | multiple | 12.1.1+ |
| filelock | 3.32.2 | multiple | 4.x |
| virtualenv | 21.7.1 | CVE-2026-113718 | 21.14.9 |

**Disposition:** No bulk upgrade applied in this cutover (regression risk). **QA:** document **FastAPI PYSEC-2024-38** as **accepted QA-only risk** until coordinated Poetry bump and full API regression. **Production:** upgrade FastAPI before go-live.

Static SAST: project uses **ruff** (no dedicated bandit job in CI observed this session).

---

## 4. Tests executed (commands and results)

### Authentication and session (PostgreSQL)

```bash
cd digitize-services
DIGITIZE_AUTH_SESSION_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  poetry run pytest tests/authentication/test_auth_session_digitize_postgres.py \
    tests/audit/test_security_event_auth_digitize_postgres.py -q
```

**Result:** **7 passed**.

### API-13 audit reads + security event on login failure

```bash
DIGITIZE_AUTH_SESSION_PG_TEST=1 DIGITIZE_AUDIT_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  poetry run pytest tests/audit/ tests/authentication/test_auth_api.py \
    tests/communication/test_whatsapp_webhook.py tests/billing/test_invoice_adjustment_balance.py -q
```

**Result:** **32 passed**, 19 skipped (non-PG opt-in).

### Platform admin security / governance

```bash
DIGITIZE_PLATFORM_ADMIN_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  poetry run pytest tests/security/test_platform_admin_security_digitize_postgres.py \
    tests/api/test_platform_admin_governance_digitize_postgres.py -q
```

**Result:** **8 passed**.

### Controls verified

| Area | Evidence |
|------|----------|
| Session idle / refresh replay | `test_auth_session_digitize_postgres.py` |
| Durable `security.security_event` on login fail | `test_security_event_auth_digitize_postgres.py` |
| Cross-org audit denial | `test_audit_reads_digitize_postgres.py` |
| Trusted client audit ingest **403** | governance service + unit tests |
| WhatsApp webhook HMAC / verify | `test_whatsapp_webhook.py` |
| Facility adjustment idempotency | `test_invoice_adjustment_balance.py` |
| Razorpay HMAC (unit) | prior suite / webhook tests |

### Flutter

`digitize-ui` present; **Flutter engine/tests not executed** in this agent session (environment permission). Run `flutter test` before UI QA sign-off.

---

## 5. Secrets and configuration

- No secrets committed in evidence docs.
- `.env` local only; QA must use **Secrets Manager** + task definition refs (Terraform QA module).
- `AUTH_DEV_BYPASS` must be **false** in QA ECS env.

---

## 6. Remaining risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| FastAPI 0.100.1 CVE | High (framework) | Upgrade to ≥0.109.1 + regression |
| Transitive pillow/filelock/certifi | Medium | Poetry lock refresh |
| No pentest | Process | Schedule independent assessment pre-production |
| QA not smoke-tested on live URL | Gate | Post-deploy §6 smoke (blocked on deploy) |

---

## 7. Sign-off statement

**Security gate for QA basic testing:** **Met on local PostgreSQL evidence** with documented dependency exceptions. **Not met for “production ready”** until dependency upgrades and live QA smoke complete.
