#!/usr/bin/env python3
"""Validate Gap V3 collision governance artifacts in reference_archive."""
from __future__ import annotations

import csv
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

EXPECTED_COLLISION_IDS = {
    "GAP-V3-COLLISION-NEURO-ONC-001",
    "GAP-V3-COLLISION-PITUITARY-001",
    "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001",
    "GAP-V3-COLLISION-CSF-IIH-001",
    "GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001",
    "GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001",
    "GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001",
}

DISEASE_NO_MERGE = INTEGRATED / "02_Diseases/脳腫瘍周術期.md"
FORBIDDEN_IN_DISEASE = ("temozolomide", "bevacizumab", "PCV", "carmustine_wafer", "テモゾロミド", "ベバシズマブ")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def add(findings: list[str], msg: str) -> None:
    findings.append(msg)


def main() -> int:
    findings: list[str] = []

    ledger_path = ARCHIVE / "09_MANIFESTS/collision_resolution_ledger.csv"
    deny_path = ARCHIVE / "09_MANIFESTS/export_denylist.csv"
    allow_path = ARCHIVE / "09_MANIFESTS/export_allowlist.csv"
    parking_path = ARCHIVE / "09_MANIFESTS/reference_profile_parking_register.csv"
    tests_path = ARCHIVE / "08_VALIDATION_CHECKS/collision_regression_tests.csv"
    audit_path = ARCHIVE / "10_FINAL_REPORTS/COLLISION_RESOLUTION_FINAL_AUDIT_REPORT.md"

    for p in (ledger_path, deny_path, allow_path, parking_path, tests_path, audit_path):
        if not p.is_file():
            add(findings, f"missing_file:{p.relative_to(WORKSPACE)}")

    if findings:
        for f in findings:
            print(f)
        return 1

    ledger = read_csv(ledger_path)
    ledger_ids = {r["collision_id"] for r in ledger}
    if ledger_ids != EXPECTED_COLLISION_IDS:
        add(findings, f"ledger_id_mismatch:expected={len(EXPECTED_COLLISION_IDS)} got={ledger_ids}")

    for row in ledger:
        if row.get("export_status") != "DO_NOT_EXPORT":
            add(findings, f"ledger_export_not_denied:{row['collision_id']}")

    deny = read_csv(deny_path)
    allow = read_csv(allow_path)
    deny_paths = {r["path_or_glob"] for r in deny}
    allow_paths = {r["path_or_glob"] for r in allow}
    if deny_paths & allow_paths:
        add(findings, f"deny_allow_overlap:{deny_paths & allow_paths}")

    if not any("neuro_oncology" in p for p in deny_paths):
        add(findings, "denylist_missing_neuro_oncology_glob")

    for row in allow:
        p = row["path_or_glob"]
        if "02_DRUG_PROFILES_SAFE_KNOWLEDGE" in p and "*.md" in p:
            add(findings, f"allowlist_has_drug_profile_glob:{p}")

    parking = read_csv(parking_path)
    if len(parking) < 120:
        add(findings, f"parking_register_too_few:{len(parking)}")
    for row in parking:
        if row.get("export_allowed", "").lower() != "no":
            add(findings, f"parking_export_allowed:{row.get('reference_path')}")

    tests = read_csv(tests_path)
    if len(tests) < 21:
        add(findings, f"regression_tests_count:{len(tests)}")

    collision_dir = INTEGRATED / "90_Audit/Collisions"
    for cid in EXPECTED_COLLISION_IDS:
        found = False
        for md in collision_dir.glob("gap_v3_*.md"):
            text = md.read_text(encoding="utf-8")
            if cid in text:
                found = True
                break
        if not found:
            add(findings, f"collision_md_missing_id:{cid}")

    if DISEASE_NO_MERGE.is_file():
        body = DISEASE_NO_MERGE.read_text(encoding="utf-8").lower()
        for term in FORBIDDEN_IN_DISEASE:
            if term.lower() in body:
                add(findings, f"disease_note_contains_forbidden_term:{term}")

    hub = INTEGRATED / "02_Diseases/下垂体・間脳下垂体疾患_REFERENCE_HUB.md"
    if not hub.is_file():
        add(findings, "missing_pituitary_reference_hub")

    print(f"collision_governance_findings={len(findings)}")
    print(f"collision_governance_gate={'FAIL' if findings else 'PASS'}")
    for f in findings:
        print(f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
