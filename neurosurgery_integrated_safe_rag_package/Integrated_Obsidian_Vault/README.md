---
note_type: "audit_or_export_note"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "統合後QC補完"
source_quote_or_summary: "統合Vault内の補助ファイル。医療判断本文ではなく、索引・監査・Export補助情報として扱う。"
gpt_structured_interpretation: "統合後QCでYAML必須項目を補完した。正式な診療ガイドライン、処方指示、施設内手順、即時CDS仕様ではない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "医学的推奨ではない"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize: 
  - "この補助ファイルを施設内手順として扱わない"
undetermined_from_source: 
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
external_primary_source_check_items: 
  - "最新電子添文"
  - "国内診療ガイドライン"
  - "関連一次資料"
facility_confirmation_items: 
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "supporting_file_not_primary_clinical_chunk"
not_to_interpret_as: 
  - "正式な診療ガイドライン"
  - "正式な処方指示"
  - "施設内手順"
  - "即時CDS仕様"
audit_status: "qc_completed_needs_human_review"
---
# Neurosurgery Priority Individual Notes Vault

作成日: 2026-05-26

このZIPは、最小安全セットおよびCore Expansionの次工程として作成した優先個別ノートパックです。

## 目的

Layer 1高リスク薬剤、主要疾患、患者状態、処置予定、診療支援候補について、薬剤名短絡・疾患名短絡・施設運用推測・CDS即時実装誤認を防ぐための初版Markdownノートを提供します。

## 注意

これは正式な診療ガイドライン、処方指示書、施設内手順、電子カルテ診療支援仕様ではありません。最終判断には外部一次資料確認と施設内確認が必要です。
