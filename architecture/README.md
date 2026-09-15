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
| [MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md](MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md) | Store compliance audit; store binary still not ready |
| [OPERATOR_CLI.md](OPERATOR_CLI.md) | Phase-1 operator CLI: Platform Admin bootstrap and first password |

Authoritative upstream documents:

- `docs/10_Backend_Engineering/BE-00` through `BE-11`
- `docs/07_API_Collections/API-00`
- `docs/06_Database_Design/DATABASE_FOUNDATION_FREEZE.md`
- `docs/99_Decision_Records/DR-004`, `DR-007` (clarified by `DR-018`), `DR-013`, `DR-019`

Runtime decision record: `docs/99_Decision_Records/DR-018_Engineering_Foundation_Runtime.md`
