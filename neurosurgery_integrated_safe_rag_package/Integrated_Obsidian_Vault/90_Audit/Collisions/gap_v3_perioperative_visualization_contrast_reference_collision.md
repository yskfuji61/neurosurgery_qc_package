---
note_type: "audit_collision"
title: "gap_v3_perioperative_visualization_contrast_reference_collision"
collision_id: "GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001"
export_status: "DO_NOT_EXPORT"
ledger_path: "reference_archive/.../09_MANIFESTS/collision_resolution_ledger.csv"
human_review_required: true
audit_status: "unresolved_intentional_hold"
pharmacist_repo_local_review: "2026-06-04_recorded"
last_reviewed: "2026-06-04"
---

# Collision: perioperative_visualization_contrast

**Status:** `unresolved_intentional_hold` — procedural/contrast notes must not become default prescribing rules.

## Pharmacist / facility review (repo-local, 2026-06-04)

| Check | Result |
|-------|--------|
| Red-flag scan on boundary hub | No dose/URL assertions |
| Facility formulary / contrast protocol | **Not confirmed** — `pending_facility_review` |
| Preview evidence for derived promotion | **None** — promotion blocked |
| Quarantine / external-ready | No elevation |

**Disposition:** Hold maintained. Sign-off pending real facility evidence.

## Operator actions

- [ ] Facility radiology + anesthesia contrast pathway review
- [ ] Do not run `apply_preview_promotion.py` until `human_reviewed_preview_examples.md` has evidence


## 添付文書・適用外ガバナンス（Stage 3）

- **用法・用量・使用方法:** 製品単位の最新電子添文（PMDA）遵守。未解決 reference から数値・ルートを断定しない。
- **適用外使用:** 医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- **正本:** [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

## Human / Facility Review Checklist

Readiness matrix: `reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv` — filter `collision_id` = `GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001`.

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

