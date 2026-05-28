---
note_type: "drug_index"
title: "Layer2 薬剤索引 初版"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗凝固薬本体、抗血小板薬本体、血栓溶解薬、抗てんかん発作薬、抗菌薬・抗ウイルス薬、VTE予防薬などを詳細ノート未作成でも索引化する。"
gpt_structured_interpretation: "Layer2を落とすと高リスク10薬剤だけで網羅したように見えるため、必ず索引に残す。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "高リスク10薬剤だけで薬剤網羅と見なすこと"
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
rag_chunk_policy: "index_only_until_detailed_note_created"
not_to_interpret_as:
  - "正式な診療ガイドラインではない"
  - "正式な処方指示書ではない"
  - "施設内手順そのものではない"
  - "即時実装可能なCDS仕様ではない"
audit_status: "draft_needs_human_review"
---

# Layer2 薬剤索引 初版

## 抗凝固薬本体
ワルファリン、ダビガトラン、アピキサバン、リバーロキサバン、エドキサバン、未分画ヘパリン、低分子ヘパリン。

## 抗血小板薬本体
アスピリン、クロピドグレル、プラスグレル、チカグレロル、シロスタゾール、その他P2Y12阻害薬。

## 血栓溶解薬
アルテプラーゼ。テネクテプラーゼは原資料登場確認後に扱う。

## 抗てんかん発作薬
レベチラセタム、ホスフェニトイン、フェニトイン、バルプロ酸、ラコサミド、ミダゾラム、ジアゼパム等。

## 抗菌薬・抗ウイルス薬
セファゾリン、セフトリアキソン、セフォタキシム、バンコマイシン、アンピシリン、セフェピム、セフタジジム、メロペネム、アシクロビル、クリンダマイシン。

## その他
VTE予防薬、鎮静薬、鎮痛薬、制吐薬、胃粘膜保護薬、血糖管理薬。

## 注意
Layer2は詳細ノート未作成でも、CSV/YAML/RAGの索引から落としてはいけない。
