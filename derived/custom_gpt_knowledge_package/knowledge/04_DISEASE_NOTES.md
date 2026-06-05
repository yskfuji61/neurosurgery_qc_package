---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/99_Exports/Upload_Bundles/02_diseases_patient_states_procedures.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: bundle_split_summary_export_commit10
included_for_custom_gpt: true
operator_side_only: false
human_review_required: true
not_a_guideline: true
not_a_prescription_order: true
not_immediate_cds_specification: true
no_patient_specific_dose_decision: true
no_auto_intervention_decision: true
requires_primary_source_check: true
requires_facility_confirmation: true
requires_human_review: true
source_repository: "https://github.com/yskfuji61/neurosurgery_qc_package"
source_scope: "Integrated_Obsidian_Vault and related audit/export files"
rag_chunk_policy: safety_first_cross_reference_required
tests_link: "derived/custom_gpt_knowledge_package/tests/pass_fail_criteria.md"
not_an_institutional_procedure: true
---
# 04 DISEASE NOTES

## このファイルの役割

このファイルは、疾患単位のノートを統合し、薬剤候補を疾患名だけで短絡しないための起点を提供します。

## clinician-facing summary

疾患名だけでは薬剤選択は決まりませんが、疾患から考え始めること自体は有用です。実際には、疾患ごとに「何を止めたいのか」「何を避けたいのか」「何を先に確認するか」を押さえ、その後で曝露薬、検査値、処置予定、施設運用へ展開する使い方を想定します。

## 実際の考え方

疾患ノートは、薬剤の可否を単独で決めるためのものではなく、問題設定を外さないための入口です。たとえば ICH と TBI では TXA の位置づけが違い、aSAH では時間軸と処置タイミングが中心になり、感染症では予防と治療の分離が先になります。

## 自然発症脳内出血

### Knowledge 上の位置づけ

出血制御、曝露薬評価、処置予定、閾値確認、Evidence 確認を横断参照する中心ノートです。

### 分岐する点

1. 抗凝固薬・抗血小板薬曝露の有無
2. PT-INR、aPTT、血小板数、フィブリノゲン値
3. 手術、EVD、保存的管理の別

### 標準化しない事項

1. rFVIIa を一律候補化しない。
2. PCC を DOAC 関連出血へ機械的に延長しない。
3. TXA を全例へ一般化しない。

### 要確認

要一次資料確認、要施設内確認、要人間レビュー。

## 外傷性脳損傷

### Knowledge 上の位置づけ

受傷時刻、TXA 関連 Evidence、抗血栓薬曝露、緊急処置の有無を結ぶノートです。

### 分岐する点

1. 受傷 3 時間以内か
2. 手術や ICP 管理が必要か
3. 抗凝固薬・抗血小板薬曝露があるか

### 標準化しない事項

1. TXA を全 TBI に一律化しない。
2. 抗血栓薬関連出血と非曝露例を同じ reversal フローにしない。

### 要確認

CRASH-3、施設 trauma workflow、夜間休日運用の確認が必要です。

## 動脈瘤性くも膜下出血

### Knowledge 上の位置づけ

動脈瘤閉鎖前の時間軸、再出血回避、処置タイミング、周術期管理を扱います。

### 分岐する点

1. 動脈瘤閉鎖前か後か
2. クリッピングかコイル塞栓術か
3. ICU / SCU の観察体制があるか

### 標準化しない事項

1. 薬剤候補だけで再出血予防を完結させない。
2. 閉鎖前 24 時間の時間条件を無視しない。

### 要確認

一次資料、脳卒中 GL、施設周術期体制の確認が必要です。

## 慢性硬膜下血腫

### Knowledge 上の位置づけ

穿頭ドレナージや再手術予定と抗血栓薬曝露評価を接続します。

### 分岐する点

1. 手術予定の有無
2. 抗凝固薬・抗血小板薬曝露
3. 再発リスクと血栓症リスクのバランス

### 標準化しない事項

1. 再開日を疾患名だけで固定しない。
2. 抗血小板薬曝露だけで血小板輸血を標準化しない。

### 要確認

施設方針、周術期運用、看護観察体制の確認が必要です。

## 脳浮腫・頭蓋内圧上昇

### Knowledge 上の位置づけ

