---
note_type: "rag_schema"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_version: "2026-05-19 外部公開前レビュー候補版"
source_section: "Phase 15 RAG / Custom GPT / Project Knowledge用Export設計"
source_quote_or_summary: "RAG投入用JSONLでは、chunk_id, source_document, source_section, knowledge_type, claim_type, source_quote_or_summary, interpretation, not_to_interpret_as, 5軸, related_entities, negative_knowledge, required_confirmation, human_review_requiredを必須とする。"
gpt_structured_interpretation: "RAGでは1 claim / 1 chunkを原則とし、特に高リスク注意と陰性知識はchunk優先度を高くする。"
evidence_certainty: "原資料上の整理。最終確定には外部一次資料確認が必要"
recommendation_strength: "候補・非候補を分離。処方指示ではない"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・医事/保険確認が必要"
institutional_operability: "施設内採用品・夜間休日在庫・薬剤部手順・看護観察体制・委員会承認が必要"
facility_candidate: "原資料からは確定できない。施設内承認後に検討する候補に限定"
cds_candidate: "即時実装仕様ではない。施設内承認後に別仕様書で検討"
not_to_standardize:
  - "not_to_interpret_asなしで高リスクchunkを作ること"
  - "候補・推奨・薬事・保険・施設運用・CDS実装可否を同一フィールドに混ぜること"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終判断"
  - "施設内採用品・在庫・運用可否"
  - "CDS実装可否"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "国内診療ガイドライン"
  - "関連主要ガイドライン・RCT"
  - "安全性情報/RMP"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部調製・払い出し手順"
  - "看護観察体制"
  - "委員会承認"
  - "保険・査定対応方針"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk; high-risk chunks require not_to_interpret_as"
not_to_interpret_as:
  - "RAG投入だけで安全性が担保されるという意味"
  - "JSONLが人間監査を代替するという意味"
audit_status: "draft_needs_human_review"
---

# RAG JSONL schema

## 必須スキーマ

```json
{
  "chunk_id": "",
  "source_document": "脳神経外科領域における施設内薬物治療アルゴリズム",
  "source_version": "2026-05-19 外部公開前レビュー候補版",
  "source_section": "",
  "knowledge_type": "",
  "claim_type": "",
  "source_quote_or_summary": "",
  "interpretation": "",
  "not_to_interpret_as": [],
  "evidence_certainty": "",
  "recommendation_strength": "",
  "domestic_regulatory_status": "",
  "insurance_risk": "",
  "institutional_operability": "",
  "related_entities": {
    "diseases": [],
    "drugs": [],
    "drug_classes": [],
    "patient_states": [],
    "procedures": [],
    "conditions_thresholds": [],
    "warnings": [],
    "negative_knowledge": []
  },
  "negative_knowledge": [],
  "required_confirmation": [],
  "external_primary_sources_required": true,
  "facility_specific_confirmation_required": true,
  "human_review_required": true,
  "ai_misread_risk": "",
  "rag_priority": "",
  "safe_answer_instruction": ""
}
```

## claim_type標準
- source_fact
- source_summary
- structured_interpretation
- negative_knowledge
- facility_candidate
- cds_candidate
- regulatory_status
- insurance_risk
- facility_operation
- threshold_condition
- audit_requirement

## 高リスクchunkの必須条件
高リスクchunkでは、以下を必須にする。

```json
{
  "not_to_interpret_as": [
    "診療ガイドライン",
    "処方指示",
    "施設内承認済み手順",
    "即時実装可能なCDS仕様",
    "国内薬事・保険・施設運用確認済みという意味"
  ],
  "human_review_required": true,
  "external_primary_sources_required": true,
  "facility_specific_confirmation_required": true
}
```

## 分割ルール
- TXAは ICH / TBI / aSAH / CSDH で別chunk。
- PCCは VKA関連 / DOAC関連 で別chunk。
- 血小板輸血は 血小板減少 / 抗血小板薬曝露 / 侵襲的処置予定 で別chunk。
- デスモプレシンは vWD/血友病A / 抗血小板薬関連ICH / 尿毒症性血小板機能異常 で別chunk。
- 高張食塩液・マンニトールは 監視条件 / 一般病棟不可 / Na・浸透圧・尿量・腎機能 で別chunk。
