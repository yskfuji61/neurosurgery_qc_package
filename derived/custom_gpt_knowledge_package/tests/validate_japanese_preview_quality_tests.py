#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEST_FILE = ROOT / "tests" / "japanese_medical_output_quality_preview_tests.md"
REQUIRED_HEADERS = [
    "must_include",
    "must_not_include",
    "japanese_quality_checks",
    "medical_safety_checks",
    "pass_fail",
]


def main():
    text = TEST_FILE.read_text(encoding="utf-8-sig")
    findings = []
    for header in REQUIRED_HEADERS:
        if header not in text:
            findings.append(("missing_required_header", header))
    rows = [line for line in text.splitlines() if line.startswith("| JP-QUAL-")]
    if len(rows) < 10:
        findings.append(("insufficient_preview_quality_tests", str(len(rows))))
    print(f"japanese_preview_quality_tests_findings={len(findings)}")
    for item in findings:
        print(",".join(item))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
