---
note_type: "cds_candidate"
title: "高制約入力制御候補"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "診療支援・ヒューマンファクター表現の安全化"
source_quote_or_summary: "公開資料だけで入力制御を決めず、情報部門・医療安全・診療科・薬剤部承認後に検討する候補。"
gpt_structured_interpretation: "診療支援候補は即時実装仕様ではなく、施設内承認後に検討する候補。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "電子カルテへ即時実装しない"
  - "公開資料だけで高制約入力制御を決めない"
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
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "即時CDS仕様として扱わない"
  - "処方指示として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 高制約入力制御候補

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

これは施設内承認後に検討する診療支援候補であり、即時実装仕様ではない。

## 3. 原資料の該当箇所要約

公開資料だけで入力制御を決めず、情報部門・医療安全・診療科・薬剤部承認後に検討する候補。

## 4. GPTによる整理・解釈

表示してよい情報と表示してはいけない断定表現を分ける必要がある。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 即時実装仕様として扱わない

## 7. 必須確認事項

- 承認部門
- 表示条件
- 抑制条件
- 監査ログ
- アラート疲労評価

## 8. 外部一次資料確認

- CDS/医療機器プログラム関連資料

## 9. 施設内確認事項

- 情報部門
- 医療安全
- 診療科
- 薬剤部
- 委員会承認

## 10. 関連ノート

- [[診療支援候補MOC]]
- [[高リスク誤回答テスト]]

## 11. AI誤回答テスト候補

- 高制約入力制御候補を即時実装仕様とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。
