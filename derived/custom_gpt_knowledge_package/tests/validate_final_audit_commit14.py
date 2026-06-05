#!/usr/bin/env python3
"""Commit 14 gate: final audit report exists and repo-local validators pass."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"
FINAL_REPORT = ROOT / "audit" / "runbook_commit_14_final_audit_report.md"
CHUNK_LOG = ROOT / "audit" / "pharmacist_red_flag_chunk_review_log_014.md"
KNOWLEDGE = ROOT / "knowledge"

REPORT_MARKERS = [
    "DERIVED-COMMIT-14-FINAL",
    "未解決ゲート",
    "custom_gpt_upload_safe",
    "external_ready_candidate",
    "NOT",
]

CHUNK_LOG_MARKERS = [
    "hold 維持",
    "cleared",
    "0/10 該当",
]

VALIDATORS = [
    "validate_upload_manifest.py",
    "validate_unsafe_patterns.py",
    "validate_preview_protocol.py",
    "validate_pharmacist_red_flag_commit13.py",
    "validate_quarantine_integrity.py",
    "validate_release_readiness.py",
    "validate_review_state_integrity.py",
    "validate_reference_migration_ledger.py",
    "validate_facility_confirmation_status.py",
    "validate_derived_export_candidate_ledger.py",
]


def add(findings: list[str], item: str, detail: str) -> None:
    findings.append(f"{item},{detail}")


def main() -> int:
    findings: list[str] = []

    if len(list(KNOWLEDGE.glob("*.md"))) != 13:
        add(findings, "knowledge", f"count={len(list(KNOWLEDGE.glob('*.md')))}")

    for path, markers in ((FINAL_REPORT, REPORT_MARKERS), (CHUNK_LOG, CHUNK_LOG_MARKERS)):
        if not path.exists():
            add(findings, path.name, "missing_file")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in markers:
            if marker not in text:
                add(findings, path.name, f"missing_marker:{marker}")

    for name in VALIDATORS:
        script = TESTS / name
        if not script.exists():
            add(findings, name, "missing_script")
            continue
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT.parents[1],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            tail = (proc.stdout or proc.stderr or "").strip().splitlines()[-1:]
            add(findings, name, f"exit_{proc.returncode}:{tail[0] if tail else ''}")

    print(f"final_audit_commit14_findings={len(findings)}")
    print(f"final_audit_commit14_gate={'FAIL' if findings else 'PASS'}")
    for line in findings:
        print(line)

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
