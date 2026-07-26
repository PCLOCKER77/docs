# Testing Documentation Sign-off Matrix and PR Summary

## Purpose
Provide a concise sign-off matrix for freezing `docs/12_Testing` and a PR-ready summary to publish the changes made (company-name normalization and expanded traceability links for high-priority TBDs).

## Sign-off Matrix
- `TEST-00_Testing_Standards.md` — Approvers: QA Lead, Product Owner, Architecture Lead, Security Lead
- `TEST-01_Test_Strategy.md` — Approvers: QA Lead, Product Owner
- `TEST-02_Test_Environment_Strategy.md` — Approvers: QA Lead, DevOps Lead, Architecture Lead
- `TEST-03_Test_Data_Management.md` — Approvers: QA Lead, Database Lead, Security Lead, Legal (for retention)
- `TEST-04_Test_Plan_and_Test_Case_Standards.md` — Approvers: QA Lead, Release Manager
- `TEST-05_Functional_Testing.md` — Approvers: QA Lead, Product Owner, BA Representative
- `TEST-06_API_Testing.md` — Approvers: QA Lead, API Owner, Backend Lead
- `TEST-07_Integration_Testing.md` — Approvers: QA Lead, Integration Owner, Backend Lead
- `TEST-08_Performance_Load_Stress_Testing.md` — Approvers: Performance Lead, Architecture Lead, Operations
- `TEST-09_Security_Testing.md` — Approvers: Security Lead, QA Lead, Architecture Lead
- `TEST-10_UAT_Release_Validation.md` — Approvers: Product Owner, Business Stakeholder, Release Manager
- `TEST-11_Test_Completion_and_Release_Readiness.md` — Approvers: QA Lead, Release Manager, Operations

## Freeze Checklist (per doc)
- [ ] Acceptance Criteria validated
- [ ] Traceability links resolved or pointed to canonical mapping
- [ ] No `[TBD]` placeholders remain for critical items (retention, performance targets, security scope)
- [ ] Reviewers assigned
- [ ] Approvals captured in PR or issue tracker
- [ ] Evidence anchors (BE/APIs/DB) referenced where applicable

## Changes applied in this PR
- Standardized company name in `docs/12_Testing` to `OrieOn` across README and TEST-00..TEST-11.
- Replaced two high-priority `[TBD]` placeholders with direct traceability links and guidance:
  - Test data retention -> `docs/06_Database_Design/DB-17_Data_Archiving_Strategy.md`
  - Performance metric thresholds -> `docs/05_Technical_Architecture/TA-02_System_Architecture.md`
- Left general `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` guidance in README for non-critical unresolved mappings.

## Suggested git workflow (local commands)
```bash
git checkout -b docs/testing/fix-company-name-and-traceability
git add docs/12_Testing/*
git commit -m "docs(testing): standardize company name to OrieOn; expand high-priority traceability links; readiness checklist"
git push --set-upstream origin docs/testing/fix-company-name-and-traceability
```

## PR Title & Description (copy-paste)
**Title:** chore(docs): testing docs — standardize company name & expand high-priority traceability

**Description:**
- Standardize company name to `OrieOn` in `docs/12_Testing` to ensure cross-document consistency.
- Resolve two high-priority `[TBD]` placeholders by linking to authoritative upstream documents:
  - Test data retention -> `docs/06_Database_Design/DB-17_Data_Archiving_Strategy.md`
  - Performance metric thresholds -> `docs/05_Technical_Architecture/TA-02_System_Architecture.md`
- Provide a sign-off matrix and freeze checklist; outstanding items require owners to approve and supply retention and performance values.

## Suggested reviewers
- QA Lead
- Product Owner
- Architecture Lead
- Security Lead
- Database Lead
- Release Manager

## Notes
- I recommend keeping the central `BE-TRACEABILITY_MAPPINGS.md` as the canonical mapping file; expand only high-priority mappings into downstream docs to avoid duplication.
