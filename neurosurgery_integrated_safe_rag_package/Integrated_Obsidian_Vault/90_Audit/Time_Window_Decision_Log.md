---
note_type: "audit_decision_log"
title: "Time Window Decision Log"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Time-window and CDS audit"
source_quote_or_summary: "time-window、trend、CDS candidate は production logic ではなく review/audit 対象として記録する。"
gpt_structured_interpretation: "time-window decision log は unresolved status、human review requirement、facility confirmation requirement、EHR/CDS governance requirement を追跡する operator-side audit note である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "time-window 文脈だけで薬剤判断を決めない"
  - "CDS candidate を production specification として扱わない"
  - "unreviewed decision を approved と記録しない"
undetermined_from_source:
  - "time-window context の臨床的解釈"
  - "EHR data quality"
  - "human confirmation の責任範囲"
  - "EHR/CDS governance review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
facility_confirmation_items:
  - "EHR data availability"
  - "EHR/CDS governance review"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "operator_side_audit_not_upload_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "approved decision log として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Time Window Decision Log

この文書は operator-side audit log です。time-window、trend、CDS candidate を production logic として承認する文書ではありません。

| decision_id | domain | source_path | current_status | human_review_status | facility_confirmation_status | EHR_CDS_governance_status | quarantine_status | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TWD-001 | lab_trend_time_window | 20_Lab_Trend_Time_Window_Policy/00_Lab_Trend_Time_Window_Policy.md | unresolved_requires_review | required_not_recorded | pending_facility_review | not_applicable_until_CDS_candidate | no_active_quarantine_repo_local | Record clinician/pharmacist review before any derived export. |
| TWD-002 | statistical_aggregation | 23_Statistical_Aggregation_Policy/00_Statistical_Aggregation_Policy.md | unresolved_requires_review | required_not_recorded | pending_facility_review | not_applicable_until_CDS_candidate | no_active_quarantine_repo_local | Confirm aggregation remains review support only. |
| TWD-003 | CDS_time_window_alert | 24_CDS_Time_Window_Alert_Boundaries/00_CDS_Time_Window_Alert_Boundaries.md | unresolved_requires_EHR_CDS_governance_review | required_not_recorded | pending_facility_review | required_not_recorded | no_active_quarantine_repo_local | Record EHR/CDS governance review and facility committee evidence before production planning. |

## Stop Conditions

- Do not mark any row approved without recorded human review evidence.
- Do not mark any row facility confirmed without evidence link.
- Do not convert candidate text into order sets, automatic intervention, or production alert logic.
