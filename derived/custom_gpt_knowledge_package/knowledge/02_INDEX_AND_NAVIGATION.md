---
document_role: "custom_gpt_rag_knowledge"
package_name: "neurosurgery_qc_custom_gpt_knowledge_package"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
requires_primary_source_check: true
requires_facility_confirmation: true
requires_human_review: true
source_repository: "https://github.com/yskfuji61/neurosurgery_qc_package"
source_scope: "Integrated_Obsidian_Vault and related audit/export files"
rag_chunk_policy: "safety_first_cross_reference_required"
---

# 02 INDEX AND NAVIGATION

## このファイルの役割

このファイルは、Custom GPT がどの質問でどの knowledge ファイルを横断参照すべきかを定義する索引です。

## 疾患ノート一覧

主に [04_DISEASE_NOTES.md](04_DISEASE_NOTES.md) を参照します。

1. 自然発症脳内出血
2. 外傷性脳損傷
3. 動脈瘤性くも膜下出血
4. 慢性硬膜下血腫
5. 脳浮腫・頭蓋内圧上昇
6. 中枢神経感染症・周術期感染
7. VTE 予防・抗凝固再開
8. 急性虚血性脳卒中
9. 脳腫瘍周術期
10. 抗血栓薬関連頭蓋内出血

## 薬剤・薬効分類ノート一覧

主に [05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md](05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md) を参照します。

1. 抗凝固薬
2. 抗血小板薬
3. 血栓溶解薬
4. 抗てんかん発作薬
5. 抗菌薬
6. 抗 MRSA 薬
7. 抗緑膿菌 β ラクタム
8. カルバペネム
9. 抗ウイルス薬
10. VTE 予防
11. 鎮静
12. 鎮痛
13. 制吐
14. 消化管保護
15. 血糖管理

## 患者状態ノート一覧

主に [06_PATIENT_STATE_NOTES.md](06_PATIENT_STATE_NOTES.md) を参照します。

1. 抗凝固薬曝露
2. 抗血小板薬曝露
3. 血栓溶解薬曝露
4. 腎機能低下
5. 肝機能低下
6. 妊娠可能性
7. 血小板減少
8. 凝固異常
9. 低フィブリノゲン血症
10. 血栓症高リスク
11. けいれんリスク
12. 夜間休日運用

## 処置・周術期ノート一覧

主に [07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md](07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md) を参照します。

1. 緊急開頭術
2. EVD
3. EVT
4. クリッピング
5. コイル塞栓術
6. シャント関連処置
7. 保存的管理
8. ICU / SCU / HCU 管理

## 閾値・条件ノート一覧

主に [08_THRESHOLDS_AND_CONDITIONS.md](08_THRESHOLDS_AND_CONDITIONS.md) を参照します。

1. 受傷 3 時間以内
2. 動脈瘤閉鎖前・原則 24 時間以内
3. PT-INR
4. aPTT / ACT
5. 血小板数
6. フィブリノゲン値
7. 血清 Na・浸透圧・尿量
8. 腎機能 CrCl / eGFR

## Evidence チェックリスト一覧

主に [09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md](09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md) を参照します。

1. PMDA 電子添文
2. RMP・安全性情報
3. 周術期抗菌薬・感染制御
4. 輸血療法関連指針
5. 国内脳卒中 GL
6. 海外主要 GL
7. CRASH-3
8. TICH-2
9. ULTRA

## 施設運用チェックリスト一覧

主に [10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md](10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md) を参照します。

1. 委員会承認
2. 施設採用品・夜間休日在庫
3. 看護観察体制
4. 薬剤部調製・払い出し
5. 輸血部運用
6. ICU / SCU / HCU / 一般病棟運用

## 誤回答テスト一覧

主に [12_AI_ERROR_TESTS_AND_VALIDATION.md](12_AI_ERROR_TESTS_AND_VALIDATION.md) を参照します。

1. PCC と DOAC 関連出血
2. 自然発症 ICH と rFVIIa
3. TXA と頭蓋内出血
4. 抗血小板薬曝露と血小板輸血
5. アンデキサネット アルファの施設即時使用可否
6. CDS 即時実装可否

## 監査・更新関連ファイル一覧

主に [13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md](13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md) を参照します。

1. 更新トリガー
2. 一次資料改訂時対応
3. 施設運用変更時対応
4. Preview 不合格時対応
5. 監査ログテンプレート

## 質問別の横断参照ガイド

1. 疾患名を含む質問: `04` + `06` + `07` + `08` + `09`
2. 薬剤名や薬効分類を含む質問: `03` + `05` + `06` + `08` + `10`
3. 周術期や処置を含む質問: `04` + `07` + `08` + `10` + `11`
4. EHR / CDS / 自動化の質問: `03` + `10` + `11` + `12` + `13`
5. 施設で使えるかを問う質問: `03` + `05` + `10` + `09`
6. 一次資料で何を確認すべきかの質問: `09` + `10` + `13`

## 検索補助語

検索補助語です。医学的同一性を断定するものではありません。

1. ICH / intracerebral hemorrhage
2. TBI / traumatic brain injury
3. SAH / subarachnoid hemorrhage
4. EVD / external ventricular drainage
5. EVT / endovascular treatment
6. PMDA / package insert / RMP

## 未確定事項・人間レビュー項目

1. 実際の質問パターンによっては、ここにない横断参照が必要になることがあります。
2. Custom GPT Preview で、索引導線が十分に機能するか確認が必要です。
