#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "manifest" / "knowledge_chunk_review_crosswalk.csv"
FACILITY_CONFIRMATION = ROOT / "manifest" / "facility_confirmation_status_ledger.csv"

REQUIRED_COLUMNS = {
    "chunk_id",
    "knowledge_file",
    "section_id",
    "facility_confirmation_scope",
    "facility_confirmation_status",
    "required_before_external_ready",
    "evidence_link",
    "blocker",
    "owner_role",
    "last_updated",
}

ALLOWED_FACILITY_CONFIRMATION_STATUS = {
    "pending_facility_review",
    "confirmed",
    "not_applicable",
    "blocked",
}


def read_csv_with_fieldnames(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), reader.fieldnames or []


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("chunk_id", ""), row.get("knowledge_file", ""))


def validate_facility_rows(
    facility_rows: list[dict[str, str]],
    fieldnames: list[str],
    crosswalk_rows: list[dict[str, str]],
    findings: list[dict[str, str]],
) -> None:
    fieldname_set = set(fieldnames)
    missing_columns = sorted(REQUIRED_COLUMNS - fieldname_set)
    if missing_columns:
        for column in missing_columns:
            add_finding(findings, "header", "missing_required_column", column)
        return

    crosswalk_keys = {row_key(row) for row in crosswalk_rows}
    facility_keys = [row_key(row) for row in facility_rows]
    facility_key_set = set(facility_keys)
    key_counts: dict[tuple[str, str], int] = {}
    for key in facility_keys:
        key_counts[key] = key_counts.get(key, 0) + 1

    for chunk_id, knowledge_file in sorted(crosswalk_keys - facility_key_set):
        add_finding(findings, chunk_id, "missing_facility_confirmation_row", knowledge_file)
    for chunk_id, knowledge_file in sorted(facility_key_set - crosswalk_keys):
        add_finding(findings, chunk_id, "extra_facility_confirmation_row", knowledge_file)
    for key, count in sorted(key_counts.items()):
        if count > 1:
            chunk_id, knowledge_file = key
            add_finding(findings, chunk_id, "duplicate_facility_confirmation_row", f"{knowledge_file}:{count}")

    crosswalk_by_key = {row_key(row): row for row in crosswalk_rows}
    for row in facility_rows:
        chunk_id = row.get("chunk_id", "")
        knowledge_file = row.get("knowledge_file", "")
        item = chunk_id or "blank_chunk_id"

        for column in REQUIRED_COLUMNS - {"evidence_link", "blocker"}:
            if not row.get(column, "").strip():
                add_finding(findings, item, "blank_required_cell", column)

        facility_status = row.get("facility_confirmation_status", "")
        required_before_external = row.get("required_before_external_ready", "").strip().lower()
        evidence_link = row.get("evidence_link", "").strip()
        blocker = row.get("blocker", "").strip()

        if facility_status not in ALLOWED_FACILITY_CONFIRMATION_STATUS:
            add_finding(findings, item, "invalid_facility_confirmation_status", facility_status)
        if required_before_external not in {"yes", "no"}:
            add_finding(findings, item, "invalid_facility_required_flag", required_before_external)

        if facility_status in {"pending_facility_review", "blocked"} and not blocker:
            add_finding(findings, item, "facility_confirmation_without_blocker", facility_status)
        if facility_status in {"confirmed", "not_applicable"} and not evidence_link and not blocker:
            add_finding(findings, item, "facility_clearance_without_evidence_or_reason", facility_status)

        crosswalk_row = crosswalk_by_key.get((chunk_id, knowledge_file))
        if not crosswalk_row:
            continue
        if crosswalk_row.get("section_id", "") != row.get("section_id", ""):
            add_finding(findings, item, "facility_section_id_mismatch", row.get("section_id", ""))
        if crosswalk_row.get("release_readiness", "") == "external_ready_candidate":
            if required_before_external == "yes" and facility_status not in {"confirmed", "not_applicable"}:
                add_finding(findings, item, "external_candidate_without_facility_clearance", facility_status)


def write_findings(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["item", "issue", "detail"])
        writer.writeheader()
        writer.writerows(findings)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    findings: list[dict[str, str]] = []
    facility_rows, fieldnames = read_csv_with_fieldnames(FACILITY_CONFIRMATION)
    crosswalk_rows, _ = read_csv_with_fieldnames(CROSSWALK)
    validate_facility_rows(facility_rows, fieldnames, crosswalk_rows, findings)

    if args.output:
        write_findings(args.output, findings)

    print(f"facility_confirmation_findings={len(findings)}")
    print(f"facility_confirmation_rows={len(facility_rows)}")
    print(f"crosswalk_rows={len(crosswalk_rows)}")
    print(f"facility_confirmation_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())