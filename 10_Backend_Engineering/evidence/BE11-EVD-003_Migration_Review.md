# BE11-EVD-003 — Migration Review

Purpose: Provide migration scripts, review notes, compatibility checks, rollback guidance, and migration test evidence.

Template:

- Release: Digitize-Release-2026-07-26
- Version: v2026.07.26
- Migration scripts location: docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md or migrations/ folder
- Migration test evidence: (preflight checks, staging migration run logs, schema-compatibility tests)
- Rollback plan: (steps to revert or mitigate)
- Owner: Database Lead
- Notes: (known risks, ordering constraints)

Populate this file with migration run IDs, links to migration logs, and reviewer comments.

How to populate (example commands):

1. If migrations are run via CI, fetch the pipeline run:

```bash
gh run list --repo OrieOn/Digitize-by-OrieOn --workflow "Migrations" --limit 5
gh run view <run-id> --repo OrieOn/Digitize-by-OrieOn --log
```

2. If migrations are applied from the `migrations/` folder, include the migration script names and any staging-run logs or DB snapshots.
