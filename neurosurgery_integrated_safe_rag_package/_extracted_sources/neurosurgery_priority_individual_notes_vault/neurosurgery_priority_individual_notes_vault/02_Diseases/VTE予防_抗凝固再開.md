---
note_type: "disease"
title: "VTE予防・抗凝固再開"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "VTE予防・抗凝固再開"
source_quote_or_summary: "VTE予防・抗凝固再開は中和とは別フロー。再開日はCDSが機械的に決めず、再評価項目として扱う。"
gpt_structured_interpretation: "再開ノートは薬剤選択ではなく再評価ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗凝固薬中和と抗凝固再開を同一フローにしない"
  - "CDSが再開日を自動決定しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "疾患名だけで薬剤選択しない"
  - "疾患ノートを薬剤推奨リストとして扱わない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# VTE予防・抗凝固再開

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

VTE予防・抗凝固再開は中和とは別フロー。再開日はCDSが機械的に決めず、再評価項目として扱う。

## 4. GPTによる整理・解釈

再開ノートは薬剤選択ではなく再評価ハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗凝固薬中和と抗凝固再開を同一フローにしない
- CDSが再開日を自動決定しない

## 7. 必須確認事項

- 画像安定
- 止血確認
- 血栓症リスク
- EVD抜去/留置
- 腎機能
- 血小板数

## 8. 外部一次資料確認

- 国内診療ガイドライン
- 関連RCT/主要GL
- 電子添文

## 9. 施設内確認事項

- 施設内手順
- 採用品
- 夜間在庫
- 看護観察体制
- 委員会承認

## 10. 関連ノート

- [[患者状態ハブ_初版]]
- [[処置予定ハブ_初版]]
- [[条件_閾値_時間条件ハブ_初版]]

## 11. AI誤回答テスト候補

- VTE予防・抗凝固再開を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。
