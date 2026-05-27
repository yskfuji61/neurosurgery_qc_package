# 02_diseases_patient_states_procedures.md

作成日: 2026-05-26

この統合MarkdownはRAG/Project Knowledge投入補助用です。正式な診療ガイドライン、処方指示、施設内手順、即時CDS仕様ではありません。



---


# FILE: 02_Diseases/VTE予防_抗凝固再開.md


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



---


# FILE: 02_Diseases/中枢神経感染症_周術期感染.md


---
note_type: "disease"
title: "中枢神経感染症・周術期感染"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "D02-D06 / 感染症"
source_quote_or_summary: "周術期予防、疑い髄膜炎、EVD/シャント感染、脳炎疑いを分ける。予防抗菌薬と感染治療を混同しない。"
gpt_structured_interpretation: "感染症ノートは予防と治療の分離ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "周術期予防抗菌薬と感染治療を混同しない"
  - "EVD全留置期間の予防的抗菌薬継続を標準化しない"
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

# 中枢神経感染症・周術期感染

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

周術期予防、疑い髄膜炎、EVD/シャント感染、脳炎疑いを分ける。予防抗菌薬と感染治療を混同しない。

## 4. GPTによる整理・解釈

感染症ノートは予防と治療の分離ハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 周術期予防抗菌薬と感染治療を混同しない
- EVD全留置期間の予防的抗菌薬継続を標準化しない

## 7. 必須確認事項

- 感染分類
- EVD/シャント有無
- 腎機能
- βラクタムアレルギー
- 施設アンチバイオグラム

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

- 中枢神経感染症・周術期感染を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/動脈瘤性くも膜下出血.md


---
note_type: "disease"
title: "動脈瘤性くも膜下出血"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.2 / W03"
source_quote_or_summary: "抗線溶薬は動脈瘤閉鎖前の短期橋渡し候補。閉鎖後の漫然継続や機能予後改善薬としての説明を避ける。"
gpt_structured_interpretation: "aSAHノートは閉鎖前後を分けるハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "閉鎖後も抗線溶薬を漫然継続しない"
  - "機能予後改善薬として説明しない"
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
  - "疾患名だけで薬剤選択しない"
  - "疾患ノートを薬剤推奨リストとして扱わない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 動脈瘤性くも膜下出血

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

抗線溶薬は動脈瘤閉鎖前の短期橋渡し候補。閉鎖後の漫然継続や機能予後改善薬としての説明を避ける。

## 4. GPTによる整理・解釈

aSAHノートは閉鎖前後を分けるハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 閉鎖後も抗線溶薬を漫然継続しない
- 機能予後改善薬として説明しない

## 7. 必須確認事項

- 動脈瘤閉鎖前後
- 閉鎖予定時刻
- 再出血リスク
- 脳虚血リスク

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

- 動脈瘤性くも膜下出血を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/外傷性脳損傷.md


---
note_type: "disease"
title: "外傷性脳損傷"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.2 / D01"
source_quote_or_summary: "TBIではTXAの扱いは受傷3時間以内など条件付き。受傷3時間超、時刻不明、既投与、禁忌では機械的候補化しない。"
gpt_structured_interpretation: "TBIノートは受傷時刻を主キーにした安全確認ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "TBIならTXAと短絡しない"
  - "受傷3時間超・時刻不明でTXAを機械的候補化しない"
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
  - "疾患名だけで薬剤選択しない"
  - "疾患ノートを薬剤推奨リストとして扱わない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 外傷性脳損傷

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

TBIではTXAの扱いは受傷3時間以内など条件付き。受傷3時間超、時刻不明、既投与、禁忌では機械的候補化しない。

## 4. GPTによる整理・解釈

TBIノートは受傷時刻を主キーにした安全確認ハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- TBIならTXAと短絡しない
- 受傷3時間超・時刻不明でTXAを機械的候補化しない

## 7. 必須確認事項

- 受傷時刻
- GCS
- 頭部CT
- 禁忌
- 既投与
- 血栓症リスク

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

