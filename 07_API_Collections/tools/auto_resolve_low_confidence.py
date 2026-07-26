#!/usr/bin/env python3
"""
Generate low-confidence candidate suggestions for missing API IDs.
Outputs: docs/07_API_Collections/tbd_candidate_suggestions_low_confidence.csv

Algorithm (relaxed):
- Treat a line as a definition if an API ID appears on a line that also contains HTTP method (GET/POST/PUT/DELETE), a path (/api/), or starts with the ID.
- Missing IDs: API IDs referenced where not considered defined.
- Candidate suggestions:
  - nearest_id_same_prefix: defined ID in same API-XX with minimal numeric distance (confidence=low)
  - token_overlap_candidate: defined ID whose definition line shares tokens with referencing line (confidence=very_low)

These are low-confidence suggestions for manual review; do NOT auto-apply without owner approval.
"""
import re
from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
MD_DIR = ROOT / '07_API_Collections'
OUT = MD_DIR / 'tbd_candidate_suggestions_low_confidence.csv'
API_REF = re.compile(r'API-\d{2}-\d{3}')
PATH_REF = re.compile(r'(/api/[^\s|`"\)]+)')
METHOD_RE = re.compile(r"\b(GET|POST|PUT|DELETE|PATCH|HEAD)\b")
WORD = re.compile(r"[a-zA-Z]{4,}")

# Read files
file_texts = {}
for md in sorted(MD_DIR.glob('*.md')):
    file_texts[md.name] = md.read_text(encoding='utf-8')

# Collect definitions: id -> (file, line, line_text)
definitions = defaultdict(list)
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for m in API_REF.findall(line):
            if METHOD_RE.search(line) or PATH_REF.search(line) or line.strip().startswith(m) or 'Endpoint' in line or 'Path' in line:
                definitions[m].append((fname, i, line.strip()))

# Find referenced ids and where
references = []
for fname, text in file_texts.items():
    for i, line in enumerate(text.splitlines(), start=1):
        for m in API_REF.findall(line):
            references.append((fname, i, m, line.strip()))

# Missing = referenced ids not in definitions
missing = [(f,i,m,ln) for (f,i,m,ln) in references if m not in definitions]

# Prepare list of defined ids for prefix lookup
defined_ids = sorted(definitions.keys())
ids_by_prefix = defaultdict(list)
for idd in defined_ids:
    pref = idd[:6]
    ids_by_prefix[pref].append(idd)

# Tokenize definition lines for token overlap
def_tokens = {}
for idd, defs in definitions.items():
    # use first definition line
    _,_,ln = defs[0]
    def_tokens[idd] = set(w.lower() for w in WORD.findall(ln))

rows = []
for fname, lineno, missing_id, line in missing:
    path_match = PATH_REF.search(line)
    match_path = path_match.group(1) if path_match else ''
    # candidate 1: nearest id in same prefix
    prefix = missing_id[:6]
    cand1 = ''
    conf1 = ''
    if ids_by_prefix.get(prefix):
        try:
            target_num = int(missing_id.split('-')[-1])
            cand = min(ids_by_prefix[prefix], key=lambda x: abs(int(x.split('-')[-1]) - target_num))
            cand1 = cand
            conf1 = 'low'
        except Exception:
            cand1 = ids_by_prefix[prefix][0]
            conf1 = 'low'
    # candidate 2: token overlap
    words = set(w.lower() for w in WORD.findall(line))
    best = ('',0)
    for idd, tokens in def_tokens.items():
        score = len(words & tokens)
        if score > best[1]:
            best = (idd, score)
    cand2 = ''
    conf2 = ''
    if best[1] > 0:
        cand2 = best[0]
        conf2 = 'very_low'
    # record row
    rows.append((missing_id, fname, lineno, match_path, cand1, conf1, cand2, conf2))

with open(OUT, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['missing_id','referencing_file','line','match_path','candidate_nearest_same_prefix','confidence1','candidate_token_overlap','confidence2'])
    w.writerows(rows)

print(f'Wrote {len(rows)} low-confidence suggestions to {OUT}')
