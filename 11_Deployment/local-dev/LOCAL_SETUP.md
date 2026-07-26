**Local Development Plan — Frontend & Backend**

Summary
- Purpose: provide a reproducible local development environment for frontend and backend, including a local Postgres database, migrations, and a sample start script.
- Files added: `docker-compose.dev.yml`, `scripts/local_dev_setup.sh`.

Prerequisites
- Docker and Docker Compose (docker-compose v2 / `docker compose`) installed.
- Node >=16 (frontend), Python 3.10+ (backend) — adjust to your project's versions.
- Git checkout of repository.

Quick start
1. Review and adjust `.env.dev` values if needed.
2. Run:

```bash
chmod +x scripts/local_dev_setup.sh
./scripts/local_dev_setup.sh
```

3. Visit `http://localhost:3000` for frontend, `http://localhost:8000` for backend.

What the setup does
- Starts a local Postgres container (image: postgres:15) with a persistent volume named `digitize_pgdata_dev`.
- Builds/starts the backend and frontend containers (or runs images) and wires them to the local DB.
- Waits for Postgres readiness, runs migrations via `scripts/run_migrations_local.sh` if present, and optionally seeds the DB from `scripts/seed.sql`.

DB setup and precautions
- Development-only credentials live in `.env.dev`. NEVER commit production secrets into the repo.
- Back up the `pgdata` volume before destructive operations: `docker volume ls` then `docker run --rm -v digitize_pgdata_dev:/data -v $(pwd):/backup alpine tar czf /backup/pgdata-backup.tgz -C /data .`
- If you need to reset the DB for a clean dev state:

```bash
docker compose -f docker-compose.dev.yml down -v
docker volume rm digitize_pgdata_dev
./scripts/local_dev_setup.sh
```

- For migrations: use the repo's migration tooling (`scripts/run_migrations_local.sh`). If you modify migration scripts, run them against a disposable DB first.
- For large schema changes, create a backup before applying and verify migration idempotency.

Secrets & Vault
- For secrets normally stored in HashiCorp Vault, use environment-variable overrides for local development and mock values.
- Do not run `vault` with production tokens locally. Instead, use `VAULT_ADDR` pointing to a safe test instance or set `VAULT_TOKEN=` empty and use dev-mode behavior if available.

Frontend notes
- The frontend dev server mounts local files and runs `npm install` then `npm start` inside the `frontend` context.
- Set `REACT_APP_API_URL` (or equivalent) in `.env.dev` to `http://localhost:8000` to call the local backend.

Backend notes
- The backend is expected to expose health and readiness endpoints used by deployment runbooks. Ensure `GET /health` and `GET /api/v1/health/smoke` (or project-equivalent) are available.
- The compose file uses `uvicorn server:app` for a FastAPI-style server; adapt the command to your framework if different.

Testing & CI alignment
- Use the same migration commands locally as the CI pipeline to prevent drift.
- When a feature branch is ready, run the pipeline and use the generated artifact (image tag + digest) to promote to staging.

Security & safety precautions
- Never use production DB connection strings or Vault tokens locally.
- Rotate and revoke any credentials used in local experiments.
- Keep local dev ports consistent to avoid accidental cross-environment calls.

Recommended next steps
- Confirm `Dockerfile` for `api_mock` and `frontend` exist; if not, I can scaffold minimal ones.
- If you want, I can: (A) create Dockerfiles for backend/frontend, (B) wire a GitHub Actions workflow to build and publish dev images, or (C) test-run this local setup in the environment and report results.

Contact me which of the recommended next steps you want me to take.
