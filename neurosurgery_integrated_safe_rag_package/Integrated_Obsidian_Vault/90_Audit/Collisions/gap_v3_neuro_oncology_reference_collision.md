---
note_type: "audit_collision"
title: "gap_v3_neuro_oncology_reference_collision"
collision_id: "GAP-V3-COLLISION-NEURO-ONC-001"
export_status: "DO_NOT_EXPORT"
ledger_path: "reference_archive/.../09_MANIFESTS/collision_resolution_ledger.csv"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_path: "references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/"
human_review_required: true
audit_status: "unresolved_intentional_hold"
pharmacist_repo_local_review: "2026-06-04_recorded"
last_reviewed: "2026-06-04"
---

# Collision: PARENT neuro_oncology vs integrated vs CHILD

## Collision ID

`GAP-V3-COLLISION-NEURO-ONC-001`

## Parties

| Layer | Path | Risk |
|-------|------|------|
| Integrated hub | `04_Drug_Classes/神経腫瘍薬物療法_境界と出典階層.md` | Boundary only |
| Integrated disease | `02_Diseases/脳腫瘍周術期.md` | Perioperative separation |
| PARENT reference | `02_DRUG_PROFILES_SAFE_KNOWLEDGE/neuro_oncology/*.md` (29 profiles) | General-name, PMDA unresolved |
| CHILD reference | `pmda_product_source_register.csv` (127 keys) | Orthogonal inventory |

## Conflict description

- PARENT profiles may name regimens (e.g. PCV, TMZ) without product-level PMDA URLs.
- Integrated disease note covers perioperative ASM/steroid/antibiotic/VTE — **not** full oncology chemotherapy selection.
- CHILD corpus does not cover most V3_RESIDUAL neuro-oncology keys.

## Resolution policy (current)

1. **No merge** of PARENT drug facts into integrated disease note.
2. **No promotion** of CHILD `package_summary.json` PMDA counts to integrated layer.
3. Hold all PARENT profiles in migration ledger until integrated drug-profile governance exists.

## Operator actions required

- [ ] Pharmacist review of high-risk profiles (`temozolomide`, `bevacizumab`, `carmustine_wafer`, etc.)
- [ ] Confirm facility formulary / protocol before any derived summary
- [ ] Re-run `validate_reference_migration_ledger.py --corpus all` after reference file changes

## Pharmacist / facility review (repo-local, 2026-06-04)

| Check | Result |
|-------|--------|
| High-risk profiles (TMZ, bevacizumab, wafer) flagged in collision | Yes |
| Facility oncology / neurosurgery protocol | **Not confirmed** — `pending_facility_review` |
| Preview evidence / `apply_preview_promotion.py` | **Blocked** |
| `external_ready_candidate` | **0** |

**Disposition:** Hold maintained. Not pharmacist sign-off.

## Status

`unresolved_intentional_hold` — not a silent collision resolution.


## 添付文書・適用外ガバナンス（Stage 3）

- **用法・用量・使用方法:** 製品単位の最新電子添文（PMDA）遵守。未解決 reference から数値・ルートを断定しない。
- **適用外使用:** 医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- **正本:** [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

## Human / Facility Review Checklist

Readiness matrix: `reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv` — filter `collision_id` = `GAP-V3-COLLISION-NEURO-ONC-001`.

- [ ] 薬剤師sign-off済み
- [ ] 施設採用品・formulary確認済み
- [ ] 施設プロトコル/SOP確認済み
- [ ] 専門科レビュー済み
- [ ] PMDA製品単位URL確認済み
- [ ] RMP / IF / 患者向医薬品ガイド確認済み
- [ ] 疾患ノート本文へ誤マージされていない
- [ ] export_denylistに残っている
- [ ] export_allowlistに誤登録されていない
- [ ] RAG regression実走済み
- [ ] 実RAG出力で禁止回答が出ない
- [ ] evidence linkを記録済み

### Review metadata

- reviewer:
- role:
- review_date:
- evidence_links:
- decision:
- residual_risk:
- next_action:

