# 03_drugs_drug_classes.md

作成日: 2026-05-26

この統合MarkdownはRAG/Project Knowledge投入補助用です。正式な診療ガイドライン、処方指示、施設内手順、即時CDS仕様ではありません。



---


# FILE: 03_Drugs/Layer1_High_Risk/FFP_新鮮凍結血漿.md


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



---


# FILE: 03_Drugs/Layer1_High_Risk/PCC_プロトロンビン複合体製剤.md


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



---


# FILE: 03_Drugs/Layer1_High_Risk/TXA_トラネキサム酸.md


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



---


# FILE: 03_Drugs/Layer1_High_Risk/rFVIIa_遺伝子組換え活性型第VII因子.md


---
note_type: "drug"
title: "rFVIIa（遺伝子組換え活性型第VII因子）"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W02 / 8.1"
source_quote_or_summary: "rFVIIaは自然発症ICHで条件確認なしに一律候補にしない。血液疾患等の承認適応文脈と自然発症ICH文脈を分ける。"
gpt_structured_interpretation: "血腫増大抑制の文脈を、機能予後改善や標準使用と同一視しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "自然発症ICHで一律候補にしない"
  - "血液疾患の適応文脈を非血友病性ICHへ横展開しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "ICH guideline"
  - "主要試験/メタ解析"
facility_confirmation_items:
  - "採用品"
  - "承認経路"
  - "理由記録"
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
  - "W02_rFVIIa_自然発症ICHで一律候補にしない"
  - "自然発症脳内出血"
  - "血友病関連出血"
---

# rFVIIa（遺伝子組換え活性型第VII因子）

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

自然発症ICHでは一律候補化せず、専門医判断、血栓症リスク、理由記録、国内薬事・保険確認を前提にする。

## 3. 原資料の該当箇所要約

rFVIIaは自然発症ICHで条件確認なしに一律候補にしない。血液疾患等の承認適応文脈と自然発症ICH文脈を分ける。

## 4. GPTによる整理・解釈

血腫増大抑制の文脈を、機能予後改善や標準使用と同一視しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 自然発症ICHで一律候補にしない
- 血液疾患の適応文脈を非血友病性ICHへ横展開しない

## 7. 必須確認事項

- 疾患文脈
- 血栓症リスク
- 血液疾患の有無
- 専門医判断
- 理由記録

## 8. 外部一次資料確認

- PMDA電子添文
- ICH guideline
- 主要試験/メタ解析

## 9. 施設内確認事項

- 採用品
- 承認経路
- 理由記録
- 保険方針

## 10. 関連ノート

- [[W02_rFVIIa_自然発症ICHで一律候補にしない]]
- [[自然発症脳内出血]]
- [[血友病関連出血]]

## 11. AI誤回答テスト候補

- rFVIIaをICH標準候補とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/ε-アミノカプロン酸.md


---
note_type: "drug"
title: "ε-アミノカプロン酸"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W03 / 8.1 / 8.3"
source_quote_or_summary: "ε-アミノカプロン酸は抗線溶薬として、TXA不適・供給上の問題時やaSAH閉鎖前短期橋渡し候補として扱うが、施設内手順候補にしない扱いが示されている。"
gpt_structured_interpretation: "TXA代替として安易に標準化しない。腎機能や血栓症リスクを確認する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "標準的施設内手順候補にしない"
  - "aSAH閉鎖後の漫然継続をしない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "aSAH guideline"
  - "ULTRA関連資料"
facility_confirmation_items:
  - "採用品"
  - "保険方針"
  - "薬剤部手順"
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
  - "動脈瘤性くも膜下出血"
  - "TXA_トラネキサム酸"
---

# ε-アミノカプロン酸

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

標準的施設内手順候補にしない。

## 3. 原資料の該当箇所要約

ε-アミノカプロン酸は抗線溶薬として、TXA不適・供給上の問題時やaSAH閉鎖前短期橋渡し候補として扱うが、施設内手順候補にしない扱いが示されている。

## 4. GPTによる整理・解釈

TXA代替として安易に標準化しない。腎機能や血栓症リスクを確認する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 標準的施設内手順候補にしない
- aSAH閉鎖後の漫然継続をしない

## 7. 必須確認事項

- aSAH閉鎖前後
- 腎機能
- 血栓症リスク
- 採用品

## 8. 外部一次資料確認

- PMDA電子添文
- aSAH guideline
- ULTRA関連資料

## 9. 施設内確認事項

- 採用品
- 保険方針
- 薬剤部手順

## 10. 関連ノート

- [[動脈瘤性くも膜下出血]]
- [[TXA_トラネキサム酸]]

## 11. AI誤回答テスト候補

- TXA代替として標準候補にする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/アンデキサネット_アルファ.md


---
note_type: "drug"
title: "アンデキサネット アルファ"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1 / D05"
source_quote_or_summary: "アンデキサネット アルファは直接作用型Xa因子阻害薬中和の文脈で扱う。対象薬剤、用量、最終服用時刻、A法/B法判定が必要。"
gpt_structured_interpretation: "PCC代替使用と同列に扱わない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "ダビガトランに使えると扱わない"
  - "PCCと同列に扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "関連GL"
facility_confirmation_items:
  - "採用品"
  - "夜間在庫"
  - "A/B法支援体制"
  - "保険方針"
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
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
---

# アンデキサネット アルファ

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Xa阻害薬以外へ拡張しない。PCCと同じ扱いにしない。

## 3. 原資料の該当箇所要約

アンデキサネット アルファは直接作用型Xa因子阻害薬中和の文脈で扱う。対象薬剤、用量、最終服用時刻、A法/B法判定が必要。

## 4. GPTによる整理・解釈

PCC代替使用と同列に扱わない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- ダビガトランに使えると扱わない
- PCCと同列に扱わない

## 7. 必須確認事項

- アピキサバン/リバーロキサバン/エドキサバン確認
- 最終服用時刻
- 用量
- 腎機能
- 血栓症リスク

## 8. 外部一次資料確認

- PMDA電子添文
- 関連GL

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- A/B法支援体制
- 保険方針

## 10. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]

## 11. AI誤回答テスト候補

- ダビガトランにも使えるとする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/イダルシズマブ.md


