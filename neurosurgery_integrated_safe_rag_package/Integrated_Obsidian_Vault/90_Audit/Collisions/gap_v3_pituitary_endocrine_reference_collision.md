---
note_type: "audit_collision"
title: "gap_v3_pituitary_endocrine_reference_collision"
collision_id: "GAP-V3-COLLISION-PITUITARY-001"
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

# Collision: PARENT pituitary_endocrine vs integrated vs CHILD

## Collision ID

`GAP-V3-COLLISION-PITUITARY-001`

## Parties

| Layer | Path | Risk |
|-------|------|------|
| Integrated hub | `04_Drug_Classes/下垂体内分泌薬_境界と出典階層.md` | Boundary only |
| PARENT reference | `02_DRUG_PROFILES_SAFE_KNOWLEDGE/pituitary_endocrine/*.md` | Context notes vs drug profiles |
| PARENT class note | `03_CLASS_NOTES/下垂体_間脳下垂体薬物療法_gap_note.md` | Domain framing |
| CHILD reference | 127-drug inventory | No pituitary-specific keys |

## Conflict description

- Stress-steroid and postop DI **context notes** can be misread as universal orders.
- Endocrine drugs (somatostatin analogs, dopamine agonists, adrenal inhibitors) require product-level labeling not present in PARENT.
- Integrated package lacks a dedicated pituitary disease hub note; boundary hub is not a substitute.

## Resolution policy (current)

1. Context notes remain **reference-only** (`adapted_port` at most for boundary language in derived README).
2. Do not infer doses or product URLs from PARENT filenames or generic names.
3. Facility endocrine protocol confirmation required before any export.

## Operator actions required

- [ ] Endocrine + neurosurgery joint review
- [ ] Map facility formulary for octreotide, cabergoline, hydrocortisone pathways separately
- [ ] Keep ledger status `gap_v3_m0_ledger_recorded_pending_operator_review` until review logged

## Pharmacist / facility review (repo-local, 2026-06-04)

| Check | Result |
|-------|--------|
| Stress-steroid / postop DI context vs chronic Rx | Separated in boundary hub |
| Endocrine + facility protocol | **Not confirmed** |
| Preview / promotion | **Blocked** |

**Disposition:** Hold maintained.

## Status

`unresolved_intentional_hold`


## 添付文書・適用外ガバナンス（Stage 3）

- **用法・用量・使用方法:** 製品単位の最新電子添文（PMDA）遵守。未解決 reference から数値・ルートを断定しない。
- **適用外使用:** 医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- **正本:** [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

## Human / Facility Review Checklist

Readiness matrix: `reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv` — filter `collision_id` = `GAP-V3-COLLISION-PITUITARY-001`.

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

