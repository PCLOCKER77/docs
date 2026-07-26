# DR-012 GitHub Actions CI/CD Baseline

> Decision record for selecting GitHub Actions as the CI/CD orchestration baseline.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-012 |
| Document Name | GitHub Actions CI/CD Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | DevOps / Engineering Governance |
| Reviewers | Backend Engineering, Frontend Engineering, QA, Security, Operations, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

GitHub Actions is selected as the CI/CD orchestration baseline for Digitize documentation and implementation pipelines.

If the source-code repository is later hosted outside GitHub, this decision shall be superseded by a repository-platform-specific CI/CD decision.

---

# 2. Context

Digitize deployment documentation requires a concrete pipeline baseline for validation, build, test, security scanning, artifact creation, environment promotion, evidence collection, and release readiness.

Leaving CI/CD undefined prevents consistent quality gates and deployment governance.

---

# 3. Decision

Digitize shall use GitHub Actions for:

- Pull request validation.
- Formatting and lint checks.
- Unit and integration test execution.
- Security and secret scanning.
- Container image build.
- Artifact publishing.
- Migration validation.
- Environment deployment workflows.
- Release readiness evidence generation.

Production deployment workflows shall require approval gates and Release Management alignment.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| GitHub Actions | Integrated Git-based CI/CD with broad ecosystem support | Accepted |
| Jenkins | Self-managed CI/CD platform | Rejected for baseline because it adds operational overhead |
| GitLab CI | Strong integrated CI/CD platform | Deferred unless repository hosting changes |
| Manual deployment | Human-run validation and deployment | Rejected because enterprise release governance requires repeatable automation |

---

# 5. Rationale

GitHub Actions provides a practical baseline for repository-triggered automation, evidence collection, checks, scanning, build, test, and deployment workflows.

It supports the documentation model where Deployment defines execution controls and Release Management owns release decisions.

---

# 6. Consequences

## Positive Consequences

- CI/CD tooling ambiguity is removed.
- Deployment standards can define concrete pipeline gates.
- Testing and security evidence can be generated consistently.
- Release Management can consume pipeline evidence.

## Tradeoffs

- CI/CD design becomes coupled to GitHub repository hosting.
- GitHub permissions and environment protections must be governed carefully.

## Risks

- Weak branch protections or environment approvals could bypass release governance.
- Long-running deployment workflows require timeout and retry controls.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `11_Deployment/DEP-03_CI_CD_Pipeline_Standards.md` | Uses GitHub Actions pipeline baseline |
| `12_Testing/` | Uses CI evidence for automated test results |
| `14_Release_Management/` | Consumes release candidate and pipeline evidence |
| `13_Operations/` | Consumes deployment evidence and operational handover context |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| CI/CD baseline | DevOps / Engineering Governance |
| Workflow implementation | DevOps / Engineering teams |
| Security gates | Security |
| Test gates | QA |
| Release approval gates | Release Management |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current CI/CD baseline.

It may be frozen after pipeline gates, environment protections, artifact retention, evidence generation, and release approval integration are reviewed.

