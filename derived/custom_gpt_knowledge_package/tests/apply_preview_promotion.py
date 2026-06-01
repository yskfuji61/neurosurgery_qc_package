#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PREVIEW_LEDGER = ROOT / "tests" / "human_reviewed_preview_examples.md"
CROSSWALK = ROOT / "manifest" / "knowledge_chunk_review_crosswalk.csv"
QUARANTINE = ROOT / "manifest" / "knowledge_quarantine_register.csv"

PENDING_VALUES = {
    "not_run_yet",
    "to_be_recorded",
    "to_be_determined_after_review",
    "required_before_approval",
    "unassigned",
    "pending",
    "pending_preview_review",
    "to_be_determined",
}
PROMOTABLE_REVIEW_STATES = {
    "source_verified",
    "human_reviewed_preliminary",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_preview_records() -> dict[str, dict[str, str]]:
    text = PREVIEW_LEDGER.read_text(encoding="utf-8")
    blocks = re.split(r"^## Review Record ", text, flags=re.MULTILINE)
    records: dict[str, dict[str, str]] = {}
    for block in blocks[1:]:
        lines = block.splitlines()
        record_id = lines[0].strip()
        values: dict[str, str] = {"review_record_id": record_id}
        for line in lines[1:]:
            match = re.match(r"^\d+\.\s+([^:]+):\s*(.*)$", line)
            if not match:
                continue
            key = match.group(1).strip().lower().replace(" ", "_")
            values[key] = match.group(2).strip()
        records[record_id] = values
    return records


def active_quarantine_targets() -> set[tuple[str, str]]:
    if not QUARANTINE.exists():
        return set()
    return {
        (row.get("knowledge_file", ""), row.get("section_id_or_chunk_id", ""))
        for row in read_csv(QUARANTINE)
        if row.get("quarantine_status", "") != "cleared"
    }


def split_related_files(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def preview_record_is_approved(record: dict[str, str]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if record.get("review_status", "") != "approved":
        reasons.append("record_not_approved")

    required_fields = {
        "model_identifier": record.get("model_identifier", ""),
        "preview_run_date": record.get("preview_run_date", ""),
        "reviewer": record.get("reviewer", ""),
        "review_date": record.get("review_date", ""),
        "raw_output": record.get("raw_output", ""),
        "lightly_normalized_output": record.get("lightly_normalized_output", ""),
        "approved_or_rejected_excerpt": record.get("approved_or_rejected_excerpt", ""),
    }
    for field_name, value in required_fields.items():
        if not value or value in PENDING_VALUES:
            reasons.append(f"missing_{field_name}")

    return (not reasons, reasons)


def evaluate_row(
    row: dict[str, str],
    record: dict[str, str],
    record_id: str,
    reviewer_role: str,
    quarantine_targets: set[tuple[str, str]],
) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    knowledge_file = row.get("knowledge_file", "")
    chunk_id = row.get("chunk_id", "")
    section_id = row.get("section_id", "")
    review_state = row.get("review_state", "")
    evidence_link = row.get("review_evidence_link", "")
    resolution_status = row.get("resolution_status", "")

    related_files = split_related_files(record.get("related_knowledge_files", ""))
    if knowledge_file not in related_files:
        reasons.append("record_not_linked_to_knowledge_file")

    if review_state not in PROMOTABLE_REVIEW_STATES:
        reasons.append("review_state_not_promotable")

    if reviewer_role == "unassigned":
        reasons.append("reviewer_role_unassigned")

    if evidence_link and evidence_link != record_id:
        reasons.append("different_review_evidence_already_linked")

    blockers = row.get("blockers", "")
    if blockers and blockers != "preview_review_pending":
        reasons.append("non_preview_blockers_present")

    if resolution_status not in {"pending_preview_review", "cleared_for_external_review"}:
        reasons.append("resolution_status_not_promotable")

    if (knowledge_file, "") in quarantine_targets or (knowledge_file, chunk_id) in quarantine_targets or (knowledge_file, section_id) in quarantine_targets:
        reasons.append("active_quarantine_present")

    if row.get("release_readiness", "") == "external_ready_candidate":
        reasons.append("already_external_ready_candidate")

    if row.get("resolution_status", "") == "quarantined_red_flag":
        reasons.append("resolution_is_quarantined")

    return (not reasons, reasons)


def promote_row(row: dict[str, str], record_id: str, reviewer_role: str) -> dict[str, str]:
    updated = dict(row)
    updated["review_state"] = "human_reviewed_preliminary"
    updated["reviewer_role"] = reviewer_role
    updated["review_evidence_link"] = record_id
    updated["blockers"] = ""
    updated["release_readiness"] = "external_ready_candidate"
    updated["resolution_status"] = "cleared_for_external_review"
    return updated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--record-id", required=True)
    parser.add_argument("--chunk-id", required=True)
    parser.add_argument("--reviewer-role", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    records = parse_preview_records()
    record = records.get(args.record_id)
    if not record:
        print("promotion_actions=0")
        print("promotion_gate=FAIL")
        print(f"missing_record={args.record_id}")
        return 1

    approved_ok, record_reasons = preview_record_is_approved(record)
    rows = read_csv(CROSSWALK)
    fieldnames = list(rows[0].keys()) if rows else []
    matching_index = next((index for index, row in enumerate(rows) if row.get("chunk_id", "") == args.chunk_id), None)

    if matching_index is None:
        print("promotion_actions=0")
        print("promotion_gate=FAIL")
        print(f"missing_chunk_id={args.chunk_id}")
        return 1

    row = rows[matching_index]
    quarantine_targets = active_quarantine_targets()
    row_ok, row_reasons = evaluate_row(row, record, args.record_id, args.reviewer_role, quarantine_targets)
    reasons = record_reasons + row_reasons

    if not approved_ok or not row_ok:
        print("promotion_actions=0")
        print("promotion_gate=PASS")
        print(f"promotion_blocked_for={args.chunk_id}")
        print("blocking_reasons=" + ";".join(reasons))
        return 0

    updated_row = promote_row(row, args.record_id, args.reviewer_role)
    if args.apply:
        rows[matching_index] = updated_row
        write_csv(CROSSWALK, rows, fieldnames)

    print("promotion_actions=1")
    print("promotion_gate=PASS")
    print(f"record_id={args.record_id}")
    print(f"chunk_id={args.chunk_id}")
    print(f"apply_mode={'yes' if args.apply else 'no'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())