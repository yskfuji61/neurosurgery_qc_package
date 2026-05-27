---
note_type: "index"
title: "Core Expansion Index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Phase 5〜21由来の中核拡張"
source_quote_or_summary: "最小安全セットの次段階として、疾患・患者状態・処置予定・条件・薬剤索引・外部確認・監査ログを追加する。"
gpt_structured_interpretation: "薬剤ノートを増やす前に、安全確認ハブと監査ハブを追加する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  []
undetermined_from_source:
  - "原資料だけでは最終判断を確定できない"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン"
  - "関連する一次資料・準一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部調製・払い出し手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインではない"
  - "正式な処方指示書ではない"
  - "施設内手順そのものではない"
  - "即時実装可能なCDS仕様ではない"
audit_status: "draft_needs_human_review"
---

# Core Expansion Index

この拡張セットは、最小安全Knowledge Vaultの次工程です。目的は、全薬剤・全疾患を無秩序に増やすことではなく、AI誤読を防ぐために必要な中核ハブを追加することです。

## 追加した中核ファイル

- `02_Diseases/疾患ハブ_初版.md`
- `05_Patient_States/患者状態ハブ_初版.md`
- `06_Procedures/処置予定ハブ_初版.md`
- `13_Thresholds_Conditions/条件_閾値_時間条件ハブ_初版.md`
- `03_Drugs/Layer1_High_Risk/Layer1薬剤索引.md`
- `03_Drugs/Layer2_Indexed/Layer2薬剤索引.md`
- `12_Evidence/外部一次資料確認チェックリスト.md`
- `90_Audit/監査ログテンプレート.md`
- `99_Exports/CSV_Masters/*.csv`
- `99_Exports/JSONL_RAG/rag_seed_high_risk.jsonl`

## 運用上の最優先原則

疾患名だけで薬剤を選択しない。薬剤名だけで標準候補にしない。国内薬事、保険、施設運用、診療支援候補をエビデンスと同一視しない。
