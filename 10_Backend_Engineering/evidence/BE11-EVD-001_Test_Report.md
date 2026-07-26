# BE11-EVD-001 — Test Report

Purpose: Provide links and summary of automated and manual test evidence required for backend release readiness.

Template:

- Release: Digitize-Release-2026-07-26
- Version: v2026.07.26
- CI Build: github.com/OrieOn/Digitize-by-OrieOn/actions/runs/<run-id>
- Test summary: (pass/fail counts, coverage, notable regressions)
- Link to full test artifacts: (link to junit/pytest/html report or artifact storage)
- Owner: QA Lead
- Notes: (any deviations, flaky tests, waivers)

Populate this file with CI job URLs, artifact references, and a short summary for reviewers.

How to populate (example commands):

1. Using GitHub CLI to list recent runs and view artifacts:

```bash
gh run list --repo OrieOn/Digitize-by-OrieOn --workflow "CI" --limit 5
gh run view <run-id> --repo OrieOn/Digitize-by-OrieOn --log
gh run download <run-id> --repo OrieOn/Digitize-by-OrieOn --name junit-report.xml
```

2. Using GitHub API (requires `GITHUB_TOKEN` with repo scope):

```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
	https://api.github.com/repos/OrieOn/Digitize-by-OrieOn/actions/runs | jq '.workflow_runs[0] | {id,html_url,status,conclusion}'
```

If CI artifacts are stored in an artifact repository (S3, Artifactory), include direct links and retention notes.
