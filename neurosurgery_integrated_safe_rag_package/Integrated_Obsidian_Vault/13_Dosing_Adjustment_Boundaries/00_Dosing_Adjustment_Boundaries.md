---
note_type: "integration_boundary"
title: "Dosing Adjustment Boundaries"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Dosing adjustment boundaries"
source_quote_or_summary: "薬剤量調整に関する記載を、source confirmation と human review が必要な境界領域として扱う。"
gpt_structured_interpretation: "薬剤量調整は原資料だけで確定せず、PMDA 製品単位確認、患者状態、併用薬、施設確認、薬剤師 review を分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "原資料だけで薬剤量調整を確定しない"
  - "単一の腎機能値だけで薬剤量調整を決めない"
  - "透析条件や施設手順を確認せず運用可能と扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "腎機能評価方法と患者状態の解釈"
  - "透析条件と施設内手順"
  - "薬剤師 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "RMP / 安全性情報"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "透析関連施設手順"
  - "EHR medication master"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "患者個別の薬剤量判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が薬剤量調整を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Dosing Adjustment Boundaries

## 1. 目的

この文書は、薬剤量調整に関する情報を Custom GPT や derived summary に自然化しないための integrated boundary note です。
ここでは確認軸と禁止解釈だけを扱い、患者個別の薬剤量、間隔、変更手順は定義しません。

## 2. 境界化する確認軸

- PMDA 製品単位確認
- 患者状態と腎機能評価方法
- 透析条件と施設手順
- 併用薬と相互作用
- 薬剤師 review
- EHR medication master と施設承認

## 3. Derived export rule

薬剤量調整に関する内容は、source path、source revision、human-review status、facility confirmation status が揃うまで、derived knowledge へ user-facing conclusion として export してはいけません。

## 4. 標準化しない事項

- 原資料だけで薬剤量調整を確定しない。
- 単一の検査値だけで薬剤量調整を決めない。
- 透析条件や施設手順が未確認のまま operationally available と扱わない。
- EHR medication master 登録を薬剤師 review の代替にしない。

## 5. Quarantine trigger

薬剤量、変更手順、透析時の扱い、患者個別の薬剤判断が source-confirmed かつ human-reviewed でないまま user-facing conclusion として現れた場合は、derived export ではなく quarantine / unresolved として扱います。