---
note_type: "drug"
title: "イダルシズマブ"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1 / D05"
source_quote_or_summary: "イダルシズマブはダビガトラン特異的中和として扱う。DOAC全般の中和薬として扱わない。"
gpt_structured_interpretation: "対象薬剤を明示し、腎機能と最終服用時刻を確認する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DOAC全般に使えると扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "国内外GL"
facility_confirmation_items:
  - "採用品"
  - "夜間在庫"
  - "薬剤部手順"
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
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
---

# イダルシズマブ

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

ダビガトラン以外のDOACに使えると扱わない。

## 3. 原資料の該当箇所要約

イダルシズマブはダビガトラン特異的中和として扱う。DOAC全般の中和薬として扱わない。

## 4. GPTによる整理・解釈

対象薬剤を明示し、腎機能と最終服用時刻を確認する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DOAC全般に使えると扱わない

## 7. 必須確認事項

- ダビガトラン内服確認
- 最終服用時刻
- 腎機能
- 出血重症度
- 手術/EVD予定

## 8. 外部一次資料確認

- PMDA電子添文
- 国内外GL

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順

## 10. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]

## 11. AI誤回答テスト候補

- Xa阻害薬にも使えるとする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/カルバゾクロム.md


---
note_type: "drug"
title: "カルバゾクロム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1"
source_quote_or_summary: "カルバゾクロムは国内電子添文上の止血関連効能を持つが、脳内出血・頭部外傷・くも膜下出血の機能予後改善を支持する十分なエビデンスは乏しいとされ、施設内手順候補にしない。"
gpt_structured_interpretation: "国内効能があることを脳神経外科急性出血の標準候補と同一視しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "血腫拡大抑制薬として施設内手順化しない"
  - "CSDH再発予防文脈を急性出血へ横展開しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "関連研究"
facility_confirmation_items:
  - "採用品"
  - "理由記録"
  - "保険方針"
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
  - "慢性硬膜下血腫"
  - "自然発症脳内出血"
---

# カルバゾクロム

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

血腫拡大抑制薬として標準化しない。

## 3. 原資料の該当箇所要約

カルバゾクロムは国内電子添文上の止血関連効能を持つが、脳内出血・頭部外傷・くも膜下出血の機能予後改善を支持する十分なエビデンスは乏しいとされ、施設内手順候補にしない。

## 4. GPTによる整理・解釈

国内効能があることを脳神経外科急性出血の標準候補と同一視しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 血腫拡大抑制薬として施設内手順化しない
- CSDH再発予防文脈を急性出血へ横展開しない

## 7. 必須確認事項

- 疾患文脈
- 目的
- 他の中和・補正が必要な状態の有無

## 8. 外部一次資料確認

- PMDA電子添文
- 関連研究

## 9. 施設内確認事項

- 採用品
- 理由記録
- 保険方針

## 10. 関連ノート

- [[慢性硬膜下血腫]]
- [[自然発症脳内出血]]

## 11. AI誤回答テスト候補

- カルバゾクロムを急性ICH標準候補とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/クリオプレシピテート.md


---
note_type: "drug"
title: "クリオプレシピテート"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1"
source_quote_or_summary: "クリオプレシピテートはフィブリノゲン等の補充として、施設基準に従い使用する扱い。"
gpt_structured_interpretation: "在庫・解凍時間・輸血部基準を確認せず候補化しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "在庫・解凍時間未確認で候補化しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "輸血療法関連指針"
facility_confirmation_items:
  - "採用品"
  - "在庫"
  - "解凍時間"
  - "輸血部SOP"
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
  - "低フィブリノゲン血症"
  - "輸血部確認"
---

# クリオプレシピテート

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

施設在庫や解凍時間未確認で候補化しない。

## 3. 原資料の該当箇所要約

クリオプレシピテートはフィブリノゲン等の補充として、施設基準に従い使用する扱い。

## 4. GPTによる整理・解釈

在庫・解凍時間・輸血部基準を確認せず候補化しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 在庫・解凍時間未確認で候補化しない

## 7. 必須確認事項

- フィブリノゲン値
- 輸血部基準
- 在庫
- 解凍時間

## 8. 外部一次資料確認

- 輸血療法関連指針

## 9. 施設内確認事項

- 採用品
- 在庫
- 解凍時間
- 輸血部SOP

## 10. 関連ノート

- [[低フィブリノゲン血症]]
- [[輸血部確認]]

## 11. AI誤回答テスト候補

- クリオを施設確認なしに候補化する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/デスモプレシン_DDAVP.md


---
note_type: "drug"
title: "デスモプレシン（DDAVP）"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W04 / 8.1 / 8.2"
source_quote_or_summary: "デスモプレシンはvWDや一部血友病Aの文脈と、抗血小板薬関連ICHの文脈を分ける。抗血小板薬関連ICHでは有効性不確実で標準候補化しない。"
gpt_structured_interpretation: "抗血小板薬曝露だけでDDAVP候補とするのは危険。低Naリスクや反復投与も確認する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬関連ICHで標準候補化しない"
  - "DDAVPを反応性未確認例に漫然反復しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "ICH guideline"
  - "血液疾患関連資料"
facility_confirmation_items:
  - "採用品"
  - "Naモニタリング体制"
  - "理由記録"
  - "専門医連携"
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
  - "W04_デスモプレシン_抗血小板薬関連ICHで標準候補化しない"
  - "抗血小板薬曝露"
---

# デスモプレシン（DDAVP）

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

抗血小板薬関連ICHでは、条件確認なしに施設内手順候補へ組み込まない。

## 3. 原資料の該当箇所要約

デスモプレシンはvWDや一部血友病Aの文脈と、抗血小板薬関連ICHの文脈を分ける。抗血小板薬関連ICHでは有効性不確実で標準候補化しない。

## 4. GPTによる整理・解釈

抗血小板薬曝露だけでDDAVP候補とするのは危険。低Naリスクや反復投与も確認する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬関連ICHで標準候補化しない
- DDAVPを反応性未確認例に漫然反復しない

## 7. 必須確認事項

- 適応文脈
- 抗血小板薬曝露
- 血小板数
- Na
- 腎機能
- 専門医判断

## 8. 外部一次資料確認

- PMDA電子添文
- ICH guideline
- 血液疾患関連資料

