---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/99_Exports/Upload_Bundles/02_diseases_patient_states_procedures.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: procedure_bundle_summary_export_commit10
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
# 07 PROCEDURE AND PERIOPERATIVE NOTES

## このファイルの役割

このファイルは、処置予定や周術期タイミングが薬剤判断を大きく変えることを固定します。

## clinician-facing summary

処置予定があるかどうかで、同じ薬剤でも意味が変わります。特に緊急開頭術、EVD、EVT、動脈瘤閉鎖前後では、薬剤の可否だけでなく、いつまでに何を確認すべきかが変わります。

## 実際の考え方

薬剤の話だけで完結させず、処置の時間軸とチーム運用まで含めて考えるのがこのノートの役割です。手術や穿刺が近いほど、検査値や曝露薬の意味は重くなります。

## 緊急開頭術

1. 抗血栓薬曝露、凝固検査、輸血関連準備、薬剤部・輸血部運用を確認します。
2. 手術予定の有無は reversal 判断を大きく変えます。

## EVD

1. 抗凝固薬、抗血小板薬、血小板数、凝固異常を確認します。
2. 手技関連出血リスクと夜間休日体制を分離して扱います。

## EVT

1. rt-PA 後 24 時間条件、抗血栓再開、出血性合併症を確認します。
2. 脳卒中 pathway と脳外科出血対応を混同しません。

## クリッピング

1. 動脈瘤閉鎖前後の時間軸を確認します。
2. 閉鎖前 24 時間条件と周術期運用を飛ばしません。

## コイル塞栓術

1. 抗血小板薬、周術期運用、血管内治療 team の flow を確認します。
2. クリッピングと同じ前提に固定しません。

## シャント関連処置

1. 感染リスク、抗菌薬文脈、抗血栓薬曝露、手技タイミングを確認します。
2. EVD と完全同一のフローにしません。

## 保存的管理

1. ICU / HCU / 一般病棟の別、神経所見観察、浸透圧療法、VTE 予防を確認します。
2. 手術なしだから確認不要とは扱いません。

## ICU / SCU / HCU 管理

1. 高張食塩液、マンニトール、鎮静、血糖管理、看護観察体制を確認します。
2. 一般病棟と同じ order 前提にしません。

## 未確定事項・人間レビュー項目

1. 実際の処置準備フローは施設ごとに異なります。
2. ここで示すのは確認軸であり、手順書そのものではありません。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

1. **術中可視化・造影:** gap v3 の造影/可視化 reference は手技・造影文脈であり、標準的な治療薬プロファイルではない。用法・用量は製品単位添付文書と放射線・麻酔・手術室 SOP で確認（`10`）。
2. **血管内・局所薬:** プロシージャル文脈と全身治療を混同しない。施設 Neuro-ICU / 血管内手順を `10` で確認。
3. 適用外使用を、医師判断なしに「当院の術中ルーティン」として断定しない。
