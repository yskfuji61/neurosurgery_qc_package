#!/usr/bin/env python3
"""Commit 13 gate: pharmacist checklist, quarantine doc, and non-empty quarantine register."""
from __future__ import annotations

from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "audit" / "pharmacist_red_flag_review_checklist.md"
QUARANTINE_DOC = ROOT / "audit" / "unapproved_content_quarantine.md"
QUARANTINE_CSV = ROOT / "manifest" / "knowledge_quarantine_register.csv"

CHECKLIST_MARKERS = [
    "Red-flag 項目",
    "Sign-off 状態",
    "未記録",
    "RF-DOSE",
    "RF-CDS",
    "停止条件",
]

QUARANTINE_DOC_MARKERS = [
    "quarantine_status",
    "under_review",
    "cleared",
    "禁止事項",
    "knowledge_quarantine_register.csv",
]

REGISTER_REQUIRED_TYPES = {
    "pending_pharmacist_red_flag_review",
}


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    findings: list[dict[str, str]] = []

    for path, markers, label in (
        (CHECKLIST, CHECKLIST_MARKERS, "pharmacist_red_flag_review_checklist.md"),
        (QUARANTINE_DOC, QUARANTINE_DOC_MARKERS, "unapproved_content_quarantine.md"),
    ):
        if not path.exists():
            add_finding(findings, label, "missing_file", str(path))
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in markers:
            if marker not in text:
                add_finding(findings, label, "missing_marker", marker)

    if not QUARANTINE_CSV.exists():
        add_finding(findings, "knowledge_quarantine_register.csv", "missing_file", "")
    else:
        lines = [ln for ln in QUARANTINE_CSV.read_text(encoding="utf-8-sig").splitlines() if ln.strip()]
        if len(lines) < 2:
            add_finding(findings, "knowledge_quarantine_register.csv", "empty_register", "")
        else:
            body = "\n".join(lines[1:])
            if "pharmacist sign-off" in body.lower() or "未記録" in CHECKLIST.read_text(encoding="utf-8"):
                pass
            found_types = {t for t in REGISTER_REQUIRED_TYPES if t in body}
            if not found_types:
                add_finding(findings, "knowledge_quarantine_register.csv", "missing_finding_type", "")
            if "cleared" in body and ",cleared," in f",{body},":
                add_finding(findings, "knowledge_quarantine_register.csv", "premature_cleared_row", "")

    if CHECKLIST.exists():
        text = CHECKLIST.read_text(encoding="utf-8", errors="ignore")
        if "approve" in text and "未記録" not in text and "hold" not in text:
            add_finding(findings, CHECKLIST.name, "missing_unresolved_signoff_state", "")

    if args.output and findings:
        import csv

        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["item", "issue", "detail"])
            writer.writeheader()
            writer.writerows(findings)

    print(f"pharmacist_red_flag_commit13_findings={len(findings)}")
    print(f"pharmacist_red_flag_commit13_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