## 9. 施設内確認事項

- 採用品
- Naモニタリング体制
- 理由記録
- 専門医連携

## 10. 関連ノート

- [[W04_デスモプレシン_抗血小板薬関連ICHで標準候補化しない]]
- [[抗血小板薬曝露]]

## 11. AI誤回答テスト候補

- 抗血小板薬関連ICHでDDAVP標準とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/フィブリノゲン製剤.md


---
note_type: "drug"
title: "フィブリノゲン製剤"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1"
source_quote_or_summary: "フィブリノゲン製剤は低フィブリノゲン血症を伴う出血、術中大量出血等で検査値に基づき検討する。"
gpt_structured_interpretation: "検査値・輸血部基準なしに候補化しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "検査値なしに候補化しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "輸血療法関連指針"
  - "PMDA電子添文"
facility_confirmation_items:
  - "採用品"
  - "輸血部基準"
  - "払い出し手順"
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
  - "低フィブリノゲン血症"
  - "凝固異常"
---

# フィブリノゲン製剤

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

フィブリノゲン値未確認で標準候補化しない。

## 3. 原資料の該当箇所要約

フィブリノゲン製剤は低フィブリノゲン血症を伴う出血、術中大量出血等で検査値に基づき検討する。

## 4. GPTによる整理・解釈

検査値・輸血部基準なしに候補化しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 検査値なしに候補化しない

## 7. 必須確認事項

- フィブリノゲン値
- 出血量
- 術中/術後文脈
- 輸血部基準

## 8. 外部一次資料確認

- 輸血療法関連指針
- PMDA電子添文

## 9. 施設内確認事項

- 採用品
- 輸血部基準
- 払い出し手順

## 10. 関連ノート

- [[低フィブリノゲン血症]]
- [[凝固異常]]

## 11. AI誤回答テスト候補

- Fib値なしに製剤候補とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/プロタミン.md


---
note_type: "drug"
title: "プロタミン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.1 / D05"
source_quote_or_summary: "プロタミンは未分画ヘパリン等の中和であり、DOACやワルファリンには用いない。"
gpt_structured_interpretation: "ヘパリン中和文脈に限定し、aPTT/ACTや投与歴を確認する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DOACやワルファリンに使えると扱わない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
facility_confirmation_items:
  - "採用品"
  - "薬剤部手順"
  - "投与速度・最大量確認"
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
  - "抗凝固薬曝露"
---

# プロタミン

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

DOACやワルファリンの中和薬として扱わない。

## 3. 原資料の該当箇所要約

プロタミンは未分画ヘパリン等の中和であり、DOACやワルファリンには用いない。

## 4. GPTによる整理・解釈

ヘパリン中和文脈に限定し、aPTT/ACTや投与歴を確認する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DOACやワルファリンに使えると扱わない

## 7. 必須確認事項

- UFH/LMWH曝露
- 投与時刻
- aPTT/ACT
- 手術予定
- 過敏症リスク

## 8. 外部一次資料確認

- PMDA電子添文

## 9. 施設内確認事項

- 採用品
- 薬剤部手順
- 投与速度・最大量確認

## 10. 関連ノート

- [[抗凝固薬曝露]]

## 11. AI誤回答テスト候補

- DOACにプロタミンと回答する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/マンニトール.md


---
note_type: "drug"
title: "マンニトール"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "安全原則 / ICP管理"
source_quote_or_summary: "マンニトールはICP/脳浮腫の文脈で、腎機能、尿量、浸透圧、投与場所、看護観察体制と一体で扱う。"
gpt_structured_interpretation: "薬剤名だけで一般病棟標準運用にしない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "一般病棟で標準単独運用しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "ICP/TBI関連GL"
facility_confirmation_items:
  - "ICU/SCU/HCU運用"
  - "採血頻度"
  - "看護体制"
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
  - "W06_高張食塩液_マンニトール_監視条件なしに一般病棟標準運用しない"
  - "脳浮腫・頭蓋内圧上昇"
---

# マンニトール

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

一般病棟で監視条件なしに標準単独運用しない。

## 3. 原資料の該当箇所要約

マンニトールはICP/脳浮腫の文脈で、腎機能、尿量、浸透圧、投与場所、看護観察体制と一体で扱う。

## 4. GPTによる整理・解釈

薬剤名だけで一般病棟標準運用にしない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 一般病棟で標準単独運用しない

## 7. 必須確認事項

- 腎機能
- 尿量
- 血清浸透圧
- 投与場所
- 看護観察体制

## 8. 外部一次資料確認

- PMDA電子添文
- ICP/TBI関連GL

## 9. 施設内確認事項

- ICU/SCU/HCU運用
- 採血頻度
- 看護体制

## 10. 関連ノート

- [[W06_高張食塩液_マンニトール_監視条件なしに一般病棟標準運用しない]]
- [[脳浮腫・頭蓋内圧上昇]]

## 11. AI誤回答テスト候補

- マンニトールを一般病棟標準とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/血小板輸血.md


---
note_type: "drug"
title: "血小板輸血"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "W05 / 8.1 / D05"
source_quote_or_summary: "血小板輸血は抗血小板薬内服のみで一律候補にしない。緊急開頭・EVDなど侵襲的処置予定、血小板数、輸血部基準で分ける。"
gpt_structured_interpretation: "抗血小板薬曝露と血小板減少を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "輸血療法関連指針"
  - "ICH guideline"
  - "関連試験"
facility_confirmation_items:
  - "輸血部基準"
  - "夜間輸血体制"
  - "血小板在庫"
  - "手術前基準"
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
  - "W05_血小板輸血_抗血小板薬内服のみで候補にしない"
  - "抗血小板薬曝露"
  - "血小板減少"
  - "EVD"
---

# 血小板輸血

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

抗血小板薬内服のみで血小板輸血を施設内手順候補にしない。

## 3. 原資料の該当箇所要約

血小板輸血は抗血小板薬内服のみで一律候補にしない。緊急開頭・EVDなど侵襲的処置予定、血小板数、輸血部基準で分ける。

## 4. GPTによる整理・解釈

抗血小板薬曝露と血小板減少を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで候補化しない
- 抗血小板薬曝露と血小板減少を混同しない

