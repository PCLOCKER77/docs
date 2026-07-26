# BE11-EVD-005 — Deployment Handoff

Purpose: Capture deployment runbooks, handoff notes, and operational evidence required for the release.

Template:

- Release: Digitize-Release-2026-07-26
- Version: v2026.07.26
- Deployment runbook: (link to deployment steps / playbook)
- Smoke test evidence: (links to smoke test results in staging)
- Rollback verification: (steps to validate rollback if applied)
- Owner: DevOps Lead
- Notes: (scheduled window, required approvers on-call)

Populate this file with runbook links, handoff notes, and verification artifacts.

How to populate (example commands):

1. Retrieve deployment-run artifacts from CI:

```bash
gh run list --repo OrieOn/Digitize-by-OrieOn --workflow "Deploy to staging" --limit 5
gh run view <run-id> --repo OrieOn/Digitize-by-OrieOn --log
```

2. Link to runbooks or ops playbooks stored in the repository or confluence, and include smoke-test run IDs.
