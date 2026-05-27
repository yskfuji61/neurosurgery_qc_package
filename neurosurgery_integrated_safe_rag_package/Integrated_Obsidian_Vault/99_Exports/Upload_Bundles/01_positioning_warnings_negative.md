# 01_positioning_warnings_negative.md

作成日: 2026-05-26

この統合MarkdownはRAG/Project Knowledge投入補助用です。正式な診療ガイドライン、処方指示、施設内手順、即時CDS仕様ではありません。



---


# FILE: 00_Index/01_Priority_Individual_Notes_Index.md


---
note_type: "index"
title: "Priority Individual Notes Index"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Phase 0〜23監査結果に基づく次工程"
source_quote_or_summary: "最小安全セットとCore Expansionの次工程として、Layer 1高リスク薬剤、主要疾患、患者状態、処置予定、CDS候補を個別ノート化する。"
gpt_structured_interpretation: "薬剤名・疾患名だけで候補化する誤読を避けるため、個別ノートでも陰性知識、外部一次資料確認、施設内確認を明示する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "このIndexを医学的推奨一覧として扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
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
rag_chunk_policy: "index_not_primary_rag_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# Priority Individual Notes Index

このパックは、前回までの最小安全セットとCore Expansionを土台に、次工程として優先個別ノートを追加するものです。

## 含めた範囲

- Layer 1高リスク薬剤 15件
- 主要疾患ハブ 10件
- 患者状態ハブ 12件
- 処置予定ハブ 8件
- CDS候補ノート 5件
- AI誤回答テスト拡張
- CSV/JSONL/YAML Export

## まだ含めない範囲

- 全Layer 2薬剤の詳細ノート
- 全疾患の完全ノート
- 院内採用品・夜間在庫・薬剤部SOPの確定値
- 電子カルテ実装仕様



---


# FILE: 00_Index/02_Layer2_Indexed_Drug_Index.md


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



---


# FILE: 00_Index/03_Validation_Audit_Operations_Index.md


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



---


# FILE: 08_Negative_Knowledge/Layer2薬剤_標準化しない事項.md


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
