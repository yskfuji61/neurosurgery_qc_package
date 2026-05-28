---
note_type: "drug_index"
title: "Layer1 高リスク薬剤索引 初版"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1 対象薬剤の分類 / W01〜W06"
source_quote_or_summary: "TXA、PCC、rFVIIa、デスモプレシン、血小板輸血、イダルシズマブ、アンデキサネット、プロタミン、マンニトール、高張食塩液などを高リスク優先索引として整理する。"
gpt_structured_interpretation: "Layer1は薬剤候補リストではなく、高リスク誤読防止のための索引である。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文等で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "Layer1薬剤を標準候補リストとして扱うこと"
  - "止血関連薬を一括して同列化すること"
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
ai_misread_risk: "very_high"
rag_chunk_policy: "drug_index_not_recommendation_list"
not_to_interpret_as:
  - "正式な診療ガイドラインではない"
  - "正式な処方指示書ではない"
  - "施設内手順そのものではない"
  - "即時実装可能なCDS仕様ではない"
audit_status: "draft_needs_human_review"
---

# Layer1 高リスク薬剤索引 初版

| 薬剤・製剤 | 主な誤読リスク | 必ず接続する注意 |
|---|---|---|
| TXA | ICH/aSAH/TBI/CSDHの条件差脱落 | W03 |
| PCC | VKA関連とDOAC関連の同列化 | W01 |
| rFVIIa | 自然発症ICHで一律候補化 | W02 |
| デスモプレシン | 抗血小板薬関連ICHで標準候補化 | W04 |
| 血小板輸血 | 抗血小板薬内服のみで候補化 | W05 |
| イダルシズマブ | DOAC全般への誤拡張 | 対象薬剤確認 |
| アンデキサネット アルファ | PCCやダビガトラン中和との混同 | 対象Xa阻害薬確認 |
| プロタミン | DOAC/ワルファリンに使えるとの誤解 | ヘパリン系に限定 |
| マンニトール | 一般病棟標準運用 | W06 |
| 高張食塩液 | Na/浸透圧/監視条件の脱落 | W06 |
| カルバゾクロム | 急性血腫拡大抑制薬としての標準化 | 陰性知識 |
| ε-アミノカプロン酸 | TXA代替を標準手順化 | aSAH閉鎖前短期橋渡し確認 |
| フィブリノゲン製剤 | 検査値なしの候補化 | Fib値・輸血部基準 |
| FFP | 凝固異常不明で候補化 | 輸血部基準 |
| クリオプレシピテート | 在庫・解凍時間未確認 | 輸血部基準 |