- 外傷性脳損傷を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/急性虚血性脳卒中.md


---
note_type: "disease"
title: "急性虚血性脳卒中"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S0/S1 急性虚血性脳卒中"
source_quote_or_summary: "AISではrt-PA/EVT適格性、出血時対応、二次予防、抗血栓薬再開を分ける。"
gpt_structured_interpretation: "AISノートは急性期治療と二次予防の混同を防ぐハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "rt-PA後24時間画像確認前に抗血小板薬・抗凝固薬を機械的開始しない"
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

# 急性虚血性脳卒中

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

AISではrt-PA/EVT適格性、出血時対応、二次予防、抗血栓薬再開を分ける。

## 4. GPTによる整理・解釈

AISノートは急性期治療と二次予防の混同を防ぐハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- rt-PA後24時間画像確認前に抗血小板薬・抗凝固薬を機械的開始しない

## 7. 必須確認事項

- 発症時刻
- 画像
- rt-PA投与歴
- EVT予定
- 血糖
- 凝固検査

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

- 急性虚血性脳卒中を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/慢性硬膜下血腫.md


---
note_type: "disease"
title: "慢性硬膜下血腫"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.2"
source_quote_or_summary: "CSDH再発予防文脈のTXA/カルバゾクロム/五苓散などを、急性頭蓋内出血止血へ横展開しない。"
gpt_structured_interpretation: "CSDHノートは急性止血との混同を防ぐハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "CSDH再発予防を急性ICH/TBI止血へ横展開しない"
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

# 慢性硬膜下血腫

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

CSDH再発予防文脈のTXA/カルバゾクロム/五苓散などを、急性頭蓋内出血止血へ横展開しない。

## 4. GPTによる整理・解釈

CSDHノートは急性止血との混同を防ぐハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- CSDH再発予防を急性ICH/TBI止血へ横展開しない

## 7. 必須確認事項

- 手術法
- 再発リスク
- 抗血栓薬
- 腎機能
- 転倒リスク

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

- 慢性硬膜下血腫を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/抗血栓薬関連頭蓋内出血.md


---
note_type: "disease"
title: "抗血栓薬関連頭蓋内出血"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "抗血栓薬中和"
source_quote_or_summary: "抗凝固薬曝露、抗血小板薬曝露、血栓溶解薬曝露を分ける。薬剤名、最終服用時刻、腎機能、処置予定を確認する。"
gpt_structured_interpretation: "抗血栓薬関連ノートは薬剤曝露タイプ別の安全確認ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗凝固薬曝露と抗血小板薬曝露を同じ扱いにしない"
  - "抗血栓薬中和と再開を同一フローにしない"
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

# 抗血栓薬関連頭蓋内出血

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

抗凝固薬曝露、抗血小板薬曝露、血栓溶解薬曝露を分ける。薬剤名、最終服用時刻、腎機能、処置予定を確認する。

## 4. GPTによる整理・解釈

抗血栓薬関連ノートは薬剤曝露タイプ別の安全確認ハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗凝固薬曝露と抗血小板薬曝露を同じ扱いにしない
- 抗血栓薬中和と再開を同一フローにしない

## 7. 必須確認事項

- 薬剤名
- 最終服用時刻
- 腎機能
- PT-INR/aPTT
- 血小板数
- EVD/手術予定

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

- 抗血栓薬関連頭蓋内出血を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/脳浮腫_頭蓋内圧上昇.md


---
note_type: "disease"
title: "脳浮腫・頭蓋内圧上昇"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "安全原則 / ICP"
source_quote_or_summary: "高張食塩液・マンニトールはNa、浸透圧、尿量、腎機能、投与場所、看護観察体制と一体で扱う。"
gpt_structured_interpretation: "ICPノートは薬剤名より監視条件を主語にする。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "高張食塩液・マンニトールを一般病棟で標準単独運用しない"
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
  - "疾患名だけで薬剤選択しない"
  - "疾患ノートを薬剤推奨リストとして扱わない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 脳浮腫・頭蓋内圧上昇

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

