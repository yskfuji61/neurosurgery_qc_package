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
UPLOAD_MANIFEST = ROOT / "manifest" / "custom_gpt_upload_manifest.csv"
QUARANTINE = ROOT / "manifest" / "knowledge_quarantine_register.csv"
FACILITY_CONFIRMATION = ROOT / "manifest" / "facility_confirmation_status_ledger.csv"

ALLOWED_RELEASE_READINESS = {
    "repo_local_only",
    "external_ready_candidate",
}
ALLOWED_RESOLUTION_STATUS = {
    "pending_preview_review",
    "human_review_pending",
    "quarantined_red_flag",
    "cleared_for_external_review",
}
ALLOWED_FACILITY_CONFIRMATION_STATUS = {
    "pending_facility_review",
    "confirmed",
    "not_applicable",
    "blocked",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
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


def read_upload_targets() -> set[str]:
    rows = read_csv(UPLOAD_MANIFEST)
    return {
        row["file"]
        for row in rows
        if row.get("upload_to_custom_gpt", "").strip().lower() == "yes"
    }


def read_active_quarantine_targets() -> set[tuple[str, str]]:
    rows = read_csv(QUARANTINE)
    return {
        (row.get("knowledge_file", ""), row.get("section_id_or_chunk_id", ""))
        for row in rows
        if row.get("quarantine_status", "") != "cleared"
    }


def read_facility_confirmation_rows() -> dict[tuple[str, str], dict[str, str]]:
    if not FACILITY_CONFIRMATION.exists():
        return {}
    return {
        (row.get("knowledge_file", ""), row.get("chunk_id", "")): row
        for row in read_csv(FACILITY_CONFIRMATION)
    }


def validate_release_rows(
    rows: list[dict[str, str]],
    preview_records: dict[str, dict[str, str]],
    upload_targets: set[str],
    quarantine_targets: set[tuple[str, str]],
    facility_confirmation_rows: dict[tuple[str, str], dict[str, str]],
    findings: list[dict[str, str]],
) -> None:
    for row in rows:
        chunk_id = row.get("chunk_id", "")
        knowledge_file = row.get("knowledge_file", "")
        review_state = row.get("review_state", "")
        reviewer_role = row.get("reviewer_role", "")
        evidence_link = row.get("review_evidence_link", "")
        blockers = row.get("blockers", "")
        release_readiness = row.get("release_readiness", "")
        resolution_status = row.get("resolution_status", "")
        facility_confirmation = facility_confirmation_rows.get((knowledge_file, chunk_id))

        if (knowledge_file, "") in quarantine_targets or (knowledge_file, chunk_id) in quarantine_targets or (knowledge_file, row.get("section_id", "")) in quarantine_targets:
            if release_readiness == "external_ready_candidate":
                add_finding(findings, chunk_id, "external_candidate_conflicts_with_quarantine", knowledge_file)

        if knowledge_file not in upload_targets:
            add_finding(findings, chunk_id, "non_upload_target_in_readiness_register", knowledge_file)

        if release_readiness not in ALLOWED_RELEASE_READINESS:
            add_finding(findings, chunk_id, "invalid_release_readiness", release_readiness)
            continue

        if resolution_status not in ALLOWED_RESOLUTION_STATUS:
            add_finding(findings, chunk_id, "invalid_resolution_status", resolution_status)
            continue

        if facility_confirmation is None:
            add_finding(findings, chunk_id, "missing_facility_confirmation_row", knowledge_file)
        else:
            facility_status = facility_confirmation.get("facility_confirmation_status", "")
            required_before_external = facility_confirmation.get("required_before_external_ready", "").strip().lower()
            facility_blocker = facility_confirmation.get("blocker", "")
            if facility_status not in ALLOWED_FACILITY_CONFIRMATION_STATUS:
                add_finding(findings, chunk_id, "invalid_facility_confirmation_status", facility_status)
            if required_before_external not in {"yes", "no"}:
                add_finding(findings, chunk_id, "invalid_facility_required_flag", required_before_external)
            if facility_status in {"pending_facility_review", "blocked"} and not facility_blocker:
                add_finding(findings, chunk_id, "facility_confirmation_without_blocker", facility_status)

        if resolution_status == "pending_preview_review" and "preview_review_pending" not in blockers:
            add_finding(findings, chunk_id, "pending_preview_without_blocker", blockers)

        if resolution_status == "quarantined_red_flag" and not blockers:
            add_finding(findings, chunk_id, "quarantined_without_blocker", "")

        if resolution_status == "cleared_for_external_review" and release_readiness != "external_ready_candidate":
            add_finding(findings, chunk_id, "cleared_status_without_external_candidate", release_readiness)

        if release_readiness == "external_ready_candidate":
            if facility_confirmation is None:
                add_finding(findings, chunk_id, "external_candidate_without_facility_confirmation_row", knowledge_file)
            else:
                facility_status = facility_confirmation.get("facility_confirmation_status", "")
                required_before_external = facility_confirmation.get("required_before_external_ready", "").strip().lower()
                if required_before_external == "yes" and facility_status not in {"confirmed", "not_applicable"}:
                    add_finding(findings, chunk_id, "external_candidate_without_facility_clearance", facility_status)
            if resolution_status != "cleared_for_external_review":
                add_finding(findings, chunk_id, "external_candidate_without_cleared_status", resolution_status)
            if review_state != "human_reviewed_preliminary":
                add_finding(findings, chunk_id, "external_candidate_without_reviewed_state", review_state)
            if reviewer_role == "unassigned":
                add_finding(findings, chunk_id, "external_candidate_without_reviewer_role", "")
            if not evidence_link:
                add_finding(findings, chunk_id, "external_candidate_without_evidence_link", "")
            if blockers:
                add_finding(findings, chunk_id, "external_candidate_with_blocker", blockers)
            if evidence_link:
                if evidence_link not in preview_records:
                    add_finding(findings, chunk_id, "external_candidate_unknown_evidence", evidence_link)
                elif preview_records[evidence_link].get("review_status", "") != "approved":
                    add_finding(findings, chunk_id, "external_candidate_without_approved_preview", evidence_link)
        elif resolution_status == "cleared_for_external_review":
            add_finding(findings, chunk_id, "repo_local_row_marked_cleared", resolution_status)


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
    upload_targets = read_upload_targets()
    quarantine_targets = read_active_quarantine_targets()
    facility_confirmation_rows = read_facility_confirmation_rows()
    rows = read_csv(CROSSWALK)
    validate_release_rows(rows, preview_records, upload_targets, quarantine_targets, facility_confirmation_rows, findings)

    if args.output:
        write_findings(args.output, findings)

    external_candidates = sum(
        1 for row in rows if row.get("release_readiness", "") == "external_ready_candidate"
    )
    print(f"release_readiness_findings={len(findings)}")
    print(f"external_ready_candidates={external_candidates}")
    print(f"release_readiness_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())