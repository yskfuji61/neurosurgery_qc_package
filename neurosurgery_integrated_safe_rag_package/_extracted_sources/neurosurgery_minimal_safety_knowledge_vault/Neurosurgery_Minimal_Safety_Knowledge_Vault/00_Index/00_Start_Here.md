---
note_type: "index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_version: "2026-05-19 外部公開前レビュー候補版"
source_section: "文書全体 / Knowledge Vault入口"
source_quote_or_summary: "本Vaultは、公開参考資料をAIが誤読しにくい形で参照するための最小安全セットであり、正式な診療ガイドライン・処方指示書・施設内手順・即時CDS仕様ではない。"
gpt_structured_interpretation: "最初に文書位置づけ、5軸分離、高リスク注意、陰性知識、AI誤回答テストを読む。薬剤名や疾患名だけで候補化しない。"
evidence_certainty: "原資料上の整理。最終確定には外部一次資料確認が必要"
recommendation_strength: "候補・非候補を分離。処方指示ではない"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・医事/保険確認が必要"
institutional_operability: "施設内採用品・夜間休日在庫・薬剤部手順・看護観察体制・委員会承認が必要"
facility_candidate: "原資料からは確定できない。施設内承認後に検討する候補に限定"
cds_candidate: "即時実装仕様ではない。施設内承認後に別仕様書で検討"
not_to_standardize:
  - "このVaultだけで施設内手順化すること"
  - "このVaultだけで電子カルテCDSへ実装すること"
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
  - "完成済み院内ガイドライン"
  - "処方指示テンプレート"
  - "電子カルテ実装仕様"
  - "施設内承認済み手順"
audit_status: "draft_needs_human_review"
---

# 00 Start Here

## このVaultの目的
この最小安全Knowledge Vaultは、添付DOCXをAI / Custom GPT / Project Knowledge / RAG / Obsidianで扱う前に、重大な誤読を防ぐための最小構成です。

## 最初に読む順番
1. [[文書位置づけ]]
2. [[5軸分離の原則]]
3. [[W01_PCC_VKA_DOACを同列に扱わない]]
4. [[W02_rFVIIa_自然発症ICHで一律候補にしない]]
5. [[W03_TXA_ICH_aSAH_TBIで条件が異なる]]
6. [[W04_デスモプレシン_抗血小板薬関連ICHで標準候補化しない]]
7. [[W05_血小板輸血_抗血小板薬内服のみで候補にしない]]
8. [[W06_高張食塩液_マンニトール_監視条件なしに一般病棟標準運用しない]]
9. [[標準化しない事項マスター]]
10. [[高リスク誤回答テスト]]
11. [[RAG_JSONL_schema]]

## 最重要禁則
このVaultでは、「候補」「推奨」「国内適応」「保険上説明可能」「施設内運用可能」「CDS実装可能」を同一視しない。

## AI回答時の安全な基本文
本資料は公開参考資料であり、正式な診療ガイドライン、処方指示書、施設内手順、即時実装可能な電子カルテ診療支援仕様ではありません。最終判断には最新電子添文、国内診療ガイドライン、施設採用品、薬剤部手順、夜間休日在庫、看護観察体制、各委員会承認が必要です。
