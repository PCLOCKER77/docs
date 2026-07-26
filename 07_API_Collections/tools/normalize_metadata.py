#!/usr/bin/env python3
"""
Normalize metadata in docs/07_API_Collections:
- Set `**Last Updated:**` to `2026-07-26` when it's free-text like 'July 2026'.
- Remove top `> **Status:**` banners when the document metadata `**Status:**` is `Design Draft` (to avoid mismatch with banners).

Run from repo root:
    python3 docs/07_API_Collections/tools/normalize_metadata.py

This script edits files in-place. Use git to review changes.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2] / '07_API_Collections'
PAT_LAST_UPDATED = re.compile(r"\*\*Last Updated:\*\*\s*.*", re.IGNORECASE)
BANNER_PREFIX = "> **Status:**"

for md in sorted(ROOT.glob('*.md')):
    path = ROOT / md.name
    text = path.read_text(encoding='utf-8')
    changed = False
    # Replace Last Updated lines containing 'July' -> standardized date
    def repl_last(m):
        nonlocal changed
        changed = True
        return '**Last Updated:** 2026-07-26'
    new_text = PAT_LAST_UPDATED.sub(repl_last, text)
    # If first non-empty line starts with banner and metadata Status is Design Draft, remove banner
    lines = new_text.splitlines()
    if lines:
        # find first non-empty
        for i, l in enumerate(lines[:3]):
            if l.strip():
                first_idx = i
                break
        else:
            first_idx = 0
        if lines[first_idx].strip().startswith(BANNER_PREFIX):
            # Check if file has '**Status:** Design Draft' later
            if '**Status:**' in new_text and 'Design Draft' in new_text.split('**Status:**')[-1].splitlines()[0]:
                # remove banner line
                del lines[first_idx]
                changed = True
        new_text = '\n'.join(lines)
    if changed:
        path.write_text(new_text, encoding='utf-8')
        print(f'Updated {path}')

print('Normalization complete.')
