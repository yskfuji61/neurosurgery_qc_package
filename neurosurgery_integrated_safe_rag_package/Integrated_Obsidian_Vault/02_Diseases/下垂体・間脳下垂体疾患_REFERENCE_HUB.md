---
note_type: "disease_reference_hub"
title: "下垂体・間脳下垂体疾患_REFERENCE_HUB"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
human_review_required: true
audit_status: "reference_routing_only"
collision_id: "GAP-V3-COLLISION-PITUITARY-001"
last_reviewed: "2026-06-04"
---

# 下垂体・間脳下垂体疾患 — REFERENCE HUB（治療推奨本文ではない）

## 位置づけ

このノートは **routing hub** のみ。診療ガイドライン・処方指示・施設内手順の代替ではない。

- **境界ハブ:** [[04_Drug_Classes/下垂体内分泌薬_境界と出典階層]]
- **Collision:** [[90_Audit/Collisions/gap_v3_pituitary_endocrine_reference_collision]]
- **Archive profiles:** `reference_archive/.../pituitary_endocrine/*.md`

## Routing（混同禁止）

| 文脈 | 扱い |
|------|------|
| 術後 DI / desmopressin 文脈 note | reference-only。慢性水欠症の確定処方にしない |
| 副腎不全 stress steroid 文脈 | reference-only。無条件ステロイド増量指示にしない |
| SIADH / CSW | 鑑別・施設プロトコル確認。固定補正ルールを書かない |
| プロラクチノーマ / 先端巨大症 / クッシング病 | 内分泌専門・製品単位 PMDA 確認後 |
| ドパミン作動薬 / ソマトスタチン系 | 製品単位ラベル・施設採用品を先に確認 |

## 添付文書・適用外（routing のみ）

- 用法・用量・使用方法: **製品単位の最新電子添文（PMDA）** で確認。本 HUB および archive reference から数値・投与期間を断定しない。
- 適用外使用: **医師の個別判断なし**に標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- 正本: [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

## Export 禁止

- `pituitary_endocrine/*.md` 本文の user-facing export
- 用量・投与期間・PMDA URL の推測記載

## 昇格条件（PMDA 解決後）

1. 製品単位 PMDA primary 確認
2. 薬剤師・内分泌・脳外の施設レビュー記録
3. `collision_resolution_ledger.csv` の `export_status` 更新（operator）
