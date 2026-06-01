# Integrated Schema Files

This directory contains operator-side machine-readable schemas for the integrated Safe RAG package.

These schemas validate structure, required metadata, source traceability, and safety-gate fields. They are not clinical references, prescribing rules, institutional procedures, facility availability records, or production EHR/CDS specifications.

## Files

1. `frontmatter_schema.json` validates required Markdown frontmatter keys used by integrated policy and knowledge notes.
2. `jsonl_rag_schema.json` validates required JSONL chunk fields used by integrated RAG exports.
3. `integrated_policy_control_schema.json` inventories the integrated policy directories and the operator-side safety gates for source traceability, human review, non-prescription status, non-procedure status, non-production-CDS status, and absence of embedded clinical values.

## Scope

The schemas intentionally do not encode dose values, dosing intervals, thresholds, IV compatibility decisions, repeat-dosing rules, TDM adjustment rules, facility availability, or production CDS behavior.

Validation pass means the package structure is mechanically coherent. It does not mean PMDA confirmation, pharmacist review, facility confirmation, committee approval, or external readiness is complete.
