---
note_type: "clinical_data_policy"
title: "Lab Trend and Time Window Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Lab trend and time window policy"
source_quote_or_summary: "検査値の時系列、変化方向、測定条件、time-window 文脈を薬剤判断へ直結させず、source confirmation と human review を必須にする。"
gpt_structured_interpretation: "検査値の推移や time-window は review support であり、単独で薬剤判断、投与管理、CDS trigger を確定しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "単一の検査値だけで薬剤判断を決めない"
  - "検査値の推移だけで薬剤判断を確定しない"
  - "time-window 文脈だけで CDS trigger を確定しない"
  - "施設の検査運用を確認せず実装可能と扱わない"
undetermined_from_source:
  - "測定条件と検査運用"
  - "時系列と患者状態の解釈"
  - "施設内観察体制"
  - "human review の承認範囲"
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
  - "検査値推移からの薬剤判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が time-window 文脈から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Lab Trend and Time Window Policy

## 目的

この文書は、検査値の推移、変化方向、測定条件、time-window 文脈を薬剤判断へ直結させないための integrated policy note です。
ここでは review support としての扱いだけを定義し、数値閾値、具体的な時間窓、薬剤変更、CDS trigger は定義しません。

## 基本原則

- 単一の検査値は薬剤判断の十分条件ではありません。
- 検査値の推移は review support であり、薬剤判断の自動条件ではありません。
- time-window 文脈は測定条件、患者状態、施設運用と一緒に確認します。
- EHR 上の時系列データは production CDS specification の成立を意味しません。

## 確認軸

- 測定条件
- 検査運用
- 患者状態
- 時系列の解釈
- unit operation
- source confirmation
- human review
- EHR/CDS governance review

## Derived export rule

検査値推移や time-window 文脈に関する content は、source traceability、human-review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。

## Quarantine trigger

検査値の推移や time-window 文脈から薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