## 7. 必須確認事項

- 血小板数
- 抗血小板薬名
- DAPT有無
- 緊急開頭/EVD/穿刺予定
- 輸血部基準

## 8. 外部一次資料確認

- 輸血療法関連指針
- ICH guideline
- 関連試験

## 9. 施設内確認事項

- 輸血部基準
- 夜間輸血体制
- 血小板在庫
- 手術前基準

## 10. 関連ノート

- [[W05_血小板輸血_抗血小板薬内服のみで候補にしない]]
- [[抗血小板薬曝露]]
- [[血小板減少]]
- [[EVD]]

## 11. AI誤回答テスト候補

- 抗血小板薬内服だけで血小板輸血とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer1_High_Risk/高張食塩液.md


---
note_type: "drug"
title: "高張食塩液"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "安全原則 / ICP管理"
source_quote_or_summary: "高張食塩液はNa、浸透圧、投与経路、腎機能、尿量、ICU/SCU相当監視と一体で扱う。"
gpt_structured_interpretation: "濃度や投与経路、Na補正速度は施設基準に連動するため原資料だけで固定しない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "監視条件なしに一般病棟標準運用しない"
  - "Na補正速度や浸透圧閾値を公開資料だけで固定しない"
undetermined_from_source:
  - "原資料からは最終運用可否を確定できない"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "ICP/TBI関連GL"
facility_confirmation_items:
  - "濃度規格"
  - "中心静脈要否"
  - "看護観察体制"
  - "採血頻度"
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
  - "W06_高張食塩液_マンニトール_監視条件なしに一般病棟標準運用しない"
  - "脳浮腫・頭蓋内圧上昇"
---

# 高張食塩液

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

監視条件なしの一般病棟標準運用をしない。

## 3. 原資料の該当箇所要約

高張食塩液はNa、浸透圧、投与経路、腎機能、尿量、ICU/SCU相当監視と一体で扱う。

## 4. GPTによる整理・解釈

濃度や投与経路、Na補正速度は施設基準に連動するため原資料だけで固定しない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 監視条件なしに一般病棟標準運用しない
- Na補正速度や浸透圧閾値を公開資料だけで固定しない

## 7. 必須確認事項

- 血清Na
- Na補正速度
- 浸透圧
- 腎機能
- 尿量
- 投与経路
- 病棟区分

## 8. 外部一次資料確認

- PMDA電子添文
- ICP/TBI関連GL

## 9. 施設内確認事項

- 濃度規格
- 中心静脈要否
- 看護観察体制
- 採血頻度

## 10. 関連ノート

- [[W06_高張食塩液_マンニトール_監視条件なしに一般病棟標準運用しない]]
- [[脳浮腫・頭蓋内圧上昇]]

## 11. AI誤回答テスト候補

- 高張食塩液を一般病棟標準とする誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/アピキサバン.md


---
note_type: "drug_layer2_indexed"
title: "アピキサバン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "アピキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "ダビガトランと同じ中和薬で扱わない"
  - "PCC代替使用を標準化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# アピキサバン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

アピキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- ダビガトランと同じ中和薬で扱わない
- PCC代替使用を標準化しない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- アピキサバンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/エドキサバン.md


---
note_type: "drug_layer2_indexed"
title: "エドキサバン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "エドキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "ダビガトランと同じ中和薬で扱わない"
  - "PCC代替使用を標準化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# エドキサバン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

エドキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- ダビガトランと同じ中和薬で扱わない
- PCC代替使用を標準化しない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- エドキサバンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/ダビガトラン.md


---
note_type: "drug_layer2_indexed"
title: "ダビガトラン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "ダビガトランはイダルシズマブの対象薬剤として分離して扱う。腎機能と最終服用時刻の確認が重要。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "Xa阻害薬と同じ中和薬で扱わない"
  - "腎機能未確認で判断しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# ダビガトラン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

ダビガトランはイダルシズマブの対象薬剤として分離して扱う。腎機能と最終服用時刻の確認が重要。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- Xa阻害薬と同じ中和薬で扱わない
- 腎機能未確認で判断しない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- ダビガトランを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/リバーロキサバン.md


---
note_type: "drug_layer2_indexed"
title: "リバーロキサバン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "リバーロキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "ダビガトランと同じ中和薬で扱わない"
  - "PCC代替使用を標準化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# リバーロキサバン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

リバーロキサバンはXa阻害薬としてアンデキサネット アルファの対象薬剤文脈で扱う。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- ダビガトランと同じ中和薬で扱わない
- PCC代替使用を標準化しない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- リバーロキサバンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/ワルファリン.md


---
note_type: "drug_layer2_indexed"
title: "ワルファリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "ワルファリンはVKA関連出血・緊急手術時の文脈で、PCCおよびビタミンK製剤と関連する。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DOAC関連出血と同列に扱わない"
  - "INR確認なしに補正候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# ワルファリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

ワルファリンはVKA関連出血・緊急手術時の文脈で、PCCおよびビタミンK製剤と関連する。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DOAC関連出血と同列に扱わない
- INR確認なしに補正候補化しない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- ワルファリンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/低分子ヘパリン.md


---
note_type: "drug_layer2_indexed"
title: "低分子ヘパリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "低分子ヘパリンはVTE予防・抗凝固再開文脈、腎機能、プロタミンでの中和可能性の扱いを確認する。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能未確認で用量・間隔を固定しない"
  - "UFHと完全同一に扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# 低分子ヘパリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

低分子ヘパリンはVTE予防・抗凝固再開文脈、腎機能、プロタミンでの中和可能性の扱いを確認する。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 腎機能未確認で用量・間隔を固定しない
- UFHと完全同一に扱わない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- 低分子ヘパリンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Anticoagulants/未分画ヘパリン.md


---
note_type: "drug_layer2_indexed"
title: "未分画ヘパリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "未分画ヘパリンはプロタミンによる中和、aPTT/ACT、治療用ヘパリンとflush heparinの区別が重要。"
gpt_structured_interpretation: "抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "flush heparinと治療用heparinを混同しない"
  - "DOAC/ワルファリンと同じ中和薬で扱わない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗凝固薬"
