---
note_type: "integration_boundary"
title: "Guideline and Label Separation"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Guideline and label separation"
source_quote_or_summary: "ガイドライン、PMDA label、施設採用品、EHR/CDS candidate を同一視しないための境界を整理する。"
gpt_structured_interpretation: "ガイドライン記載、国内薬事、保険・査定、施設採用、EHR/CDS 実装は別軸であり、derived summary で単一の承認状態として自然化してはいけない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "ガイドライン記載を国内薬事確認の代替にしない"
  - "国内薬事確認を施設採用確認の代替にしない"
  - "施設採用確認を production EHR/CDS specification の代替にしない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "EHR/CDS governance review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "RMP / 安全性情報"
  - "Minds / 国内診療ガイドライン"
  - "学会ガイドライン"
  - "JAPIC"
  - "manufacturer documents"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "委員会承認"
  - "EHR medication master"
  - "EHR/CDS governance review"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "国内適応確認として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI がガイドラインと label の優劣を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Guideline and Label Separation

## 1. 目的

この文書は、ガイドライン記載、PMDA label、保険・査定、施設採用、EHR/CDS candidate を同一視しないための integrated boundary note です。
この文書は医療方針や処方指示ではなく、source class と承認状態を分離する operator-side governance です。

## 2. 分離する軸

- ガイドライン記載
- 国内薬事確認
- 保険・査定上の扱い
- 施設採用品と施設手順
- EHR medication master
- EHR/CDS governance review

## 3. Derived export rule

ガイドライン記載だけで国内薬事、施設採用、EHR/CDS 実装を確定したように見える summary は derived export してはいけません。
source traceability、human-review status、facility confirmation status が揃わない場合は unresolved として扱います。

## 4. 標準化しない事項

- ガイドライン記載を国内薬事確認の代替にしない。
- PMDA label 確認を施設採用確認の代替にしない。
- 施設採用確認を EHR/CDS governance review の代替にしない。
- EHR medication master 登録を production EHR/CDS specification として扱わない。

## 5. Quarantine trigger

ガイドライン、label、保険、施設採用、EHR/CDS candidate のいずれかを他の承認状態と同一視する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
