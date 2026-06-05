#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "audit" / "japanese_plain_language_rewrite_ledger.csv"
REQUIRED_TERMS = {
    "operator-side", "boundary export", "upload safe", "reference-only", "hold",
    "negative knowledge", "clinician-facing summary", "source corpus", "derived export",
    "migration ledger", "blind copy", "runtime fetch", "preview promotion", "shortcut",
    "workflow", "routine", "order set", "reversal", "de-escalation", "antibiogram",
    "high-risk", "must-have", "must-not-have", "pass/fail", "validation", "release ready",
}


def main():
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8-sig", newline="")))
    findings = []
    seen = {row.get("original_expression") for row in rows}
    for term in sorted(REQUIRED_TERMS - seen):
        findings.append((term, "missing_required_term", ""))
    for i, row in enumerate(rows, start=2):
        if not row.get("proposed_japanese_expression"):
            findings.append((i, "missing_proposed_japanese_expression", row.get("original_expression", "")))
        if row.get("clinical_meaning_change_risk") == "high" and row.get("auto_rewrite_allowed") == "yes":
            findings.append((i, "high_risk_marked_auto_rewrite", row.get("original_expression", "")))
    print(f"plain_language_rewrite_ledger_findings={len(findings)}")
    for item in findings:
        print(",".join(map(str, item)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
