**Title:** CTO assignment — resolve remaining TBD source mappings

- **Owner:** CTO / Cofounder
- **Files:** docs/07_API_Collections (entire collection)
- **Attachments:** [missing_api_ids_cto.csv](docs/07_API_Collections/missing_api_ids_cto.csv), [missing_api_ids_cto_summary.csv](docs/07_API_Collections/missing_api_ids_cto_summary.csv), [tbd_resolutions_cto.csv](docs/07_API_Collections/tbd_resolutions_cto.csv), [tbd_candidate_suggestions_low_confidence.csv](docs/07_API_Collections/tbd_candidate_suggestions_low_confidence.csv)

Task:

1. Review the `missing_api_ids_cto_summary.csv` to see the 219 unique missing API IDs and their referencing file locations.
2. For each missing ID, either:
   - Add an authoritative definition to the appropriate API document (a heading or definition line starting with the `API-XX-YYY` token), or
   - Update `docs/07_API_Collections/tbd_resolutions_cto.csv` with a `new_snippet` replacement specifying the authoritative mapping or `Not Applicable — reason`.
3. Re-run the exporter and link-check scripts to validate: `python3 docs/07_API_Collections/tools/export_tbd.py` and `python3 docs/07_API_Collections/tools/link_check.py`.

Notes:

- A low-confidence suggestion file was generated; entries are explicitly flagged and must be verified before acceptance.
- Replacements applied so far used CTO placeholders; real authoritative IDs should replace them before documentation freeze.

Please update `tbd_resolutions_cto.csv` or the individual documents and notify me to re-run the validation scripts.
