# Integrated Validation Scripts

This directory contains operator-side validation scripts for the integrated Safe RAG package.

These scripts are repository maintenance tools. They are not clinical guidelines, prescription orders, institutional procedures, facility availability records, or production EHR/CDS specifications.

## Commands

Run from `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package`.

```bash
python Integrated_Obsidian_Vault/scripts/validate_frontmatter.py \
  --root Integrated_Obsidian_Vault \
  --output /tmp/qc_integrated_frontmatter_findings.csv

python Integrated_Obsidian_Vault/scripts/validate_jsonl_schema.py \
  --schema Integrated_Obsidian_Vault/schemas/jsonl_rag_schema.json \
  --jsonl Integrated_Obsidian_Vault/99_Exports/Unified_RAG/unified_safe_rag_seed.jsonl \
  --output /tmp/qc_integrated_jsonl_schema_findings.csv

python Integrated_Obsidian_Vault/scripts/validate_knowledge_integrity.py \
  --jsonl Integrated_Obsidian_Vault/99_Exports/Unified_RAG/unified_safe_rag_seed.jsonl \
  --output /tmp/qc_integrated_knowledge_integrity_findings.csv

python Integrated_Obsidian_Vault/scripts/validation/check_integrated_policy_controls.py \
  --root Integrated_Obsidian_Vault \
  --schema Integrated_Obsidian_Vault/schemas/integrated_policy_control_schema.json \
  --output /tmp/qc_integrated_policy_control_findings.csv
```

## Scope

`validate_frontmatter.py` checks integrated Markdown frontmatter keys and excludes operator-side script/schema/report support files.

`validate_jsonl_schema.py` checks required JSONL chunk fields, simple field types, and safety-gate constants using only the Python standard library.

`validate_knowledge_integrity.py` checks high-risk JSONL chunks for `not_to_interpret_as`, human review, external-primary-source, facility-confirmation, and required-confirmation gates.

`validation/check_integrated_policy_controls.py` checks integrated policy notes for source-traceability fields, required human review, non-guideline / non-prescription / non-procedure / non-production-CDS constants, required boundary terms, allowed audit status, and absence of embedded clinical value patterns.

Validation pass means structural consistency only. It does not mean PMDA product confirmation, pharmacist review, facility confirmation, committee approval, Custom GPT Preview approval, or external readiness is complete.
