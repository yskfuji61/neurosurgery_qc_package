#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "audit" / "abbreviation_first_use_review_ledger.csv"
REQUIRED_ABBREVIATIONS = {
    "DOAC", "VKA", "ICH", "TBI", "aSAH", "EVD", "ICP", "SCU", "ICU", "EVT",
    "CDS", "RAG", "PMDA", "MHLW", "RMP", "TDM", "PT-INR", "aPTT", "SCr",
    "CrCl", "eGFR", "DAPT", "VTE", "CNS", "CSF", "IIH", "ITB", "DBS", "DI",
    "GL", "SOP",
}


def main():
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8-sig", newline="")))
    findings = []
    seen = {row.get("abbreviation") for row in rows}
    for abbr in sorted(REQUIRED_ABBREVIATIONS - seen):
        findings.append((abbr, "missing_required_abbreviation", ""))
    for i, row in enumerate(rows, start=2):
        if not row.get("recommended_first_use"):
            findings.append((i, "missing_recommended_first_use", row.get("abbreviation", "")))
        if row.get("needs_definition") == "yes" and row.get("human_review_required") not in {"yes", "no"}:
            findings.append((i, "invalid_human_review_required", row.get("human_review_required", "")))
    print(f"abbreviation_first_use_ledger_findings={len(findings)}")
    for item in findings:
        print(",".join(map(str, item)))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
