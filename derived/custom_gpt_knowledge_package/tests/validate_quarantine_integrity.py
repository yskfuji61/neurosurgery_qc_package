#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
QUARANTINE = ROOT / "manifest" / "knowledge_quarantine_register.csv"
CROSSWALK = ROOT / "manifest" / "knowledge_chunk_review_crosswalk.csv"
UPLOAD_MANIFEST = ROOT / "manifest" / "custom_gpt_upload_manifest.csv"

ALLOWED_QUARANTINE_STATUS = {"quarantined", "under_review", "cleared"}
ALLOWED_REVIEW_DISPOSITION = {
    "pending",
    "confirmed_red_flag",
    "false_positive",
    "mitigated",
}
JOINABLE_VALIDATORS = {"validate_unsafe_patterns.py"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def read_upload_targets() -> set[str]:
    rows = read_csv(UPLOAD_MANIFEST)
    return {
        row["file"]
        for row in rows
        if row.get("upload_to_custom_gpt", "").strip().lower() == "yes"
    }


def active_quarantine_targets(rows: list[dict[str, str]]) -> set[tuple[str, str]]:
    targets: set[tuple[str, str]] = set()
    for row in rows:
        if row.get("quarantine_status", "") == "cleared":
            continue
        targets.add(
            (
                row.get("knowledge_file", ""),
                row.get("section_id_or_chunk_id", ""),
            )
        )
    return targets


def validate_quarantine_rows(
    rows: list[dict[str, str]], upload_targets: set[str], findings: list[dict[str, str]]
) -> None:
    seen_ids: set[str] = set()
    for row in rows:
        finding_id = row.get("finding_id", "")
        knowledge_file = row.get("knowledge_file", "")
        source_validator = row.get("source_validator", "")
        severity = row.get("severity", "")
        finding_type = row.get("finding_type", "")
        quarantine_status = row.get("quarantine_status", "")
        blocking_reason = row.get("blocking_reason", "")
        review_disposition = row.get("review_disposition", "")
        evidence_link = row.get("evidence_link", "")
        cleared_by = row.get("cleared_by", "")
        cleared_date = row.get("cleared_date", "")

        if not finding_id:
            add_finding(findings, knowledge_file or "quarantine", "missing_finding_id", "")
        elif finding_id in seen_ids:
            add_finding(findings, finding_id, "duplicate_finding_id", "")
        else:
            seen_ids.add(finding_id)

        if knowledge_file not in upload_targets:
            add_finding(findings, finding_id or knowledge_file, "non_upload_target_quarantine_entry", knowledge_file)

        if not source_validator:
            add_finding(findings, finding_id or knowledge_file, "missing_source_validator", "")
        elif source_validator in JOINABLE_VALIDATORS and "::" not in finding_id:
            add_finding(findings, finding_id, "non_joinable_finding_id", source_validator)

        if severity not in {"RED", "YELLOW", "REVIEW_CONTEXT"}:
            add_finding(findings, finding_id or knowledge_file, "invalid_severity", severity)

        if not finding_type:
            add_finding(findings, finding_id or knowledge_file, "missing_finding_type", "")

        if quarantine_status not in ALLOWED_QUARANTINE_STATUS:
            add_finding(findings, finding_id or knowledge_file, "invalid_quarantine_status", quarantine_status)
            continue

        if review_disposition not in ALLOWED_REVIEW_DISPOSITION:
            add_finding(findings, finding_id or knowledge_file, "invalid_review_disposition", review_disposition)

        if quarantine_status == "quarantined" and not blocking_reason:
            add_finding(findings, finding_id or knowledge_file, "quarantined_without_blocking_reason", "")

        if quarantine_status == "cleared":
            if review_disposition not in {"false_positive", "mitigated"}:
                add_finding(findings, finding_id or knowledge_file, "cleared_without_disposition", review_disposition)
            if not evidence_link:
                add_finding(findings, finding_id or knowledge_file, "cleared_without_evidence_link", "")
            if not cleared_by:
                add_finding(findings, finding_id or knowledge_file, "cleared_without_reviewer", "")
            if not cleared_date:
                add_finding(findings, finding_id or knowledge_file, "cleared_without_date", "")
        else:
            if cleared_by or cleared_date:
                add_finding(findings, finding_id or knowledge_file, "non_cleared_with_clearance_metadata", "")


def validate_crosswalk_conflicts(
    quarantine_rows: list[dict[str, str]], crosswalk_rows: list[dict[str, str]], findings: list[dict[str, str]]
) -> None:
    active_targets = active_quarantine_targets(quarantine_rows)
    for row in crosswalk_rows:
        chunk_id = row.get("chunk_id", "")
        knowledge_file = row.get("knowledge_file", "")
        section_id = row.get("section_id", "")
        release_readiness = row.get("release_readiness", "")
        resolution_status = row.get("resolution_status", "")

        if release_readiness != "external_ready_candidate":
            continue

        if (knowledge_file, "") in active_targets:
            add_finding(findings, chunk_id, "external_candidate_conflicts_with_file_quarantine", knowledge_file)
            continue

        if (knowledge_file, chunk_id) in active_targets or (knowledge_file, section_id) in active_targets:
            add_finding(findings, chunk_id, "external_candidate_conflicts_with_section_quarantine", knowledge_file)

        if resolution_status == "quarantined_red_flag":
            add_finding(findings, chunk_id, "external_candidate_marked_quarantined", resolution_status)


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
    quarantine_rows = read_csv(QUARANTINE)
    upload_targets = read_upload_targets()
    crosswalk_rows = read_csv(CROSSWALK)

    validate_quarantine_rows(quarantine_rows, upload_targets, findings)
    validate_crosswalk_conflicts(quarantine_rows, crosswalk_rows, findings)

    if args.output:
        write_findings(args.output, findings)

    print(f"quarantine_integrity_findings={len(findings)}")
    print(f"quarantine_rows={len(quarantine_rows)}")
    print(f"quarantine_integrity_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())