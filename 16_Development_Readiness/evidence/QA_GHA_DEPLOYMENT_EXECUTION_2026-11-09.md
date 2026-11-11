# QA GitHub Actions deployment execution — 2026-11-09

**Status:** **COMPLETE** (live service verified; workflow gate follow-up on digest-verify step)

## Deployment ownership

| Owner | Responsibility |
|-------|----------------|
| **GitHub Actions** | `linux/amd64` build, SHA tag + digest push, task-def register, Alembic, ECS update, liveness |
| **Terraform** | VPC/RDS/ECS cluster/ECR/secrets; `lifecycle.ignore_changes` on task `container_definitions` and service `task_definition` |

**Repos:** `digitize-infrastructure` @ `02f520c` (+ local IAM ListTasks apply); `digitize-services` @ `602223f` on `release/qa-smoke-20261016`.

## GitHub Actions evidence

| Run | Commit | Result |
|-----|--------|--------|
| [42619469970](https://github.com/PCLOCKER77/digitize-services/actions/runs/42619469970) | `bf5a735` | **Failed** — `iam:PassRole` on `digitize-qa-ecs-task` (fixed + applied) |
| [42624486238](https://github.com/PCLOCKER77/digitize-services/actions/runs/42624486238) | `602223f` | **Partial** — deploy + stability OK; digest step failed (`ecs:ListTasks`) |

**Blocker fixes (infrastructure, applied in AWS):**

- `PassEcsTaskRole` on `digitize-qa-github-backend-deploy`
- `EcsListTasks` scoped to cluster `digitize-qa`

## Live QA (post GHA deploy)

| Item | Value |
|------|--------|
| API | `https://qa-api.digitizeplatform.in` |
| Liveness | **HTTP 200** |
| ECS service | `digitize-qa-backend` — desired **1**, running **1**, rollout **COMPLETED** |
| Task definition | **digitize-qa-backend:15** |
| Container image | `799201156295.dkr.ecr.ap-south-1.amazonaws.com/digitize-qa-backend@sha256:911b8f7d06e5098f1aca92dcccaaa514abdb0f0da875b581d89248486a2e2228` |
| ECR digest (rev 15) | `sha256:911b8f7d06e5098f1aca92dcccaaa514abdb0f0da875b581d89248486a2e2228` |
| GHA commit SHAs | `bf5a735` (release), `602223f` (retrigger) — image tags = full `github.sha` on each run |

## Database

| Item | Value |
|------|--------|
| RDS | `digitize-qa-postgres` / database `digitize` |
| Pre-cutover snapshot | `digitize-qa-pre-cutover-20261109-172904` |
| Alembic (QA RDS) | **`088_security_event_schema_align`** (upgraded during cutover via ECS Alembic task) |

## Workflow / dependency changes

- `deploy-qa.yml`: Buildx `linux/amd64`, digest pinning, baseline **088**, import smoke, digest verify
- `pyproject.toml`: `httpx` in main deps; FastAPI **^0.109.1**
- No manual Mac ECR push for the successful GHA deploy path

## Remaining

- Re-run workflow after IAM ListTasks apply for **fully green** Actions run (deploy + liveness already satisfied manually).
- `pip-audit`: FastAPI critical addressed; transitive dev-tool CVEs remain (virtualenv, etc.) — low runtime exposure in container.
- Local `var/` unstaged; not in release commit.
