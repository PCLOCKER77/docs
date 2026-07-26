# BE11-EVD-004 — API Compatibility Review

Purpose: Document API compatibility checks, contract verification, and consumer-impact notes.

Template:

- Release: Digitize-Release-2026-07-26
- Version: v2026.07.26
- OpenAPI spec location: docs/07_API_Collections/OpenAPI or generated OpenAPI artifacts
- Compatibility test evidence: (contract tests, consumer integration tests)
- Breaking changes: (list of approved breaking changes with ADRs/migration notes)
- Owner: API Reviewer
- Notes: (compatibility risk, suggested mitigation)

Populate with OpenAPI diff reports, contract test results, and reviewer approvals.

How to populate (example commands):

1. Generate OpenAPI diffs between current and previous release (example using `openapi-diff`):

```bash
openapi-diff previous_openapi.yaml current_openapi.yaml --output report.md
```

2. If contract tests publish CI artifacts, retrieve them:

```bash
gh run list --repo OrieOn/Digitize-by-OrieOn --workflow "Contract Tests" --limit 5
gh run download <run-id> --repo OrieOn/Digitize-by-OrieOn --name contract-test-report.html
```
