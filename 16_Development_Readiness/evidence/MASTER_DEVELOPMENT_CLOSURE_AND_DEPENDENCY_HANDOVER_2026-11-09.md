# Master development closure and dependency handover

**Document ID:** MASTER-DEV-CLOSURE-2026-11-09  
**Authority:** Repository code, machine audit (`scripts/contract_numbered_audit.py`), DEV-19/21/22/23, gap evidence, local PostgreSQL inspection (2026-11-09).  
**Status:** **Maximum achievable local development closure** — external gates remain for statutory, providers, QA DB, DBA concurrency DB, skeleton promotions, production certification.

This is the consolidated execution outcome. It does not reopen completed gaps for review and does not propose new product scope.

---

## 1. What is genuinely complete (implemented + verified on authorized scope)

| Area | Closure evidence | Verification class |
| --- | --- | --- |
| GAP-API05-001 | Customer membership list (additive GET) + Flutter reload | Unit + PG `digitize` (`DIGITIZE_MEMBERSHIP_PG_TEST=1`) |
| GAP-API07-001 | Batch enrollment list (additive GET) + Flutter reload | Extended GAP-API07-004 PG suite on `digitize` |
| GAP-API07-002 | Facility/site schedule conflicts (NULL-site rule) | Unit + sequential PG on `digitize`; trainer conflicts preserved |
| GAP-API12-001 / GAP-JRN-012 | Support escalation Phase 1 | Mig 083, PG + Flutter IV |
| GAP-API09-005 | Cheque bounce grace + worker | Mig 084, dev DB verified |
| API-08 Phase 1 slice | Credit notes, refunds, customer wallet, receipts, offline lock | PG IV modules on `digitize` (per DEV-21) |
| GAP-INT-001/002 | Communication consolidation | Service boundaries + unit tests; live providers gated |
| Catalog / scaffold | GAP-API01-003, API03-005, metadata drift | Tests + registry alignment |
| Auth / org / subscription core | Existing numbered routes | Per module acceptance + DEV-19 session history |

**Machine audit (2026-11-09):** `contract_numbered_audit.py` → **212** `BACKEND_IMPLEMENTED`, **16** `SKELETON_CREATED` (228 numbered contracts). Reconcile via `var/api_audit_matrix.csv`.

**Flutter (latest delta):** `listBatchEnrollments` pagination fix; `batch_enrollment_test.dart` **5 passed** (2026-11-09).

---

## 2. Implemented but awaiting specific verification

| Item | Done in code | Not yet verified |
| --- | --- | --- |
| GAP-API07-002 facility concurrency | `test_facility_schedule_concurrency_postgres.py` + guard | **Real two-transaction PostgreSQL** on isolated DB |
| GAP-API08-006 / GAP-JRN-008 | Mock + sandbox SDK paths | Manual live card checkout (user-owned) |
| GAP-API09-003 | Webhook + PG paths | Manual Razorpay sandbox card capture |
| GAP-INT-002 / GAP-API10-002 | SES/MSG91 adapters (fail-closed) | Live provider delivery in authorized env |
| GAP-API11-001 | Schedule worker + HELD notifier | Live SMTP/SES report delivery |

---

## 3. Final dependency register (authoritative)

| Item | Module | Current state | Completed work | Remaining work | Dependency type | Required action | Next execution once unblocked | Closure criteria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Facility schedule concurrency PG | API-07 | Partially verified | Enforcement on `digitize`; concurrency test module + guard | Run 5 concurrency tests with real `pg_advisory_xact_lock` overlap | DBA / infrastructure | Superuser (or owner) creates `digitize_trainer_concurrency`; grant `digitize_app`; never use `digitize` for concurrency tests | `ENVIRONMENT=development DB_HOST=localhost DB_PORT=5434 DB_NAME=digitize_trainer_concurrency alembic upgrade head` (or authorized clone from `digitize`); then `DIGITIZE_FACILITY_SCHEDULE_CONCURRENCY_PG_TEST=1` + seed env vars; `pytest tests/training/test_facility_schedule_concurrency_postgres.py -q` | All 5 tests pass; one overlap scenario proves single winner + `FACILITY_SCHEDULE_CONFLICT_001` on loser |
| Statutory SaaS invoice issue | API-09 | Blocked fail-closed | Subscription/installment logic; `ISSUANCE_BLOCKERS`; professional pack doc | Implement only INV-001/002/003 approved controls | Legal / accounting / product | Complete §9 in `GAP-API09-002_STATUTORY_INVOICE_PROFESSIONAL_APPROVAL_PACK_2026-11-09.md`; register sign-off in DEV-19 | Implement approved blockers removal incrementally; PG issue tests | Issued statutory invoice on `digitize` without invented tax rules |
| SMS / OTP live | INT / API-04 / API-10 | Deferred / blocked | MSG91 boundary; memory/none default | Activate vendor + DLT + QA OTP journey | Provider + product | Product de-scope or authorize MSG91 creds + DLT | Provider QA on isolated config | OTP register/attendance OTP pass in authorized QA |
| Email / WhatsApp live | INT / API-10 | App prepared | `CommunicationService`, sender resolution, tenant isolation | SES + Meta WA live delivery | Provider credentials | Configure SES/WA in env; no silent central WA fallback | Opt-in delivery IV with real credentials | Successful delivery + audit rows; fail-closed without creds |
| EQ-011 / `digitize_test` head | QA / API-01 | Blocked | Local `digitize` IV suites | Migrate `digitize_test` per TEST-13 | Migration authorization | Owner approves TEST-13; DBA runs `036→084` on `digitize_test` | `eq011_digitize_test_preflight.py`; EQ-011 suite | Documented pass on shared test DB |
| API-13 write skeletons (8 ops) | API-13 | Skeleton | Phase-1 reads IV (`GAP-API13-006`) | Migrations + ingest/policy writes | Product + schema | GAP-API13-001 capture-POST stance; schema DDL auth | Per-operation promotion with mig + tests | Routes live + PG IV; no client ingest without stance |
| API-14 reference skeletons (7 ops) | API-14 | Deferred skeleton | Extras / Flutter references elsewhere | GMD seed + numbered route promotion | Product | Approve GMD seed set (GAP-API14-001…004) | Seed migration + implement list endpoints | PG IV + registry `BACKEND_IMPLEMENTED` |
| API-08-005 adjustments | API-08 | Skeleton | Distinct from online pay | Adjustment entity decision | Product | Confirm deferral vs design in facility billing register | Only if approved — mig + route | Contract tests + PG IV |
| Media polish | API-02 | Deferred partial | — | Concrete defect-led scope only | Product | Approve scope for GAP-API02-004 or keep deferred | Implement approved slice only | Flutter/tests for defined scope |
| Facility-level vs site cross-block | API-07 | Explicitly open | Separate resources enforced | Optional unified resource model | Product | Written decision if facility-wide blocks site slots | Code + PG only after approval | New rule documented + regression |
| 16 numbered skeletons (inventory) | Multi | Blocked aggregate | 212 implemented routes | Promote each with auth | Mixed | Per-row decision in `var/api_audit_matrix.csv` | Same as API-13/14 rows above | Audit matrix zero skeletons or accepted deferrals |
| Production / shared QA certification | All | Not performed | Local `digitize` IV | Deploy + certify | Deployment / QA | Authorized shared env + pipelines | Run module PG suites on target env | DEV-19 labels Integration-verified only with env evidence |

