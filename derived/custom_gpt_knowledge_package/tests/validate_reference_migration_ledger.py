#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = ROOT.parents[3]
REFERENCE_ROOT = ROOT.parents[2] / "neurosurgery_safe_rag_pmda_product_source_register_resolved"
MIGRATION_LEDGER = ROOT / "manifest" / "reference_migration_decision_ledger.csv"

REQUIRED_COLUMNS = {
    "reference_path",
    "file_class",
    "purpose",
    "target_decision",
    "target_path",
    "migration_mode",
    "reason",
    "upload_safe",
    "operator_side_only",
    "unresolved_needed",
    "quarantine_needed",
    "human_review_required",
    "facility_confirmation_required",
    "preview_evidence_required",
    "validator_or_gate",
    "status_after_this_slice",
}

ALLOWED_MIGRATION_MODES = {
    "direct_structural_port",
    "adapted_port",
    "operator_side_only_port",
    "no_port_keep_as_reference_only",
    "no_port_unresolved",
    "no_port_quarantine",
}

FLAG_COLUMNS = {
    "upload_safe",
    "operator_side_only",
    "unresolved_needed",
    "quarantine_needed",
    "human_review_required",
    "facility_confirmation_required",
    "preview_evidence_required",
}

OPERATOR_SIDE_TARGET_PREFIXES = (
    "README.md",
    "audit/",
    "derived/",
    "instructions/",
    "manifest/",
    "tests/",
)


def read_csv_with_fieldnames(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), reader.fieldnames or []


def reference_files() -> set[str]:
    return {
        path.relative_to(WORKSPACE_ROOT).as_posix()
        for path in REFERENCE_ROOT.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def split_targets(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def target_is_operator_side(target: str) -> bool:
    if not target or target == "-":
        return False
    if target.startswith("knowledge/"):
        return False
    return target.startswith(OPERATOR_SIDE_TARGET_PREFIXES) or not target.startswith("references/")


def validate_ledger(
    rows: list[dict[str, str]],
    fieldnames: list[str],
    actual_reference_files: set[str],
    findings: list[dict[str, str]],
) -> None:
    fieldname_set = set(fieldnames)
    missing_columns = sorted(REQUIRED_COLUMNS - fieldname_set)
    extra_required_check_blocked = bool(missing_columns)
    for column in missing_columns:
        add_finding(findings, "header", "missing_required_column", column)

    if extra_required_check_blocked:
        return

    paths = [row.get("reference_path", "") for row in rows]
    path_counts: dict[str, int] = {}
    for reference_path in paths:
        path_counts[reference_path] = path_counts.get(reference_path, 0) + 1

    ledger_paths = set(paths)
    missing_paths = sorted(actual_reference_files - ledger_paths)
    extra_paths = sorted(ledger_paths - actual_reference_files)
    duplicate_paths = sorted(path for path, count in path_counts.items() if count > 1)

    for reference_path in missing_paths:
        add_finding(findings, reference_path, "missing_reference_path", "")
    for reference_path in extra_paths:
        add_finding(findings, reference_path, "extra_reference_path", "")
    for reference_path in duplicate_paths:
        add_finding(findings, reference_path, "duplicate_reference_path", str(path_counts[reference_path]))

    for row in rows:
        reference_path = row.get("reference_path", "")
        item = reference_path or "blank_reference_path"

        for column in REQUIRED_COLUMNS:
            if not row.get(column, "").strip():
                add_finding(findings, item, "blank_required_cell", column)

        for column in FLAG_COLUMNS:
            flag = row.get(column, "").strip().lower()
            if flag not in {"yes", "no"}:
                add_finding(findings, item, "invalid_yes_no_flag", f"{column}={flag}")

        migration_mode = row.get("migration_mode", "")
        if migration_mode not in ALLOWED_MIGRATION_MODES:
            add_finding(findings, item, "invalid_migration_mode", migration_mode)

        if migration_mode == "no_port_unresolved" and row.get("unresolved_needed", "").strip().lower() != "yes":
            add_finding(findings, item, "no_port_unresolved_without_unresolved_flag", row.get("unresolved_needed", ""))

        if migration_mode == "no_port_quarantine" and row.get("quarantine_needed", "").strip().lower() != "yes":
            add_finding(findings, item, "no_port_quarantine_without_quarantine_flag", row.get("quarantine_needed", ""))

        upload_safe = row.get("upload_safe", "").strip().lower()
        operator_side_only = row.get("operator_side_only", "").strip().lower()
        if upload_safe == "yes" and operator_side_only == "yes":
            add_finding(findings, item, "upload_safe_marked_operator_side_only", "")

        if upload_safe == "yes":
            operator_targets = [target for target in split_targets(row.get("target_path", "")) if target_is_operator_side(target)]
            if operator_targets:
                add_finding(findings, item, "upload_safe_points_to_operator_side_target", ";".join(operator_targets))


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
    rows, fieldnames = read_csv_with_fieldnames(MIGRATION_LEDGER)
    actual_reference_files = reference_files()
    validate_ledger(rows, fieldnames, actual_reference_files, findings)

    if args.output:
        write_findings(args.output, findings)

    print(f"migration_ledger_findings={len(findings)}")
    print(f"migration_ledger_rows={len(rows)}")
    print(f"reference_file_count={len(actual_reference_files)}")
    print(f"migration_ledger_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())