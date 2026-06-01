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
DEFAULT_SCHEMA = DEFAULT_ROOT / "schemas" / "jsonl_rag_schema.json"
DEFAULT_JSONL = DEFAULT_ROOT / "99_Exports" / "Unified_RAG" / "unified_safe_rag_seed.jsonl"


def load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


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


def validate_array_items(value: Any, item_rules: dict[str, Any]) -> bool:
    if not isinstance(value, list):
        return False
    expected_type = item_rules.get("type")
    return all(type_matches(item, expected_type) for item in value) if expected_type else True


def validate_object_additional(value: Any, additional_rules: dict[str, Any]) -> bool:
    if not isinstance(value, dict):
        return False
    expected_type = additional_rules.get("type")
    item_rules = additional_rules.get("items", {})
    for item in value.values():
        if expected_type and not type_matches(item, expected_type):
            return False
        if expected_type == "array" and item_rules and not validate_array_items(item, item_rules):
            return False
    return True


def validate_record(record: dict[str, Any], schema: dict[str, Any], file_name: str, line_number: int) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    chunk_id = str(record.get("chunk_id", ""))
    required = schema.get("required", [])
    properties = schema.get("properties", {})
    for key in required:
        if key not in record:
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "missing_required_field", "detail": key})
            continue
        value = record[key]
        rules = properties.get(key, {})
        expected_type = rules.get("type")
        if expected_type and not type_matches(value, expected_type):
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "invalid_type", "detail": f"{key} expected {expected_type}"})
        if "const" in rules and value != rules["const"]:
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "invalid_const", "detail": f"{key} must be {rules['const']}"})
        if "enum" in rules and value not in rules["enum"]:
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "invalid_enum", "detail": f"{key}={value}"})
        if rules.get("type") == "array" and rules.get("items") and not validate_array_items(value, rules["items"]):
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "invalid_array_items", "detail": key})
        if rules.get("type") == "object" and rules.get("additionalProperties") and not validate_object_additional(value, rules["additionalProperties"]):
            findings.append({"file": file_name, "line": str(line_number), "chunk_id": chunk_id, "issue": "invalid_object_values", "detail": key})
    return findings


def validate_jsonl(path: Path, schema: dict[str, Any]) -> tuple[int, list[dict[str, str]]]:
    findings: list[dict[str, str]] = []
    records_checked = 0
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as error:
                findings.append({"file": path.name, "line": str(line_number), "chunk_id": "", "issue": "invalid_json", "detail": str(error)})
                continue
            if not isinstance(record, dict):
                findings.append({"file": path.name, "line": str(line_number), "chunk_id": "", "issue": "record_not_object", "detail": ""})
                continue
            records_checked += 1
            findings.extend(validate_record(record, schema, path.name, line_number))
    return records_checked, findings


def write_findings(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "line", "chunk_id", "issue", "detail"])
        writer.writeheader()
        writer.writerows(findings)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    schema = load_schema(args.schema.resolve())
    records_checked, findings = validate_jsonl(args.jsonl.resolve(), schema)

    if args.output:
        write_findings(args.output, findings)

    print(f"jsonl_records_checked={records_checked}")
    print(f"jsonl_schema_findings={len(findings)}")
    print(f"jsonl_schema_gate={'FAIL' if findings else 'PASS'}")
    for finding in findings:
        print(f"{finding['file']},{finding['line']},{finding['chunk_id']},{finding['issue']},{finding['detail']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
