#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "manifest" / "knowledge_chunk_review_crosswalk.csv"
PREVIEW_LEDGER = ROOT / "tests" / "human_reviewed_preview_examples.md"

ALLOWED_REVIEW_STATES = {
    "source_verified",
    "human_reviewed_preliminary",
    "operationally_unconfirmed",
    "unresolved_pending_gate",
}
ALLOWED_PENDING_VALUES = {
    "not_run_yet",
    "to_be_recorded",
    "to_be_determined_after_review",
    "required_before_approval",
    "unassigned",
    "pending",
    "pending_preview_review",
    "to_be_determined",
}


def read_crosswalk() -> list[dict[str, str]]:
    with CROSSWALK.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_preview_records() -> dict[str, dict[str, str]]:
    text = PREVIEW_LEDGER.read_text(encoding="utf-8")
    blocks = re.split(r"^## Review Record ", text, flags=re.MULTILINE)
    records: dict[str, dict[str, str]] = {}
    for block in blocks[1:]:
        lines = block.splitlines()
        record_id = lines[0].strip()
        values: dict[str, str] = {"record_id": record_id}
        for line in lines[1:]:
            match = re.match(r"^\d+\.\s+([^:]+):\s*(.*)$", line)
            if not match:
                continue
            key = match.group(1).strip().lower().replace(" ", "_")
            values[key] = match.group(2).strip()
        records[record_id] = values
    return records


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def validate_preview_records(records: dict[str, dict[str, str]], findings: list[dict[str, str]]) -> None:
    for record_id, record in records.items():
        review_status = record.get("review_status", "")
        reviewer = record.get("reviewer", "")
        review_date = record.get("review_date", "")
        raw_output = record.get("raw_output", "")
        normalized = record.get("lightly_normalized_output", "")
        excerpt = record.get("approved_or_rejected_excerpt", "")
        model_identifier = record.get("model_identifier", "")
        preview_run_date = record.get("preview_run_date", "")

        if review_status == "pending":
            if reviewer != "unassigned":
                add_finding(findings, record_id, "pending_with_assigned_reviewer", reviewer)
            if review_date != "unassigned":
                add_finding(findings, record_id, "pending_with_review_date", review_date)
        elif review_status in {"approved", "rejected"}:
            required_fields = {
                "model_identifier": model_identifier,
                "preview_run_date": preview_run_date,
                "reviewer": reviewer,
                "review_date": review_date,
                "raw_output": raw_output,
                "lightly_normalized_output": normalized,
                "approved_or_rejected_excerpt": excerpt,
            }
            for field_name, value in required_fields.items():
                if not value or value in ALLOWED_PENDING_VALUES:
                    add_finding(findings, record_id, "reviewed_record_missing_field", field_name)
        else:
            add_finding(findings, record_id, "invalid_review_status", review_status)


def validate_crosswalk(rows: list[dict[str, str]], preview_records: dict[str, dict[str, str]], findings: list[dict[str, str]]) -> None:
    preview_ids = set(preview_records)
    for row in rows:
        chunk_id = row.get("chunk_id", "")
        state = row.get("review_state", "")
        reviewer_role = row.get("reviewer_role", "")
        evidence_link = row.get("review_evidence_link", "")
        blockers = row.get("blockers", "")

        if state not in ALLOWED_REVIEW_STATES:
            add_finding(findings, chunk_id, "invalid_review_state", state)
            continue

        if state == "human_reviewed_preliminary":
            if not evidence_link:
                add_finding(findings, chunk_id, "reviewed_state_without_evidence", "")
            if reviewer_role == "unassigned":
                add_finding(findings, chunk_id, "reviewed_state_without_reviewer_role", "")
        else:
            if evidence_link and evidence_link not in preview_ids:
                add_finding(findings, chunk_id, "unknown_review_evidence_link", evidence_link)

        if evidence_link:
            if evidence_link not in preview_ids:
                add_finding(findings, chunk_id, "missing_preview_record", evidence_link)
            else:
                linked_status = preview_records[evidence_link].get("review_status", "")
                if state == "human_reviewed_preliminary" and linked_status != "approved":
                    add_finding(findings, chunk_id, "reviewed_state_without_approved_record", evidence_link)

        if state == "source_verified" and not blockers:
            add_finding(findings, chunk_id, "source_verified_without_blocker", "")


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
    preview_records = parse_preview_records()
    validate_preview_records(preview_records, findings)
    validate_crosswalk(read_crosswalk(), preview_records, findings)

    if args.output:
        write_findings(args.output, findings)

    print(f"review_state_findings={len(findings)}")
    print(f"review_state_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())