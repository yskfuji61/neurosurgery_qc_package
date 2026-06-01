---
note_type: "validation_report"
title: "Safety Term Scan Report"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Safety term scan"
source_quote_or_summary: "unsafe medical action terms, source-traceability gaps, and unresolved gates are tracked as operator-side validation state."
gpt_structured_interpretation: "この report は unsafe shortcuts を検出・隔離するための scan report であり、医療判断、処方指示、施設手順、CDS 仕様ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "unsafe term scan pass を clinical approval と扱わない"
  - "numeric assertion absence を PMDA confirmation と扱わない"
  - "operator-side report を upload target にしない"
undetermined_from_source:
  - "human review decision"
  - "facility confirmation evidence"
  - "Preview approval evidence"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "国内診療ガイドライン"
  - "学会ガイドライン"
facility_confirmation_items:
  - "facility evidence link"
  - "EHR/CDS governance review"
  - "committee approval"
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

# Safety Term Scan Report

この report は Commit 9 の operator-side safety scan report です。validation pass は clinical approval、external-ready、facility-ready、Preview approved を意味しません。

## Safety Scan Scope

- unsafe pattern scan in derived package
- integrated policy control gate
- frontmatter gate
- JSONL schema gate
- knowledge integrity gate
- release readiness gate
- review-state gate
- quarantine integrity gate
- reference repo safe knowledge / manifest / PMDA resolution gates

## Terms That Must Not Be Promoted Without Evidence

| term area | safe handling |
| --- | --- |
| dose / amount | keep absent or unresolved unless source-confirmed and reviewed |
| dosing interval | keep absent or unresolved unless source-confirmed and reviewed |
| IV compatibility / admixture | keep absent or unresolved unless source-confirmed and reviewed |
| repeat dosing | keep as interpretation boundary, not action rule |
| TDM adjustment | keep as review domain, not concentration-to-action rule |
| dialysis operation | keep pending facility confirmation |
| CDS trigger / production behavior | keep candidate / production split and require EHR/CDS governance review |
| facility-ready / external-ready | do not use without evidence gates |
| approved / confirmed | do not use for unreviewed or evidence-absent rows |

## Current Gate Snapshot

| gate | current_state |
| --- | --- |
| active derived quarantine rows | 0 |
| reference migration quarantine decisions | 1 traceable decision remains |
| export_candidate yes rows | 0 |
| external-ready candidates | 0 |
| Preview approved rows | 0 |
| human-review recorded rows | 0 |
| facility confirmed/not_applicable rows | 0 / 0 |
| PMDA product-level resolved rows | 0 |

## Stop Conditions

- Do not move unresolved or quarantined content into derived knowledge.
- Do not treat operator-side report files as Custom GPT upload targets.
- Do not silently resolve terminology, source, or safety collisions.
