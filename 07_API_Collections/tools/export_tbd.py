#!/usr/bin/env python3
"""
Extract all `[[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md) — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` occurrences into a CSV.

Usage:
    python3 docs/07_API_Collections/tools/export_tbd.py > docs/07_API_Collections/tbd_report_raw.csv

Outputs CSV columns: file,line,snippet
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2] / '07_API_Collections'
OUT = ROOT / 'tbd_report_raw.csv'
keyword = '[[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md) — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)'
rows = []
for md in sorted(ROOT.glob('*.md')):
    path = ROOT / md.name
    text = path.read_text(encoding='utf-8').splitlines()
    for i, line in enumerate(text, start=1):
        if keyword in line:
            rows.append((str(md.name), i, line.strip()))

with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['file','line','snippet'])
    w.writerows(rows)
print(f'Wrote {len(rows)} rows to {OUT}')
