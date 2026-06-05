---
note_type: "index"
title: "Validation Audit Operations Index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Phase 22〜23 / 次工程"
source_quote_or_summary: "外部一次資料確認、施設内確認、条件・閾値監査、CDS readiness、監査ログ、RAG検証を実施するための運用パック。"
gpt_structured_interpretation: "これまで作成したVaultを運用可能な安全管理体系へ接続する。ただし、施設内承認済み手順やCDS仕様ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "このIndexを承認済み運用手順として扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部調製・払い出し手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "index_not_primary_clinical_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "薬剤名だけで標準候補と判断しない"
  - "疾患名だけで薬剤選択しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# Validation Audit Operations Index

このパックは、最小安全セット、Core Expansion、Priority Individual Notes、Layer 2 Indexed Drug Vaultの次工程です。

## 目的

外部一次資料確認、施設内確認、条件・閾値監査、CDS readiness評価、監査ログ、RAG検証を行うための運用用Vaultです。

## 重要

これは正式な施設内手順でも、電子カルテCDS仕様でもありません。  
最終判断は、最新の電子添文、国内診療ガイドライン、施設内採用品、薬剤部手順、夜間休日在庫、看護観察体制、各委員会承認に依存します。

## Stage 3 ガバナンス（添付文書・適用外）

- [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]] — 用法・用量・使用方法は製品単位電子添文（PMDA）遵守；適用外使用は医師の個別判断なしに標準化・推奨しない（原則禁止）
- Gap V3: [[00_Index/04_Gap_V3_Reference_Parked_Index]]
