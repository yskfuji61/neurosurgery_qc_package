# Gap V3 Pharmacist / Facility Review Log（2026-06-04）

## 位置づけ

repo-local 監査記録。薬剤師 sign-off または施設 evidence **ではない**。collision はすべて `unresolved_intentional_hold` を維持する。

## Preview / promotion / external-ready ゲート

| Gate | Status |
|------|--------|
| `human_reviewed_preview_examples.md` に実 Preview 記録 | **なし** |
| `apply_preview_promotion.py --apply` | **実行禁止** |
| `external_ready_candidate` | **0** |
| `custom_gpt_upload_safe` | **false 維持** |

## Integrated boundary hubs（Phase 2 全 7 領域）

| Domain | Boundary hub | Collision | Facility confirmed |
|--------|--------------|-----------|-------------------|
| neuro_oncology | 神経腫瘍薬物療法_境界と出典階層 | gap_v3_neuro_oncology_* | No |
| pituitary_endocrine | 下垂体内分泌薬_境界と出典階層 | gap_v3_pituitary_* | No |
| perioperative_visualization_contrast | 術中可視化・造影剤_* | gap_v3_perioperative_* | No |
| csf_iih | CSF_IIH関連薬_* | gap_v3_csf_iih_* | No |
| vasospasm_endovascular | 血管内治療・血管攣縮局所薬_* | gap_v3_vasospasm_* | No |
| spasticity_functional | 痙縮・機能的脳神経外科薬_* | gap_v3_spasticity_* | No |
| healthcare_associated_cns_infection | 中枢神経感染・脳室内投与_* | gap_v3_healthcare_* | No |

## Red-flag 照合（boundary hubs）

- 用量・投与間隔・IV 相容性・固定閾値・PMDA URL 断定: **なし**
- procedural → 標準治療化: **境界で禁止明記**

## Reference archive 移行

PARENT sibling `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` を削除し、正本を `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` に集約。当時 ledger **540** 行（366 CHILD + 174 PARENT）の PARENT パスを更新済み。（**Current 2026-06-05:** archive 191 files; ledger **557** rows — collision/review-ready manifests 追補含む）

## 次の operator ステップ

Review-ready slice (2026-06-05): integrated log [`neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/90_Audit/gap_v3_pharmacist_facility_review_log_20260605_REVIEW_READY.md`](../../neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/90_Audit/gap_v3_pharmacist_facility_review_log_20260605_REVIEW_READY.md) — still **not** sign-off.

1. 施設薬剤師による collision 7 件のレビュー（evidence 付きでなければ `confirmed` にしない）
2. Preview 実施後のみ promotion helper を dry-run
3. integrated drug-profile 層整備後に reference プロファイル hold を再評価