layer: "Layer2"
related_notes:
  - "抗凝固薬曝露"
  - "PCC_プロトロンビン複合体製剤"
  - "イダルシズマブ"
  - "アンデキサネット_アルファ"
  - "プロタミン"
  - "VTE予防_抗凝固再開"
---

# 未分画ヘパリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

未分画ヘパリンはプロタミンによる中和、aPTT/ACT、治療用ヘパリンとflush heparinの区別が重要。

## 4. GPTによる整理・解釈

抗凝固薬本体は中和薬ノートと再開ノートに接続するが、薬剤ごとの標的・検査・腎機能・中和薬を分離する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- flush heparinと治療用heparinを混同しない
- DOAC/ワルファリンと同じ中和薬で扱わない

## 7. 必須確認事項

- 薬剤名
- 最終服用/投与時刻
- 腎機能
- 関連凝固検査
- 手術/EVD予定
- 出血重症度

## 8. 関連ノート

- [[抗凝固薬曝露]]
- [[PCC_プロトロンビン複合体製剤]]
- [[イダルシズマブ]]
- [[アンデキサネット_アルファ]]
- [[プロタミン]]
- [[VTE予防_抗凝固再開]]

## 9. AI誤回答テスト候補

- 未分画ヘパリンを抗凝固薬として一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/アシクロビル.md


---
note_type: "drug_layer2_indexed"
title: "アシクロビル"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "脳炎疑い文脈で扱う。腎機能確認が重要。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗ウイルス薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# アシクロビル

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

脳炎疑い文脈で扱う。腎機能確認が重要。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 腎機能確認なしに候補化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- アシクロビルを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/アンピシリン.md


---
note_type: "drug_layer2_indexed"
title: "アンピシリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "リステリアリスクなど特定条件での追加文脈として扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "全髄膜炎疑いで一律追加としない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗菌薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# アンピシリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

リステリアリスクなど特定条件での追加文脈として扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 全髄膜炎疑いで一律追加としない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- アンピシリンを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/クリンダマイシン.md


---
note_type: "drug_layer2_indexed"
title: "クリンダマイシン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "βラクタムアレルギー時の周術期予防代替などで文脈化される。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "βラクタムアレルギー時の全感染症代替として一律化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗菌薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# クリンダマイシン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

βラクタムアレルギー時の周術期予防代替などで文脈化される。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- βラクタムアレルギー時の全感染症代替として一律化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- クリンダマイシンを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/セファゾリン.md


---
note_type: "drug_layer2_indexed"
title: "セファゾリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "清潔脳神経外科手術の周術期予防抗菌薬候補として文脈化される。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "予防抗菌薬と感染治療を混同しない"
  - "過長予防投与を標準化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗菌薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# セファゾリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

清潔脳神経外科手術の周術期予防抗菌薬候補として文脈化される。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 予防抗菌薬と感染治療を混同しない
- 過長予防投与を標準化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- セファゾリンを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/セフェピム.md


---
note_type: "drug_layer2_indexed"
title: "セフェピム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "EVD/シャント関連感染など医療関連感染文脈で扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗緑膿菌βラクタム"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# セフェピム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

EVD/シャント関連感染など医療関連感染文脈で扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 腎機能確認なしに候補化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- セフェピムを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/セフォタキシム.md


---
note_type: "drug_layer2_indexed"
title: "セフォタキシム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "疑い細菌性髄膜炎の初期対応文脈で扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "周術期予防抗菌薬と混同しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗菌薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# セフォタキシム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

疑い細菌性髄膜炎の初期対応文脈で扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 周術期予防抗菌薬と混同しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- セフォタキシムを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/セフタジジム.md


---
note_type: "drug_layer2_indexed"
title: "セフタジジム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "EVD/シャント関連感染など医療関連感染文脈で扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗緑膿菌βラクタム"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# セフタジジム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

EVD/シャント関連感染など医療関連感染文脈で扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 腎機能確認なしに候補化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- セフタジジムを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/セフトリアキソン.md


---
note_type: "drug_layer2_indexed"
title: "セフトリアキソン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "疑い細菌性髄膜炎の初期対応文脈で扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "周術期予防抗菌薬と混同しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗菌薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# セフトリアキソン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

疑い細菌性髄膜炎の初期対応文脈で扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 周術期予防抗菌薬と混同しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- セフトリアキソンを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/バンコマイシン.md


---
note_type: "drug_layer2_indexed"
title: "バンコマイシン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "EVD/シャント関連感染、髄膜炎、βラクタムアレルギー時など文脈別に扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "TDM・腎機能確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗MRSA薬"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# バンコマイシン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

EVD/シャント関連感染、髄膜炎、βラクタムアレルギー時など文脈別に扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- TDM・腎機能確認なしに候補化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- バンコマイシンを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antimicrobials/メロペネム.md


---
note_type: "drug_layer2_indexed"
title: "メロペネム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "EVD/シャント関連感染など医療関連感染文脈で扱う。"
gpt_structured_interpretation: "抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "耐性菌・施設アンチバイオグラム確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "カルバペネム"
layer: "Layer2"
related_notes:
  - "中枢神経感染症_周術期感染"
  - "EVD"
  - "シャント関連処置"
---

# メロペネム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

EVD/シャント関連感染など医療関連感染文脈で扱う。

## 4. GPTによる整理・解釈

抗菌薬・抗ウイルス薬は、周術期予防、疑い髄膜炎、EVD/シャント関連感染、脳炎疑いを分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 耐性菌・施設アンチバイオグラム確認なしに候補化しない

## 7. 必須確認事項

- 感染分類
- 予防か治療か
- EVD/シャント有無
- 腎機能
- アレルギー
- 施設アンチバイオグラム

## 8. 関連ノート

- [[中枢神経感染症_周術期感染]]
- [[EVD]]
- [[シャント関連処置]]

## 9. AI誤回答テスト候補

- メロペネムを予防と治療で混同する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/その他P2Y12阻害薬.md


---
note_type: "drug_layer2_indexed"
title: "その他P2Y12阻害薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "原資料または施設採用品に応じて追加確認するP2Y12阻害薬群。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# その他P2Y12阻害薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

原資料または施設採用品に応じて追加確認するP2Y12阻害薬群。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- その他P2Y12阻害薬内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/アスピリン.md