マンニトール、高張食塩液、Na / 浸透圧 / 尿量監視、病棟レベル制約を扱います。

### 分岐する点

1. ICU レベルの観察が可能か
2. 腎機能、尿量、浸透圧評価
3. 併存する外傷、出血、腫瘍、感染の別

### 標準化しない事項

1. 一般病棟での固定運用を前提にしない。
2. Na、浸透圧、尿量を見ずに薬剤候補化しない。

### 要確認

施設内観察体制、採用品、補液・モニタリング体制の確認が必要です。

## 中枢神経感染症・周術期感染

### Knowledge 上の位置づけ

予防抗菌薬と治療抗菌薬を分離し、EVD・シャント・術後感染文脈を扱います。

### 分岐する点

1. 予防か治療か
2. EVD / シャント / 術後感染の別
3. 腎機能、アレルギー、施設 antibiogram

### 標準化しない事項

1. セファゾリンなどの周術期予防抗菌薬を感染治療に流用しない。
2. 広域薬を antibiogram 未確認で一律化しない。

### 要確認

感染制御資料、PMDA 電子添文、施設採用品の確認が必要です。

## VTE 予防・抗凝固再開

### Knowledge 上の位置づけ

VTE 予防と therapeutic anticoagulation 再開を分離するための中核ノートです。

### 分岐する点

1. 予防か再開か
2. 出血再発リスクと血栓症リスク
3. 手術、EVD、ドレーン、安静度

### 標準化しない事項

1. 再開日を自動決定しない。
2. 予防と治療を同一 order set 的に扱わない。

### 要確認

国内外 GL、施設術後 SOP、看護体制の確認が必要です。

## 急性虚血性脳卒中

### Knowledge 上の位置づけ

血栓溶解療法後 24 時間条件、EVT、抗血栓再開、出血性合併症の境界を扱います。

### 分岐する点

1. アルテプラーゼ曝露の有無
2. EVT 実施の有無
3. 24 時間画像確認前か後か

### 標準化しない事項

1. rt-PA 後 24 時間条件を飛ばさない。
2. 出血性合併症を一般 ICH と完全同一に扱わない。

### 要確認

脳卒中 GL、施設 stroke pathway、画像確認体制の確認が必要です。

## 脳腫瘍周術期

### Knowledge 上の位置づけ

けいれん予防・治療、脳浮腫管理、感染予防、血栓予防を周術期文脈で結びます。

### 分岐する点

1. 予防投与か治療投与か
2. 開頭術前後か
3. 腎機能、肝機能、相互作用、看護体制

### 標準化しない事項

1. 抗てんかん薬の予防投与と発作治療を混同しない。
2. 鎮静や制吐を routine で固定化しない。

### 要確認

術式、術後経過、薬剤部方針、病棟運用の確認が必要です。

## 抗血栓薬関連頭蓋内出血

### Knowledge 上の位置づけ

曝露薬同定、特異的中和薬、代替候補、輸血関連判断、処置予定を最も厳格に分離するノートです。

### 分岐する点

1. VKA、ダビガトラン、Xa 阻害薬、ヘパリン、抗血小板薬の別
2. 最終服用・投与時刻
3. 手術、EVD、保存的管理の別

### 標準化しない事項

1. 薬剤クラス横断で同じ reversal を当てない。
2. 施設採用品や在庫を未確認で可用と書かない。

### 要確認

PMDA、RMP、輸血関連指針、施設在庫、薬剤部と輸血部運用の確認が必要です。

## 未確定事項・人間レビュー項目

1. 個別疾患の最終候補は `05` から `10` と必ず横断参照してください。
2. 疾患名だけの問い合わせには、必ず不足情報を明示して答える必要があります。
### Integrated governance boundary export（Stage 4 — 脳腫瘍周術期）

1. 本ノートの脳腫瘍周術期は、けいれん・浮腫・感染予防・血栓予防など**周術期文脈**に限る。
2. PARENT gap v3 の神経腫瘍薬物プロファイル（一般名・PMDA 未解決）は **reference-only**。本ノート本文へ化学療法レジメン・抗腫瘍薬用量をマージしない。
3. 抗腫瘍薬の用法・用量は製品単位電子添文と施設腫瘍プロトコルで確認。適用外は医師判断なしに推奨しない。
