#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent
DEFAULT_JSONL = DEFAULT_ROOT / "99_Exports" / "Unified_RAG" / "unified_safe_rag_seed.jsonl"
HIGH_RISK_VALUES = {"high", "very_high"}


def add_finding(findings: list[dict[str, str]], file_name: str, line_number: int, chunk_id: str, issue: str, detail: str) -> None:
    findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": issue, "detail": detail})


def non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(item, str) and item.strip() for item in value)


def validate_record(record: dict[str, Any], file_name: str, line_number: int, findings: list[dict[str, str]]) -> None:
    chunk_id = str(record.get("chunk_id", ""))
    risk = str(record.get("ai_misread_risk", "")).strip()
    if risk not in {"medium", "high", "very_high"}:
        add_finding(findings, file_name, line_number, chunk_id, "invalid_or_missing_ai_misread_risk", risk)
        return
    if risk not in HIGH_RISK_VALUES:
        return

    if not non_empty_list(record.get("not_to_interpret_as")):
        add_finding(findings, file_name, line_number, chunk_id, "missing_not_to_interpret_as", "high-risk chunks require explicit unsafe interpretations")
    if record.get("human_review_required") is not True:
        add_finding(findings, file_name, line_number, chunk_id, "human_review_required_not_true", str(record.get("human_review_required")))
    if record.get("external_primary_sources_required") is not True:
        add_finding(findings, file_name, line_number, chunk_id, "external_primary_sources_required_not_true", str(record.get("external_primary_sources_required")))
    if record.get("facility_specific_confirmation_required") is not True:
        add_finding(findings, file_name, line_number, chunk_id, "facility_specific_confirmation_required_not_true", str(record.get("facility_specific_confirmation_required")))
    if not non_empty_list(record.get("required_confirmation")):
        add_finding(findings, file_name, line_number, chunk_id, "missing_required_confirmation", "high-risk chunks require confirmation gates")


def validate_jsonl(path: Path) -> tuple[int, list[dict[str, str]]]:
    findings: list[dict[str, str]] = []
    records_checked = 0
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as error:
                add_finding(findings, path.name, line_number, "", "invalid_json", str(error))
                continue
            if not isinstance(record, dict):
                add_finding(findings, path.name, line_number, "", "record_not_object", "")
                continue
            records_checked += 1
            validate_record(record, path.name, line_number, findings)
    return records_checked, findings


def write_findings(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "line", "chunk_id", "issue", "detail"])
        writer.writeheader()
        writer.writerows(findings)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    records_checked, findings = validate_jsonl(args.jsonl.resolve())

    if args.output:
        write_findings(args.output, findings)

    print(f"knowledge_integrity_records_checked={records_checked}")
    print(f"knowledge_integrity_findings={len(findings)}")
    print(f"knowledge_integrity_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['file']},{finding['line']},{finding['chunk_id']},{finding['issue']},{finding['detail']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