高張食塩液・マンニトールはNa、浸透圧、尿量、腎機能、投与場所、看護観察体制と一体で扱う。

## 4. GPTによる整理・解釈

ICPノートは薬剤名より監視条件を主語にする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 高張食塩液・マンニトールを一般病棟で標準単独運用しない

## 7. 必須確認事項

- 血清Na
- 浸透圧
- 尿量
- 腎機能
- ICU/SCU/HCU相当監視

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

- 脳浮腫・頭蓋内圧上昇を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/脳腫瘍周術期.md


---
note_type: "disease"
title: "脳腫瘍周術期"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "付録S1/S2 脳腫瘍周術期"
source_quote_or_summary: "脳腫瘍周術期ではステロイド、ASM、抗菌薬、VTE予防を目的別に分離する。"
gpt_structured_interpretation: "周術期ノートは予防・治療・再評価期限の分離ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗てんかん発作薬の予防投与と治療投与を混同しない"
  - "周術期予防抗菌薬と感染治療を混同しない"
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

# 脳腫瘍周術期

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

脳腫瘍周術期ではステロイド、ASM、抗菌薬、VTE予防を目的別に分離する。

## 4. GPTによる整理・解釈

周術期ノートは予防・治療・再評価期限の分離ハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗てんかん発作薬の予防投与と治療投与を混同しない
- 周術期予防抗菌薬と感染治療を混同しない

## 7. 必須確認事項

- 発作歴
- 浮腫
- 術式
- 感染リスク
- VTEリスク

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

- 脳腫瘍周術期を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 02_Diseases/自然発症脳内出血.md


---
note_type: "disease"
title: "自然発症脳内出血"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "8.2 疾患・患者状態別の最終配置"
source_quote_or_summary: "抗血栓薬曝露、血腫拡大リスク、spot sign、手術予定、腎機能を確認し、TXA/rFVIIa/DDAVP/血小板輸血を条件確認なしに標準候補化しない。"
gpt_structured_interpretation: "疾患ノートは薬剤推奨表ではなく、患者状態・処置予定・条件・陰性知識へ接続するハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "TXAを日常的施設内手順候補にしない"
  - "rFVIIaを一律候補化しない"
  - "抗血小板薬内服のみで血小板輸血を候補にしない"
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
  - "疾患名だけで薬剤選択しない"
  - "疾患ノートを薬剤推奨リストとして扱わない"
  - "即時CDS仕様として扱わない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 自然発症脳内出血

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

疾患名だけで薬剤を選択せず、患者状態・処置予定・条件・陰性知識を確認する。

## 3. 原資料の該当箇所要約

抗血栓薬曝露、血腫拡大リスク、spot sign、手術予定、腎機能を確認し、TXA/rFVIIa/DDAVP/血小板輸血を条件確認なしに標準候補化しない。

## 4. GPTによる整理・解釈

疾患ノートは薬剤推奨表ではなく、患者状態・処置予定・条件・陰性知識へ接続するハブ。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- TXAを日常的施設内手順候補にしない
- rFVIIaを一律候補化しない
- 抗血小板薬内服のみで血小板輸血を候補にしない

## 7. 必須確認事項

- 抗凝固薬曝露
- 抗血小板薬曝露
- 血小板数
- PT-INR/aPTT/フィブリノゲン
- 手術/EVD予定
- 腎機能

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

- 自然発症脳内出血を薬剤推奨リストとして扱う誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/けいれんリスク.md


---
note_type: "patient_state"
title: "けいれんリスク"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "発作歴、病変、術式、EEG要否、腎肝機能を確認し、予防投与と治療投与を分ける。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗てんかん発作薬の予防投与と治療投与を混同しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# けいれんリスク

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

発作歴、病変、術式、EEG要否、腎肝機能を確認し、予防投与と治療投与を分ける。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗てんかん発作薬の予防投与と治療投与を混同しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- けいれんリスクを無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/低フィブリノゲン血症.md


