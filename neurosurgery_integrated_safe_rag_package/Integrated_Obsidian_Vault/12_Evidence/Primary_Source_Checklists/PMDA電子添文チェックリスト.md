---
note_type: "external_primary_source_checklist"
title: "PMDA電子添文チェックリスト"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "PMDA電子添文"
source_quote_or_summary: "PMDA電子添文で確認すべき項目を整理する。"
gpt_structured_interpretation: "原資料から確定できない事項を、外部一次資料・準一次資料に接続するためのチェックリスト。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "国内適応内/外をGPTが確定しない"
  - "海外GL記載を国内適応内と同一視しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "PMDA電子添文"
facility_confirmation_items:
  - "該当する施設内SOP"
  - "採用品"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "薬剤名だけで標準候補と判断しない"
  - "疾患名だけで薬剤選択しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# PMDA電子添文チェックリスト

## 1. 目的

このチェックリストは、Vault内の記載を外部一次資料・準一次資料で確認するためのものです。  
確認結果そのものを処方指示や院内手順として扱ってはいけません。

## 2. 確認項目

- 効能・効果
- 用法・用量
- 禁忌
- 警告
- 重要な基本的注意
- 腎機能・肝機能
- 妊娠可能性
- 相互作用
- 重大な副作用

## 3. 標準化しない事項

- 国内適応内/外をGPTが確定しない
- 海外GL記載を国内適応内と同一視しない

## 4. 更新対象

- 薬剤ノート
- 疾患ノート
- 患者状態ノート
- 処置予定ノート
- 条件・閾値ノート
- 陰性知識ノート
- RAG JSONL
