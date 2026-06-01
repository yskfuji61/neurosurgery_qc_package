---
note_type: "clinical_data_policy"
title: "Clinical Data Reference Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Clinical data reference policy"
source_quote_or_summary: "臨床データを薬剤判断へ直結させず、患者状態、測定条件、時系列、source confirmation、human review を分離する。"
gpt_structured_interpretation: "単一の検査値や単一のバイタル値は薬剤判断の十分条件ではなく、source confirmation、施設内観察体制、患者文脈、human review が必要である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "単一の検査値から薬剤判断へ直結しない"
  - "単一のバイタル値から薬剤判断へ直結しない"
  - "測定条件や時系列が不明な値を確定判断に使わない"
  - "EHR data availability を clinical approval として扱わない"
undetermined_from_source:
  - "測定条件とデータ品質"
  - "患者状態と時系列の解釈"
  - "施設内観察体制"
  - "薬剤師・臨床担当者 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "看護観察体制"
  - "検査運用"
  - "EHR medication master"
  - "EHR data availability"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "単一データからの薬剤判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が臨床データから薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Clinical Data Reference Policy

## 目的

この文書は、検査値、バイタル、観察情報、EHR 上のデータを薬剤判断へ直結させないための integrated policy note です。
ここでは確認軸と禁止解釈だけを扱い、数値閾値、時間窓、薬剤変更、CDS trigger は定義しません。

## 基本原則

- 単一の検査値は薬剤判断の十分条件ではありません。
- 単一のバイタル値は薬剤判断の十分条件ではありません。
- 測定条件、患者状態、時系列、検査運用、施設内観察体制を分離して確認します。
- EHR に値が存在することは、clinical approval や production CDS specification の成立を意味しません。

## 確認軸

- source confirmation
- patient context
- measurement condition
- data quality
- trend context
- facility observation capability
- pharmacist and clinician review
- EHR/CDS governance review

## Derived export rule

臨床データに関する内容は、source traceability、human-review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。
未確認の内容は unresolved、operator-side checklist、または quarantine として分離します。

## Quarantine trigger

単一の臨床データから薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
