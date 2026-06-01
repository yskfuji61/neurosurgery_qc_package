#!/usr/bin/env python3
from pathlib import Path
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_LEDGER = ROOT / "manifest" / "derived_export_candidate_ledger.csv"
PROVENANCE = ROOT / "manifest" / "summary_layer_provenance.csv"

REQUIRED_COLUMNS = {
    "chunk_id",
    "knowledge_file",
    "section_label",
    "source_traceability_present",
    "human_review_status_present",
    "export_candidate",
    "recorded_review_state",
    "blocking_reason",
    "required_next_evidence",
    "readiness_note",
}


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def yes_no(value: str) -> bool:
    return value.strip().lower() in {"yes", "no"}


def add_finding(findings, row_id: str, kind: str, detail: str = ""):
    findings.append((row_id, kind, detail))


def main() -> int:
    findings = []
    rows = read_csv(CANDIDATE_LEDGER)
    provenance_rows = read_csv(PROVENANCE)

    if rows:
        missing_columns = sorted(REQUIRED_COLUMNS - set(rows[0].keys()))
        for column in missing_columns:
            add_finding(findings, "header", "missing_required_column", column)

    provenance_chunks = {
        row["target_section_id"].strip()
        for row in provenance_rows
        if row.get("target_section_id", "").strip()
    }
    candidate_chunks = [row.get("chunk_id", "").strip() for row in rows]

    for chunk_id in sorted(provenance_chunks - set(candidate_chunks)):
        add_finding(findings, chunk_id, "missing_candidate_row_for_provenance_chunk")
    for chunk_id in sorted(set(candidate_chunks) - provenance_chunks):
        add_finding(findings, chunk_id, "candidate_row_without_provenance_chunk")

    seen = set()
    for row in rows:
        chunk_id = row.get("chunk_id", "").strip()
        if not chunk_id:
            add_finding(findings, "blank", "blank_chunk_id")
            continue
        if chunk_id in seen:
            add_finding(findings, chunk_id, "duplicate_chunk_id")
        seen.add(chunk_id)

        for column in ("source_traceability_present", "human_review_status_present", "export_candidate"):
            if not yes_no(row.get(column, "")):
                add_finding(findings, chunk_id, "invalid_yes_no", f"{column}={row.get(column, '')}")

        traceability = row.get("source_traceability_present", "").strip().lower()
        human_review = row.get("human_review_status_present", "").strip().lower()
        export_candidate = row.get("export_candidate", "").strip().lower()
        blocking_reason = row.get("blocking_reason", "").strip()

        if export_candidate == "yes" and (traceability != "yes" or human_review != "yes"):
            add_finding(findings, chunk_id, "export_candidate_without_required_evidence")
        if export_candidate == "no" and not blocking_reason:
            add_finding(findings, chunk_id, "non_candidate_without_blocking_reason")

    print(f"derived_export_candidate_findings={len(findings)}")
    print(f"derived_export_candidate_rows={len(rows)}")
    print(f"summary_layer_provenance_rows={len(provenance_rows)}")
    for row_id, kind, detail in findings:
        print(f"{row_id},{kind},{detail}")
    print(f"derived_export_candidate_gate={'FAIL' if findings else 'PASS'}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())