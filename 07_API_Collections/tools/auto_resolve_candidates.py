#!/usr/bin/env python3
"""
Attempt to auto-resolve missing API IDs by matching endpoint paths.

Outputs: docs/07_API_Collections/tbd_candidate_mappings.csv
Columns: referencing_file,missing_id,match_path,candidate_id,candidate_file,confidence

This script does NOT edit docs; it only suggests candidate mappings.
"""
import re
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
MD_DIR = ROOT
OUT = ROOT / 'tbd_candidate_mappings.csv'
API_REF = re.compile(r'API-\d{2}-\d{3}')
PATH_REF = re.compile(r'(/api/[^\s|`"\)]+)')

# Build index of api ids defined in files and nearby paths
id_to_file = {}
file_texts = {}
for md in sorted(MD_DIR.glob('*.md')):
    text = md.read_text(encoding='utf-8')
    file_texts[md.name] = text
    for line in text.splitlines():
        for m in API_REF.findall(line):
            id_to_file.setdefault(m, set()).add(md.name)

# Find references and missing ones by checking if id exists
missing = []
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for ref in API_REF.findall(line):
            if ref not in id_to_file:
                missing.append((fname, i, ref, line.strip()))

candidates = []
for fname, lineno, missing_id, line in missing:
    # try extract an api path from the same line
    path_match = PATH_REF.search(line)
    match_path = path_match.group(1) if path_match else ''
    candidate_id = ''
    candidate_file = ''
    confidence = 'low'
    if match_path:
        # search other files for this path and any api ids on same or nearby lines
        for other_name, other_text in file_texts.items():
            if match_path in other_text:
                # find nearby api ids
                for j, other_line in enumerate(other_text.splitlines(), start=1):
                    if match_path in other_line:
                        ids = API_REF.findall(other_line)
                        if ids:
                            candidate_id = ids[0]
                            candidate_file = other_name
                            confidence = 'high'
                            break
                if candidate_id:
                    break
    candidates.append((fname, missing_id, match_path, candidate_id, candidate_file, confidence))

with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['referencing_file','missing_id','match_path','candidate_id','candidate_file','confidence'])
    w.writerows(candidates)

print(f'Wrote {len(candidates)} candidate mappings to {OUT}')
