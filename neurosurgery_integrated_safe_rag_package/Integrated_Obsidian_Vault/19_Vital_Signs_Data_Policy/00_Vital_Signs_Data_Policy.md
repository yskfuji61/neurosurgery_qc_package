---
note_type: "clinical_data_policy"
title: "Vital Signs Data Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Vital signs data policy"
source_quote_or_summary: "血圧、体温、呼吸循環などのバイタル値を薬剤判断へ直結させず、測定条件、症状、時系列、施設観察体制を分離する。"
gpt_structured_interpretation: "単一のバイタル値は薬剤判断の十分条件ではなく、測定条件、症状、患者状態、時系列、施設観察体制、human review が必要である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "単一の血圧値だけで薬剤判断を決めない"
  - "単一の体温値だけで抗菌薬判断を決めない"
  - "測定条件が不明なバイタル値を確定判断に使わない"
  - "施設観察体制なしに CDS 実装可能と扱わない"
undetermined_from_source:
  - "測定条件とデータ品質"
  - "症状と患者状態の解釈"
  - "時系列と観察体制"
  - "臨床担当者 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "看護観察体制"
  - "病棟・ICU・SCU・HCU の運用"
  - "EHR data availability"
  - "EHR/CDS governance review"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "単一バイタル値からの薬剤判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI がバイタル値から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Vital Signs Data Policy

## 目的

この文書は、血圧、体温、呼吸循環などのバイタル値を薬剤判断へ直結させないための integrated policy note です。
ここでは測定条件、症状、患者状態、時系列、施設観察体制を分離し、薬剤変更や CDS trigger は定義しません。

## 基本原則

- 単一の血圧値は薬剤判断の十分条件ではありません。
- 単一の体温値は抗菌薬判断の十分条件ではありません。
- 測定条件、症状、患者状態、時系列、観察体制を分離して確認します。
- EHR 上に値があることは、production CDS specification の成立を意味しません。

## 確認軸

- 測定条件
- 症状と患者状態
- 時系列
- 看護観察体制
- unit operation
- source confirmation
- clinician review
- EHR/CDS governance review

## Derived export rule

バイタル値に関する content は、source traceability、human-review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。

## Quarantine trigger

単一のバイタル値から薬剤開始、薬剤変更、抗菌薬判断、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