---
note_type: "patient_state"
title: "低フィブリノゲン血症"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "フィブリノゲン値、出血量、輸血部基準を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "閾値を公開資料だけで固定しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 低フィブリノゲン血症

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

フィブリノゲン値、出血量、輸血部基準を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 閾値を公開資料だけで固定しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 低フィブリノゲン血症を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/凝固異常.md


---
note_type: "patient_state"
title: "凝固異常"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "PT-INR、aPTT、フィブリノゲン、薬剤歴、肝疾患、DICなど原因を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "検査未確認で補正薬を出さない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 凝固異常

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

PT-INR、aPTT、フィブリノゲン、薬剤歴、肝疾患、DICなど原因を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 検査未確認で補正薬を出さない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 凝固異常を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/夜間休日運用.md


---
note_type: "patient_state"
title: "夜間休日運用"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "夜間在庫、薬剤師当直/オンコール、輸血部、看護観察体制を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "夜間実行不能な手順を標準化しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 夜間休日運用

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

夜間在庫、薬剤師当直/オンコール、輸血部、看護観察体制を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 夜間実行不能な手順を標準化しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 夜間休日運用を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/妊娠可能性.md


---
note_type: "patient_state"
title: "妊娠可能性"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "妊娠可能性例は既定候補経路から外し、専門科協議とする。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "妊娠可能性例で薬剤選択を機械的候補化しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 妊娠可能性

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

妊娠可能性例は既定候補経路から外し、専門科協議とする。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 妊娠可能性例で薬剤選択を機械的候補化しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 妊娠可能性を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/抗凝固薬曝露.md


---
note_type: "patient_state"
title: "抗凝固薬曝露"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "薬剤名、最終服用時刻、腎機能、PT-INR/aPTT/ACT、手術/EVD予定を先に確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗凝固薬を一括してPCC候補にしない"
  - "中和と再開を同一フローにしない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 抗凝固薬曝露

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

薬剤名、最終服用時刻、腎機能、PT-INR/aPTT/ACT、手術/EVD予定を先に確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗凝固薬を一括してPCC候補にしない
- 中和と再開を同一フローにしない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 抗凝固薬曝露を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/抗血小板薬曝露.md


---
note_type: "patient_state"
title: "抗血小板薬曝露"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "内服のみで血小板輸血候補にしない。血小板数、DAPT、手術/EVD予定を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血を候補にしない"
  - "血小板減少と混同しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 抗血小板薬曝露

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

内服のみで血小板輸血候補にしない。血小板数、DAPT、手術/EVD予定を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬内服のみで血小板輸血を候補にしない
- 血小板減少と混同しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 抗血小板薬曝露を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/肝機能低下.md


---
note_type: "patient_state"
title: "肝機能低下"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "DOAC、ワルファリン、VPA等に影響する。重篤肝障害では機械的候補化しない。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "重篤肝障害で薬剤選択を機械的候補化しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 肝機能低下

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

DOAC、ワルファリン、VPA等に影響する。重篤肝障害では機械的候補化しない。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 重篤肝障害で薬剤選択を機械的候補化しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 肝機能低下を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/腎機能低下.md


---
note_type: "patient_state"
title: "腎機能低下"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "DOAC、TXA、LMWH、VCM、ACV、CFPM、MEPMなどに影響する。Cr/eGFR/CrCl、尿量を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能未確認で用量・間隔を固定しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 腎機能低下

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

DOAC、TXA、LMWH、VCM、ACV、CFPM、MEPMなどに影響する。Cr/eGFR/CrCl、尿量を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 腎機能未確認で用量・間隔を固定しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 腎機能低下を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/血小板減少.md


---
note_type: "patient_state"
title: "血小板減少"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "血小板数、出血、処置予定、輸血部基準を確認する。抗血小板薬曝露とは分ける。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬曝露と血小板減少を混同しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 血小板減少

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

