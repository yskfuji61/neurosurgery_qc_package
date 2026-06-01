---
note_type: "validation_report"
title: "Clinical Data Policy Validation Report"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Clinical data policy validation"
source_quote_or_summary: "clinical data policy の single-value、trend、aggregation、time-window、CDS candidate gate を operator-side report として記録する。"
gpt_structured_interpretation: "この report は clinical data を medication action に直結させないための validation state を記録するものであり、医療判断または施設 CDS 仕様ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "検査運用・看護観察体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "単一データから medication action を決めない"
  - "time-window 文脈から production CDS を作らない"
  - "aggregation method を action logic として扱わない"
undetermined_from_source:
  - "measurement condition"
  - "data quality"
  - "patient context"
  - "facility workflow"
  - "EHR/CDS governance review"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
facility_confirmation_items:
  - "検査運用"
  - "看護観察体制"
  - "EHR data availability"
  - "EHR/CDS governance review"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "operator_side_validation_report_not_upload_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "外部利用可能な承認済み report として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Clinical Data Policy Validation Report

この report は Commit 9 の operator-side validation report です。clinical data の医療判断化、薬剤判断化、施設 CDS 仕様化を承認するものではありません。

## Scope

- Clinical data reference policy
- Renal function data policy
- Vital signs data policy
- Lab trend / time-window policy
- Statistical aggregation policy
- CDS time-window alert boundary
- Clinical data source register
- Time-window decision log

## Repo-Local Gate Snapshot

| gate | repo-local status | external-ready meaning |
| --- | --- | --- |
| single-value decision prohibition | present | not clinical approval |
| renal / vital / lab trend boundary | present | no patient-specific medication action |
| statistical aggregation boundary | present | review support only |
| CDS candidate / production split | present | no production EHR/CDS behavior |
| clinical data source register | present | all rows remain not approved |
| time-window decision log | present | unresolved until review evidence exists |

## Unresolved Gates

| unresolved_gate | blocking_reason | required_operator_action |
| --- | --- | --- |
| clinical human review | reviewer/date/decision evidence is absent | record clinician/pharmacist review evidence |
| facility confirmation | evidence_link is absent | add facility evidence link before confirmed or not_applicable |
| EHR/CDS governance review | governance review evidence is absent | record governance review before production planning |
| Preview approval | approved Preview rows are absent | manually record Custom GPT Preview evidence and reviewer decision |

## Collision / Quarantine State

- Clinical data, time-window, aggregation, and CDS candidate material remains operator-side or integrated policy material.
- No derived user-facing clinical data export is permitted by this report.
- Any value-to-medication-action or candidate-to-production-CDS statement must remain unresolved or quarantined.

## Stop Conditions

- Do not treat single value, trend, aggregation, or time-window context as sufficient for medication action.
- Do not treat EHR data availability as clinical approval or facility-ready status.
- Do not use this report as production CDS specification.
