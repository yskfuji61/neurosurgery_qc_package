---
note_type: "warning"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_version: "2026-05-19 外部公開前レビュー候補版"
source_section: "W02 / 8.1 対象薬剤の分類"
source_quote_or_summary: "rFVIIaは自然発症ICHの条件確認なしに一律に使用を検討することとして施設内手順候補にしない。国内適応外、血栓症リスク、専門医判断、理由記録を前提とする。"
gpt_structured_interpretation: "rFVIIaは止血方向の薬剤として見えやすいが、自然発症ICHの標準候補ではない。血液疾患等の適応文脈と非血友病性ICH文脈を分ける。"
evidence_certainty: "原資料上の整理。最終確定には外部一次資料確認が必要"
recommendation_strength: "候補・非候補を分離。処方指示ではない"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・医事/保険確認が必要"
institutional_operability: "施設内採用品・夜間休日在庫・薬剤部手順・看護観察体制・委員会承認が必要"
facility_candidate: "原資料からは確定できない。施設内承認後に検討する候補に限定"
cds_candidate: "即時実装仕様ではない。施設内承認後に別仕様書で検討"
not_to_standardize:
  - "rFVIIaを自然発症ICHで一律候補にしない"
  - "血腫増大抑制可能性を機能予後改善や標準使用と同一視しない"
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

# W02 rFVIIa：自然発症ICHで一律候補にしない

## 結論
rFVIIaは、自然発症ICHに対して条件確認なしに一律候補化してはいけない。

## 原資料要約
原資料では、rFVIIaについて、自然発症ICHで条件確認なしに一律に使用を検討することとして施設内手順候補にしないこと、国内適応外、血栓症リスク、専門医判断、理由記録を前提にすることが整理されている。

## GPTによる整理・解釈
「出血しているからrFVIIa」という短絡を防ぐため、自然発症ICHの文脈と、血友病等の血液疾患文脈を別chunkにする。

## 標準化しない事項
- 自然発症ICHでrFVIIaを一律候補化しない。
- 血栓症リスクを評価せずに候補化しない。
- 適応外可能性や理由記録を省略しない。

## 診療支援候補
即時実装仕様ではない。専門医判断、血栓症リスク、国内薬事、理由記録を確認する情報提示候補に留める。

## AI誤回答テスト
質問：rFVIIaは自然発症ICHで標準候補ですか。  
期待回答：標準候補ではない。一律候補化せず、専門医判断、適応外可能性、血栓症リスク、理由記録を確認する。