---
note_type: "drug_layer2_indexed"
title: "アスピリン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗血小板薬曝露の文脈で、血小板輸血やDDAVPの誤候補化を防ぐために索引化する。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# アスピリン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

抗血小板薬曝露の文脈で、血小板輸血やDDAVPの誤候補化を防ぐために索引化する。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- アスピリン内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/クロピドグレル.md


---
note_type: "drug_layer2_indexed"
title: "クロピドグレル"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# クロピドグレル

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- クロピドグレル内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/シロスタゾール.md


---
note_type: "drug_layer2_indexed"
title: "シロスタゾール"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗血小板薬本体として、薬剤名だけで血小板輸血候補化しないために索引化する。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# シロスタゾール

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

抗血小板薬本体として、薬剤名だけで血小板輸血候補化しないために索引化する。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- シロスタゾール内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/チカグレロル.md


---
note_type: "drug_layer2_indexed"
title: "チカグレロル"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# チカグレロル

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- チカグレロル内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiplatelets/プラスグレル.md


---
note_type: "drug_layer2_indexed"
title: "プラスグレル"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。"
gpt_structured_interpretation: "抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補化しない"
  - "抗血小板薬曝露と血小板減少を混同しない"
  - "DAPTを公開資料だけで固定候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗血小板薬"
layer: "Layer2"
related_notes:
  - "抗血小板薬曝露"
  - "血小板輸血"
  - "デスモプレシン_DDAVP"
  - "EVD"
  - "緊急開頭術"
---

# プラスグレル

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

P2Y12阻害薬として抗血小板薬曝露・DAPT文脈で扱う。

## 4. GPTによる整理・解釈

抗血小板薬本体は、抗血小板薬内服のみで血小板輸血・DDAVPを標準候補化しないための索引として扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補化しない
- 抗血小板薬曝露と血小板減少を混同しない
- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 薬剤名
- DAPT有無
- 最終内服時刻
- 血小板数
- 手術/EVD/穿刺予定

## 8. 関連ノート

- [[抗血小板薬曝露]]
- [[血小板輸血]]
- [[デスモプレシン_DDAVP]]
- [[EVD]]
- [[緊急開頭術]]

## 9. AI誤回答テスト候補

- プラスグレル内服だけで血小板輸血とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/ジアゼパム.md


---
note_type: "drug_layer2_indexed"
title: "ジアゼパム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "発作重積・救急初期対応や鎮静文脈で別救急セットと接続する薬剤。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "脳外科予防投与セットに混ぜない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# ジアゼパム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

発作重積・救急初期対応や鎮静文脈で別救急セットと接続する薬剤。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 脳外科予防投与セットに混ぜない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- ジアゼパムを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/バルプロ酸.md


---
note_type: "drug_layer2_indexed"
title: "バルプロ酸"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "肝機能、妊娠可能性、血小板などを確認すべき抗てんかん発作薬。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "妊娠可能性や肝機能を無視して候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# バルプロ酸

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

肝機能、妊娠可能性、血小板などを確認すべき抗てんかん発作薬。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 妊娠可能性や肝機能を無視して候補化しない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- バルプロ酸を予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/フェニトイン.md


---
note_type: "drug_layer2_indexed"
title: "フェニトイン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "TDM、相互作用、投与目的の確認が必要な抗てんかん発作薬。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "TDMや相互作用確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# フェニトイン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

TDM、相互作用、投与目的の確認が必要な抗てんかん発作薬。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- TDMや相互作用確認なしに候補化しない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- フェニトインを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/ホスフェニトイン.md


---
note_type: "drug_layer2_indexed"
title: "ホスフェニトイン"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗てんかん発作薬として、投与速度、循環器リスク、目的確認が必要。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "発作重積初期対応と脳外科予防投与セットを混同しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# ホスフェニトイン

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

抗てんかん発作薬として、投与速度、循環器リスク、目的確認が必要。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 発作重積初期対応と脳外科予防投与セットを混同しない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- ホスフェニトインを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/ミダゾラム.md


---
note_type: "drug_layer2_indexed"
title: "ミダゾラム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "発作重積・救急初期対応や鎮静文脈で別救急セットと接続する薬剤。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "脳外科予防投与セットに混ぜない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# ミダゾラム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

発作重積・救急初期対応や鎮静文脈で別救急セットと接続する薬剤。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 脳外科予防投与セットに混ぜない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- ミダゾラムを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/ラコサミド.md


---
note_type: "drug_layer2_indexed"
title: "ラコサミド"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "腎肝機能、心伝導、目的を確認すべき抗てんかん発作薬。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "心伝導・腎肝機能を無視して候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# ラコサミド

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

腎肝機能、心伝導、目的を確認すべき抗てんかん発作薬。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 心伝導・腎肝機能を無視して候補化しない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- ラコサミドを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Antiseizure_Medications/レベチラセタム.md


---
note_type: "drug_layer2_indexed"
title: "レベチラセタム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗てんかん発作薬として、予防投与・治療投与・重積初期対応を分ける。腎機能確認も必要。"
gpt_structured_interpretation: "抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "予防投与と治療投与を混同しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "抗てんかん発作薬"
layer: "Layer2"
related_notes:
  - "けいれんリスク"
  - "脳腫瘍周術期"
  - "外傷性脳損傷"
---

# レベチラセタム

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

抗てんかん発作薬として、予防投与・治療投与・重積初期対応を分ける。腎機能確認も必要。

## 4. GPTによる整理・解釈

抗てんかん発作薬は、発作治療、予防投与、重積初期対応、周術期管理を目的別に分ける。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 予防投与と治療投与を混同しない

## 7. 必須確認事項

- 投与目的
- 発作の有無
- 予防か治療か
- 腎機能
- 肝機能
- 相互作用
- 投与経路

## 8. 関連ノート

- [[けいれんリスク]]
- [[脳腫瘍周術期]]
- [[外傷性脳損傷]]

## 9. AI誤回答テスト候補

- レベチラセタムを予防・治療で一括扱いする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/VTE予防薬_方法.md


---
note_type: "drug_layer2_indexed"
title: "VTE予防薬・方法"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "薬物予防、機械的予防、抗凝固再開を分ける。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "中和と再開を同一フローにしない"
  - "CDSが再開日を自動決定しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "VTE予防"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# VTE予防薬・方法

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

