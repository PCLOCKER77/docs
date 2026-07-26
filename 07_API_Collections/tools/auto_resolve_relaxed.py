#!/usr/bin/env python3
"""
Relaxed auto-resolve candidate finder for missing API IDs.
- Uses path similarity, API document prefix matching, and token overlap to suggest candidates.
- Produces docs/07_API_Collections/tbd_candidate_mappings_relaxed.csv

Confidence levels: high (path+id), medium (path match), low (prefix or token overlap)
"""
import re
from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
MD_DIR = ROOT
OUT = ROOT / 'tbd_candidate_mappings_relaxed.csv'
API_REF = re.compile(r'API-\d{2}-\d{3}')
PATH_REF = re.compile(r'(/api/[^\s|`"\)]+)')
WORD = re.compile(r"[a-zA-Z]{4,}")

# Load files
file_texts = {}
for md in sorted(MD_DIR.glob('*.md')):
    file_texts[md.name] = md.read_text(encoding='utf-8')

# Index all defined API IDs and anchor lines
id_to_files = defaultdict(set)
file_id_lines = defaultdict(list)
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for m in API_REF.findall(line):
            id_to_files[m].add(fname)
            file_id_lines[fname].append((m, i, line.strip()))

# Find missing refs
missing = []
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for ref in API_REF.findall(line):
            if ref not in id_to_files:
                missing.append((fname, i, ref, line.strip()))

candidates = []
for fname, lineno, missing_id, line in missing:
    match_path = ''
    pathm = PATH_REF.search(line)
    if pathm:
        match_path = pathm.group(1)
    candidate_id = ''
    candidate_file = ''
    confidence = 'none'
    # 1) Path exact search in other files
    if match_path:
        for other, other_text in file_texts.items():
            if other == fname:
                continue
            if match_path in other_text:
                # find API IDs in vicinity (+/-5 lines)
                lines = other_text.splitlines()
                for idx, other_line in enumerate(lines, start=1):
                    if match_path in other_line:
                        # look nearby for API ids
                        start = max(0, idx-6)
                        end = min(len(lines), idx+5)
                        block = '\n'.join(lines[start:end])
                        ids = API_REF.findall(block)
                        if ids:
                            candidate_id = ids[0]
                            candidate_file = other
                            confidence = 'high'
                            break
                if candidate_id:
                    break
        if not candidate_id:
            # path exists in file but no nearby id; treat as medium candidate if any id in file
            for other, ids in file_id_lines.items():
                if any(match_path in ln for _,_,ln in ids):
                    candidate_id = ids[0][0]
                    candidate_file = other
                    confidence = 'medium'
                    break
    # 2) Prefix-based heuristic: use API-XX prefix to find defined ids in same prefix
    if not candidate_id:
        prefix = missing_id[:6]  # API-07
        possible = [id for id in id_to_files.keys() if id.startswith(prefix)]
        if possible:
            # choose smallest numeric distance
            try:
                target_num = int(missing_id.split('-')[-1])
                best = min(possible, key=lambda x: abs(int(x.split('-')[-1])-target_num))
                candidate_id = best
                candidate_file = next(iter(id_to_files[best]))
                confidence = 'low'
            except Exception:
                candidate_id = possible[0]
                candidate_file = next(iter(id_to_files[possible[0]]))
                confidence = 'low'
    # 3) Token overlap heuristic (fallback)
    if not candidate_id:
        words = set(w.lower() for w in WORD.findall(line))
        best_score = 0
        best_pair = (None, None)
        for other, text in file_texts.items():
            if other == fname:
                continue
            for id, i, other_line in file_id_lines.get(other, []):
                other_words = set(w.lower() for w in WORD.findall(other_line))
                score = len(words & other_words)
                if score > best_score:
                    best_score = score
                    best_pair = (id, other)
        if best_pair[0] and best_score>0:
            candidate_id, candidate_file = best_pair
            confidence = 'low'
    candidates.append((fname, lineno, missing_id, match_path, candidate_id, candidate_file, confidence))

with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['referencing_file','line','missing_id','match_path','candidate_id','candidate_file','confidence'])
    w.writerows(candidates)

print(f'Wrote {len(candidates)} candidate mappings to {OUT}')
