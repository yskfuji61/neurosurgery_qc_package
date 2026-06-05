---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/10_Operationalization/Formulary_Stock/施設採用品_夜間休日在庫チェックリスト.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: operational_checklist_summary_export_commit10
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
# 10 OPERATIONAL AND FACILITY CHECKLISTS

## このファイルの役割

このファイルは、候補が施設内で実際に扱えるかを確認する operational checklist を集約します。

## clinician-facing summary

薬剤や対応が理論上ありえても、施設で実際に扱えるかは別問題です。このファイルは「使えるか使えないか」を断定するためではなく、採用品、在庫、手順、看護体制、病棟レベルのどこで実運用が止まりうるかを整理するために使います。

## 実際の考え方

施設運用の話題では、医学的適応と operational feasibility を一つに潰さないことが重要です。臨床的に論点になることと、今その施設で安全に回せることは別々に確認します。

## 委員会承認

1. 高リスク薬剤や新規運用が委員会承認済みか
2. 例外運用の責任者が明確か

## 施設採用品・夜間休日在庫

1. アンデキサネット アルファ、イダルシズマブ、PCC、輸血関連製剤などの採用品確認
2. 夜間休日の在庫・払出可否確認

## 看護観察体制

1. 高張食塩液、マンニトール、鎮静、血糖管理、輸血時の監視体制確認
2. 一般病棟で実施可能かの確認

## 薬剤部調製・払い出し

1. 調製手順、払出手順、オンコール体制
2. 高リスク薬剤の理由記録やダブルチェック要件

## 輸血部運用

1. 血小板、FFP、フィブリノゲン関連製剤の手配可否
2. 緊急手術時の turnaround と連絡体制

## ICU / SCU / HCU / 一般病棟運用

1. 病棟レベルごとの観察、投与、モニタリング可否
2. ICU 前提の療法を一般病棟へ延長しない

## 施設運用の使い方

1. 施設運用が未確認のときは「施設内確認が必要」と答えます。
2. 採用品不明、在庫不明、手順不明を可用と書きません。

## 未確定事項・人間レビュー項目

1. 実運用は施設差が大きいため、現場責任者確認が必要です。
2. 本ファイルは施設運用確認の論点整理であり、施設手順書ではありません。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

1. **適用外使用:** 施設内で適用外が許容される場合でも、本 Knowledge だけでは可用と断定しない。医師判断・委員会・記録様式を施設で確認する。
2. **Gap v3 領域:** 腫瘍プロトコル、造影 SOP、IIH/ICP プロトコル、ITB/DBS パスウェイ、脳室内投与 SOP など、領域ごとの施設 evidence が未確認のときは「施設内確認が必要」と答える。
3. **採用品:** reference プロファイルの薬剤名を、施設採用品確定と混同しない。
