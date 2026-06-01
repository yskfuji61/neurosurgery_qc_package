---
note_type: "validation_report"
title: "Drug Data Policy Validation Report"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Drug data policy validation"
source_quote_or_summary: "drug data policy の validation gate と unresolved evidence を operator-side report として記録する。"
gpt_structured_interpretation: "この report は source traceability、review gate、facility gate、quarantine gate の状態を記録するものであり、医療判断または承認済み drug policy ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "validation pass を clinical approval と扱わない"
  - "PMDA unresolved row を confirmed と扱わない"
  - "human review 未記録 row を export candidate にしない"
undetermined_from_source:
  - "PMDA product-level source"
  - "pharmacist review decision"
  - "facility evidence link"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "EHR medication master"
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

# Drug Data Policy Validation Report

この report は Commit 9 の operator-side validation report です。薬剤方針の承認、PMDA 製品単位確認、薬剤師 review、施設確認、Custom GPT Preview approval を意味しません。

## Scope

- Source hierarchy policy
- Dosing adjustment boundary
- Interaction / contraindication boundary
- IV compatibility / administration boundary
- Guideline-label-facility-CDS separation
- Repeat dosing / interval policy
- TDM / steady state policy
- Drug source register and pharmacist red-flag checklist

## Repo-Local Gate Snapshot

| gate | repo-local status | external-ready meaning |
| --- | --- | --- |
| integrated source hierarchy | present | not clinical approval |
| drug information boundaries | present | not prescribing guidance |
| repeat dosing / TDM boundaries | present | no fixed interval or concentration-to-action approval |
| drug source register | present | all rows remain not approved |
| pharmacist red-flag checklist | present | checklist only, not pharmacist sign-off |
| PMDA product-level resolution | 0 resolved / 127 unresolved | external-ready blocked |
| derived export candidates | 0 yes | no user-facing promotion |

## Unresolved Gates

| unresolved_gate | blocking_reason | required_operator_action |
| --- | --- | --- |
| PMDA product-level source | product-level evidence is absent in repo-local source | manually collect product name, formulation, strength, manufacturer, and source URL without guessing |
| pharmacist review | reviewer, date, source scope, and approve/reject are not recorded | record pharmacist review evidence per row or domain |
| facility confirmation | evidence_link is absent | add facility evidence link before confirmed or not_applicable |
| Custom GPT Preview | approved Preview rows are absent | manually record raw output, normalized output, and reviewer decision |

## Collision / Quarantine State

- No derived active quarantine rows are present in the derived quarantine register.
- Reference migration ledger still contains one `no_port_quarantine` decision and must remain traceable.
- No unresolved drug-data collision is silently resolved by this report.

## Stop Conditions

- Do not treat this report as approval.
- Do not derive dose, interval, IV compatibility, TDM adjustment, repeat dosing, dialysis operation, or production EHR/CDS behavior from this report.
- Do not proceed to derived export unless source traceability, human review, facility evidence, and Preview evidence gates are satisfied.