血小板数、出血、処置予定、輸血部基準を確認する。抗血小板薬曝露とは分ける。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 抗血小板薬曝露と血小板減少を混同しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 血小板減少を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/血栓溶解薬曝露.md


---
note_type: "patient_state"
title: "血栓溶解薬曝露"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "rt-PA等の投与時刻、画像、フィブリノゲン、症候性出血を確認し、二次予防と分ける。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "一般ICHと同じ扱いにしない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 血栓溶解薬曝露

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

rt-PA等の投与時刻、画像、フィブリノゲン、症候性出血を確認し、二次予防と分ける。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 一般ICHと同じ扱いにしない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 血栓溶解薬曝露を無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 05_Patient_States/血栓症高リスク.md


---
note_type: "patient_state"
title: "血栓症高リスク"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "患者状態別判断"
source_quote_or_summary: "止血薬、抗線溶薬、rFVIIa、再開判断に影響する。既往や機械弁、DVT/PE等を確認する。"
gpt_structured_interpretation: "患者状態ノートは薬剤選択前の安全確認ハブとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "出血対応と血栓予防を一括化しない"
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
  - "患者状態ノートを処方指示として扱わない"
  - "薬剤名だけで候補化しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 血栓症高リスク

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

薬剤候補を考える前に確認する患者状態であり、処方指示ではない。

## 3. 原資料の該当箇所要約

止血薬、抗線溶薬、rFVIIa、再開判断に影響する。既往や機械弁、DVT/PE等を確認する。

## 4. GPTによる整理・解釈

関連薬剤・疾患に先立ち、安全確認事項を提示する。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 出血対応と血栓予防を一括化しない

## 7. 必須確認事項

- 関連薬剤歴
- 検査値
- 処置予定
- 施設内運用可否

## 8. 外部一次資料確認

- 電子添文
- 国内GL
- 関連指針

## 9. 施設内確認事項

- 採用品
- 夜間在庫
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[処置予定ハブ_初版]]

## 11. AI誤回答テスト候補

- 血栓症高リスクを無視して薬剤候補を出す誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/EVD.md


---
note_type: "procedure"
title: "EVD"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "挿入/抜去前後の抗血栓薬、凝固・血小板、感染予防、VTE再開を分ける。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "EVD全留置期間の予防抗菌薬継続を標準化しない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# EVD

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

挿入/抜去前後の抗血栓薬、凝固・血小板、感染予防、VTE再開を分ける。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- EVD全留置期間の予防抗菌薬継続を標準化しない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- EVDを疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/EVT.md


---
note_type: "procedure"
title: "EVT"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "rt-PA、抗血小板、抗凝固、造影剤、腎機能、画像確認を分ける。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DAPT/bridgingを公開資料だけで候補化しない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# EVT

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

rt-PA、抗血小板、抗凝固、造影剤、腎機能、画像確認を分ける。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DAPT/bridgingを公開資料だけで候補化しない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- EVTを疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/ICU_SCU_HCU管理.md


---
note_type: "procedure"
title: "ICU/SCU/HCU管理"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "高リスク薬、浸透圧療法、鎮静、重症出血、感染症治療の監視条件を扱う。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "一般病棟と同じ運用にしない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# ICU/SCU/HCU管理

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

高リスク薬、浸透圧療法、鎮静、重症出血、感染症治療の監視条件を扱う。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 一般病棟と同じ運用にしない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- ICU/SCU/HCU管理を疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/クリッピング.md


---
note_type: "procedure"
title: "クリッピング"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "aSAHの動脈瘤閉鎖前後で抗線溶薬の扱いを分ける。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "閉鎖後TXA漫然継続をしない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# クリッピング

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

aSAHの動脈瘤閉鎖前後で抗線溶薬の扱いを分ける。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 閉鎖後TXA漫然継続をしない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- クリッピングを疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/コイル塞栓術.md


---
note_type: "procedure"
title: "コイル塞栓術"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "閉鎖前後、ステント有無、抗血小板薬要否を専門医判断として分ける。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "DAPTを公開資料だけで固定候補化しない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# コイル塞栓術

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

