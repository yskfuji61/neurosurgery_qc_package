---
note_type: "integration_boundary"
title: "Interactions and Contraindications Boundaries"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Interactions and contraindications boundaries"
source_quote_or_summary: "相互作用、禁忌、注意事項を source confirmation と human review が必要な境界領域として扱う。"
gpt_structured_interpretation: "相互作用や禁忌は薬剤名の組み合わせだけで確定せず、PMDA 製品単位確認、患者状態、併用薬、時系列、施設手順、薬剤師 review を分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "薬剤名の組み合わせだけで相互作用を確定しない"
  - "海外資料だけで国内の禁忌や注意事項を確定しない"
  - "相互作用候補を production CDS logic として扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "患者状態と併用薬の解釈"
  - "施設内採用薬と代替薬の扱い"
  - "薬剤師 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "RMP / 安全性情報"
  - "interview form"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "EHR medication master"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "患者個別の相互作用判断として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が禁忌や相互作用の最終判断を行う根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Interactions and Contraindications Boundaries

## 1. 目的

この文書は、相互作用、禁忌、注意事項を source-confirmed で human-reviewed な情報に限定して扱うための integrated boundary note です。
薬剤名の組み合わせだけで、患者個別の判断や CDS 実装を決めるものではありません。

## 2. 境界化する確認軸

- PMDA 製品単位確認
- RMP / 安全性情報
- 併用薬と投与文脈
- 患者状態
- 施設内採用薬と代替薬
- 薬剤師 review
- EHR/CDS governance review

## 3. Derived export rule

相互作用や禁忌に関する内容は、source traceability と review status が揃わない限り、Custom GPT の user-facing conclusion として export してはいけません。
未確認のものは候補、unresolved、または quarantine として分離します。

## 4. 標準化しない事項

- 薬剤名だけで禁忌または併用可否を確定しない。
- 海外資料だけで国内薬事上の扱いを確定しない。
- EHR medication master の登録を相互作用 review の代替にしない。
- alert candidate を production CDS logic として扱わない。

## 5. Quarantine trigger

source-confirmed かつ human-reviewed でない相互作用、禁忌、併用可否、患者個別の判断が user-facing conclusion として現れた場合は、derived export ではなく quarantine / unresolved として扱います。
