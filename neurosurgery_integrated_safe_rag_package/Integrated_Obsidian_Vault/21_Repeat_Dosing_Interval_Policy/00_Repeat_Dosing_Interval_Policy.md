---
note_type: "repeat_dosing_interval_policy"
title: "Repeat Dosing Interval Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Repeat dosing interval policy"
source_quote_or_summary: "repeat dosing、last administration time、cumulative exposure、dosing interval は、source confirmation と pharmacist review が必要な解釈領域として扱う。"
gpt_structured_interpretation: "last administration time、cumulative exposure、dosing interval は単独で薬剤判断を確定する十分条件ではなく、患者状態、腎機能文脈、source confirmation、施設運用、pharmacist review と分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "last administration time だけで反復投与可否を決めない"
  - "cumulative exposure だけで薬剤判断を確定しない"
  - "dosing interval を施設確認なしに固定 rule として扱わない"
  - "EHR timestamp だけで production CDS behavior を作らない"
undetermined_from_source:
  - "最終投与時刻の信頼性"
  - "累積曝露の解釈範囲"
  - "患者状態と腎機能文脈"
  - "薬剤師 review の承認範囲"
  - "施設内投与記録と EHR timestamp の運用差"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "薬剤部手順"
  - "投与記録運用"
  - "看護観察体制"
  - "EHR medication master"
  - "EHR timestamp governance"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "反復投与の固定 rule として扱わない"
  - "投与間隔からの薬剤判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が時刻や間隔から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Repeat Dosing Interval Policy

## 目的

この文書は、repeat dosing、last administration time、cumulative exposure、dosing interval を、AI が自動的な薬剤判断へ変換しないための integrated policy note です。
ここでは解釈に必要な確認軸だけを扱い、固定された投与間隔、薬剤量、再投与手順、CDS trigger、production EHR/CDS behavior は定義しません。

## 基本原則

- last administration time は、反復投与や薬剤判断の十分条件ではありません。
- cumulative exposure は、患者状態、腎機能文脈、併用薬、source confirmation と分離して解釈します。
- dosing interval は、PMDA 製品単位確認、施設内投与記録、薬剤師 review が必要な解釈軸です。
- EHR timestamp が存在することは、production CDS specification の成立を意味しません。

## 確認軸

- last administration time
- cumulative exposure
- medication administration record reliability
- renal function context
- patient context
- concomitant medication context
- source confirmation
- pharmacist review
- facility administration workflow
- EHR/CDS governance review

## Derived export rule

repeat dosing や dosing interval に関する content は、source traceability、pharmacist review status、facility confirmation status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。
未確認の内容は unresolved、operator-side checklist、または quarantine として分離します。

## Quarantine trigger

last administration time、cumulative exposure、dosing interval から、反復投与、薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