閉鎖前後、ステント有無、抗血小板薬要否を専門医判断として分ける。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- DAPTを公開資料だけで固定候補化しない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- コイル塞栓術を疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/シャント関連処置.md


---
note_type: "procedure"
title: "シャント関連処置"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "予防抗菌薬、感染治療、抗血栓管理を分ける。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "予防抗菌薬と感染治療を混同しない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# シャント関連処置

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

予防抗菌薬、感染治療、抗血栓管理を分ける。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 予防抗菌薬と感染治療を混同しない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- シャント関連処置を疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/保存的管理.md


---
note_type: "procedure"
title: "保存的管理"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "侵襲的処置前補正と分け、再評価、画像、VTE予防/再開を管理する。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "処置予定なしでEVD/手術前補正を自動表示しない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 保存的管理

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

侵襲的処置前補正と分け、再評価、画像、VTE予防/再開を管理する。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 処置予定なしでEVD/手術前補正を自動表示しない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- 保存的管理を疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 06_Procedures/緊急開頭術.md


---
note_type: "procedure"
title: "緊急開頭術"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "処置予定別判断"
source_quote_or_summary: "抗凝固薬・抗血小板薬、血小板数、PT-INR/aPTT/Fib、予防抗菌薬、ASM、輸血部/薬剤部確認を横断する。"
gpt_structured_interpretation: "処置予定ノートは休薬・中和・補正・感染予防・VTE再開の横断ハブ。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "疾患名だけで術前薬剤を決めない"
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
  - "処置予定ノートを処方指示として扱わない"
  - "疾患名だけで処置前後の薬剤判断をしない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-05-26"
---

# 緊急開頭術

## 1. このノートの位置づけ

このノートは、添付DOCXをAIが誤読しないようにするためのKnowledge Vault用初版です。正式な診療ガイドライン、処方指示、施設内手順、電子カルテ診療支援仕様ではありません。

## 2. 結論

処置予定により、休薬・中和・補正・感染予防・VTE再開の判断が変わる。

## 3. 原資料の該当箇所要約

抗凝固薬・抗血小板薬、血小板数、PT-INR/aPTT/Fib、予防抗菌薬、ASM、輸血部/薬剤部確認を横断する。

## 4. GPTによる整理・解釈

疾患ノートや薬剤ノートから独立した横断ハブとする。

## 5. 原資料からは確定できないこと

- 国内薬事上の最終位置づけ。
- 保険・査定上の最終扱い。
- 施設内採用品、在庫、夜間休日対応。
- 薬剤部調製・払い出し手順。
- 看護観察体制。
- 委員会承認後の標準運用可否。
- 電子カルテ診療支援としての実装可否。

## 6. 標準化しない事項

- 疾患名だけで術前薬剤を決めない

## 7. 必須確認事項

- 処置予定
- 緊急度
- 抗血栓薬曝露
- 凝固検査
- 血小板数
- 感染リスク

## 8. 外部一次資料確認

- 国内GL
- 周術期抗菌薬指針
- 輸血指針

## 9. 施設内確認事項

- 手術SOP
- 輸血部基準
- 薬剤部手順
- 看護観察体制

## 10. 関連ノート

- [[疾患ハブ_初版]]
- [[患者状態ハブ_初版]]

## 11. AI誤回答テスト候補

- 緊急開頭術を疾患名だけで判断する誤答を検出

## 12. 人間監査事項

このノートは、薬剤部、診療科、医療安全、必要に応じて輸血部・感染制御・情報部門が確認してから運用候補に進める。



---


# FILE: 13_Thresholds_Conditions/PT_INR.md


---
note_type: "condition_threshold"
title: "PT-INR"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "抗凝固薬関連出血 / VKA"
source_quote_or_summary: "PT-INRは薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "INR未確認でPCC等を候補化しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# PT-INR

## 確認事項

- ワルファリン
- PCC
- ビタミンK
- 手術/EVD予定

## 標準化しない事項

- INR未確認でPCC等を候補化しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/aPTT_ACT.md


