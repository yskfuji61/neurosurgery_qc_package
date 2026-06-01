---
note_type: "statistical_aggregation_policy"
title: "Statistical Aggregation Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Statistical aggregation policy"
source_quote_or_summary: "統計集約は review support であり、単独で薬剤判断、投与管理、CDS trigger、production EHR/CDS behavior を確定しない。"
gpt_structured_interpretation: "single value、mean、median、moving average、maximum、latest value、rate of change、slope、outlier、missing data、time-window context は、患者状態、測定条件、source confirmation、human review と分離して扱う review-support 情報である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "統計集約値だけで薬剤判断を決めない"
  - "平均値または中央値だけで薬剤判断を確定しない"
  - "moving average、rate of change、slope だけで CDS trigger を確定しない"
  - "outlier または missing data の扱いを施設確認なしに自動処理しない"
undetermined_from_source:
  - "集約対象データの測定条件"
  - "欠測値と外れ値の扱い"
  - "time-window context の運用上の解釈"
  - "統計集約 use case の human review 範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "検査運用"
  - "看護観察体制"
  - "EHR data availability"
  - "EHR/CDS governance review"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "統計手法からの薬剤判断として扱わない"
  - "統計集約を automated medical decision logic として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が統計集約から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Statistical Aggregation Policy

## 目的

この文書は、統計集約を automated medical decision logic と誤読させないための integrated policy note です。
ここでは review support としての境界だけを定義し、数値閾値、具体的な time-window、薬剤変更、CDS trigger、production EHR/CDS behavior は定義しません。

## 基本原則

- statistical aggregation は薬剤判断の十分条件ではありません。
- single value、mean、median、moving average、maximum、latest value は、測定条件と患者状態から切り離して解釈しません。
- rate of change と slope は trend review の補助情報であり、薬剤判断や CDS 実装の自動条件ではありません。
- outlier と missing data は、施設のデータ品質ルール、検査運用、human review と一緒に扱います。
- time-window context は review support であり、単独で action logic にはしません。

## 確認軸

- aggregation method
- source data quality
- measurement condition
- missing data handling
- outlier handling
- time-window context
- patient context
- source confirmation
- human review
- facility data governance
- EHR/CDS governance review

## Derived export rule

統計集約に関する content は、source traceability、human-review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。
未確認の統計集約 rule は unresolved、operator-side checklist、または quarantine として分離します。

## Quarantine trigger

single value、mean、median、moving average、maximum、latest value、rate of change、slope、outlier、missing data、time-window context から、薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
