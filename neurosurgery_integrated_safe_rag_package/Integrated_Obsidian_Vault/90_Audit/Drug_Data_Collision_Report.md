---
note_type: "collision_report"
title: "Drug Data Collision Report"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Drug data collision report"
source_quote_or_summary: "drug data expansion に関する source, terminology, review, facility, Preview, quarantine collisions を silent resolution せず記録する。"
gpt_structured_interpretation: "この collision report は unresolved gate と required next action を記録する operator-side audit document であり、医療判断や承認済み source register ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "collision を silent resolution しない"
  - "unverified source material を approved と記録しない"
  - "PMDA unresolved drug を product-level resolved と扱わない"
  - "facility pending row を external-ready と扱わない"
undetermined_from_source:
  - "PMDA product-level source"
  - "human review decision"
  - "facility confirmation evidence"
  - "Preview approval evidence"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "facility evidence link"
  - "EHR medication master"
  - "committee approval"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "operator_side_collision_report_not_upload_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "承認済み collision resolution として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Drug Data Collision Report

この report は Commit 9 の operator-side collision report です。collision の存在、未解決 gate、必要な operator action を記録し、silent resolution を防ぎます。

## Collision Summary

| collision_id | collision_type | affected_surface | current_status | required_next_action |
| --- | --- | --- | --- | --- |
| DCR-001 | PMDA product-level source missing | 127 drug inventory rows | unresolved | collect product-level source evidence manually; do not guess product fields |
| DCR-002 | validation pass vs external approval | validation reports and validators | unresolved distinction required | keep repo-local pass separate from PMDA/pharmacist/facility/Preview approval |
| DCR-003 | human review missing | derived export candidate ledger and audit registers | unresolved | record reviewer, date, scope, and approve/reject before export candidate promotion |
| DCR-004 | facility evidence missing | facility confirmation ledger and source registers | pending | add evidence_link before confirmed or not_applicable |
| DCR-005 | Preview evidence missing | human_reviewed_preview_examples.md | pending | record actual Preview raw output, normalized output, and reviewer decision |
| DCR-006 | reference quarantine decision remains traceable | reference migration decision ledger | unresolved / traceable | keep quarantine decision separated from upload target until reviewed |
| DCR-007 | CDS candidate vs production behavior | CDS time-window alert boundary | unresolved until governance review | keep candidate / production split; do not write final alert logic |

## No Silent Resolution Rule

- A collision is resolved only when source evidence, human review, facility evidence, and applicable governance evidence are linked.
- Repo-local validation pass does not resolve PMDA, pharmacist, facility, Preview, or EHR/CDS governance collisions.
- Absence of active derived quarantine rows does not erase reference-level quarantine decisions.

## Current Evidence State

| evidence_type | current_state |
| --- | --- |
| PMDA product-level resolved rows | 0 |
| PMDA unresolved rows | 127 |
| human-review recorded rows | 0 |
| facility confirmed/not_applicable rows | 0 / 0 |
| Preview approved rows | 0 |
| export_candidate=yes rows | 0 |
| external-ready candidates | 0 |

## Stop Conditions

- Do not mark any collision resolved without linked evidence.
- Do not promote unresolved collision content into derived knowledge.
- Do not use this report as clinical approval, facility approval, or production EHR/CDS specification.
