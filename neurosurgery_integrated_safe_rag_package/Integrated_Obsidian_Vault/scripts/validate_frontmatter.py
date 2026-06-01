#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent
DEFAULT_SCHEMA = DEFAULT_ROOT / "schemas" / "frontmatter_schema.json"
EXCLUDED_PARTS = {"schemas", "scripts"}
EXCLUDED_SUFFIXES = (
    ("99_Exports", "Validation_Reports"),
    ("99_Exports", "Upload_Bundles"),
)


def load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def is_excluded(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts
    if any(part in EXCLUDED_PARTS for part in relative_parts):
        return True
    return any(relative_parts[: len(suffix)] == suffix for suffix in EXCLUDED_SUFFIXES)


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and not is_excluded(path, root)
    )


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
            item = stripped[1:].strip()
            frontmatter.setdefault(current_list_key, []).append(parse_scalar(item))
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


def type_matches(value: Any, expected: str | list[str]) -> bool:
    expected_types = expected if isinstance(expected, list) else [expected]
    for expected_type in expected_types:
        if expected_type == "string" and isinstance(value, str):
            return True
        if expected_type == "boolean" and isinstance(value, bool):
            return True
        if expected_type == "array" and isinstance(value, list):
            return True
        if expected_type == "object" and isinstance(value, dict):
            return True
    return False


def validate_document(path: Path, root: Path, schema: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    relative_path = path.relative_to(root).as_posix()
    frontmatter, parse_issue = parse_frontmatter(path)
    if parse_issue:
        return [{"file": relative_path, "issue": parse_issue, "detail": ""}]

    required = schema.get("required", [])
    properties = schema.get("properties", {})
    for key in required:
        if key not in frontmatter:
            findings.append({"file": relative_path, "issue": "missing_required_key", "detail": key})
            continue
        value = frontmatter[key]
        rules = properties.get(key, {})
        expected_type = rules.get("type")
        if expected_type and not type_matches(value, expected_type):
            findings.append({"file": relative_path, "issue": "invalid_type", "detail": f"{key} expected {expected_type}"})
        if "const" in rules and value != rules["const"]:
            findings.append({"file": relative_path, "issue": "invalid_const", "detail": f"{key} must be {rules['const']}"})
        if "enum" in rules and value not in rules["enum"]:
            findings.append({"file": relative_path, "issue": "invalid_enum", "detail": f"{key}={value}"})
    return findings


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
    findings: list[dict[str, str]] = []
    files = markdown_files(root)
    for path in files:
        findings.extend(validate_document(path, root, schema))

    if args.output:
        write_findings(args.output, findings)

    print(f"frontmatter_files_checked={len(files)}")
    print(f"frontmatter_findings={len(findings)}")
    print(f"frontmatter_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['file']},{finding['issue']},{finding['detail']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
