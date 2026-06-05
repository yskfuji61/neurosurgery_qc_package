---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/24_CDS_Time_Window_Alert_Boundaries/00_CDS_Time_Window_Alert_Boundaries.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: integrated_cds_time_window_boundary_summary_export_commit10
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
# 11 CDS CANDIDATE BOUNDARIES

## このファイルの役割

このファイルは、Knowledge に含まれる CDS candidate を、即時実装可能な仕様と誤読させないための境界定義です。

## clinician-facing summary

このファイルは「電子カルテにそのまま入れられる仕様」を示すものではありません。使い方としては、どこまでが注意喚起や設計たたき台で、どこから先が承認済みの本番仕様なのかを分けるための境界整理です。

## 実際の考え方

CDS の話題では、候補を出すこと自体は有用でも、薬剤提案や処方誘導に直結させると危険です。したがって、表示候補、入力条件、除外条件、責任分界、ログ設計を段階的に分けて考えます。

## CDS 候補の意味

CDS 候補とは、入力条件、表示条件、理由記録、確認フローの候補であって、order 自動生成や最終推奨を意味しません。

## High Constraint Input Control

1. 疾患名だけで trigger しない
2. 薬剤名だけで trigger しない
3. 患者状態、検査値、処置予定、施設運用確認が揃うまで確定出力しない

## 候補と実装仕様の差

1. 候補: 注意喚起、確認項目、理由記録案
2. 実装仕様: 入力制約、画面文言、責任者承認、監査ログ、受入テスト

## 実装前に必要なもの

1. 一次資料確認
2. 施設内 SOP との整合
3. 委員会承認
4. 誤作動時の責任分界
5. 監査ログ要件
6. 受入テスト

## 表示すべき確認項目の例

1. 最終服用・投与時刻
2. 薬剤クラス
3. 腎機能・凝固検査・血小板数
4. 手術 / EVD / 穿刺予定
5. 採用品・在庫・夜間休日可用性

## 表示してはいけないこと

1. 「この薬を投与すべき」と断定する文言
2. 「自動で order してよい」と読める文言
3. 施設未確認の薬剤を利用可能と断定する文言

## CDS 候補としては扱えるが即時仕様化しない例

1. 抗凝固薬関連出血の確認ダイアログ
2. rt-PA 後 24 時間画像未確認時の抗血栓再開警告
3. 高張食塩液開始前の Na / 浸透圧 / 尿量確認
4. EVD 前の抗血栓曝露確認

## 未確定事項・人間レビュー項目

1. 実装画面文言、ロジック、責任分界は別設計が必要です。
2. 本ファイルは CDS readiness の前提整理であり、 build spec ではありません。

## Integrated policy boundary export（Runbook Commit 10）

出典: `24_CDS_Time_Window_Alert_Boundaries/` の boundary summary。

1. confirmation-promoting CDS candidate の境界だけを扱い、production EHR/CDS specifications と混同しない。
2. automatic dose adjustment、administration、discontinuation、AI-determined prescribing behavior は禁止する。
3. CDS candidate、time-window context、EHR data availability、alert candidate から order set や final alert logic へ直結する user-facing conclusion は quarantine / unresolved とする。
