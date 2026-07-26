# BE11-EVD-002 — Security Review

Purpose: Document the security review evidence for the backend release.

Template:

- Release: Digitize-Release-2026-07-26
- Version: v2026.07.26
- Security checklist: (SAST/Bandit results, dependency-scan report, secret-scan, threat model updates)
- Link to security artifacts: (URLs to SCA, SAST, secret-scan, and manual review notes)
- Owner: Security Lead
- Notes: (any accepted risks, waivers, remediation plan)

Populate this file with links to scan outputs and review notes.

How to populate (example commands):

1. GitHub Actions artifact retrieval:

```bash
gh run list --repo OrieOn/Digitize-by-OrieOn --workflow "Security Scan" --limit 5
gh run download <run-id> --repo OrieOn/Digitize-by-OrieOn --name dependency-scan.html
```

2. Security scanners (SCA/SAST) usually upload reports to artifacts or S3 — include direct links and scan timestamps.
