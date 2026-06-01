---
note_type: "tdm_steady_state_policy"
title: "TDM and Steady State Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "TDM and steady state policy"
source_quote_or_summary: "TDM、trough/peak、steady state、sampling time、assay context は、source confirmation と pharmacist review が必要な解釈領域として扱う。"
gpt_structured_interpretation: "TDM、trough/peak、steady state、sampling time、assay context、renal function context は、単独で薬剤判断を確定する十分条件ではなく、source confirmation、患者状態、施設検査運用、pharmacist review と分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "TDM result だけで薬剤判断を決めない"
  - "trough/peak だけで薬剤判断を確定しない"
  - "steady state の推定だけで投与管理を確定しない"
  - "sampling time または assay context が不明な値を確定判断に使わない"
  - "renal function context を確認せず TDM を自動解釈しない"
undetermined_from_source:
  - "採血時刻と投与時刻の関係"
  - "trough/peak の測定文脈"
  - "steady state の解釈範囲"
  - "assay context と検査運用"
  - "腎機能文脈と患者状態"
  - "薬剤師 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "検査運用"
  - "採血・検体運用"
  - "薬剤部手順"
  - "EHR medication master"
  - "EHR data availability"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "TDM 結果からの薬剤判断として扱わない"
  - "濃度または採血時刻だけで action が決まる根拠として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が TDM や steady state から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# TDM and Steady State Policy

## 目的

この文書は、TDM、trough/peak、steady state、sampling time、assay context を、AI が自動的な薬剤判断へ変換しないための integrated policy note です。
ここでは解釈に必要な確認軸だけを扱い、薬剤量、濃度に基づく action、固定された調整 rule、CDS trigger、production EHR/CDS behavior は定義しません。

## 基本原則

- TDM result は、薬剤判断の十分条件ではありません。
- trough/peak は、採血時刻、投与時刻、assay context、患者状態と分離して解釈しません。
- steady state は、source confirmation、患者状態、腎機能文脈、薬剤師 review が必要な解釈軸です。
- sampling time が不明な濃度情報は、確定的な薬剤判断に使いません。
- EHR 上に濃度や採血時刻が存在することは、production CDS specification の成立を意味しません。

## 確認軸

- TDM result context
- trough/peak context
- steady state interpretation
- sampling time
- assay context
- last administration time
- renal function context
- patient context
- source confirmation
- pharmacist review
- facility laboratory workflow
- EHR/CDS governance review

## Derived export rule

TDM や steady state に関する content は、source traceability、pharmacist review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。
未確認の内容は unresolved、operator-side checklist、または quarantine として分離します。

## Quarantine trigger

TDM result、trough/peak、steady state、sampling time、assay context、renal function context から、薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
