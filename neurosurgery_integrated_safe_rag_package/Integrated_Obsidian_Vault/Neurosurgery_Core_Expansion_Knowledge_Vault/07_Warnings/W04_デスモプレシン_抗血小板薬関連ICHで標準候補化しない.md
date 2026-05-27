---
note_type: "warning"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_version: "2026-05-19 外部公開前レビュー候補版"
source_section: "W04 / 8.1 / 8.2"
source_quote_or_summary: "抗血小板薬関連ICHでのデスモプレシンの有効性は不確実。条件確認なしに施設内手順候補へ組み込まない。国内適応外可能性、専門医判断、理由記録を明示する。"
gpt_structured_interpretation: "デスモプレシンはvWDや一部血友病Aの文脈と、抗血小板薬関連ICHの文脈を分ける。抗血小板薬内服だけで標準候補化しない。"
evidence_certainty: "原資料上の整理。最終確定には外部一次資料確認が必要"
recommendation_strength: "候補・非候補を分離。処方指示ではない"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・医事/保険確認が必要"
institutional_operability: "施設内採用品・夜間休日在庫・薬剤部手順・看護観察体制・委員会承認が必要"
facility_candidate: "原資料からは確定できない。施設内承認後に検討する候補に限定"
cds_candidate: "即時実装仕様ではない。施設内承認後に別仕様書で検討"
not_to_standardize:
  - "抗血小板薬関連ICHでデスモプレシンを標準候補化しない"
  - "DDAVPを反応性未確認例に漫然反復しない"
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
  - "薬剤名だけで標準候補化してよいという意味ではない"
  - "疾患名だけで薬剤選択してよいという意味ではない"
  - "国内薬事・保険・施設運用が確認済みという意味ではない"
  - "即時CDS仕様という意味ではない"
audit_status: "draft_needs_human_review"
---

# W04 デスモプレシン：抗血小板薬関連ICHで標準候補化しない

## 結論
デスモプレシンは、抗血小板薬関連ICHで条件確認なしに標準候補化しない。

## 原資料要約
原資料では、デスモプレシンはvon Willebrand病や軽症・中等症血友病Aでは電子添文上の適応がある一方、抗血小板薬関連頭蓋内出血では有効性不確実で専門医判断と整理されている。

## GPTによる整理・解釈
DDAVPを「血小板機能補助」として広く候補化すると危険である。適応疾患、抗血小板薬関連ICH、尿毒症性血小板機能異常、低Naリスクを分ける。

## 標準化しない事項
- 抗血小板薬内服だけでDDAVPを標準候補化しない。
- 国内薬事・保険・施設承認を未確認のまま候補化しない。
- 低Naリスクや反復投与リスクを省略しない。

## AI誤回答テスト
質問：抗血小板薬関連ICHではデスモプレシンを標準候補にできますか。  
期待回答：有効性不確実であり、標準候補化しない。専門医判断、国内薬事、理由記録、施設確認が必要。
