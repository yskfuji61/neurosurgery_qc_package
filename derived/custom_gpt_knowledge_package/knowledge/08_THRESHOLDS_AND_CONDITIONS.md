---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/23_Statistical_Aggregation_Policy/00_Statistical_Aggregation_Policy.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: integrated_aggregation_boundary_summary_export_commit10
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
# 08 THRESHOLDS AND CONDITIONS

## このファイルの役割

このファイルは、時刻条件、検査値条件、監視条件を閾値ノートとしてまとめ、疾患名や薬剤名だけで判断しないことを支えます。

## clinician-facing summary

このファイルは、検査値や時刻条件だけで結論を出すためのものではありません。実務上は、どの場面で条件を切り分けないと危険かを整理するために使い、疾患、薬剤、患者状態、処置予定を分ける補助線として参照します。

## 実際の考え方

閾値や条件は、候補を絞る材料ではあっても、それ自体が推奨や処方の根拠になるわけではありません。たとえば受傷時刻、凝固検査、血小板数、Na や浸透圧は、何を避けるべきか、どこで追加確認が必要かを見極めるために使います。

## 受傷 3 時間以内

1. TBI と TXA 関連 Evidence を参照するときの時間条件です。
2. 3 時間外で同じ意味に扱いません。

## 動脈瘤閉鎖前・原則 24 時間以内

1. くも膜下出血の再出血回避と周術期判断に関わる時間条件です。
2. 閉鎖前後を混同しません。

## PT-INR

1. VKA 関連評価の中心検査です。
2. 検査値のみで DOAC と区別しません。

## aPTT / ACT

1. ヘパリン関連評価や手技前確認の補助検査です。
2. 単独で最終判断しません。

## 血小板数

1. 抗血小板薬曝露と独立して確認します。
2. 曝露と血小板減少を同一概念として扱いません。

## フィブリノゲン値

1. 出血時や輸血関連判断で参照します。
2. 単独で輸血製剤候補を確定しません。

## 血清 Na・浸透圧・尿量

1. 浸透圧療法や高張食塩液関連では、処方・投与判断の根拠ではなく、確認漏れを避けるために優先して確認する項目です。
2. ICU以外で扱う場合は、検査値だけでなく、施設手順、看護観察体制、責任医・薬剤部確認を含めて運用可否を確認します。

## 腎機能 CrCl / eGFR

1. DOAC、LMWH、アシクロビル、バンコマイシンなどで重要です。
2. 腎機能未確認で候補化しません。

## 閾値の使い方

1. 閾値は候補の絞り込み条件であり、単独の推奨条件ではありません。
2. 閾値が揃っても、一次資料確認、施設内確認、人間レビューは残ります。

## 未確定事項・人間レビュー項目

1. 具体的な cut-off や運用閾値は施設資料で確認が必要です。
2. 本ファイルは、閾値確認が必要な場面を示すためのものです。

## Integrated policy boundary export（Runbook Commit 10）

出典: `20_Lab_Trend_Time_Window_Policy/`、`23_Statistical_Aggregation_Policy/` の boundary summary。

1. 検査値の推移や time-window 文脈から薬剤開始、薬剤変更、投与管理、CDS 実装へ直結する conclusion は出さない。
2. 統計処理（mean、median、moving average、rate of change、slope 等）は review support であり、medication decision ではない。
3. single value、latest value、outlier だけで action を決めない。aggregation を十分条件として記載しない。
