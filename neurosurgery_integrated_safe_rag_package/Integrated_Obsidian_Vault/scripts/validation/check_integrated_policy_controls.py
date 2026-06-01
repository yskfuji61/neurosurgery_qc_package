#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent.parent
DEFAULT_SCHEMA = DEFAULT_ROOT / "schemas" / "integrated_policy_control_schema.json"


def load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def parse_scalar(value: str) -> Any:
    stripped = value.strip()
    if stripped in {"true", "True"}:
        return True
    if stripped in {"false", "False"}:
        return False
    if stripped in {"[]", ""}:
        return [] if stripped == "[]" else ""
    if (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'")):
        return stripped[1:-1]
    return stripped


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing_opening_frontmatter_delimiter"
    try:
        end_index = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, "missing_closing_frontmatter_delimiter"

    frontmatter: dict[str, Any] = {}
    current_list_key: str | None = None
    for raw_line in lines[1:end_index]:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("-") and current_list_key:
            frontmatter.setdefault(current_list_key, []).append(parse_scalar(stripped[1:].strip()))
            continue
        if ":" not in line:
            current_list_key = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            current_list_key = None
            continue
        if value == "":
            frontmatter[key] = []
            current_list_key = key
        else:
            frontmatter[key] = parse_scalar(value)
            current_list_key = None
    return frontmatter, None


def policy_files(root: Path, prefixes: list[str]) -> list[Path]:
    files: list[Path] = []
    for prefix in prefixes:
        directory = root / prefix
        if directory.exists():
            files.extend(path for path in directory.rglob("*.md") if path.is_file())
    return sorted(files)


def add_finding(findings: list[dict[str, str]], path: Path, root: Path, issue: str, detail: str) -> None:
    findings.append({"file": path.relative_to(root).as_posix(), "issue": issue, "detail": detail})


def is_placeholder(value: Any, disallowed: set[str]) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value.strip()
    return normalized in disallowed


def validate_frontmatter_controls(path: Path, root: Path, frontmatter: dict[str, Any], schema: dict[str, Any], findings: list[dict[str, str]]) -> None:
    disallowed = set(schema.get("disallowed_placeholder_values", []))

    for key in schema.get("required_frontmatter_keys", []):
        if key not in frontmatter:
            add_finding(findings, path, root, "missing_required_policy_key", key)

    for key in schema.get("required_true_keys", []):
        if frontmatter.get(key) is not True:
            add_finding(findings, path, root, "required_true_key_not_true", key)

    for key in schema.get("source_traceability_keys", []):
        value = frontmatter.get(key)
        if not isinstance(value, str) or not value.strip() or is_placeholder(value, disallowed):
            add_finding(findings, path, root, "invalid_source_traceability_value", key)

    for key in schema.get("required_non_empty_array_keys", []):
        value = frontmatter.get(key)
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
            add_finding(findings, path, root, "missing_or_empty_policy_array", key)

    audit_status = frontmatter.get("audit_status")
    allowed_audit_status = set(schema.get("allowed_audit_status", []))
    if audit_status not in allowed_audit_status:
        add_finding(findings, path, root, "invalid_audit_status", str(audit_status))

    not_to_interpret_as = " ".join(frontmatter.get("not_to_interpret_as", [])) if isinstance(frontmatter.get("not_to_interpret_as"), list) else ""
    for term in schema.get("required_not_to_interpret_as_terms", []):
        if term not in not_to_interpret_as:
            add_finding(findings, path, root, "missing_required_boundary_term", term)


def validate_no_clinical_values(path: Path, root: Path, text: str, schema: dict[str, Any], findings: list[dict[str, str]]) -> None:
    for rule in schema.get("forbidden_clinical_value_patterns", []):
        pattern = rule.get("pattern", "")
        rule_id = rule.get("id", "forbidden_clinical_value")
        if pattern and re.search(pattern, text):
            add_finding(findings, path, root, "forbidden_clinical_value_pattern", rule_id)


def write_findings(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "issue", "detail"])
        writer.writeheader()
        writer.writerows(findings)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    schema = load_schema(args.schema.resolve())
    prefixes = schema.get("policy_directory_prefixes", [])
    files = policy_files(root, prefixes)
    findings: list[dict[str, str]] = []

    for path in files:
        frontmatter, parse_issue = parse_frontmatter(path)
        if parse_issue:
            add_finding(findings, path, root, parse_issue, "")
            continue
        validate_frontmatter_controls(path, root, frontmatter, schema, findings)
        validate_no_clinical_values(path, root, path.read_text(encoding="utf-8"), schema, findings)

    if args.output:
        write_findings(args.output, findings)

    print(f"integrated_policy_files_checked={len(files)}")
    print(f"integrated_policy_control_findings={len(findings)}")
    print(f"integrated_policy_control_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['file']},{finding['issue']},{finding['detail']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
