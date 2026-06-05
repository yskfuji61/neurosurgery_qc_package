---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/13_Dosing_Adjustment_Boundaries/00_Dosing_Adjustment_Boundaries.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: integrated_drug_boundary_summary_export_commit10
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
# 05 DRUG CLASS AND LAYER2 DRUG NOTES

## このファイルの役割

このファイルは、薬効分類ノートと Layer 2 indexed drugs の caution を統合し、薬剤名だけで候補化しないための参照面を提供します。

## clinician-facing summary

薬剤ノートは「この薬を使うべきか」を直ちに決めるためではなく、何を確認しないと危険かを整理するために使います。実務上は、薬剤名から考え始めてもよいですが、その直後に薬剤クラス、適応文脈、患者状態、処置予定、施設で扱えるかを切り分ける必要があります。

## 実際の考え方

同じ「抗凝固薬関連」「抗血小板薬関連」と見えても、中和や代替候補は薬剤ごとに異なります。薬剤名は出発点にはなりますが、結論そのものではありません。

## 抗凝固薬

代表例: ワルファリン、ダビガトラン、アピキサバン、リバーロキサバン、エドキサバン、未分画ヘパリン、低分子ヘパリン。

1. 薬剤名、最終服用時刻、腎機能、関連凝固検査、手術 / EVD 予定を確認します。
2. VKA、ダビガトラン、Xa 阻害薬、ヘパリン系を同じ reversal にしません。
3. flush heparin と治療用 heparin を混同しません。

## 抗血小板薬

代表例: アスピリン、クロピドグレル、プラスグレル、チカグレロル、シロスタゾール、その他 P2Y12 阻害薬。

1. DAPT の有無、最終内服時刻、血小板数、手術 / EVD / 穿刺予定を確認します。
2. 抗血小板薬曝露だけで血小板輸血を候補化しません。
3. DAPT を公開資料だけで固定候補化しません。

## 血栓溶解薬

代表例: アルテプラーゼ、テネクテプラーゼ。

1. 投与時刻、24 時間画像確認、出血性合併症の有無を確認します。
2. アルテプラーゼとテネクテプラーゼを同一扱いにしません。
3. 原資料に登場しない薬剤を原資料記載ありと扱いません。

## 抗てんかん発作薬

代表例: レベチラセタム、ホスフェニトイン、フェニトイン、バルプロ酸、ラコサミド、ミダゾラム、ジアゼパム。

1. 予防投与か治療投与かを分離します。
2. 腎機能、肝機能、相互作用、投与経路を確認します。
3. 発作重積初期対応と脳外科予防投与セットを混同しません。

## 抗菌薬

代表例: セファゾリン、セフトリアキソン、セフォタキシム、アンピシリン、クリンダマイシン。

1. 予防か治療か、感染分類、EVD / シャント有無、アレルギーを確認します。
2. 周術期予防抗菌薬を治療レジメンへ機械的に流用しません。

## 抗 MRSA 薬

代表例: バンコマイシン。

1. TDM、腎機能、施設・地域の薬剤感受性傾向をまとめた資料（antibiogram）を確認します。
2. 予防投与と治療投与を混同しません。

## 抗緑膿菌 β ラクタム

代表例: セフェピム、セフタジジム。

1. 腎機能と対象感染症を確認します。
2. 広域抗菌薬への変更を、一律運用として扱いません。

## カルバペネム

代表例: メロペネム。

1. 耐性菌リスク、施設・地域の薬剤感受性傾向をまとめた資料（antibiogram）、感染重症度を確認します。
2. 耐性圧や抗菌薬の狭域化（de-escalation）を無視して、一律の候補として扱いません。

## 抗ウイルス薬

代表例: アシクロビル。

1. 腎機能と適応文脈を確認します。
2. すべての CNS 感染疑いで一律化しません。

## VTE 予防

代表例: VTE 予防薬・方法。

1. 機械的予防と薬物予防を分離します。
2. 出血高リスク時に自動で薬物予防へ寄せません。

## 鎮静

代表例: 鎮静薬。

1. 神経所見評価への影響を確認します。
2. ICU 以外で routine 化しません。

## 鎮痛

代表例: 鎮痛薬。

1. 意識評価や呼吸抑制への影響を確認します。
2. 画一的 order set として扱いません。

## 制吐

代表例: 制吐薬。

1. 禁忌、相互作用、採用品を確認します。
2. 併用薬と病棟運用を無視して固定化しません。

## 消化管保護

代表例: 胃粘膜保護薬。

1. 目的不明の予防投与を標準化しません。
2. すべての患者へ自動付与しません。

## 血糖管理

代表例: 血糖管理薬。

1. 低血糖リスク、看護体制、病棟レベルを確認します。
2. ICU と一般病棟を同じ管理前提で扱いません。

## Layer 2 薬剤名の検索補助語

検索補助語です。医学的同一性を断定するものではありません。

1. Warfarin
2. Dabigatran
3. Apixaban
4. Rivaroxaban
5. Edoxaban
6. Aspirin
7. Clopidogrel
8. Alteplase
9. Levetiracetam
10. Vancomycin

## 未確定事項・人間レビュー項目

1. 薬剤ごとの国内薬事、保険、採用品、在庫は対象施設で再確認が必要です。
2. 個別薬剤の候補可否は `06`、`07`、`08`、`09`、`10` を併用して判断します。

## Integrated policy boundary export（Runbook Commit 10）

出典: integrated vault の `13_Dosing_Adjustment_Boundaries/`、`14_Interactions_Contraindications/`、`15_IV_Compatibility_Admin_Boundaries/`、`21_Repeat_Dosing_Interval_Policy/`、`22_TDM_Steady_State_Policy/` の boundary summary。具体用量・間隔・同一ライン混注・側管投与の可否断定は含めない。

1. **用量調整**: source-confirmed かつ human-reviewed でない患者個別の薬剤量・透析時運用・投与管理は user-facing conclusion にしない。
2. **相互作用・禁忌**: source-confirmed かつ human-reviewed でない相互作用、禁忌、併用可否は結論として出さない。
3. **IV compatibility / 投与境界**: facility-confirmed でない compatibility、調製、投与管理、投与経路は結論にしない。
4. **反復投与間隔**: last administration、cumulative exposure、interval だけで反復投与・薬剤変更・投与管理・CDS 実装へ直結しない。固定間隔や dose-adjustment assertion を書かない。
5. **TDM / steady state**: trough/peak、steady state、sampling timing だけで薬剤開始・変更・投与管理・CDS 実装へ直結しない。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

**Gap v3 薬効領域（reference-only / hold — 第一選択薬リストではない）:**

1. 神経腫瘍薬物療法 — 一般名プロファイル、PMDA 製品単位未解決
2. 下垂体内分泌薬 — 同上
3. 術中可視化・造影剤 — 手技・造影文脈。治療薬プロファイルと混同しない
4. CSF / IIH 関連薬 — 施設 IIH・ICP プロトコル要確認
5. 血管内治療・血管攣縮局所薬 — Neuro-ICU / 調製・施設手順要確認
6. 痙縮・機能的脳神経外科薬 — ITB / ボツリヌス / DBS パスウェイ要確認
7. 中枢神経感染・脳室内投与 — 脳室内投与 SOP 要確認

いずれも: 用法・用量は製品単位添付文書遵守。適用外は医師の個別判断なしに標準化しない。CHILD 127 inventory との盲検マージ禁止。
