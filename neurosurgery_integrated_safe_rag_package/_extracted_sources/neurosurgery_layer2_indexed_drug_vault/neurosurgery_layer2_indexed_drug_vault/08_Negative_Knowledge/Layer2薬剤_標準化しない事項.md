---
note_type: "negative_knowledge_master"
title: "Layer2薬剤_標準化しない事項"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Layer2索引作成工程"
source_quote_or_summary: "Layer 2薬剤を詳細ノート化する前に、クラス短絡・目的混同・施設運用推測を防ぐ陰性知識をまとめる。"
gpt_structured_interpretation: "薬剤クラス名や薬剤名だけで標準候補を出す誤答を防止する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗凝固薬を一括してPCC候補にしない"
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗菌薬予防投与と感染治療を混同しない"
  - "抗てんかん発作薬の予防投与と治療投与を混同しない"
  - "CDSが抗凝固薬再開日を自動決定しない"
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
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
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

# Layer2薬剤_標準化しない事項

## 主要な陰性知識

- 抗凝固薬本体を一括してPCC候補にしない。
- DOACを一括して同じ特異的中和薬対象にしない。
- 抗血小板薬内服のみで血小板輸血を候補化しない。
- P2Y12阻害薬をすべて同一の処置前対応にしない。
- 血栓溶解薬曝露と一般ICHを同じ扱いにしない。
- 抗てんかん発作薬の予防投与、治療投与、重積初期対応を混同しない。
- 周術期予防抗菌薬と感染治療を混同しない。
- EVD全留置期間の予防抗菌薬継続を標準化しない。
- VTE予防と抗凝固薬再開を自動決定しない。
