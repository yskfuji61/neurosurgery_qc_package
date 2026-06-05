# STAGE 3 — Integrated-First Governance Audit Report

**Date:** 2026-06-05  
**Scope:** Label compliance (PMDA package insert) and off-label use routing in integrated layer only. **No** derived `knowledge/*.md` edits. **No** promotion.

## User constraints applied

1. **用法・用量・使用方法** — 製品単位の最新電子添文（PMDA）遵守。reference からの数値断定禁止。
2. **適用外使用** — 添付文書の承認範囲を超える使用は、**医師の個別判断なし**に標準治療・推奨・標準オーダーとして提示しない（原則禁止）。

## Files created / updated

| Path | Change |
|------|--------|
| `Integrated_Obsidian_Vault/00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス.md` | **New** — central governance index |
| `04_Drug_Classes/*_境界と出典階層.md` (×7) | Appended Stage 3 section |
| `90_Audit/Collisions/gap_v3_*_reference_collision.md` (×7) | Inserted 添付文書・適用外 block before Human checklist |
| `00_Index/04_Gap_V3_Reference_Parked_Index.md` | Link to governance index |
| `00_Index/03_Validation_Audit_Operations_Index.md` | Stage 3 pointer |
| `02_Diseases/下垂体・間脳下垂体疾患_REFERENCE_HUB.md` | Routing-only 添付文書・適用外 |
| `90_Audit/gap_v3_pharmacist_facility_review_log_20260605_REVIEW_READY.md` | Review order updated |
| `scripts/_apply_stage3_label_offlabel_governance.py` | Idempotent apply helper |

## Explicitly not done (Stage 3 stop)

- `derived/custom_gpt_knowledge_package/knowledge/*.md` — **unchanged**
- Dose tables, TDM targets, IV compatibility, CDS triggers, formulary assertions
- `export_status` / `export_candidate` / `safe_to_promote` promotion
- `apply_preview_promotion.py`
- PARENT profile body merge into disease notes

## Validation (run after apply)

```bash
cd references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package
python3 tests/validate_classification_vocabulary.py
python3 tests/validate_reference_migration_ledger.py --corpus all
python3 tests/validate_upload_manifest.py
python3 tests/validate_release_readiness.py
python3 tests/validate_gap_v3_review_ready.py
python3 tests/validate_collision_governance.py
python3 tests/validate_unsafe_patterns.py
python3 tests/validate_quarantine_register.py
python3 tests/validate_facility_confirmation_ledger.py
python3 tests/validate_derived_export_candidate.py
```

Integrated (optional):

```bash
cd references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/scripts/validation
python3 check_integrated_policy_controls.py
```

## Next stage (not started)

- **Stage 4:** Export concise boundary language into 13 `knowledge/*.md` files — only after integrated validation and human review gates.