---

## 4. Classification summary

1. **Implemented and verified (local dev):** Membership list, enrollment list, facility conflict (sequential PG), support escalation, cheque grace app slice, API-08/local billing IV surfaces, communication app boundary, majority of P1 Flutter journeys (per DEV-21).
2. **Implemented, integration partial:** Facility concurrency PG; Razorpay manual card; live comms delivery.
3. **Awaiting credentials:** SES, MSG91, Meta WA, live Razorpay card QA.
4. **Awaiting legal/accounting:** GAP-API09-002 statutory invoice issue.
5. **Awaiting product decisions:** API-14 GMD, API-13 client ingest, media polish, facility/site cross-block, SMS launch scope.
6. **Awaiting DBA/migration auth:** `digitize_trainer_concurrency`; TEST-13 `digitize_test` upgrade.
7. **Deployment not performed:** Production certification, shared QA sign-off.
8. **Explicitly deferred:** SMS first release, statutory until INV pack, skeleton bulk promotion without per-family auth.

---

## 5. Test commands reference (closure evidence)

```bash
# Membership list PG (digitize @ :5434)
ENVIRONMENT=development DB_HOST=localhost DB_PORT=5434 DB_NAME=digitize \
  DIGITIZE_MEMBERSHIP_PG_TEST=1 \
  pytest tests/membership/test_membership_list_by_customer_digitize_postgres.py -q

# Training PG incl. enrollment list + facility rules (digitize)
ENVIRONMENT=development DB_HOST=localhost DB_PORT=5434 DB_NAME=digitize \
  DIGITIZE_TRAINING_PG_TEST=1 \
  pytest tests/training/test_training_programs_digitize_postgres.py -q

# Facility concurrency (requires digitize_trainer_concurrency — NOT provisioned 2026-11-09)
ENVIRONMENT=development DB_HOST=localhost DB_PORT=5434 \
  DB_NAME=digitize_trainer_concurrency \
  DIGITIZE_FACILITY_SCHEDULE_CONCURRENCY_PG_TEST=1 \
  pytest tests/training/test_facility_schedule_concurrency_postgres.py -q

# Unit regression slice (no DB)
pytest tests/membership/test_membership_list_by_customer.py \
  tests/training/test_facility_schedule_conflict.py \
  tests/training/test_trainer_schedule_conflict_enforcement.py -q

# Flutter enrollment UI
cd digitize-ui && flutter test test/features/training_operations/batch_enrollment_test.dart
```

**Concurrency DB check (2026-11-09):** Only `digitize` and `digitize_test` exist; `digitize_trainer_concurrency` absent; `digitize_app` cannot `CREATE DATABASE`.

---

## 6. Handover — who does what next

| Owner | Action |
| --- | --- |
| **DBA / infra** | Create `digitize_trainer_concurrency`; run Alembic head or authorized clone; document connection for devs |
| **Product owner** | Close Phase 0 rows in DEV-23 (GMD, API-13 stance, media scope, SMS scope); facility cross-block if needed |
| **Legal / accounting** | INV pack §9 for GAP-API09-002 |
| **Engineering** | On DBA completion → run facility concurrency pytest; on INV approval → implement approved statutory controls only; on TEST-13 → migrate `digitize_test` and re-run EQ-011 |
| **User (manual)** | Razorpay sandbox card checkout when convenient — not a code blocker |

---

## 7. Document updates

- **DEV-19:** Session log + pointer to this file (2026-11-09).
- **DEV-21:** Final dependency register section (table condensed from §3).
- **DEV-23:** Phase 0 — membership/training list/facility items **closed**; master status unchanged for external gates.
- **Module evidence:** GAP-API05/07 evidence files current; API-05/07 acceptance updated.

**Product is not production-complete.** Local authorized engineering for the current backlog is **exhausted** except execution steps that depend on the table above.
