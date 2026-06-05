#!/usr/bin/env python3
"""Scan Custom GPT upload targets for dangerous terms and numeric assertions.

Aligned with sibling reference corpus `08_VALIDATION_CHECKS/validate_safe_knowledge.py`
discipline (pattern categories only; not a drop-in replacement). Repo-local PASS does not
mean clinical approval, PMDA resolution, or custom_gpt_upload_safe.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import csv
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest" / "custom_gpt_upload_manifest.csv"

PATTERNS = [
    ("numeric_drug_operation", "RED", r"\d+(\.\d+)?\s*(mg|mL|ml|μg|mcg|IU|mEq|mmol|mg/kg)"),
    ("interval_expression", "YELLOW", r"\bq\d+h\b"),
    ("infusion_rate_expression", "RED", r"(mL/h|mg/h|μg/kg/min|mcg/kg/min)"),
    ("tdm_concrete", "RED", r"(TDM目標|トラフ目標|AUC目標)"),
    ("compatibility_expression", "YELLOW", r"(混注可|側管可|同一ルート可|Y-site|Yサイト)"),
    ("ai_drug_decision", "RED", r"(AIが判断|自動投与|自動中止|自動減量|自動増量|自動調整)"),
    ("cds_production_condition", "RED", r"(CDS発火|Override条件|オーダーセット|CDS本番仕様)"),
    ("prescriptive_directive", "RED", r"(使用すべき|中止すべき|増量すべき|減量すべき|標準的に投与)"),
]

REVIEW_CONTEXT_MARKERS = (
    "must-not-have",
    "must_not_have",
    "fail 条件",
    "fail condition",
    "unsafe",
    "危険",
    "誤回答",
    "禁止",
    "anti-pattern",
    "must_not_have_violations",
    "判断するためのものではない",
    "判断するためのものではありません",
    "意味しない",
    "確定しない",
    "確定しません",
)


def read_upload_targets(path: Path) -> list[str]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return [
            row["file"]
            for row in csv.DictReader(handle)
            if row.get("upload_to_custom_gpt", "").strip().lower() == "yes"
        ]


def write_findings(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "finding_id",
                "file",
                "line",
                "pattern_name",
                "severity",
                "context_snippet",
                "approval_status",
            ],
        )
        writer.writeheader()
        writer.writerows(findings)


def in_review_context(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in REVIEW_CONTEXT_MARKERS)


def scan_file(rel_path: str) -> list[dict[str, str]]:
    path = ROOT / rel_path
    if not path.exists():
        return [
            {
                "finding_id": f"{rel_path}::::missing_upload_target",
                "file": rel_path,
                "line": "",
                "pattern_name": "missing_upload_target",
                "severity": "RED",
                "context_snippet": "",
                "approval_status": "pending_human_review",
            }
        ]

    findings: list[dict[str, str]] = []
    in_code_block = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        for pattern_name, severity, expression in PATTERNS:
            if not re.search(expression, line, re.IGNORECASE):
                continue

            effective_severity = "REVIEW_CONTEXT" if in_review_context(line) else severity
            approval_status = (
                "review_context_only"
                if effective_severity == "REVIEW_CONTEXT"
                else "pending_human_review"
            )
            findings.append(
                {
                    "finding_id": f"{rel_path}::{line_no}::{pattern_name}",
                    "file": rel_path,
                    "line": str(line_no),
                    "pattern_name": pattern_name,
                    "severity": effective_severity,
                    "context_snippet": stripped,
                    "approval_status": approval_status,
                }
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    findings: list[dict[str, str]] = []
    for rel_path in read_upload_targets(MANIFEST):
        findings.extend(scan_file(rel_path))

    if args.output:
        write_findings(args.output, findings)

    gate_failures = [item for item in findings if item["severity"] in {"RED", "YELLOW"}]
    print(f"unsafe_pattern_findings={len(findings)}")
    print(f"unsafe_pattern_gate={'FAIL' if gate_failures else 'PASS'}")
    for item in findings:
        print(
            ",".join(
                [
                    item["finding_id"],
                    item["file"],
                    item["line"],
                    item["pattern_name"],
                    item["severity"],
                    item["context_snippet"].replace(",", " "),
                    item["approval_status"],
                ]
            )
        )

    return 1 if gate_failures else 0


if __name__ == "__main__":
    sys.exit(main())