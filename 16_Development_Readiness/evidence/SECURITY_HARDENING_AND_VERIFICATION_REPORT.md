# Security hardening and verification — pre-QA gate

**Date:** 2026-11-09  
**Environment:** Local development (`digitize-services`); QA AWS not mutated in this pass.  
**Verdict:** **PASS with documented follow-ups** (no open critical / high tenant-isolation defects identified in executed suites).

---

## 1. Baseline verified

| Item | Result |
|------|--------|
| Numbered API catalog | **228/228** `BACKEND_IMPLEMENTED` |
| Local Alembic head | **087_audit_governance_security** (085–087 applied) |
| Auth architecture | RS256 JWT, hashed refresh, session rotation (preserved) |

---

## 2. Authentication and session (Phase 1 §3)

**Inspected / preserved:** `app/modules/authentication/service.py`, `app/core/security/jwt.py`, refresh cookie helpers, password reset flows, rate limiter.

**Enhancement this pass:** Durable `security.security_event` rows on login failure, refresh replay, and expired refresh via `record_durable_security_event` (mig **087**).

**Tests executed:**

```bash
cd digitize-services
.venv/bin/pytest tests/authentication/test_auth_api.py \
  tests/authentication/test_session_refresh_policy.py \
  tests/authentication/test_rate_limit.py -q
```

**Result:** **19 passed**, 19 skipped (PG opt-in), 0 failed in targeted auth bundle.

**Not executed:** Full `DIGITIZE_AUTH_PG_TEST=1` postgres IV this session (prior evidence in `test_auth_session_digitize_postgres.py` remains valid after wiring).

---

## 3. Authorization and tenant isolation (§4)

**Architecture:** Database-backed principal + permission codes (unchanged).

**Regression:** Existing principal and governance tests not weakened. Cross-org audit denial covered in prior API-13 PG IV.

**Platform Admin:** Governance-only routes; no new tenant superuser paths introduced in 085–087.

**IDOR:** No new identifier bypass in skeleton promotion; facility/org scoping preserved on adjustments and audit governance routes.

---

## 4. API security (§5)

| Control | Status |
|---------|--------|
| Pydantic validation on new routes | Yes |
| Pagination params | Existing deps |
| Auth rate limits | Login / refresh / recovery (`limiter`) — tested |
| Security headers middleware | Preserved (`SecurityHeadersMiddleware`) |
| Error envelope | No stack traces to clients (existing handlers) |
| Client trusted audit ingest | **403** (`AuditGovernanceService.reject_trusted_client_ingest`) |

**New surface:** `GET/POST /api/v1/webhooks/whatsapp` — verify token + HMAC only; rejects unsigned POST.

---

## 5. Financial security (§6)

Facility adjustments: idempotent posting, compensating reversal, outstanding integration (unit: `test_invoice_adjustment_balance.py`).

Razorpay webhook HMAC: existing tests unchanged (not re-run full PG suite this session).

---

## 6. API-13 security events (§7)

| Workflow | Wired |
|----------|--------|
| Login failure | `security_event` + `authentication_event` |
| Refresh replay | `security_event` + session revoke |
| Expired refresh | `security_event` |
| Permission denial (global) | Log-only today — **follow-up:** selective durable events |

No secrets in `summary` fields; tokens/passwords never stored.

**Retention:** `retention_days` in audit policy JSON remains **null** pending legal approval (not invented).

---

## 7. Database and secrets (§8)

- Migrations **085–087** applied to local DB connected via app settings (not QA RDS).
- `.env.example` updated with `WHATSAPP_APP_SECRET`, `WHATSAPP_WEBHOOK_VERIFY_TOKEN` (no live values committed).
- `pip-audit`: not available in venv this session — **follow-up:** run in CI.

---

## 8. Infrastructure security (§9)

**Terraform QA** (`digitize-infrastructure/environments/qa`): reviewed structure — VPC, private subnets, ALB, ECS, RDS module, Secrets Manager, IAM modules present. **No `terraform apply` in this session.**

**Finding (informational):** `additional_rds_ingress_security_group_ids` documents transitional RDS client SG — confirm during QA cutover; not changed here.

---

## 9. Dependency assessment (§10)

Static: targeted pytest security/auth/communication suites green.  
**Not claimed:** External penetration test.

---

## Findings summary

| Severity | Count | Disposition |
|----------|-------|-------------|
| Critical | 0 | — |
| High | 0 open | — |
| Medium | 2 | Documented |
| Low | 2 | Documented |

| ID | Finding | Priority |
|----|---------|----------|
| SEC-M01 | WhatsApp delivery status idempotency is in-process only (not yet persisted to `communication.*`) | Medium — before live WhatsApp |
| SEC-M02 | Durable security events on generic `AuthorizationFailed` not wired | Medium — incremental |
| SEC-L01 | `pip-audit` not run | Low |
| SEC-L02 | Full PG auth IV not re-run post-wiring | Low — run before QA sign-off |

---

## Release gate

**Security gate for QA deployment preparation:** **PASS** (subject to EQ-011 / RDS migration authorization and optional PG auth re-IV).
