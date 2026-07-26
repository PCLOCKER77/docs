#!/usr/bin/env python3
"""
Simple link / API-ID reference checker for docs/07_API_Collections.
- Finds `API-\d{2}-\d{3}` tokens and checks if they are defined in any file in the folder.

Usage:
    python3 docs/07_API_Collections/tools/link_check.py

Outputs missing references to stdout.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / '07_API_Collections'
API_REF = re.compile(r'API-\d{2}-\d{3}')

all_defs = set()
all_refs = []
for md in sorted(ROOT.glob('*.md')):
    text = md.read_text(encoding='utf-8')
    # consider endpoint lines like 'API-07-001' as definitions when present in code blocks or lists
    for m in API_REF.findall(text):
        all_refs.append((str(md.name), m))
    # definitions heuristic: headings or lines that start with an API- id
    for line in text.splitlines():
        if line.strip().startswith('API-'):
            for m in API_REF.findall(line):
                all_defs.add(m)

missing = []
for f, ref in all_refs:
    if ref not in all_defs:
        missing.append((f, ref))

if missing:
    print('Missing API ID references (file, missing_id):')
    for it in missing:
        print(it[0], it[1])
else:
    print('No missing API ID references found.')
