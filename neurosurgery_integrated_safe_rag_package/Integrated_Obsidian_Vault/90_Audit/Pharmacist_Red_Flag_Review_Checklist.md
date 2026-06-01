---
note_type: "pharmacist_red_flag_review_checklist"
title: "Pharmacist Red Flag Review Checklist"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Pharmacist red flag review checklist"
source_quote_or_summary: "薬剤量、投与間隔、IV compatibility、TDM、repeat dosing、透析具体運用、CDS 実装は pharmacist review と source confirmation がない限り昇格しない。"
gpt_structured_interpretation: "pharmacist red-flag checklist は、未承認 drug data を approved content にしないための operator-side review scaffold である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認・EHR/CDS governance を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "薬剤量を source-confirmed and reviewed なしに標準化しない"
  - "投与間隔を source-confirmed and reviewed なしに標準化しない"
  - "IV compatibility を source-confirmed and reviewed なしに標準化しない"
  - "TDM adjustment を source-confirmed and reviewed なしに標準化しない"
  - "repeat dosing を source-confirmed and reviewed なしに標準化しない"
  - "透析具体運用を施設確認なしに標準化しない"
  - "production EHR/CDS behavior を governance review なしに作らない"
undetermined_from_source:
  - "PMDA product-level source"
  - "pharmacist review decision"
  - "facility formulary status"
  - "facility workflow and EHR/CDS governance"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "看護観察体制"
  - "EHR medication master"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "operator_side_audit_not_upload_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "薬剤師承認済み記録として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Pharmacist Red Flag Review Checklist

この文書は pharmacist review の checklist です。薬剤師承認そのものではありません。

## Red Flag Items

- dose or amount value appears as a recommendation.
- fixed dosing interval appears as an action rule.
- IV compatibility or admixture conclusion appears without source confirmation.
- repeat dosing is inferred from time alone.
- TDM or concentration is converted into action without sampling and assay context review.
- dialysis operation is treated as facility-ready.
- EHR/CDS candidate is written as production behavior.
- facility formulary or stock status is assumed.
- PMDA product-level source is missing.
- human review status is missing or not linked.

## Required Review Record

| field | required_state_before_approval |
| --- | --- |
| reviewer_role | pharmacist or delegated governance reviewer recorded |
| reviewer_identity | recorded outside generated text or linked audit record |
| review_date | recorded |
| source_scope | product-level source or unresolved status recorded |
| decision | approve or reject recorded by human reviewer |
| facility_scope | confirmed evidence link or pending/blocker recorded |

## Stop Conditions

- Keep the item unresolved if PMDA product-level evidence is absent.
- Keep the item unresolved if pharmacist review is not recorded.
- Keep the item pending if facility evidence is absent.
- Do not convert checklist completion into clinical approval.
