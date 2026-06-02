#!/usr/bin/env python3
"""Ensure Knowledge upload targets stay limited to knowledge/ (13 files).

Complements sibling reference `validate_manifest_completeness.py` discipline and
`manifest/reference_migration_decision_ledger.csv` (306 reference files, 1:1 decisions).
Does not approve reference-corpus rows for upload by itself.
"""
from pathlib import Path
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest" / "custom_gpt_upload_manifest.csv"


def normalize(path: Path) -> str:
    return path.as_posix()


def read_manifest(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def package_files(root: Path):
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.name == ".DS_Store":
            continue
        files.append(normalize(path.relative_to(root)))
    return sorted(files)


def main() -> int:
    rows = read_manifest(MANIFEST)
    findings = []

    manifest_files = sorted(row["file"] for row in rows)
    actual_files = package_files(ROOT)

    missing_from_manifest = sorted(set(actual_files) - set(manifest_files))
    extra_in_manifest = sorted(set(manifest_files) - set(actual_files))

    for path in missing_from_manifest:
        findings.append((path, "missing_from_upload_manifest", ""))
    for path in extra_in_manifest:
        findings.append((path, "listed_but_missing", ""))

    upload_targets = []
    expected_knowledge = sorted(
        normalize(path.relative_to(ROOT))
        for path in (ROOT / "knowledge").glob("*.md")
    )

    for row in rows:
        file_path = row["file"]
        upload_flag = row["upload_to_custom_gpt"].strip().lower()
        is_knowledge = file_path.startswith("knowledge/") and file_path.endswith(".md")

        if upload_flag not in {"yes", "no"}:
            findings.append((file_path, "invalid_upload_flag", upload_flag))
            continue

        if upload_flag == "yes":
            upload_targets.append(file_path)
            if not is_knowledge:
                findings.append((file_path, "non_knowledge_marked_for_upload", ""))
        elif is_knowledge:
            findings.append((file_path, "knowledge_not_marked_for_upload", ""))

    upload_targets = sorted(upload_targets)
    if upload_targets != expected_knowledge:
        findings.append(
            (
                "knowledge/*",
                "upload_target_set_mismatch",
                f"expected={len(expected_knowledge)} actual={len(upload_targets)}",
            )
        )

    print(f"upload_manifest_findings={len(findings)}")
    for file_path, kind, detail in findings:
        print(f"{file_path},{kind},{detail}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())