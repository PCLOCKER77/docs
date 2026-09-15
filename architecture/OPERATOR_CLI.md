# Operator CLI (Phase-1)

This is the **Phase-1 operator path**. It is not an HTTP API and is not part of
the 222 numbered registry.

Authentication HTTP remains unchanged: RS256 access JWT, 15-minute access
token, refresh through the `digitize_refresh` Secure + HttpOnly cookie.

Passwords never appear in HTTP responses, logs, or CLI success output.

## Bootstrap Platform Admin

Create one or more Platform Admin accounts:

```bash
poetry run python -m app.cli bootstrap-platform-admin \
  --login-identifier platform.operator
```

Rules:

* `user_type = PLATFORM_ADMIN`
* `organization_id = NULL`
* Duplicate `login_identifier` is rejected
* The first Platform Admin does not require extra confirmation
* Creating an additional Platform Admin requires `--confirm-additional`
* Production and staging also require `--confirm-production` /
  `--confirm-staging`
* The last active Platform Admin cannot be suspended or deactivated

There is **no** HTTP Platform Admin-management API in this phase.

## First credential establishment

Set the first password for a staff account or Platform Admin:

```bash
poetry run python -m app.cli set-staff-password \
  --login-identifier org.admin@example.test
```

Rules:

* Uses the existing Argon2id + pepper hashing pipeline
* Uses the existing password policy
* Password is prompted twice and is never printed
* Deactivated accounts are rejected
* Notification delivery is **not** implemented here; API-10 will own it later
