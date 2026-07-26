#!/usr/bin/env python3
"""
Apply owner-provided TBD resolutions from CSV.
CSV columns: file,old_snippet,new_snippet
The script replaces the first occurrence of old_snippet in the specified file with new_snippet.

Run from repo root:
    python3 docs/07_API_Collections/tools/apply_tbd_resolutions.py docs/07_API_Collections/tbd_resolutions.csv

Produces a backup copy with `.bak` suffix for each file modified.
"""
import csv
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print('Usage: python3 apply_tbd_resolutions.py path/to/tbd_resolutions.csv')
    sys.exit(2)

csv_path = Path(sys.argv[1])
if not csv_path.exists():
    print('CSV not found:', csv_path)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2] / '07_API_Collections'

with open(csv_path, newline='', encoding='utf-8') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        file = row['file'].strip()
        old = row['old_snippet']
        new = row['new_snippet']
        p = ROOT / file
        if not p.exists():
            print('File not found:', p)
            continue
        text = p.read_text(encoding='utf-8')
        if old not in text:
            print(f'Old snippet not found in {file}: {old[:60]}...')
            continue
        backup = p.with_suffix(p.suffix + '.bak')
        backup.write_text(text, encoding='utf-8')
        new_text = text.replace(old, new, 1)
        p.write_text(new_text, encoding='utf-8')
        print(f'Applied resolution in {file} -> replaced first occurrence of snippet.')

print('Done applying resolutions.')
