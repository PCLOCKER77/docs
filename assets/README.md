# Documentation Assets

> Shared diagrams, images, and supporting visual assets for Digitize documentation.

---

# 1. Purpose

This folder stores shared documentation assets used by the Digitize documentation set.

Assets may include architecture diagrams, process diagrams, UI images, exported visuals, and supporting reference images.

---

# 2. Folder Structure

```text
assets/
├── README.md
├── Asset_Register.md
├── diagrams/
└── images/
```

---

# 3. Usage Rules

- Assets shall support documentation content and shall not replace source documentation.
- Diagrams should be stored in source-friendly formats where possible.
- Generated or exported images should have clear names.
- Sensitive infrastructure, credential, customer, or production data shall not be stored in this folder.
- Documents referencing assets should use relative paths.

---

# 4. Ownership

| Asset Type | Owner |
|---|---|
| Architecture diagrams | Architecture |
| Database diagrams | Database Engineering |
| API and integration diagrams | API / Integration |
| UI images | UI/UX Design |
| Deployment and operations diagrams | DevOps / Operations |

---

# 5. Summary

The assets folder supports documentation readability while keeping primary decisions, standards, and requirements in Markdown documents.
