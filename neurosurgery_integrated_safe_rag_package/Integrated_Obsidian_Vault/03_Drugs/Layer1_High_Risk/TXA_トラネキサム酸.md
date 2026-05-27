---
note_type: "drug"
title: "TXA（トラネキサム酸）"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W03 / D01 / 8.1 / 8.2 / 8.3"
source_quote_or_summary: "TXAはICH、aSAH、TBIで条件が異なる。自然発症ICHは日常的施設内手順候補にしない。aSAHは動脈瘤閉鎖前短期橋渡し、TBIは受傷3時間以内などの条件付き候補。"
gpt_structured_interpretation: "TXAは同じ抗線溶薬でも、疾患・受傷/発症時刻・処置予定・腎機能・血栓症リスクで扱いを分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "自然発症ICHの日常的施設内手順候補にしない"
  - "TBIで受傷3時間超・時刻不明・既投与例に機械的候補化しない"
  - "aSAHで動脈瘤閉鎖後も漫然継続しない"
  - "CSDH再発予防を急性止血へ横展開しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "CRASH-3"
  - "TICH-2"
  - "ULTRA"
  - "国内診療ガイドライン"
facility_confirmation_items:
  - "採用品"
  - "夜間在庫"
  - "薬剤部払い出し"
  - "腎機能低下時確認方法"
  - "委員会承認"
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
  - "W03_TXA_ICH_aSAH_TBIで条件が異なる"
  - "自然発症脳内出血"
  - "外傷性脳損傷"
  - "動脈瘤性くも膜下出血"
---

# TXA（トラネキサム酸）

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

TXAは薬剤名だけで標準候補にしない。自然発症ICH、aSAH、TBI、CSDHの文脈を必ず分離する。

## 3. 原資料の該当箇所要約

TXAはICH、aSAH、TBIで条件が異なる。自然発症ICHは日常的施設内手順候補にしない。aSAHは動脈瘤閉鎖前短期橋渡し、TBIは受傷3時間以内などの条件付き候補。

## 4. GPTによる整理・解釈

TXAは同じ抗線溶薬でも、疾患・受傷/発症時刻・処置予定・腎機能・血栓症リスクで扱いを分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 自然発症ICHの日常的施設内手順候補にしない
- TBIで受傷3時間超・時刻不明・既投与例に機械的候補化しない
- aSAHで動脈瘤閉鎖後も漫然継続しない
- CSDH再発予防を急性止血へ横展開しない

## 7. 必須確認事項

- 疾患名
- 受傷/発症時刻
- 動脈瘤閉鎖前後
- 腎機能
- 血栓症リスク
- 既投与の有無

## 8. 外部一次資料確認

- PMDA電子添文
- CRASH-3
- TICH-2
- ULTRA
- 国内診療ガイドライン

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部払い出し
- 腎機能低下時確認方法
- 委員会承認

## 10. 関連ノート

- [[W03_TXA_ICH_aSAH_TBIで条件が異なる]]
- [[自然発症脳内出血]]
- [[外傷性脳損傷]]
- [[動脈瘤性くも膜下出血]]

## 11. AI誤回答テスト候補

- 自然発症ICHでTXAを標準候補にする誤答を検出
- TBIならTXAと回答する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。
