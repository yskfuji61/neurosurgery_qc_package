#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "audit" / "japanese_expression_risk_ledger.csv"
REQUIRED = {
    "file_path",
    "line_or_section",
    "original_expression",
    "risk_type",
    "priority",
    "human_review_required",
    "status",
}
ALLOWED_STATUS = {
    "NEEDS_REVIEW",
    "HUMAN_REVIEW_REQUIRED",
    "REVIEWED",
    "DEFERRED",
    "FALSE_POSITIVE",
    "APPLIED_AFTER_HUMAN_REVIEW",
    "REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW",
    "PARTIALLY_APPLIED_AFTER_HUMAN_REVIEW",
    "DEFERRED_HUMAN_REVIEW_REQUIRED",
    "REJECTED_CLINICAL_MEANING_RISK",
    "KEPT_AS_BOUNDARY_EXPRESSION_AFTER_REVIEW",
}


def main():
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8-sig", newline="")))
    findings = []
    missing = REQUIRED - set(rows[0].keys() if rows else [])
    for col in sorted(missing):
        findings.append(("header", "missing_required_column", col))
    high_human = 0
    for i, row in enumerate(rows, start=2):
        status = row.get("status", "")
        if status not in ALLOWED_STATUS:
            findings.append((i, "invalid_status", status))
        if row.get("priority") == "high" and row.get("human_review_required") == "yes":
            high_human += 1
            if not row.get("original_expression"):
                findings.append((i, "empty_expression_for_high_human_review", ""))
    if high_human == 0:
        findings.append(("ledger", "missing_high_priority_human_review_rows", ""))
    print(f"japanese_expression_ledger_findings={len(findings)}")
    for item in findings:
        print(",".join(map(str, item)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
