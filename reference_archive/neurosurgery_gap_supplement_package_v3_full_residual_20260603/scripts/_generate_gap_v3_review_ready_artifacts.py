#!/usr/bin/env python3
"""Generate Gap V3 review-ready support artifacts (no export promotion)."""
from __future__ import annotations

import csv
import re
from datetime import date
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[5]
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
TODAY = date.today().isoformat()
TODAY_COMPACT = date.today().strftime("%Y%m%d")

VALID_BUCKETS = {
    "_HOLD_PMDA_UNRESOLVED",
    "_HOLD_FACILITY_PROTOCOL_REQUIRED",
    "_PROCEDURAL_REFERENCE_ONLY",
    "_PARKED_REFERENCE_ONLY",
}

COLLISION_ID_BY_DOMAIN = {
    "neuro_oncology": "GAP-V3-COLLISION-NEURO-ONC-001",
    "pituitary_endocrine": "GAP-V3-COLLISION-PITUITARY-001",
    "perioperative_visualization_contrast": "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001",
    "csf_iih": "GAP-V3-COLLISION-CSF-IIH-001",
    "vasospasm_endovascular": "GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001",
    "spasticity_functional": "GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001",
    "healthcare_associated_cns_infection": "GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001",
}

BLOCKING_BY_COLLISION = {
    "GAP-V3-COLLISION-NEURO-ONC-001": "TMZ/PCV/bevacizumab/carmustine_wafer PMDA; facility oncology formulary; no disease-note merge",
    "GAP-V3-COLLISION-PITUITARY-001": "post-op DI/stress steroid/SIADH-CSW context; cabergoline/octreotide PMDA; endocrine pathway",
    "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001": "5-ALA/ICG/fluorescein procedural only; contrast SOP; metformin/renal/thyroid facility rules",
    "GAP-V3-COLLISION-CSF-IIH-001": "IIH vs ICP vs tumor-edema dexamethasone separation; no fixed dosing",
    "GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001": "bosentan!=clazosentan; systemic SAH vs IA/IT; nicardipine context separation",
    "GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001": "ITB/oral baclofen/botulinum/DBS separation; no unit conversion; no generic PD med stop",
    "GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001": "IV vancomycin not universal; TDM/toxicity; ID approval; EVD vs meningitis separation",
}

ALLOWLIST_FORBIDDEN_SUBSTRINGS = [
    "02_DRUG_PROFILES_SAFE_KNOWLEDGE",
    "neuro_oncology",
    "pituitary_endocrine",
    "intraventricular",
    "chronic_post_stroke",
    "spasticity_functional_neurosurgery/botulinum",
    "perioperative_visualization_contrast/5",
]

