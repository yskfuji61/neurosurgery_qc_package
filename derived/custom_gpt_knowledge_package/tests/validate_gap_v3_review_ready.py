#!/usr/bin/env python3
"""Validate Gap V3 review-ready artifacts; does not approve clinical export."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[3]
ARCHIVE = (
    WORKSPACE
    / "references/neurosurgery_qc_package/reference_archive"
    / "neurosurgery_gap_supplement_package_v3_full_residual_20260603"
)
INTEGRATED = (
    WORKSPACE
    / "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package"
    / "Integrated_Obsidian_Vault"
)
DERIVED = ROOT

EXPECTED_COLLISION_IDS = {
    "GAP-V3-COLLISION-NEURO-ONC-001",
    "GAP-V3-COLLISION-PITUITARY-001",
    "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001",
    "GAP-V3-COLLISION-CSF-IIH-001",
    "GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001",
    "GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001",
    "GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001",
}

ALLOWLIST_FORBIDDEN = [
    "02_DRUG_PROFILES_SAFE_KNOWLEDGE",
    "neuro_oncology/",
    "pituitary_endocrine/",
    "intraventricular",
    "chronic_post_stroke",
    "botulinum",
    "5-ala",
    "5_ala",
]

CHECKLIST_HEADING = "## Human / Facility Review Checklist"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def add(findings: list[str], msg: str) -> None:
    findings.append(msg)


def main() -> int:
    findings: list[str] = []

    matrix_path = ARCHIVE / "09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv"
    if not matrix_path.is_file():
        add(findings, "missing:gap_v3_human_review_readiness_matrix.csv")
    else:
        matrix = read_csv(matrix_path)
        if len(matrix) != 7:
            add(findings, f"readiness_matrix_row_count:{len(matrix)}")
        for row in matrix:
            if row.get("safe_to_promote", "").lower() not in {"false", "no", "0"}:
                add(findings, f"safe_to_promote_not_false:{row.get('collision_id')}")
            if row.get("export_status") != "DO_NOT_EXPORT":
                add(findings, f"matrix_export_status:{row.get('collision_id')}")

    ledger = read_csv(ARCHIVE / "09_MANIFESTS/collision_resolution_ledger.csv")
    if {r["collision_id"] for r in ledger} != EXPECTED_COLLISION_IDS:
        add(findings, "ledger_collision_id_mismatch")
    for row in ledger:
        if row.get("export_status") != "DO_NOT_EXPORT":
            add(findings, f"ledger_export_status:{row['collision_id']}")

    parking = read_csv(ARCHIVE / "09_MANIFESTS/reference_profile_parking_register.csv")
    if len(parking) < 139:
        add(findings, f"parking_row_count:{len(parking)}")
    for row in parking:
        if row.get("export_allowed", "").lower() != "no":
            add(findings, f"parking_export_allowed:{row.get('reference_path')}")

    allow = read_csv(ARCHIVE / "09_MANIFESTS/export_allowlist.csv")
    for row in allow:
        p = row["path_or_glob"].lower()
        for forbidden in ALLOWLIST_FORBIDDEN:
            if forbidden.lower() in p:
                add(findings, f"allowlist_forbidden_pattern:{row['path_or_glob']}:{forbidden}")

    template = ARCHIVE / "08_VALIDATION_CHECKS/collision_regression_results_TEMPLATE.csv"
    if not template.is_file():
        add(findings, "missing:collision_regression_results_TEMPLATE.csv")
    else:
        trows = read_csv(template)
        if len(trows) < 21:
            add(findings, f"regression_template_rows:{len(trows)}")
        prefilled_pass = [r for r in trows if r.get("pass_fail", "").strip().upper() == "PASS"]
        if prefilled_pass:
            add(findings, f"regression_template_fabricated_pass:{len(prefilled_pass)}")

    for md in (INTEGRATED / "90_Audit/Collisions").glob("gap_v3_*.md"):
        if CHECKLIST_HEADING not in md.read_text(encoding="utf-8"):
            add(findings, f"missing_checklist:{md.name}")

    blockers = ARCHIVE / "11_INTEGRATION_GUIDES/GAP_V3_PROMOTION_BLOCKERS.md"
    if not blockers.is_file():
        add(findings, "missing:GAP_V3_PROMOTION_BLOCKERS.md")

    reports = list((ARCHIVE / "10_FINAL_REPORTS").glob("GAP_V3_REVIEW_READY_AUDIT_REPORT_*.md"))
    if not reports:
        add(findings, "missing:GAP_V3_REVIEW_READY_AUDIT_REPORT")

    parking_audit = ARCHIVE / "09_MANIFESTS/reference_parking_gate_audit.csv"
    if not parking_audit.is_file():
        add(findings, "missing:reference_parking_gate_audit.csv")

    integrated_log = list((INTEGRATED / "90_Audit").glob("gap_v3_pharmacist_facility_review_log_*_REVIEW_READY.md"))
    if not integrated_log:
        add(findings, "missing:integrated_REVIEW_READY_log")

    # external_ready_candidate scan in derived manifest
    export_ledger = DERIVED / "manifest/derived_export_candidate_ledger.csv"
    if export_ledger.is_file():
        for row in read_csv(export_ledger):
            if row.get("external_ready_candidate", "").strip().lower() in {"true", "yes", "1"}:
                add(findings, f"external_ready_candidate_true:{row.get('file','')}")

    # custom_gpt_upload_safe must not be affirmatively set true in derived JSON manifests
    for path in DERIVED.rglob("*.json"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r'"custom_gpt_upload_safe"\s*:\s*true', text):
            add(findings, f"custom_gpt_upload_safe_true:{path.relative_to(WORKSPACE)}")

    print(f"gap_v3_review_ready_findings={len(findings)}")
    print(f"gap_v3_review_ready_gate={'FAIL' if findings else 'PASS'}")
    for f in findings:
        print(f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
