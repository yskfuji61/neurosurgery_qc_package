#!/usr/bin/env python3
"""Validate Stage 2 classification_vocabulary on operator-side ledgers."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest"

ALLOWED = {
    "direct_boundary_port",
    "adapted_boundary_port",
    "operator_side_only",
    "reference_only",
    "quarantine",
    "unresolved_do_not_export",
    "hold_as_reference_until_integrated_layer_exists",
}

LEDGER_FILES = [
    MANIFEST / "reference_migration_decision_ledger.csv",
    MANIFEST / "knowledge_quarantine_register.csv",
    MANIFEST / "facility_confirmation_status_ledger.csv",
    MANIFEST / "derived_export_candidate_ledger.csv",
    MANIFEST / "knowledge_chunk_review_crosswalk.csv",
    MANIFEST / "integrated_origin_reclassification_summary.csv",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    findings: list[str] = []

    registry = MANIFEST / "classification_vocabulary_registry.md"
    if not registry.is_file():
        findings.append("missing:classification_vocabulary_registry.md")

    for path in LEDGER_FILES:
        if not path.is_file():
            findings.append(f"missing:{path.name}")
            continue
        rows = read_csv(path)
        if not rows:
            findings.append(f"empty:{path.name}")
            continue
        if "classification_vocabulary" not in rows[0]:
            findings.append(f"missing_column:classification_vocabulary:{path.name}")
            continue
        for i, row in enumerate(rows, start=2):
            vocab = row.get("classification_vocabulary", "").strip()
            if vocab not in ALLOWED:
                findings.append(f"invalid_vocab:{path.name}:line{i}:{vocab}")

    ledger = read_csv(MANIFEST / "reference_migration_decision_ledger.csv")
    # Must match validate_reference_migration_ledger.py --corpus all (CHILD + PARENT reference files).
    if len(ledger) != 598:
        findings.append(f"ledger_row_count:{len(ledger)}")

    export_rows = read_csv(MANIFEST / "derived_export_candidate_ledger.csv")
    for row in export_rows:
        if row.get("export_candidate", "").lower() == "yes":
            findings.append(f"export_candidate_yes:{row.get('chunk_id')}")

    quarantine = read_csv(MANIFEST / "knowledge_quarantine_register.csv")
    for row in quarantine:
        if row.get("quarantine_status", "").lower() == "cleared":
            findings.append(f"quarantine_cleared:{row.get('finding_id')}")
        if row.get("classification_vocabulary") != "quarantine":
            findings.append(f"quarantine_wrong_vocab:{row.get('finding_id')}")

    facility = read_csv(MANIFEST / "facility_confirmation_status_ledger.csv")
    for row in facility:
        if row.get("facility_confirmation_status", "").lower() == "confirmed":
            findings.append(f"facility_confirmed_without_evidence:{row.get('chunk_id')}")

    print(f"classification_vocabulary_findings={len(findings)}")
    print(f"classification_vocabulary_gate={'FAIL' if findings else 'PASS'}")
    for f in findings:
        print(f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
