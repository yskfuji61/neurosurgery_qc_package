---
note_type: "audit_log"
title: "Gap V3 review-ready preparation log"
not_pharmacist_signoff: true
not_facility_evidence: true
review_ready_slice_date: "2026-06-05"
---

# Gap V3 — Review-Ready Preparation Log（2026-06-05）

## 位置づけ

- **薬剤師 sign-off ではない**
- **施設 evidence ではない**
- **統合完了ではない** — collision gate 維持のまま、人間レビュー用チェックリスト・matrix・regression 記録テンプレを整備した作業記録

Prior repo-local log (2026-06-04): `derived/custom_gpt_knowledge_package/audit/gap_v3_pharmacist_facility_review_log_20260604.md` — **do not overwrite**.

## 7 collision 現状（すべて hold）

| collision_id | export_status | pharmacist | facility | RAG regression |
|--------------|---------------|------------|----------|----------------|
| GAP-V3-COLLISION-NEURO-ONC-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-PITUITARY-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-CSF-IIH-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |
| GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001 | DO_NOT_EXPORT | NOT_SIGNED_OFF | NO_EVIDENCE | NOT_RUN |

## 薬剤師が見る順序

1. `reference_archive/.../09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv`
2. `90_Audit/Collisions/gap_v3_*_reference_collision.md` — **Human / Facility Review Checklist**（空欄のまま）
3. `04_Drug_Classes/*_境界と出典階層.md` — Collision governance 節 + **添付文書・適用外（Stage 3）**
4. `00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス.md` — 用法・用量は添付文書遵守；適用外は医師判断必須
5. `reference_archive/.../09_MANIFESTS/export_denylist.csv`
6. `11_INTEGRATION_GUIDES/GAP_V3_PROMOTION_BLOCKERS.md`

## 施設担当が見る順序（facility 必須 domain）

- PERIOP-VIS-CONTRAST: 放射線・麻酔・手術室 contrast SOP
- CSF-IIH: IIH / ICP プロトコル
- VASOSPASM-ENDOVASCULAR: Neuro-ICU / 血管内 / 調製
- SPASTICITY-FUNCTIONAL: ITB / ボツリヌス / DBS パスウェイ
- CNS-INFECTION: 脳室内投与・抗菌薬 SOP

## RAG regression の実施方法

1. Read `reference_archive/.../08_VALIDATION_CHECKS/collision_regression_results_README.md`
2. Copy `collision_regression_results_TEMPLATE.csv` → `collision_regression_results_YYYYMMDD.csv`
3. Run 21 prompts; fill `pass_fail` only after human review
4. Link file in collision checklist `evidence_links`

## Export 昇格禁止（再掲）

- `safe_to_promote` は全行 **false** のまま
- `apply_preview_promotion.py` 実行禁止（Preview 未記録）
- CHILD PMDA pilot 結果を V3 profile へ自動流用禁止

## 残リスク

- RAG が boundary hub を retrieve しない場合の hallucination
- V3 と CHILD 127 の key 重複による誤解
- integrated drug-profile 物理層が未整備
