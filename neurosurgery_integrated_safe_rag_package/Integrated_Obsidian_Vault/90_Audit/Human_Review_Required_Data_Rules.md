---
note_type: "human_review_rules"
title: "Human Review Required Data Rules"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Human review required data rules"
source_quote_or_summary: "薬剤情報、臨床データ、time-window、TDM、CDS candidate は human review と source confirmation が揃うまで export しない。"
gpt_structured_interpretation: "human review rules は未承認 content の昇格を防ぐ operator-side gate であり、医療判断や承認記録ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "human review 未記録 row を export candidate にしない"
  - "Preview evidence 未記録 row を promotion しない"
  - "facility pending row を confirmed と扱わない"
  - "validation pass を clinical approval と扱わない"
undetermined_from_source:
  - "human reviewer identity"
  - "review date"
  - "approve or reject decision"
  - "facility evidence link"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
facility_confirmation_items:
  - "facility evidence link"
  - "committee approval"
  - "EHR/CDS governance review"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "operator_side_audit_not_upload_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "承認済み review record として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Human Review Required Data Rules

この文書は operator-side gate です。human review の必要条件を列挙しますが、review 完了を意味しません。

## Required Review Before Derived Export

- source traceability must be present.
- human review status must be recorded as approve or reject with reviewer and date.
- facility confirmation status must have evidence before confirmed or not_applicable is used.
- Preview evidence must include raw output, lightly normalized output, and approve/reject before promotion.
- active quarantine must be resolved or explicitly blocked before external-ready consideration.

## Current Repository State

| gate | current_status | required_next_action |
| --- | --- | --- |
| PMDA product-level resolution | 127 rows unresolved | Manually collect product-level source evidence without guessing. |
| human review | not recorded | Record reviewer, date, scope, raw reviewed content, and approve/reject. |
| facility confirmation | pending facility review | Add evidence_link before confirmed or not_applicable. |
| Preview approval | no approved Preview rows | Record actual Custom GPT Preview raw output and reviewer decision. |
| derived export candidate | zero yes rows | Keep export_candidate=no until review and evidence gates are satisfied. |

## Stop Conditions

- Do not write approved, confirmed, facility-ready, or external-ready without evidence.
- Do not use validation pass as clinical approval.
- Do not promote content with missing source traceability or missing human review status.
