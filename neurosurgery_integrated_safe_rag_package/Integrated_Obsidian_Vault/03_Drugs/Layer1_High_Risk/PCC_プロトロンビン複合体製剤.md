---
note_type: "drug"
title: "PCC（プロトロンビン複合体製剤）"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W01 / D05 / 8.1"
source_quote_or_summary: "PCCはVKA関連重篤出血・緊急手術と、DOAC関連出血への代替・条件付き使用を同列に扱わない。"
gpt_structured_interpretation: "PCCは抗凝固薬関連出血の汎用中和薬ではない。対象抗凝固薬別に分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DOAC関連出血の標準中和薬として機械的に出さない"
  - "VKA関連とDOAC関連を同列に扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "AHA/ASA ICH guideline"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "PCC採用品"
  - "夜間在庫"
  - "薬剤部調製"
  - "理由記録テンプレート"
  - "保険方針"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤名だけで標準候補と判断しない"
  - "疾患名だけで薬剤選択しない"
  - "国内薬事・保険・施設運用をエビデンスと同一視しない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
related_notes:
  - "W01_PCC_VKA_DOACを同列に扱わない"
  - "抗凝固薬曝露"
  - "緊急開頭術"
  - "EVD"
---

# PCC（プロトロンビン複合体製剤）

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

VKA関連とDOAC関連を分け、DOACでは特異的中和薬の可否、施設承認、理由記録を確認する。

## 3. 原資料の該当箇所要約

PCCはVKA関連重篤出血・緊急手術と、DOAC関連出血への代替・条件付き使用を同列に扱わない。

## 4. GPTによる整理・解釈

PCCは抗凝固薬関連出血の汎用中和薬ではない。対象抗凝固薬別に分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DOAC関連出血の標準中和薬として機械的に出さない
- VKA関連とDOAC関連を同列に扱わない

## 7. 必須確認事項

- 抗凝固薬名
- 最終服用時刻
- PT-INR
- 腎機能
- 特異的中和薬可否
- 手術/EVD予定

## 8. 外部一次資料確認

- PMDA電子添文
- AHA/ASA ICH guideline
- 国内診療ガイドライン

## 9. 施設内確認事項

- PCC採用品
- 夜間在庫
- 薬剤部調製
- 理由記録テンプレート
- 保険方針

## 10. 関連ノート

- [[W01_PCC_VKA_DOACを同列に扱わない]]
- [[抗凝固薬曝露]]
- [[緊急開頭術]]
- [[EVD]]

## 11. AI誤回答テスト候補

- DOAC関連出血にPCCを標準とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。
