---
note_type: "index"
title: "Layer2 Indexed Drug Index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗凝固薬本体、抗血小板薬本体、血栓溶解薬、抗てんかん発作薬、抗菌薬・抗ウイルス薬、VTE予防薬・方法等をLayer 2として索引化する。"
gpt_structured_interpretation: "Layer 2薬剤は初回から全て詳細な推奨ノートにするのではなく、まず薬剤名短絡・クラス短絡を防ぐ索引ノートとして整備する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "Layer 2索引を標準処方リストとして扱わない"
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

# Layer2 Indexed Drug Index

このパックは、前工程までに作成した最小安全セット、Core Expansion、Priority Individual Notesに続く工程です。

## 今回の目的

Layer 2薬剤をVault上から漏らさないように、詳細ノート化の前段階として索引化します。

## 含める範囲

- 抗凝固薬本体
- 抗血小板薬本体
- 血栓溶解薬
- 抗てんかん発作薬
- 抗菌薬・抗ウイルス薬
- VTE予防薬・方法
- 鎮静薬、鎮痛薬、制吐薬、胃粘膜保護薬、血糖管理薬の索引

## まだ行わないこと

- 施設内採用品の確定
- 投与量・投与速度・オーダーセットの確定
- CDS即時実装仕様化

## Gap V3 reference（parked / hold）

Gap supplement V3 の reference profile は標準処方対象外。境界ハブ・衝突記録・正本 manifest への導線のみ: [[00_Index/04_Gap_V3_Reference_Parked_Index]]
