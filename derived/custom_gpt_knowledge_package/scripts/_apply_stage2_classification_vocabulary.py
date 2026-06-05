#!/usr/bin/env python3
"""Stage 2: add classification_vocabulary column to operator-side ledgers (no promotion)."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest"

ALLOWED_VOCABULARY = {
    "direct_boundary_port",
    "adapted_boundary_port",
    "operator_side_only",
    "reference_only",
    "quarantine",
    "unresolved_do_not_export",
    "hold_as_reference_until_integrated_layer_exists",
}


def classify_migration_row(row: dict[str, str]) -> str:
    mode = row.get("migration_mode", "")
    path = row.get("reference_path", "")
    file_class = row.get("file_class", "")

    if mode == "no_port_quarantine":
        return "quarantine"
    if mode == "no_port_unresolved":
        return "unresolved_do_not_export"
    if mode == "operator_side_only_port":
        return "operator_side_only"
    if mode == "adapted_port":
        return "adapted_boundary_port"
    if mode == "direct_structural_port":
        return "direct_boundary_port"
    if mode == "no_port_keep_as_reference_only":
        if file_class == "drug_profile" or "/02_DRUG_PROFILES_SAFE_KNOWLEDGE/" in path:
            return "hold_as_reference_until_integrated_layer_exists"
        return "reference_only"
    return "reference_only"


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def patch_ledger() -> Counter[str]:
    path = MANIFEST / "reference_migration_decision_ledger.csv"
    rows, fields = read_csv(path)
    if "classification_vocabulary" not in fields:
        fields.append("classification_vocabulary")
    counts: Counter[str] = Counter()
    for row in rows:
        vocab = classify_migration_row(row)
        row["classification_vocabulary"] = vocab
        counts[vocab] += 1
    write_csv(path, fields, rows)
    return counts


def patch_csv_column(
    path: Path,
    default_vocab: str,
    per_row: dict[str, str] | None = None,
    key_field: str = "chunk_id",
) -> None:
    if not path.is_file():
        return
    rows, fields = read_csv(path)
    if "classification_vocabulary" not in fields:
        fields.append("classification_vocabulary")
    for row in rows:
        key = row.get(key_field, "")
        row["classification_vocabulary"] = (per_row or {}).get(key, default_vocab)
    write_csv(path, fields, rows)


def rebuild_integrated_summary(ledger_counts: Counter[str]) -> None:
    path = MANIFEST / "integrated_origin_reclassification_summary.csv"
    rows = [
        {
            "review_scope": "ledger_vocabulary_adapted_boundary_port",
            "migration_mode": "adapted_port",
            "row_count": str(ledger_counts["adapted_boundary_port"]),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "adapted_port maps to adapted_boundary_port; not auto export",
            "derived_export_implication": "does_not_auto_promote_to_derived_export",
            "evidence_status": "operator_review_required",
            "classification_vocabulary": "adapted_boundary_port",
        },
        {
            "review_scope": "ledger_vocabulary_operator_side_only",
            "migration_mode": "operator_side_only_port",
            "row_count": str(ledger_counts["operator_side_only"]),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "operator-side discipline only",
            "derived_export_implication": "operator_side_only_not_upload_target",
            "evidence_status": "operator_review_required",
            "classification_vocabulary": "operator_side_only",
        },
        {
            "review_scope": "ledger_vocabulary_unresolved_do_not_export",
            "migration_mode": "no_port_unresolved",
            "row_count": str(ledger_counts["unresolved_do_not_export"]),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "PMDA/facility/preview incomplete",
            "derived_export_implication": "not_eligible_for_derived_export",
            "evidence_status": "pending_external_evidence",
            "classification_vocabulary": "unresolved_do_not_export",
        },
        {
            "review_scope": "ledger_vocabulary_reference_only",
            "migration_mode": "no_port_keep_as_reference_only",
            "row_count": str(
                ledger_counts["reference_only"]
            ),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "non-profile reference registers/manifests",
            "derived_export_implication": "not_eligible_for_derived_export",
            "evidence_status": "kept_for_audit_context",
            "classification_vocabulary": "reference_only",
        },
        {
            "review_scope": "ledger_vocabulary_hold_until_integrated_layer",
            "migration_mode": "no_port_keep_as_reference_only",
            "row_count": str(ledger_counts["hold_as_reference_until_integrated_layer_exists"]),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "drug profiles await integrated layer",
            "derived_export_implication": "not_eligible_for_derived_export",
            "evidence_status": "hold_reference_only",
            "classification_vocabulary": "hold_as_reference_until_integrated_layer_exists",
        },
        {
            "review_scope": "ledger_vocabulary_quarantine",
            "migration_mode": "no_port_quarantine",
            "row_count": str(ledger_counts["quarantine"]),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "quarantine row must not be naturalized",
            "derived_export_implication": "not_eligible_for_derived_export",
            "evidence_status": "quarantine_review_required",
            "classification_vocabulary": "quarantine",
        },
        {
            "review_scope": "ledger_total_rows",
            "migration_mode": "all_modes",
            "row_count": str(sum(ledger_counts.values())),
            "source_basis": "reference_migration_decision_ledger.csv",
            "priority_reason": "557/557 coverage; not clinical approval",
            "derived_export_implication": "not_eligible_without_evidence",
            "evidence_status": "stage2_classification_hardened_20260605",
            "classification_vocabulary": "operator_side_only",
        },
        {
            "review_scope": "derived_knowledge_summary_chunks",
            "migration_mode": "n/a",
            "row_count": "18",
            "source_basis": "derived_export_candidate_ledger.csv",
            "priority_reason": "knowledge summary export_candidate remains no",
            "derived_export_implication": "export_candidate_no_until_review_evidence_exists",
            "evidence_status": "pending_preview_and_facility_evidence",
            "classification_vocabulary": "adapted_boundary_port",
        },
    ]
    fields = list(rows[0].keys())
    write_csv(path, fields, rows)


def main() -> None:
    counts = patch_ledger()
    patch_csv_column(MANIFEST / "knowledge_quarantine_register.csv", "quarantine", key_field="finding_id")
    patch_csv_column(
        MANIFEST / "facility_confirmation_status_ledger.csv",
        "adapted_boundary_port",
        key_field="chunk_id",
    )
    patch_csv_column(
        MANIFEST / "derived_export_candidate_ledger.csv",
        "adapted_boundary_port",
        key_field="chunk_id",
    )
    patch_csv_column(
        MANIFEST / "knowledge_chunk_review_crosswalk.csv",
        "adapted_boundary_port",
        key_field="chunk_id",
    )
    rebuild_integrated_summary(counts)
    print("stage2_classification_vocabulary_applied")
    for k, v in sorted(counts.items()):
        print(f"  {k}={v}")


if __name__ == "__main__":
    main()