薬物予防、機械的予防、抗凝固再開を分ける。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 中和と再開を同一フローにしない
- CDSが再開日を自動決定しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- VTE予防薬・方法を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/制吐薬.md


---
note_type: "drug_layer2_indexed"
title: "制吐薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "QT延長、錐体外路症状、採用品を確認する。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "採用品・禁忌確認なしに候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "制吐"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# 制吐薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

QT延長、錐体外路症状、採用品を確認する。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 採用品・禁忌確認なしに候補化しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- 制吐薬を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/胃粘膜保護薬.md


---
note_type: "drug_layer2_indexed"
title: "胃粘膜保護薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "過剰予防を避け、適応目的を確認する。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "目的不明の予防投与を標準化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "消化管保護"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# 胃粘膜保護薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

過剰予防を避け、適応目的を確認する。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 目的不明の予防投与を標準化しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- 胃粘膜保護薬を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/血糖管理薬.md


---
note_type: "drug_layer2_indexed"
title: "血糖管理薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "周術期・ICU・ステロイド使用時の血糖管理として施設基準を確認する。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "低血糖リスクや看護体制を無視して候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "血糖管理"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# 血糖管理薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

周術期・ICU・ステロイド使用時の血糖管理として施設基準を確認する。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 低血糖リスクや看護体制を無視して候補化しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- 血糖管理薬を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/鎮痛薬.md


---
note_type: "drug_layer2_indexed"
title: "鎮痛薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "意識評価、腎肝機能、併用薬との関係を確認する。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "意識評価への影響を無視して候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "鎮痛"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# 鎮痛薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

意識評価、腎肝機能、併用薬との関係を確認する。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 意識評価への影響を無視して候補化しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- 鎮痛薬を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Other_Supportive/鎮静薬.md


---
note_type: "drug_layer2_indexed"
title: "鎮静薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "神経評価、呼吸抑制、ICU運用との関係を確認する。"
gpt_structured_interpretation: "支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "神経評価への影響を無視して候補化しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "medium"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "鎮静"
layer: "Layer2"
related_notes:
  - "VTE予防_抗凝固再開"
  - "ICU_SCU_HCU管理"
  - "脳腫瘍周術期"
---

# 鎮静薬

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

神経評価、呼吸抑制、ICU運用との関係を確認する。

## 4. GPTによる整理・解釈

支持療法系薬剤は、主要アルゴリズムの中心ではないが、索引化して目的不明投与や施設運用推測を防ぐ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 神経評価への影響を無視して候補化しない

## 7. 必須確認事項

- 投与目的
- 禁忌
- 腎肝機能
- 看護観察体制
- 施設採用品

## 8. 関連ノート

- [[VTE予防_抗凝固再開]]
- [[ICU_SCU_HCU管理]]
- [[脳腫瘍周術期]]

## 9. AI誤回答テスト候補

- 鎮静薬を目的確認なしに候補化する誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Thrombolytics/アルテプラーゼ.md


---
note_type: "drug_layer2_indexed"
title: "アルテプラーゼ"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "急性虚血性脳卒中の血栓溶解薬として、投与適格性、出血時対応、24時間画像確認、二次予防との分離が必要。"
gpt_structured_interpretation: "アルテプラーゼは急性期治療、出血合併対応、抗血栓薬再開を分離して扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "rt-PA後24時間画像確認前に抗血小板薬・抗凝固薬を機械的開始しない"
  - "一般ICHと同じ出血対応にしない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "very_high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "血栓溶解薬"
layer: "Layer2"
related_notes:
  - "急性虚血性脳卒中"
  - "血栓溶解薬曝露"
  - "EVT"
---

# アルテプラーゼ

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

急性虚血性脳卒中の血栓溶解薬として、投与適格性、出血時対応、24時間画像確認、二次予防との分離が必要。

## 4. GPTによる整理・解釈

アルテプラーゼは急性期治療、出血合併対応、抗血栓薬再開を分離して扱う。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- rt-PA後24時間画像確認前に抗血小板薬・抗凝固薬を機械的開始しない
- 一般ICHと同じ出血対応にしない

## 7. 必須確認事項

- 発症時刻
- 画像
- 禁忌
- 凝固検査
- 投与時刻
- 症候性出血の有無

## 8. 関連ノート

- [[急性虚血性脳卒中]]
- [[血栓溶解薬曝露]]
- [[EVT]]

## 9. AI誤回答テスト候補

- rt-PA後すぐ抗血小板薬開始とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 03_Drugs/Layer2_Indexed/Thrombolytics/テネクテプラーゼ.md


---
note_type: "drug_layer2_indexed"
title: "テネクテプラーゼ"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "原資料に登場するか、また国内運用対象かを確認すべき血栓溶解薬。現時点では原資料から確定しない項目として索引化する。"
gpt_structured_interpretation: "テネクテプラーゼは、原資料内登場・国内薬事・施設採用を確認するまで標準候補にしない。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "原資料に登場するものとして扱わない"
  - "アルテプラーゼと同一扱いにしない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "最新電子添文"
  - "国内診療ガイドライン/関連指針"
  - "関連一次資料"
facility_confirmation_items:
  - "施設内採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "看護観察体制"
  - "委員会承認"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "Layer 2索引を処方指示として扱わない"
  - "薬剤名だけで標準候補と判断しない"
  - "同じ薬効群を同一扱いしない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
drug_class: "血栓溶解薬"
layer: "Layer2"
related_notes:
  - "急性虚血性脳卒中"
  - "血栓溶解薬曝露"
---

# テネクテプラーゼ

## 1. このノートの位置づけ

このノートは、Layer 2薬剤をKnowledge Vault上で索引化し、Layer 1高リスク薬剤・疾患・患者状態・処置予定との文脈混線を防ぐための初版です。正式な処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

Layer 2索引対象。詳細な施設内手順や処方候補ではなく、文脈混線を防ぐために登録する。

## 3. 原資料の該当箇所要約

原資料に登場するか、また国内運用対象かを確認すべき血栓溶解薬。現時点では原資料から確定しない項目として索引化する。

## 4. GPTによる整理・解釈

