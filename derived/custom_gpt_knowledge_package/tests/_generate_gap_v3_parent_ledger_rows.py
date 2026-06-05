#!/usr/bin/env python3
"""One-shot generator: append PARENT gap v3 rows to reference_migration_decision_ledger.csv."""
from __future__ import annotations

import csv
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[5]
PARENT_ROOT = (
    WORKSPACE
    / "references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603"
)
PARENT_PREFIX = "references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603"
LEDGER = Path(__file__).resolve().parents[1] / "manifest" / "reference_migration_decision_ledger.csv"
STATUS = "gap_v3_m0_ledger_recorded_pending_operator_review"
TARGET_LEDGER = "derived/custom_gpt_knowledge_package/manifest/reference_migration_decision_ledger.csv"


def classify(rel: str) -> dict[str, str]:
    if rel.startswith("00_START_HERE/"):
        return {
            "file_class": "governance_doc",
            "purpose": "gap_v3_package_positioning",
            "target_decision": "adapt_boundary_language_into_existing_docs",
            "target_path": "derived/custom_gpt_knowledge_package/README.md;derived/README.md;derived/gpt_drug_data_policy_expansion_runbook.md",
            "migration_mode": "adapted_port",
            "reason": "PARENT is PMDA-unresolved gap supplement; preserve non_guideline framing and UNRESOLVED_DO_NOT_GUESS | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "validate_upload_manifest.py;operator_review",
        }
    if rel.startswith("11_INTEGRATION_GUIDES/"):
        return {
            "file_class": "integration_guide",
            "purpose": "gap_v3_integration_rules",
            "target_decision": "adapt_integration_rules_into_runbook",
            "target_path": "derived/gpt_drug_data_policy_expansion_runbook.md",
            "migration_mode": "adapted_port",
            "reason": "V3 integration prohibitions (no PMDA guess, no procedural-as-standard) | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("03_CLASS_NOTES/"):
        return {
            "file_class": "class_note",
            "purpose": "domain_gap_class_boundary",
            "target_decision": "adapt_class_boundary_into_integrated_or_derived",
            "target_path": "neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/04_Drug_Classes/",
            "migration_mode": "adapted_port",
            "reason": "Class-level gap notes; boundary language only after integrated hub exists | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "yes",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("09_MANIFESTS/"):
        return {
            "file_class": "manifest",
            "purpose": "gap_v3_inventory_and_file_manifest",
            "target_decision": "keep_manifest_as_reference_inventory",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "V3_ALL/V3_RESIDUAL master CSVs are reference inventory; not facility-confirmed | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "yes",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "validate_reference_migration_ledger.py;operator_review",
        }
    if rel.startswith("01_SOURCE_REGISTERS/"):
        return {
            "file_class": "source_register",
            "purpose": "pmda_unresolved_source_register",
            "target_decision": "keep_pmda_unresolved_register_as_reference",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "pmda_product_source_register_v3_residual is UNRESOLVED_DO_NOT_GUESS input; do not promote rows to TARGET | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "yes",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "yes",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("02_DRUG_PROFILES_SAFE_KNOWLEDGE/"):
        return {
            "file_class": "drug_profile",
            "purpose": "safe_boundary_drug_profile",
            "target_decision": "hold_as_reference_until_target_integrated_drug_profile_layer_exists",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "PARENT drug profiles are general-name gap supplement without PMDA product resolution; mirror CHILD hold pattern | gap_v3_m0: no TARGET copy.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "yes",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "yes",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review;gpt_drug_data_policy_expansion_runbook.md",
        }
    if rel.startswith("08_VALIDATION_CHECKS/"):
        return {
            "file_class": "validation_artifact",
            "purpose": "gap_v3_rag_safety_validation",
            "target_decision": "keep_reference_validation_as_history",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "Reference-only safety tests; do not copy scripts into TARGET without operator review | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "validate_reference_migration_ledger.py",
        }
    if rel.startswith("scripts/"):
        return {
            "file_class": "reference_script",
            "purpose": "gap_v3_apply_script",
            "target_decision": "keep_reference_scripts_as_history",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "PARENT apply script stays in reference corpus | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("10_FINAL_REPORTS/"):
        return {
            "file_class": "audit_report",
            "purpose": "gap_v3_audit_closeout",
            "target_decision": "keep_audit_report_as_reference_history",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_keep_as_reference_only",
            "reason": "V3 audit report is reference history; not TARGET completion fact | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("12_RESEARCH_EVIDENCE/"):
        return {
            "file_class": "research_evidence",
            "purpose": "evidence_source_targets",
            "target_decision": "keep_evidence_targets_unresolved",
            "target_path": TARGET_LEDGER,
            "migration_mode": "no_port_unresolved",
            "reason": "Evidence targets require primary-source resolution before port | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "yes",
            "quarantine_needed": "no",
            "human_review_required": "yes",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    if rel.startswith("07_VSCODE_AGENT_INTEGRATION/"):
        return {
            "file_class": "agent_integration",
            "purpose": "vscode_agent_scaffold",
            "target_decision": "keep_agent_integration_as_operator_side",
            "target_path": "derived/README.md",
            "migration_mode": "operator_side_only_port",
            "reason": "Agent integration files are operator-side only | gap_v3_m0: ledger-only.",
            "upload_safe": "no",
            "operator_side_only": "yes",
            "unresolved_needed": "no",
            "quarantine_needed": "no",
            "human_review_required": "no",
            "facility_confirmation_required": "no",
            "preview_evidence_required": "no",
            "validator_or_gate": "operator_review",
        }
    return {
        "file_class": "reference_other",
        "purpose": "gap_v3_reference_file",
        "target_decision": "keep_as_reference_only",
        "target_path": TARGET_LEDGER,
        "migration_mode": "no_port_keep_as_reference_only",
        "reason": "Unclassified PARENT file; reference-only | gap_v3_m0: ledger-only.",
        "upload_safe": "no",
        "operator_side_only": "yes",
        "unresolved_needed": "no",
        "quarantine_needed": "no",
        "human_review_required": "yes",
        "facility_confirmation_required": "no",
        "preview_evidence_required": "no",
        "validator_or_gate": "operator_review",
    }


def main() -> None:
    parent_files = sorted(
        p.relative_to(PARENT_ROOT).as_posix()
        for p in PARENT_ROOT.rglob("*")
        if p.is_file() and p.name != ".DS_Store"
    )
    with LEDGER.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        existing = list(reader)

    existing_paths = {row["reference_path"] for row in existing}
    new_rows: list[dict[str, str]] = []
    for rel in parent_files:
        ref_path = f"{PARENT_PREFIX}/{rel}"
        if ref_path in existing_paths:
            continue
        row = classify(rel)
        row["reference_path"] = ref_path
        row["status_after_this_slice"] = STATUS
        new_rows.append(row)

    if not new_rows:
        print("no new rows to append")
        return

    with LEDGER.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing)
        writer.writerows(new_rows)

    print(f"appended={len(new_rows)} total={len(existing) + len(new_rows)}")


if __name__ == "__main__":
    main()
