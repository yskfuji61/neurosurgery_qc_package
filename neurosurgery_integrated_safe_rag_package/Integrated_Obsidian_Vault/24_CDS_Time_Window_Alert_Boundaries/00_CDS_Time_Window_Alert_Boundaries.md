---
note_type: "cds_time_window_alert_boundary"
title: "CDS Time Window Alert Boundaries"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "CDS time-window alert boundaries"
source_quote_or_summary: "CDS time-window や alert に関する候補表現は、confirmation-promoting candidate と production EHR/CDS specification を分離して扱う。"
gpt_structured_interpretation: "CDS time-window、alert、EHR data availability は、human confirmation と EHR/CDS governance review を促す候補情報であり、production EHR/CDS specification、order set、automatic intervention ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "confirmation-promoting candidate only; production specification ではない"
not_to_standardize:
  - "CDS candidate を production EHR/CDS specification として扱わない"
  - "time-window 文脈だけで alert logic を確定しない"
  - "EHR data availability を clinical approval として扱わない"
  - "order set、automatic dose adjustment、automatic administration、automatic discontinuation を作らない"
undetermined_from_source:
  - "EHR data availability と data quality"
  - "time-window context の臨床的解釈"
  - "alert fatigue と workflow impact"
  - "human confirmation の責任範囲"
  - "EHR/CDS governance review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "EHR medication master"
  - "EHR data availability"
  - "EHR/CDS governance review"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "production EHR/CDS specification として扱わない"
  - "order set として扱わない"
  - "automatic intervention として扱わない"
  - "AI が time-window や alert candidate から薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# CDS Time Window Alert Boundaries

## 目的

この文書は、CDS time-window や alert に関する候補表現を、production EHR/CDS specification と誤読させないための integrated policy note です。
ここでは confirmation-promoting candidate と governance review requirement だけを定義し、order set、automatic dose adjustment、automatic administration、automatic discontinuation、final alert logic、production EHR/CDS behavior は定義しません。

## 基本原則

- CDS candidate は production EHR/CDS specification ではありません。
- time-window context は human confirmation を促す補助情報であり、automatic intervention の条件ではありません。
- EHR data availability は clinical approval、facility-ready、external-ready を意味しません。
- alert candidate は EHR/CDS governance review、workflow review、human review が必要な operator-side planning item として扱います。
- final alert logic は、この integrated policy note では作成しません。

## Candidate / production split

- confirmation-promoting candidate: source confirmation、患者文脈、施設運用、human review、EHR/CDS governance review を促す候補情報。
- production specification: 実装対象の alert logic、order set、automatic intervention、workflow behavior、責任者、監査記録、運用停止条件を含む施設承認済み仕様。
- Commit 6 で扱うのは confirmation-promoting candidate の境界だけです。

## 確認軸

- source confirmation
- patient context
- time-window context
- EHR data availability
- EHR data quality
- alert fatigue and workflow impact
- human confirmation responsibility
- pharmacist / clinician review
- EHR/CDS governance review
- facility committee approval

## Derived export rule

CDS time-window や alert candidate に関する content は、source traceability、human-review status、facility confirmation status、EHR/CDS governance review status が揃うまで、Custom GPT の user-facing conclusion として export してはいけません。
未確認の内容は unresolved、operator-side checklist、または quarantine として分離します。

## Quarantine trigger

CDS candidate、time-window context、EHR data availability、alert candidate から、order set、automatic dose adjustment、automatic administration、automatic discontinuation、final alert logic、production EHR/CDS behavior へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