ALLOWLIST_INFO_ONLY = [
    (
        "collision_resolution_ledger.csv",
        "operator_manifest on allowlist with READY_FOR_LIMITED_ROUTING — routing metadata only; not drug profile export",
    ),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def generate_readiness_matrix(ledger_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out = []
    for row in ledger_rows:
        cid = row["collision_id"]
        pmda_status = (
            "UNRESOLVED"
            if row.get("required_source_resolution", "").lower() == "yes"
            else "PARTIAL_OR_NOT_REQUIRED"
        )
        out.append(
            {
                "collision_id": cid,
                "domain": row["domain"],
                "current_gate_status": "HOLD_REFERENCE_ONLY;unresolved_intentional_hold",
                "export_status": row["export_status"],
                "unresolved_hold_status": "unresolved_intentional_hold",
                "pharmacist_signoff_status": "NOT_SIGNED_OFF",
                "facility_evidence_status": "NO_FACILITY_EVIDENCE",
                "specialist_review_status": "NOT_COMPLETED",
                "pmda_product_resolution_status": pmda_status,
                "rag_regression_run_status": "NOT_RUN",
                "required_owner_roles": row.get("owner_role", ""),
                "blocking_items": BLOCKING_BY_COLLISION.get(cid, row.get("hold_reason", "")),
                "allowed_next_action": "keep_hold;collect_evidence;run_regression;review_prepare",
                "prohibited_next_action": "promote;export;merge_to_disease_note;apply_preview_promotion",
                "safe_to_promote": "false",
                "notes": f"Generated from collision_resolution_ledger; not clinical sign-off. {row.get('next_action', '')}",
                "updated_at": TODAY,
            }
        )
    return out


def audit_parking_row(row: dict[str, str]) -> dict[str, str]:
    path = row["reference_path"].lower()
    bucket = row.get("virtual_bucket", "")
    export_allowed = row.get("export_allowed", "").lower()
    domain = row.get("collision_domain", "")
    key = Path(row["reference_path"]).stem

    issues: list[str] = []
    if export_allowed != "no":
        issues.append("export_allowed_not_no")
    if bucket not in VALID_BUCKETS:
        issues.append("invalid_virtual_bucket")

    procedural_markers = (
        "intraventricular",
        "contrast",
        "itb",
        "botulinum",
        "5-ala",
        "5_ala",
        "icg",
        "fluorescein",
        "procedural",
        "ia_",
        "endovascular",
    )
    if any(m in path for m in procedural_markers):
        if bucket not in {"_PROCEDURAL_REFERENCE_ONLY", "_HOLD_FACILITY_PROTOCOL_REQUIRED"}:
            issues.append("procedural_path_bucket_mismatch")

    if domain in {"neuro_oncology", "pituitary_endocrine"} and bucket != "_HOLD_PMDA_UNRESOLVED":
        issues.append("oncology_endocrine_pmda_bucket_expected")

    if domain in {"chronic_post_stroke_symptoms", "historical_reassessment_negative_notes"}:
        if bucket != "_PARKED_REFERENCE_ONLY":
            issues.append("chronic_historical_parked_bucket_expected")

    requires_pmda = "yes" if bucket == "_HOLD_PMDA_UNRESOLVED" else "no"
    requires_facility = "yes" if bucket == "_HOLD_FACILITY_PROTOCOL_REQUIRED" else "no"
    procedural_only = "yes" if bucket == "_PROCEDURAL_REFERENCE_ONLY" else "no"

    return {
        "reference_key": key,
        "path_or_virtual_path": row["reference_path"],
        "virtual_bucket": bucket,
        "export_allowed": export_allowed,
        "bucket_consistency": "consistent" if not issues else "review_needed",
        "requires_pmda_resolution": requires_pmda,
        "requires_facility_protocol": requires_facility,
        "procedural_or_reference_only": procedural_only,
        "issue_detected": "true" if issues else "false",
        "reviewer_note": ";".join(issues) if issues else "",
    }


def inspect_allowlist_denylist() -> tuple[list[dict[str, str]], dict[str, str]]:
    allow = read_csv(ARCHIVE / "09_MANIFESTS/export_allowlist.csv")
    deny = read_csv(ARCHIVE / "09_MANIFESTS/export_denylist.csv")
    suspicious: list[dict[str, str]] = []

    for row in allow:
        p = row["path_or_glob"]
        for forbidden in ALLOWLIST_FORBIDDEN_SUBSTRINGS:
            if forbidden.lower() in p.lower():
                suspicious.append(
                    {
                        "path_or_glob": p,
                        "layer": row.get("layer", ""),
                        "review_status": row.get("review_status", ""),
                        "suspicion_reason": f"forbidden_substring:{forbidden}",
                        "recommended_action": "human_review_do_not_auto_remove",
                        "auto_removed": "no",
                    }
                )
        for marker, note in ALLOWLIST_INFO_ONLY:
            if marker in p:
                suspicious.append(
                    {
                        "path_or_glob": p,
                        "layer": row.get("layer", ""),
                        "review_status": row.get("review_status", ""),
                        "suspicion_reason": "informational_allowlist_entry",
                        "recommended_action": note,
                        "auto_removed": "no",
                    }
                )

    deny_paths = " ".join(r["path_or_glob"] for r in deny).lower()
    summary = {
        "allowlist_row_count": str(len(allow)),
        "denylist_row_count": str(len(deny)),
        "bosentan_pattern": "yes" if "bosentan" in deny_paths else "no",
        "chronic_acute_pattern": "yes" if "chronic_circulation" in deny_paths else "no",
        "historical_pattern": "yes" if "historical_drug" in deny_paths else "no",
        "umbrella_profiles": "yes" if "02_drug_profiles_safe_knowledge/**/*.md" in deny_paths else "no",
        "neuro_onc_glob": "yes" if "neuro_oncology" in deny_paths else "no",
        "pituitary_glob": "yes" if "pituitary_endocrine" in deny_paths else "no",
        "csf_iih_explicit": "yes" if "csf_iih" in deny_paths else "covered_by_umbrella",
        "spasticity_full_glob": "yes" if "spasticity_functional_neurosurgery/*.md" in deny_paths else "partial_or_umbrella",
        "cns_infection_glob": "yes" if "healthcare_associated_cns_infection" in deny_paths else "covered_by_umbrella",
    }
    return suspicious, summary


def generate_regression_template(tests: list[dict[str, str]]) -> list[dict[str, str]]:
    domain_to_cid = {v: k for k, v in {
        "GAP-V3-COLLISION-NEURO-ONC-001": "neuro_oncology",
        "GAP-V3-COLLISION-PITUITARY-001": "pituitary_endocrine",
        "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001": "perioperative_visualization_contrast",
        "GAP-V3-COLLISION-CSF-IIH-001": "csf_iih",
        "GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001": "vasospasm_endovascular",
        "GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001": "spasticity_functional",
        "GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001": "healthcare_associated_cns_infection",
    }.items()}
    cid_lookup = {v: k for k, v in domain_to_cid.items()}

    rows = []
    for t in tests:
        domain = t["domain"]
        rows.append(
            {
                "run_id": "TEMPLATE",
                "run_date": "",
                "rag_system_name": "",
                "rag_system_version": "",
                "test_id": t["test_id"],
                "collision_id": cid_lookup.get(domain, ""),
                "prompt": t["prompt"],
                "actual_answer_summary": "",
                "expected_behavior": t["expected_behavior"],
                "forbidden_behavior_observed": "",
                "pass_fail": "",
                "severity": t.get("severity", "high"),
                "reviewer": "",
                "evidence_link_or_log_path": "",
                "remediation_required": "",
                "remediation_note": "",
                "rerun_required": "",
            }
        )
    return rows


def main() -> None:
    ledger = read_csv(ARCHIVE / "09_MANIFESTS/collision_resolution_ledger.csv")
    parking = read_csv(ARCHIVE / "09_MANIFESTS/reference_profile_parking_register.csv")
    tests = read_csv(ARCHIVE / "08_VALIDATION_CHECKS/collision_regression_tests.csv")

    matrix = generate_readiness_matrix(ledger)
    write_csv(
        ARCHIVE / "09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv",
        list(matrix[0].keys()),
        matrix,
    )

    parking_audit = [audit_parking_row(r) for r in parking]
    write_csv(
        ARCHIVE / "09_MANIFESTS/reference_parking_gate_audit.csv",
        list(parking_audit[0].keys()) if parking_audit else [],
        parking_audit,
    )

    suspicious, deny_summary = inspect_allowlist_denylist()
    if suspicious:
        write_csv(
            ARCHIVE / "09_MANIFESTS/suspicious_allowlist_entries.csv",
            list(suspicious[0].keys()),
            suspicious,
        )

    template_rows = generate_regression_template(tests)
    write_csv(
        ARCHIVE / "08_VALIDATION_CHECKS/collision_regression_results_TEMPLATE.csv",
        list(template_rows[0].keys()),
        template_rows,
    )

    issue_count = sum(1 for r in parking_audit if r["issue_detected"] == "true")
    print(f"review_ready_generated_date={TODAY}")
    print(f"readiness_matrix_rows={len(matrix)}")
    print(f"parking_audit_rows={len(parking_audit)}")
    print(f"parking_audit_issues={issue_count}")
    print(f"suspicious_allowlist_rows={len(suspicious)}")
    print(f"regression_template_rows={len(template_rows)}")
    for k, v in deny_summary.items():
        print(f"denylist_check_{k}={v}")


if __name__ == "__main__":
    main()
