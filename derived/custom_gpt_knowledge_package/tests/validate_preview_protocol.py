#!/usr/bin/env python3
"""Commit 12 gate: preview protocol files exist and cover required high-risk domains."""
from __future__ import annotations

from pathlib import Path
import argparse
import sys


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "tests" / "preview_test_protocol.md"
CDS_TESTS = ROOT / "tests" / "cds_time_window_alert_tests.md"

REQUIRED_DOMAIN_MARKERS = {
    "D-RENAL": ["D-RENAL", "eGFR", "CrCl"],
    "D-BP": ["D-BP", "血圧"],
    "D-TEMP": ["D-TEMP", "体温"],
    "D-Na": ["D-Na", "ナトリウム"],
    "D-MANN": ["D-MANN", "マンニトール"],
    "D-TDM": ["D-TDM", "TDM"],
    "D-IV": ["D-IV", "compatibility"],
    "D-CDS-AUTO": ["D-CDS-AUTO", "CDS"],
}

REQUIRED_SECTION_MARKERS = [
    "Unsafe prompt",
    "Pass pattern",
    "Fail pattern",
    "Must-have",
    "Must-not-have",
]

CDS_REQUIRED = [
    "TEST-CDS-01",
    "TEST-CDS-02",
    "TEST-CDS-03",
    "Must-have",
    "Must-not-have",
    "Pass pattern",
    "Fail pattern",
]


def add_finding(findings: list[dict[str, str]], item: str, issue: str, detail: str) -> None:
    findings.append({"item": item, "issue": issue, "detail": detail})


def check_file(path: Path, findings: list[dict[str, str]]) -> str:
    if not path.exists():
        add_finding(findings, str(path.relative_to(ROOT)), "missing_file", "")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    findings: list[dict[str, str]] = []
    protocol_text = check_file(PROTOCOL, findings)
    cds_text = check_file(CDS_TESTS, findings)

    if protocol_text:
        for section in REQUIRED_SECTION_MARKERS:
            if section not in protocol_text:
                add_finding(findings, "preview_test_protocol.md", "missing_section_marker", section)
        for domain, markers in REQUIRED_DOMAIN_MARKERS.items():
            if not all(marker in protocol_text for marker in markers):
                add_finding(
                    findings,
                    "preview_test_protocol.md",
                    "missing_domain_coverage",
                    domain,
                )
        for label in ("manual Preview", "must-have", "must-not-have"):
            if label not in protocol_text:
                add_finding(findings, "preview_test_protocol.md", "missing_protocol_label", label)

    if cds_text:
        for marker in CDS_REQUIRED:
            if marker not in cds_text:
                add_finding(findings, "cds_time_window_alert_tests.md", "missing_cds_marker", marker)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        import csv

        with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["item", "issue", "detail"])
            writer.writeheader()
            writer.writerows(findings)

    print(f"preview_protocol_findings={len(findings)}")
    print(f"preview_protocol_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['item']},{finding['issue']},{finding['detail']}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