---
note_type: "condition_threshold"
title: "aPTT / ACT"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "ヘパリン関連 / 血管内治療"
source_quote_or_summary: "aPTT / ACTは薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "UFHとDOACを同じ検査軸で扱わない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# aPTT / ACT

## 確認事項

- UFH
- プロタミン
- EVT
- 手術

## 標準化しない事項

- UFHとDOACを同じ検査軸で扱わない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/フィブリノゲン値.md


---
note_type: "condition_threshold"
title: "フィブリノゲン値"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "低フィブリノゲン血症 / 輸血製剤"
source_quote_or_summary: "フィブリノゲン値は薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "閾値を公開資料だけで固定しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# フィブリノゲン値

## 確認事項

- フィブリノゲン製剤
- FFP
- クリオ
- 大量出血

## 標準化しない事項

- 閾値を公開資料だけで固定しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/動脈瘤閉鎖前_原則24時間以内.md


---
note_type: "condition_threshold"
title: "動脈瘤閉鎖前・原則24時間以内"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "aSAH / 抗線溶薬"
source_quote_or_summary: "動脈瘤閉鎖前・原則24時間以内は薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "閉鎖後に抗線溶薬を漫然継続しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# 動脈瘤閉鎖前・原則24時間以内

## 確認事項

- 閉鎖前後
- 閉鎖予定時刻
- 搬送遅延
- 脳虚血リスク

## 標準化しない事項

- 閉鎖後に抗線溶薬を漫然継続しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/受傷3時間以内.md


---
note_type: "condition_threshold"
title: "受傷3時間以内"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "TBI / TXA"
source_quote_or_summary: "受傷3時間以内は薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "受傷3時間超・不明でTXAを機械的候補化しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# 受傷3時間以内

## 確認事項

- 受傷時刻
- 信頼性
- 既投与
- 禁忌
- GCS/CT

## 標準化しない事項

- 受傷3時間超・不明でTXAを機械的候補化しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/腎機能_CrCl_eGFR.md


---
note_type: "condition_threshold"
title: "腎機能 CrCl/eGFR"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "DOAC / TXA / 抗菌薬 / ACV / LMWH"
source_quote_or_summary: "腎機能 CrCl/eGFRは薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "腎機能未確認で用量・間隔を固定しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# 腎機能 CrCl/eGFR

## 確認事項

- DOAC
- TXA
- VCM
- ACV
- CFPM
- MEPM
- LMWH

## 標準化しない事項

- 腎機能未確認で用量・間隔を固定しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/血小板数.md


---
note_type: "condition_threshold"
title: "血小板数"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "血小板輸血 / 処置予定"
source_quote_or_summary: "血小板数は薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "抗血小板薬内服のみで血小板輸血にしない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# 血小板数

## 確認事項

- 血小板減少
- 抗血小板薬曝露
- 緊急開頭
- EVD

## 標準化しない事項

- 抗血小板薬内服のみで血小板輸血にしない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。



---


# FILE: 13_Thresholds_Conditions/血清Na_浸透圧_尿量.md


---
note_type: "condition_threshold"
title: "血清Na・浸透圧・尿量"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "ICP管理 / 浸透圧療法"
source_quote_or_summary: "血清Na・浸透圧・尿量は薬剤候補化前に確認すべき条件・閾値である。"
gpt_structured_interpretation: "条件・閾値ノートは薬剤名や疾患名の短絡を防ぐ主キーとして扱う。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "監視条件なしに一般病棟標準運用しない"
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
  - "施設内閾値"
  - "検査実施体制"
  - "夜間休日対応"
  - "看護観察体制"
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

# 血清Na・浸透圧・尿量

## 確認事項

- 高張食塩液
- マンニトール
- 腎機能
- ICU/SCU

## 標準化しない事項

- 監視条件なしに一般病棟標準運用しない

## 注意

この条件ノートは、処方指示ではありません。閾値や時間条件は外部一次資料と施設内基準で確認する必要があります。
