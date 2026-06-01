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
PROMOTABLE_REVIEW_STATES = {
    "source_verified",
    "human_reviewed_preliminary",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_preview_records() -> list[dict[str, str]]:
    text = PREVIEW_LEDGER.read_text(encoding="utf-8")
    blocks = re.split(r"^## Review Record ", text, flags=re.MULTILINE)
    records: list[dict[str, str]] = []
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
        records.append(values)
    return records


def active_quarantine_targets() -> set[tuple[str, str]]:
    if not QUARANTINE.exists():
        return set()
    return {
        (row.get("knowledge_file", ""), row.get("section_id_or_chunk_id", ""))
        for row in read_csv(QUARANTINE)
        if row.get("quarantine_status", "") != "cleared"
    }


def split_related_files(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def report_rows() -> list[dict[str, str]]:
    crosswalk_rows = read_csv(CROSSWALK)
    quarantine_targets = active_quarantine_targets()
    rows: list[dict[str, str]] = []

    for record in parse_preview_records():
        if record.get("review_status", "") != "approved":
            continue

        related_files = set(split_related_files(record.get("related_knowledge_files", "")))
        for row in crosswalk_rows:
            knowledge_file = row.get("knowledge_file", "")
            if knowledge_file not in related_files:
                continue

            chunk_id = row.get("chunk_id", "")
            section_id = row.get("section_id", "")
            blockers = row.get("blockers", "")
            review_state = row.get("review_state", "")
            reviewer_role = row.get("reviewer_role", "")
            evidence_link = row.get("review_evidence_link", "")
            readiness = row.get("release_readiness", "")
            resolution = row.get("resolution_status", "")

            reasons: list[str] = []
            if review_state not in PROMOTABLE_REVIEW_STATES:
                reasons.append("review_state_not_promotable")
            if evidence_link and evidence_link != record.get("review_record_id", ""):
                reasons.append("different_review_evidence_already_linked")
            if blockers and blockers != "preview_review_pending":
                reasons.append("non_preview_blockers_present")
            if readiness == "external_ready_candidate":
                reasons.append("already_external_ready_candidate")
            if resolution == "quarantined_red_flag":
                reasons.append("resolution_is_quarantined")
            if resolution not in {"pending_preview_review", "cleared_for_external_review", "quarantined_red_flag"}:
                reasons.append("resolution_status_not_promotable")
            if (knowledge_file, "") in quarantine_targets or (knowledge_file, chunk_id) in quarantine_targets or (knowledge_file, section_id) in quarantine_targets:
                reasons.append("active_quarantine_present")

            rows.append(
                {
                    "review_record_id": record.get("review_record_id", ""),
                    "knowledge_file": knowledge_file,
                    "chunk_id": chunk_id,
                    "section_id": section_id,
                    "current_review_state": review_state,
                    "current_reviewer_role": reviewer_role,
                    "current_release_readiness": readiness,
                    "current_resolution_status": resolution,
                    "promotion_candidate": "yes" if not reasons else "no",
                    "blocking_reasons": ";".join(reasons),
                }
            )
    return rows


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "review_record_id",
                "knowledge_file",
                "chunk_id",
                "section_id",
                "current_review_state",
                "current_reviewer_role",
                "current_release_readiness",
                "current_resolution_status",
                "promotion_candidate",
                "blocking_reasons",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    rows = report_rows()
    if args.output:
        write_rows(args.output, rows)

    candidate_count = sum(1 for row in rows if row["promotion_candidate"] == "yes")
    approved_record_count = len({row["review_record_id"] for row in rows})
    print(f"approved_preview_records={approved_record_count}")
    print(f"promotion_candidate_rows={candidate_count}")
    print(f"promotion_report_rows={len(rows)}")
    for row in rows:
        print(
            ",".join(
                [
                    row["review_record_id"],
                    row["knowledge_file"],
                    row["chunk_id"],
                    row["promotion_candidate"],
                    row["blocking_reasons"].replace(",", " "),
                ]
            )
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())