テネクテプラーゼは、原資料内登場・国内薬事・施設採用を確認するまで標準候補にしない。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設採用品・夜間休日在庫。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 原資料に登場するものとして扱わない
- アルテプラーゼと同一扱いにしない

## 7. 必須確認事項

- 原資料内登場有無
- 国内薬事
- 採用品
- 脳卒中SOP

## 8. 関連ノート

- [[急性虚血性脳卒中]]
- [[血栓溶解薬曝露]]

## 9. AI誤回答テスト候補

- テネクテプラーゼを原資料記載済み標準候補とする誤答を検出

## 10. 人間監査事項

薬剤部、診療科、医療安全、必要に応じて感染制御・輸血部・情報部門が確認してから、施設内候補や診療支援候補へ進める。



---


# FILE: 04_Drug_Classes/VTE予防.md


---
note_type: "drug_class"
title: "VTE予防"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "VTE予防に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "VTE予防は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "VTE予防薬・方法"
---

# VTE予防

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[VTE予防薬・方法]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/カルバペネム.md


---
note_type: "drug_class"
title: "カルバペネム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "カルバペネムに含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "カルバペネムは同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "メロペネム"
---

# カルバペネム

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[メロペネム]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/制吐.md


---
note_type: "drug_class"
title: "制吐"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "制吐に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "制吐は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "制吐薬"
---

# 制吐

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[制吐薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗MRSA薬.md


---
note_type: "drug_class"
title: "抗MRSA薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗MRSA薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗MRSA薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "バンコマイシン"
---

# 抗MRSA薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[バンコマイシン]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗てんかん発作薬.md


---
note_type: "drug_class"
title: "抗てんかん発作薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗てんかん発作薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗てんかん発作薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "レベチラセタム"
  - "ホスフェニトイン"
  - "フェニトイン"
  - "バルプロ酸"
  - "ラコサミド"
  - "ミダゾラム"
  - "ジアゼパム"
---

# 抗てんかん発作薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[レベチラセタム]]
- [[ホスフェニトイン]]
- [[フェニトイン]]
- [[バルプロ酸]]
- [[ラコサミド]]
- [[ミダゾラム]]
- [[ジアゼパム]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗ウイルス薬.md


---
note_type: "drug_class"
title: "抗ウイルス薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗ウイルス薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗ウイルス薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "アシクロビル"
---

# 抗ウイルス薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[アシクロビル]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗凝固薬.md


---
note_type: "drug_class"
title: "抗凝固薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗凝固薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗凝固薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "ワルファリン"
  - "ダビガトラン"
  - "アピキサバン"
  - "リバーロキサバン"
  - "エドキサバン"
  - "未分画ヘパリン"
  - "低分子ヘパリン"
---

# 抗凝固薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[ワルファリン]]
- [[ダビガトラン]]
- [[アピキサバン]]
- [[リバーロキサバン]]
- [[エドキサバン]]
- [[未分画ヘパリン]]
- [[低分子ヘパリン]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗緑膿菌βラクタム.md


---
note_type: "drug_class"
title: "抗緑膿菌βラクタム"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗緑膿菌βラクタムに含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗緑膿菌βラクタムは同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "セフェピム"
  - "セフタジジム"
---

# 抗緑膿菌βラクタム

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[セフェピム]]
- [[セフタジジム]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗菌薬.md


---
note_type: "drug_class"
title: "抗菌薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗菌薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗菌薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "セファゾリン"
  - "セフトリアキソン"
  - "セフォタキシム"
  - "アンピシリン"
  - "クリンダマイシン"
---

# 抗菌薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[セファゾリン]]
- [[セフトリアキソン]]
- [[セフォタキシム]]
- [[アンピシリン]]
- [[クリンダマイシン]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/抗血小板薬.md


---
note_type: "drug_class"
title: "抗血小板薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "抗血小板薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "抗血小板薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "アスピリン"
  - "クロピドグレル"
  - "プラスグレル"
  - "チカグレロル"
  - "シロスタゾール"
  - "その他P2Y12阻害薬"
---

# 抗血小板薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[アスピリン]]
- [[クロピドグレル]]
- [[プラスグレル]]
- [[チカグレロル]]
- [[シロスタゾール]]
- [[その他P2Y12阻害薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/消化管保護.md


---
note_type: "drug_class"
title: "消化管保護"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "消化管保護に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "消化管保護は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "胃粘膜保護薬"
---

# 消化管保護

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[胃粘膜保護薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/血栓溶解薬.md


---
note_type: "drug_class"
title: "血栓溶解薬"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "血栓溶解薬に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "血栓溶解薬は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "アルテプラーゼ"
  - "テネクテプラーゼ"
---

# 血栓溶解薬

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[アルテプラーゼ]]
- [[テネクテプラーゼ]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/血糖管理.md


---
note_type: "drug_class"
title: "血糖管理"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "血糖管理に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "血糖管理は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "血糖管理薬"
---

# 血糖管理

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[血糖管理薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/鎮痛.md


---
note_type: "drug_class"
title: "鎮痛"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "鎮痛に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "鎮痛は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "鎮痛薬"
---

# 鎮痛

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[鎮痛薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。



---


# FILE: 04_Drug_Classes/鎮静.md


---
note_type: "drug_class"
title: "鎮静"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S2 薬剤クラス詳細調査材料表"
source_quote_or_summary: "鎮静に含まれる薬剤を索引化し、薬剤ごとの差異を保持する。"
gpt_structured_interpretation: "鎮静は同効薬を一括推奨するための分類ではなく、製剤差・対象疾患差・禁忌差・運用差を確認するための索引。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終推奨は外部一次資料と施設内承認後に判断"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "同じ薬効群の薬剤を同一扱いしない"
  - "クラス名だけで薬剤を選択しない"
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
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "薬剤クラスノートを処方指示として扱わない"
  - "同効薬を一括推奨しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
included_drugs:
  - "鎮静薬"
---

# 鎮静

## 1. 位置づけ

このノートは薬剤クラス索引です。処方指示ではありません。

## 2. 含まれる薬剤

- [[鎮静薬]]

## 3. 標準化しない事項

- クラス名だけで薬剤を選択しない。
- 同じ薬効群でも、対象薬剤、禁忌、腎機能、処置予定、施設内運用が異なる場合は分ける。
