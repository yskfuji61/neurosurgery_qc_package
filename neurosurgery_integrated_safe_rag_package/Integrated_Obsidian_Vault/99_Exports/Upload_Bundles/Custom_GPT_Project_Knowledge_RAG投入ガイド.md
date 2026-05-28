---
note_type: "export_guide"
title: "Custom GPT Project Knowledge RAG投入ガイド"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "統合Export工程"
source_quote_or_summary: "統合VaultをCustom GPT、Project Knowledge、RAGに投入する際の安全な手順を整理する。"
gpt_structured_interpretation: "RAG投入時は、Markdown原本、CSV監査表、JSONLを用途別に分け、未監査の施設内運用値を確定済みとして扱わない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "技術的投入手順であり医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "統合JSONLを承認済みCDS仕様として扱わない"
  - "Custom GPT回答を処方指示として扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk_with_not_to_interpret_as"
not_to_interpret_as:
  - "正式な診療ガイドライン"
  - "正式な処方指示"
  - "施設内手順"
  - "即時CDS仕様"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# Custom GPT / Project Knowledge / RAG投入ガイド

## 1. 推奨投入順序

1. `00_Index/`
2. `01_Positioning/`
3. `07_Warnings/`
4. `08_Negative_Knowledge/`
5. `91_AI_Error_Tests/`
6. `02_Diseases/`, `05_Patient_States/`, `06_Procedures/`
7. `03_Drugs/`, `04_Drug_Classes/`
8. `09_Regulatory_Insurance/`, `10_Operationalization/`, `12_Evidence/`
9. `99_Exports/Unified_RAG/unified_safe_rag_seed.jsonl`

## 2. RAG投入時の必須条件

- `not_to_interpret_as` が空のchunkは投入しない。
- `human_review_required` がfalseのchunkは作らない。
- 施設内採用品・在庫・薬剤部手順・看護体制が未確認の内容を「運用可能」と回答させない。
- 診療支援候補を即時実装仕様として回答させない。

## 3. 投入後に必ず実行するテスト

- `91_AI_Error_Tests/` 以下の全テスト。
- `99_Exports/Validation_Reports/yaml_frontmatter_required_keys_audit.csv` の未充足項目確認。
- 高リスク薬剤に関する誤回答テスト。
