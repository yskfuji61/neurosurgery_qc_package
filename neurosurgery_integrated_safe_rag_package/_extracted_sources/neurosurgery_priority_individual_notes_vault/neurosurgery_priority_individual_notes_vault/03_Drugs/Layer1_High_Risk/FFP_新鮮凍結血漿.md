---
note_type: "drug"
title: "FFP（新鮮凍結血漿）"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1"
source_quote_or_summary: "FFPは凝固因子欠乏、大量出血等で検査値と輸血部基準に基づき扱う。"
gpt_structured_interpretation: "凝固異常の原因や検査値を確認せずに機械的候補化しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "凝固異常不明で機械的候補化しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "輸血療法関連指針"
facility_confirmation_items:
  - "在庫"
  - "解凍時間"
  - "輸血部運用"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤名だけで標準候補と判断しない"
  - "疾患名だけで薬剤選択しない"
  - "国内薬事・保険・施設運用をエビデンスと同一視しない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
related_notes:
  - "凝固異常"
  - "緊急開頭術"
---

# FFP（新鮮凍結血漿）

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

凝固異常不明で標準候補化しない。

## 3. 原資料の該当箇所要約

FFPは凝固因子欠乏、大量出血等で検査値と輸血部基準に基づき扱う。

## 4. GPTによる整理・解釈

凝固異常の原因や検査値を確認せずに機械的候補化しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 凝固異常不明で機械的候補化しない

## 7. 必須確認事項

- PT-INR
- aPTT
- フィブリノゲン
- 出血状況
- 輸血部基準

## 8. 外部一次資料確認

- 輸血療法関連指針

## 9. 施設内確認事項

- 在庫
- 解凍時間
- 輸血部運用

## 10. 関連ノート

- [[凝固異常]]
- [[緊急開頭術]]

## 11. AI誤回答テスト候補

- 凝固異常ならFFPと短絡する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。
