---
note_type: "clinical_data_policy"
title: "Renal Function Data Policy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Renal function data policy"
source_quote_or_summary: "腎機能データを薬剤判断へ直結させず、評価方法、患者状態、急性変化、透析条件、source confirmation を分離する。"
gpt_structured_interpretation: "腎機能データは薬剤判断の補助情報であり、単一値だけで薬剤量調整や透析時運用を確定しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "単一の腎機能値だけで薬剤量調整を決めない"
  - "AKI と安定した慢性腎機能低下を同一視しない"
  - "透析条件を施設確認なしに薬剤運用へ反映しない"
  - "EHR 上の腎機能値だけで CDS 実装可能と扱わない"
undetermined_from_source:
  - "腎機能評価方法"
  - "AKI と安定した慢性腎機能低下の区別"
  - "透析条件と施設内手順"
  - "薬剤師 review の承認範囲"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "interview form"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "検査運用"
  - "透析関連施設手順"
  - "薬剤部手順"
  - "EHR data availability"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "腎機能値だけで薬剤量調整を決める根拠として扱わない"
  - "透析時運用として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "AI が腎機能データから薬剤判断を決める根拠として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Renal Function Data Policy

## 目的

この文書は、腎機能データを薬剤判断へ直結させないための integrated policy note です。
ここでは評価方法、患者状態、急性変化、透析条件、施設確認を分離し、薬剤量や変更手順は定義しません。

## 基本原則

- eGFR、CCr、Cr は同じ意味として扱いません。
- AKI と安定した慢性腎機能低下は同じ文脈として扱いません。
- 透析条件は施設手順と薬剤師 review が必要な別軸です。
- 単一の腎機能値だけで薬剤量調整、投与管理、CDS 実装へ進めません。

## 確認軸

- 評価方法
- 患者状態
- 急性変化の有無
- 透析条件
- source confirmation
- 薬剤師 review
- 施設内手順
- EHR/CDS governance review

## Derived export rule

腎機能データに関する content は、source traceability、薬剤師 review、facility confirmation が揃わない限り、derived knowledge へ user-facing conclusion として export してはいけません。

## Quarantine trigger

腎機能値だけで薬剤量調整、透析時運用、投与管理、CDS trigger へ直結する user-facing conclusion が現れた場合は、derived export ではなく quarantine / unresolved として扱います。
