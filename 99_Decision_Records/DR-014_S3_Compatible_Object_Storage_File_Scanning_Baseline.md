# DR-014 S3-Compatible Object Storage and File Scanning Baseline

> Decision record for object storage and uploaded-file scanning.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-014 |
| Document Name | S3-Compatible Object Storage and File Scanning Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Architecture Governance / Security / Backend Engineering |
| Reviewers | Product, Backend Engineering, Integration, Security, DevOps, Operations, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Digitize shall use S3-compatible object storage for uploaded and generated files, with ClamAV-based malware scanning as the initial file-scanning baseline.

The implementation may use AWS S3, MinIO, or another S3-compatible service depending on environment and provider strategy.

---

# 2. Context

Digitize needs storage for customer documents, support attachments, report exports, generated files, provider artifacts, and operational evidence.

API and Integration documents previously identified file storage and scanning as unresolved source mappings.

---

# 3. Decision

Digitize shall use:

- S3-compatible object storage for files.
- Metadata records in PostgreSQL for ownership, tenant scope, lifecycle, audit, and access control.
- Pre-signed upload or download URLs only where approved by API and Security.
- ClamAV-based scanning for uploaded files in the initial baseline.
- Quarantine state for files that are pending scan, failed scan, or flagged as unsafe.
- Tenant-scoped access checks before file metadata or file access is granted.

Raw files shall not be stored directly in PostgreSQL unless an explicit exception is approved.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| S3-compatible object storage + ClamAV | Provider-flexible object storage with concrete scanning baseline | Accepted |
| PostgreSQL byte storage | Store files in database | Rejected for general file storage due to size, backup, and performance concerns |
| Local filesystem storage | Store files on application nodes | Rejected for production because containerized workloads are ephemeral |
| Provider-specific object storage only | Use one cloud provider directly | Deferred until provider strategy is approved |

---

# 5. Rationale

S3-compatible storage is widely supported and works across managed cloud and self-hosted environments.

Keeping file metadata in PostgreSQL preserves tenant ownership, lifecycle, auditability, and traceability while object storage handles binary content.

ClamAV provides a concrete initial scanning baseline that can later be replaced or supplemented by a managed scanning service.

---

# 6. Consequences

## Positive Consequences

- File storage ambiguity is removed.
- API and Integration documents can define concrete file behavior.
- Tenant access and auditability remain database-backed.
- Deployment can provision object storage and scanner workloads.

## Tradeoffs

- S3-compatible behavior must be tested across selected environments.
- ClamAV signatures and scanner capacity must be operationally managed.

## Risks

- Pre-signed URL misuse may expose files if TTLs and permissions are weak.
- Scanner outage may delay file availability.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `07_API_Collections/API-02_Organization_Facility_Site_Collection.md` | File handling can reference object storage baseline |
| `07_API_Collections/API-04_Customer_Management_Collection.md` | Customer document upload/download behavior can be resolved |
| `08_Integration_Contracts/IC-06_File_Storage_Integration_Contract.md` | Uses S3-compatible storage and ClamAV scanning |
| `10_Backend_Engineering/BE-00_Backend_Engineering_Standards.md` | Object storage baseline is concrete |
| `11_Deployment/DEP-02_Infrastructure_Deployment_Architecture.md` | Includes object storage and scanner runtime dependencies |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Object storage baseline | Architecture Governance / DevOps |
| File API behavior | Backend Engineering / API |
| File security and scanning | Security / Backend Engineering |
| Storage operations | DevOps / Operations |
| Future provider changes | Architecture Governance |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current file storage and scanning baseline.

It may be frozen after API, Integration, Backend, Deployment, Security, and Operations documents align with storage and scanning behavior.
