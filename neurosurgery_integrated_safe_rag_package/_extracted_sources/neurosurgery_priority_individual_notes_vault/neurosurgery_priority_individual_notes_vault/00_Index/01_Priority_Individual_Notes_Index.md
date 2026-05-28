---
note_type: "index"
title: "Priority Individual Notes Index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Phase 0〜23監査結果に基づく次工程"
source_quote_or_summary: "最小安全セットとCore Expansionの次工程として、Layer 1高リスク薬剤、主要疾患、患者状態、処置予定、CDS候補を個別ノート化する。"
gpt_structured_interpretation: "薬剤名・疾患名だけで候補化する誤読を避けるため、個別ノートでも陰性知識、外部一次資料確認、施設内確認を明示する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "このIndexを医学的推奨一覧として扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部調製・払い出し手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "index_not_primary_rag_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# Priority Individual Notes Index

このパックは、前回までの最小安全セットとCore Expansionを土台に、次工程として優先個別ノートを追加するものです。

## 含めた範囲

- Layer 1高リスク薬剤 15件
- 主要疾患ハブ 10件
- 患者状態ハブ 12件
- 処置予定ハブ 8件
- CDS候補ノート 5件
- AI誤回答テスト拡張
- CSV/JSONL/YAML Export

## まだ含めない範囲

- 全Layer 2薬剤の詳細ノート
- 全疾患の完全ノート
- 院内採用品・夜間在庫・薬剤部SOPの確定値
- 電子カルテ実装仕様
