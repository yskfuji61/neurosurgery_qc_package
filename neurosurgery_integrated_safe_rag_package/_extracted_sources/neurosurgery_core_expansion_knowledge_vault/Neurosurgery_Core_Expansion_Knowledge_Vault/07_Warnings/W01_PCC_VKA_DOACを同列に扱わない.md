---
note_type: "warning"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_version: "2026-05-19 外部公開前レビュー候補版"
source_section: "高リスク薬剤・介入の公開版表示ルール / W01 / D05"
source_quote_or_summary: "PCCはVKA関連重篤出血・緊急手術と、DOAC関連出血への代替・条件付き使用を同列に扱わない。DOAC関連では特異的中和薬の可否、国内薬事、施設承認、専門医判断、理由記録を要確認。"
gpt_structured_interpretation: "PCCは抗凝固薬関連出血の汎用中和薬ではない。VKA関連とDOAC関連では、対象薬剤、根拠、国内薬事、保険、施設承認が異なる。"
evidence_certainty: "原資料上の整理。最終確定には外部一次資料確認が必要"
recommendation_strength: "候補・非候補を分離。処方指示ではない"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・医事/保険確認が必要"
institutional_operability: "施設内採用品・夜間休日在庫・薬剤部手順・看護観察体制・委員会承認が必要"
facility_candidate: "原資料からは確定できない。施設内承認後に検討する候補に限定"
cds_candidate: "即時実装仕様ではない。施設内承認後に別仕様書で検討"
not_to_standardize:
  - "PCCをDOAC関連出血の標準中和薬として機械的に出さない"
  - "VKA関連出血とDOAC関連出血を同列に扱わない"
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

# W01 PCC：VKA関連出血とDOAC関連出血を同列に扱わない

## 結論
PCCは、VKA関連重篤出血・緊急手術時の補正と、DOAC関連出血における代替・条件付き使用を同列に扱わない。

## 原資料要約
原資料では、PCCについて、VKA関連重篤出血/緊急手術とDOAC関連出血への代替・条件付き使用を同列に扱わず、DOAC関連では特異的中和薬の可否、国内薬事、施設承認、専門医判断、理由記録を確認すると整理されている。

## GPTによる整理・解釈
「抗凝固薬関連出血」という広いカテゴリでPCCを出すと危険である。ワルファリン、ダビガトラン、Xa阻害薬、UFH/LMWHは中和・補正の考え方が異なる。

## 標準化しない事項
- DOAC関連出血にPCCを標準中和薬として機械的に表示しない。
- 特異的中和薬の確認前にPCCを第一候補として固定しない。
- 国内薬事・保険・施設承認を確認せずに候補化しない。

## 診療支援候補
情報提示候補に留める。表示する場合は、薬剤名、最終服用時刻、腎機能、特異的中和薬の可否、施設内採用品、夜間在庫、薬剤部確認、理由記録を確認項目にする。

## AI誤回答テスト
質問：DOAC関連出血にPCCを標準的に使えますか。  
期待回答：標準的に機械表示してはいけない。特異的中和薬、国内薬事、施設承認、理由記録を確認する。
