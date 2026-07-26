# DB Design Freeze — Sign-off Package (2026-07-26)

This package collects the artifacts, verification steps, evidence, and approvers required to mark the Database Design folder `docs/06_Database_Design` as Frozen.

Branch: `docs/freeze-2026-07-26`
PR: Create a PR from `docs/freeze-2026-07-26` into `main` with the migration artifacts in `database/migrations/` and the docs state changes.

Required approvers (placeholders — replace with real names/emails):
- Product Architecture: NAME <email@example.com>
- Data Architecture: NAME <email@example.com>
- Solution Architecture: NAME <email@example.com>
- Security Architecture: NAME <email@example.com>
- Finance/Commercial: NAME <email@example.com>
- Compliance/Audit: NAME <email@example.com>
- DevOps/Platform: NAME <email@example.com>
- QA Lead: NAME <email@example.com>

Artifacts included in the PR:
- `database/migrations/001_*` .. `008_*` — versioned migration SQL files
- `database/migrations/verify_schema.sql` — schema verification queries
- `scripts/run_migrations_local.sh` — local migration runner
- `database/traceability/db10_table_columns.csv` and `database/traceability/db10_full.md` — DB-10 traceability artifacts
- Updated docs under `docs/06_Database_Design` marking DB-00..DB-11 as `Frozen` (provisional)

Verification steps for approvers:
1. Clone repo and checkout the branch:

```bash
git fetch origin
git checkout -b docs/freeze-2026-07-26
```

2. Run local migrations against a disposable Postgres (use Docker):

```bash
docker run --name digitize-pg -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=digitize_dev -p 5432:5432 -d postgres:15
# wait for startup
scripts/run_migrations_local.sh
psql "postgresql://postgres:postgres@localhost:5432/digitize_dev" -f database/migrations/verify_schema.sql
```

3. Review `database/traceability/db10_full.md` and the CSV for sensitivity classifications and examples.
4. Run CI workflow `DB Migrations Verify` (or trigger via Actions tab) to validate migrations in an ephemeral runner.

Evidence collection and sign-off:
- Approvers must respond in PR review with an approval comment and link to any verification logs (CI run ID / Docker run output / psql verification SQL output).
- Add recorded approval lines below once received.

Approvals (sign here):
- Product Architecture: 
- Data Architecture: 
- Solution Architecture: 
- Security Architecture: 
- Finance/Commercial: 
- Compliance/Audit: 
- DevOps/Platform: 
- QA Lead: 

Notes:
- Sensitive columns requiring RLS/encryption are noted in `database/traceability/db10_full.md` but require security owner confirmation before production rollout.
- This package marks DB-00..DB-11 as `Frozen` provisionally; final canonical freeze occurs once approvals are collected and the PR is merged.
