---
note_type: "cds_readiness_assessment"
title: "CDS Readiness Assessment"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "診療支援・ヒューマンファクター"
source_quote_or_summary: "診療支援候補を即時実装仕様として扱わないためのreadiness評価表。"
gpt_structured_interpretation: "CDS実装前には、表示内容、禁止表現、承認、監査ログ、アラート疲労、医療機器プログラム該当性を評価する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "診療支援候補を即時実装仕様として扱わない"
  - "公開資料だけで高制約入力制御を決めない"
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

# CDS Readiness Assessment

| 候補種別 | 表示してよい情報 | 禁止事項 | 承認部門 |
| --- | --- | --- | --- |
| 情報提示 | 薬剤名・時刻・検査値・処置予定の提示 | 推奨・処方指示として表示しない | 診療科/薬剤部/医療安全/情報部門 |
| 注意喚起 | W01〜W06などの誤読防止 | アラート疲労を無視しない | 医療安全/情報部門 |
| 高制約入力制御 | 適応外・例外使用・危険条件の入力制御候補 | 公開資料だけで制御しない | 情報部門/医療安全/診療科/薬剤部 |
| 理由記録 | 例外使用時の理由・専門医判断の記録 | 理由記録があれば使用可能としない | 診療科/薬剤部/医事課 |
| 監査ログ | 表示・確認・override・承認の記録 | ログだけで安全とみなさない | 情報部門/医療安全 |
