#!/usr/bin/env python3
"""
Find API-XX-YYY references that are not defined in any docs/07_API_Collections files,
write a per-file CSV and append an 'Outstanding Missing API IDs' section to each file.

Run from repo root:
    python3 docs/07_API_Collections/tools/find_and_annotate_missing_api_ids.py
"""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
MD_DIR = ROOT
API_REF = re.compile(r'API-\d{2}-\d{3}')
OUT_CSV = ROOT / 'missing_api_ids_per_file.csv'

# Read all files
file_texts = {}
for md in sorted(MD_DIR.glob('*.md')):
    file_texts[md.name] = md.read_text(encoding='utf-8')

# Collect definitions
defined_ids = set()
for fname, text in file_texts.items():
    for line in text.splitlines():
        for m in API_REF.findall(line):
            # Heuristic: if line starts with the id or it's in a heading/code block, treat as definition
            if line.strip().startswith(m) or line.strip().startswith('|') or line.strip().startswith('-') or 'Endpoint ID' in line:
                defined_ids.add(m)

# Find references that are not defined
missing_per_file = defaultdict(set)
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for m in API_REF.findall(line):
            if m not in defined_ids:
                missing_per_file[fname].add(m)

# Write CSV
with open(OUT_CSV, 'w', encoding='utf-8') as fh:
    fh.write('file,missing_ids\n')
    for f, ids in missing_per_file.items():
        fh.write(f'{f},"{";".join(sorted(ids))}"\n')
print(f'Wrote {OUT_CSV} with {len(missing_per_file)} files containing missing ids')

# Append section to files
MARKER = '<!-- MISSING_API_IDS_SECTION -->'
for f, ids in missing_per_file.items():
    path = MD_DIR / f
    text = path.read_text(encoding='utf-8')
    if MARKER in text:
        # replace existing section
        before, sep, after = text.partition(MARKER)
        # find end marker
        end_marker = '<!-- MISSING_API_IDS_SECTION_END -->'
        if end_marker in after:
            _, _, after_rest = after.partition(end_marker)
            new_section = MARKER + '\n' + '\n'.join([
                '## Outstanding Missing API IDs',
                '',
                'The following API endpoint IDs are referenced in this document but no authoritative definition was found across `docs/07_API_Collections`. Owners should supply definitive endpoint definitions or confirm the IDs are not applicable.',
                '',
                '| Missing API ID | Notes |',
                '|---|---|',
            ] + [f'| {mid} | See docs/07_API_Collections/tbd_report_raw.csv and docs/07_API_Collections/api_chg_drafts/ |' for mid in sorted(ids)]) + '\n' + end_marker + '\n' + after_rest
            new_text = before + new_section
            path.write_text(new_text, encoding='utf-8')
            print(f'Updated section in {f}')
        else:
            # no end marker; append fresh
            new_section = '\n' + MARKER + '\n' + '\n'.join([
                '## Outstanding Missing API IDs',
                '',
                'The following API endpoint IDs are referenced in this document but no authoritative definition was found across `docs/07_API_Collections`. Owners should supply definitive endpoint definitions or confirm the IDs are not applicable.',
                '',
                '| Missing API ID | Notes |',
                '|---|---|',
            ] + [f'| {mid} | See docs/07_API_Collections/tbd_report_raw.csv and docs/07_API_Collections/api_chg_drafts/ |' for mid in sorted(ids)]) + '\n' + '<!-- MISSING_API_IDS_SECTION_END -->\n'
            path.write_text(text + new_section, encoding='utf-8')
            print(f'Appended section to {f}')
    else:
        # append new section
        new_section = '\n' + MARKER + '\n' + '\n'.join([
            '## Outstanding Missing API IDs',
            '',
            'The following API endpoint IDs are referenced in this document but no authoritative definition was found across `docs/07_API_Collections`. Owners should supply definitive endpoint definitions or confirm the IDs are not applicable.',
            '',
            '| Missing API ID | Notes |',
            '|---|---|',
        ] + [f'| {mid} | See docs/07_API_Collections/tbd_report_raw.csv and docs/07_API_Collections/api_chg_drafts/ |' for mid in sorted(ids)]) + '\n' + '<!-- MISSING_API_IDS_SECTION_END -->\n'
        path.write_text(text + new_section, encoding='utf-8')
        print(f'Appended section to {f}')

print('Annotation complete')
