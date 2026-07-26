"""
Small utility to apply Status updates in IC documents based on a CSV of approvals.

Usage (run locally):
    python3 docs/08_Integration_Contracts/apply_status_from_approvals.py approvals.csv

`approvals.csv` format: DocumentID,Status,Approver,Date,Notes
Example:
    IC-01,Review Draft,Integration Architecture,2026-07-26,"All owners approved"

This script will update the `**Status:**` line in the target IC-XX markdown files.

Caution: Run in workspace root. This script makes in-place edits.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IC_DIR = ROOT / 'docs' / '08_Integration_Contracts'

def apply_status(document_id, new_status):
    fname = IC_DIR / f"{document_id}_*.md"
    # Find matching file
    files = list(IC_DIR.glob(f"{document_id}_*.md"))
    if not files:
        print(f"No file found for {document_id}")
        return
    file = files[0]
    text = file.read_text(encoding='utf-8')
    if '**Status:**' not in text:
        print(f"No Status field in {file}")
        return
    new_text = []
    for line in text.splitlines():
        if line.strip().startswith('**Status:**'):
            new_text.append(f"**Status:** {new_status}")
        else:
            new_text.append(line)
    file.write_text('\n'.join(new_text), encoding='utf-8')
    print(f"Updated {file} -> {new_status}")

def main(csv_path):
    with open(csv_path, newline='') as fh:
        reader = csv.reader(fh)
        for row in reader:
            if not row or row[0].strip().startswith('#'):
                continue
            document_id = row[0].strip()
            new_status = row[1].strip()
            apply_status(document_id, new_status)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 apply_status_from_approvals.py approvals.csv')
        sys.exit(2)
    main(sys.argv[1])
