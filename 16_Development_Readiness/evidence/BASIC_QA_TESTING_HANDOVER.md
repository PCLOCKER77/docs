# Basic QA testing handover

**Date:** 2026-11-10 (frontend QA deploy)  
**Audience:** QA engineers — first controlled test pass.  
**Status:** **ACTIVE — backend + Flutter web QA deployed via GitHub Actions** (backend: [QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md](./QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md); frontend: `digitize-ui` run [42853568888](https://github.com/PCLOCKER77/digitize-ui/actions/runs/42853568888)).

---

## 1. Environment entry (when deployed)

| Item | Value |
|------|--------|
| API base | `https://qa-api.digitizeplatform.in/api/v1` |
| Health | `GET /api/v1/health/liveness` → **200** (verified 2026-11-09) |
| Flutter web | `https://qa.digitizeplatform.in` (S3 `digitize-qa-web-799201156295`, CloudFront `EC7UZ5XYA9CNE`; API compile-time base `https://qa-api.digitizeplatform.in`) |
| WhatsApp | **Off** until Meta onboarding — expect `WHATSAPP_PROVIDER=none` |
| Schema head | **`088_security_event_schema_align`** (QA RDS must match after TEST-13 migration) |

**Build version:** ECS `digitize-qa-backend:15`; image `…/digitize-qa-backend@sha256:911b8f7d06e5098f1aca92dcccaaa514abdb0f0da875b581d89248486a2e2228`; GHA commit `602223f0de4ce411aab58a4dd8f27fef03237737` (branch `release/qa-smoke-20261016`).

---

## 2. Test accounts

Provision via existing identity flows:

- **Platform Admin** — platform governance only (no tenant data superuser). **E2E (laptop, AWS, RDS, PA, password):** [QA_LOCAL_AWS_SETUP_PLATFORM_ADMIN_E2E.md](./QA_LOCAL_AWS_SETUP_PLATFORM_ADMIN_E2E.md). Broader ops reference: [QA_PLATFORM_ADMIN_ONBOARDING_KT.md](./QA_PLATFORM_ADMIN_ONBOARDING_KT.md).  
- **Organization Admin** — full org scope.  
- **Facility Admin** — facility-scoped billing/ops.  
- **Support Agent** — ticket + escalate (API-12-008).  

Use **synthetic** org/customer data; no real PAN/GSTIN unless statutory SaaS pack approved.

---

## 3. Enabled modules (228 APIs)

All numbered product APIs registered. Notable **new** since last handover:

- Facility invoice **adjustments** (API-08-005) — requires `Idempotency-Key`.  
- Reference **countries/states/languages/timezones/activity-types/localization**.  
- Audit **governance** (investigations, compliance report request, archive request, policies, violations list).  
- Trusted audit **POST** ingest → **403** (by design).

---

## 4. Disabled / incomplete

| Feature | State |
|---------|--------|
| WhatsApp live delivery | Awaiting Meta |
| Statutory SaaS invoice issue | Legal blockers (API-09) |
| EQ-011 `digitize_test` at full migration head | TEST-13 authorization (**currently 083**, need **088**) |
| Client POST audit capture | Forbidden |

---

## 5. Core scenarios (§22)

1. Login / logout / session idle expiry — use refresh rotation.  
2. Org onboarding + activate.  
3. Facility + site CRUD and activate.  
4. Customer register + membership lifecycle.  
5. Attendance check-in / walk-in.  
6. Trainer assignment + schedule conflict rules.  
7. Invoice + offline payment + receipt.  
8. Facility billing **adjustment** (charge reduction then compensating reversal).  
9. Support ticket + escalation panel.  
10. `GET /reference/countries` + currencies.  
11. `GET /audit-events` + export (org scope).  
12. `POST /audit-events` → expect **403**.  
13. Cross-org IDOR: second org token on first org `organization_id` → deny.  
14. WhatsApp — skip unless ops enables provider.

---

## 6. Defect reporting

Use project issue template; include:

- `correlation_id` from API error envelope  
- Principal role and `organization_id`  
- Route `operation_id` from OpenAPI  
- No paste of refresh cookies or secrets  

---

## 7. Data policy

- Prefer tagged test prefixes (`digitize-iv-*` patterns in billing PG tests).  
- Do not run destructive scripts on shared QA without ops approval.  
- **Do not** apply `alembic upgrade` on protected DBs without TEST-13 / ops sign-off.

---

## 8. Schedule / cost

QA stack is **on-demand** (Terraform QA design). Coordinate start/stop with ops to respect RDS stop-window limits.

---

## 9. Evidence links

- [CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md](./CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md)  
- [FINAL_SECURITY_VERIFICATION_REPORT.md](./FINAL_SECURITY_VERIFICATION_REPORT.md)  
- [FINAL_WHATSAPP_INTEGRATION_REPORT.md](./FINAL_WHATSAPP_INTEGRATION_REPORT.md)  
- [FINAL_QA_DEPLOYMENT_REPORT.md](./FINAL_QA_DEPLOYMENT_REPORT.md)  
- [MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md](./MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md)
