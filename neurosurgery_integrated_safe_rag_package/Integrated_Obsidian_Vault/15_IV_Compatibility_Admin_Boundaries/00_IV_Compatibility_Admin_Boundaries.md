---
note_type: "integration_boundary"
title: "IV Compatibility and Administration Boundaries"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "IV compatibility and administration boundaries"
source_quote_or_summary: "IV compatibility、調製、投与経路、投与管理に関する情報を、source confirmation と facility confirmation が必要な境界領域として扱う。"
gpt_structured_interpretation: "IV compatibility や投与管理は source、濃度、溶媒、容器、時間条件、施設表、薬剤部手順に依存し、AI や derived summary が確定してはいけない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "IV compatibility を原資料だけで確定しない"
  - "施設表や薬剤部手順なしに投与管理を運用可能と扱わない"
  - "調製・投与経路に関する候補を処方指示として扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "施設内 compatibility table の扱い"
  - "薬剤部調製手順"
  - "看護観察体制と投与管理責任"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "interview form"
  - "manufacturer documents"
  - "RMP / 安全性情報"
facility_confirmation_items:
  - "薬剤部手順"
  - "facility compatibility table"
  - "採用品"
  - "看護体制"
  - "EHR medication master"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "IV compatibility 判断として扱わない"
  - "調製・投与手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が投与経路や調製を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# IV Compatibility and Administration Boundaries

## 1. 目的

この文書は、IV compatibility、調製、投与経路、投与管理に関する情報を、source confirmation と facility confirmation が必要な高リスク境界領域として扱うための integrated boundary note です。
ここでは確認責務と禁止解釈だけを定義し、compatibility status や具体的な調製・投与条件は定義しません。

## 2. 境界化する確認軸

- PMDA 製品単位確認
- interview form と manufacturer documents
- facility compatibility table
- 薬剤部手順
- 看護観察体制
- 採用品と EHR medication master
- 委員会承認

## 3. Derived export rule

IV compatibility、調製、投与経路、投与管理に関する内容は、source-confirmed、facility-confirmed、human-reviewed でない限り、Custom GPT の user-facing conclusion として export してはいけません。

## 4. 標準化しない事項

- 原資料だけで IV compatibility を確定しない。
- 施設表や薬剤部手順なしに調製・投与管理を運用可能と扱わない。
- 薬剤名だけで投与経路や compatibility を判断しない。
- CDS candidate を production EHR/CDS specification として扱わない。

## 5. Quarantine trigger

source-confirmed かつ facility-confirmed でない compatibility、調製、投与管理、投与経路に関する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
