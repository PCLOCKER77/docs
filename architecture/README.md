# Digitize architecture freeze

This folder records the **engineering foundation** and the **API contract /
skeleton freeze**. It does not replace approved standards in
`10_Backend_Engineering`, `07_API_Collections`, or `06_Database_Design`.

| Document | Role |
| --- | --- |
| [BACKEND_CODING_STANDARDS.md](BACKEND_CODING_STANDARDS.md) | Authoritative repository-wide backend coding standard |
| [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md) | Architectural freeze: invariants, deferred items, cross-cutting rules |
| [BACKEND_FOUNDATION.md](BACKEND_FOUNDATION.md) | Runtime wiring: middleware, logging, UoW, health, bootstrap |
| [AUTH_CONTRACT_FREEZE.md](AUTH_CONTRACT_FREEZE.md) | Frozen Authentication HTTP/security contract (not implemented) |
| [API_CONTRACT_REGISTRY.md](API_CONTRACT_REGISTRY.md) | Authoritative API-01..14 registry, extras, skeletons, and deferred decisions |
| [NAMING_AUDIT.md](NAMING_AUDIT.md) | Semantic naming identities vs API inventory / migration history |
| [API_03_IDENTITY_USER_ROLE_PREIMPLEMENTATION.md](API_03_IDENTITY_USER_ROLE_PREIMPLEMENTATION.md) | API-03 identity/user/role pre-implementation gate |
| [ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md](ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md) | Frozen access, Phase-1 personas, commerce boundary (DR-019) |
| [API-05_MEMBERSHIP_PLAN_CONTRACT_REVIEW.md](API-05_MEMBERSHIP_PLAN_CONTRACT_REVIEW.md) | API-05 Slice 1 contract finalization (v2.0; 12 membership ops; not implementation) |
| [API-05_IMPLEMENTATION_READINESS_REVIEW.md](API-05_IMPLEMENTATION_READINESS_REVIEW.md) | API-05 Slice 1 implementation-readiness (**PASS**; implementation not done in that review) |
| [API-05_MEMBERSHIP_PLAN_PRODUCT_DECISION_BRIEF.md](API-05_MEMBERSHIP_PLAN_PRODUCT_DECISION_BRIEF.md) | API-05 P0/P1 options and recommendations for product approval |
| [../99_Decision_Records/DR-020_API-05_Membership_Plan_and_Membership_Scope.md](../99_Decision_Records/DR-020_API-05_Membership_Plan_and_Membership_Scope.md) | DR-020 API-05 scope (**Accepted**; next: contract finalization, not implementation) |
| [ORGANIZATION_ONBOARDING_PA_BOUNDARY_FREEZE.md](ORGANIZATION_ONBOARDING_PA_BOUNDARY_FREEZE.md) | DR-021 org onboarding lifecycle + PA tenant-data boundary |
| [ORG_ONBOARDING_CHANGE_MATRIX.md](ORG_ONBOARDING_CHANGE_MATRIX.md) | Internal change matrix for DR-021 delivery |
| [DR-022_TRANSITION_FROM_DR-021.md](DR-022_TRANSITION_FROM_DR-021.md) | Reusable foundations reserved **DR-022** (Customer module) must consume (no DR-022 implementation) |
| [../99_Decision_Records/DR-023_Company_Branch_Site_Facility_Hierarchy.md](../99_Decision_Records/DR-023_Company_Branch_Site_Facility_Hierarchy.md) | DR-023 target Company → Branch/Site → Facility (**Accepted** for development; deploy/`main` not authorized) |
| [DR-023_HIERARCHY_MIGRATION_PLAN.md](DR-023_HIERARCHY_MIGRATION_PLAN.md) | Hierarchy migration plan for DR-023 (additive schema; no auto-mapping of test/QA/prod fixtures) |
| [MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md](MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md) | Store compliance audit; store binary still not ready |
| [OPERATOR_CLI.md](OPERATOR_CLI.md) | Phase-1 operator CLI: Platform Admin bootstrap and first password |
| [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) | SaaS invoice / Razorpay unresolved decision registry |
| [API-08_FACILITY_BILLING_DECISION_REGISTER.md](API-08_FACILITY_BILLING_DECISION_REGISTER.md) | Facility billing skeleton decision register (**proposals**; 8 remaining) |
| [API-13_AUDIT_PRODUCT_DECISION.md](API-13_AUDIT_PRODUCT_DECISION.md) | API-13 audit capture / schema product recommendation (**not approved DR**) |
| [API-14_REFERENCE_SOURCE_OF_TRUTH.md](API-14_REFERENCE_SOURCE_OF_TRUTH.md) | API-14 reference catalog source-of-truth recommendation (**not approved DR**) |
| [../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md) | Authoritative feature / API completion tracker (228 inventory) |
| [../12_Testing/TEST-12_Engineering_Quality_QA_Readiness_Review_2026-11-02.md](../12_Testing/TEST-12_Engineering_Quality_QA_Readiness_Review_2026-11-02.md) | Engineering quality / QA readiness findings (2026-11-02) |
| [../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md) | EQ-011 `digitize_test` migration authorization **proposal** |
| [../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) | API-12-008 escalate persistence migration **proposal** |

Authoritative upstream documents:

- `docs/10_Backend_Engineering/BE-00` through `BE-11`
- `docs/07_API_Collections/API-00`
- `docs/06_Database_Design/DATABASE_FOUNDATION_FREEZE.md`
- `docs/99_Decision_Records/DR-004` (live hierarchy), `DR-007` (clarified by `DR-018`), `DR-013`, `DR-019`, `DR-020`, `DR-023` (proposed hierarchy successor; not live)

Runtime decision record: `docs/99_Decision_Records/DR-018_Engineering_Foundation_Runtime.md`
