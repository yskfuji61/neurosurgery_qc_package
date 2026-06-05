---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/12_Drug_Label_Source_Hierarchy/00_Source_Hierarchy.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: integrated_source_hierarchy_summary_export_commit10
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
# 09 EVIDENCE AND PRIMARY SOURCE CHECKLISTS

## このファイルの役割

このファイルは、Knowledge内の候補や注意事項を確認するために、参照すべき一次資料とエビデンス確認項目をまとめたものです。

## 医療従事者向け要約（clinician-facing summary）

このファイルは、候補をそのまま正当化するための一覧ではなく、何を確認したいときにどの資料を見るべきかを整理するためのガイドです。PMDA、RMP、国内外 guideline、RCT は役割が異なるため、確認目的を分けて参照する前提で使います。

## このファイルを開く場面

薬剤や対応の候補が見えてきたあとに、国内薬事、安全性情報、ガイドライン、臨床試験でどこまで確認できるかを整理するために使います。エビデンスは重要な確認材料ですが、それだけで施設採用品、処方、またはオーダー化を確定する根拠にはなりません。

## PMDA製品単位確認が未完了のgap v3参考資料（Sibling gap v3 reference）

この参考資料は、神経腫瘍、下垂体、造影・手技などに関する一般名ベースの補足資料です。販売名、添付文書URL、RMPなどのPMDA製品単位情報は未確認のため、推測で補完しません。この資料は、本Knowledge 13本へそのまま取り込む対象ではありません。確認が必要な場合は、まず製品単位のPMDAページと施設採用品を確認します。この参考資料は、人間レビュー後の索引としてのみ使用します。127薬剤のPMDA作業資料と、内容確認なしに統合してはいけません。

参照パス: `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/`

## PMDA 電子添文チェック

1. 国内薬事上の位置づけ
2. 禁忌、警告、慎重投与
3. 用法用量、投与経路、適応

## RMP・安全性情報チェック

1. 安全性更新情報
2. 追加リスク最小化策
3. 高リスク薬剤の注意事項

## 周術期抗菌薬・感染制御チェック

1. 予防抗菌薬と治療抗菌薬の区別
2. 術式、デバイス、感染制御の確認
3. 施設・地域の薬剤感受性傾向をまとめた資料（antibiogram）の確認

## 輸血療法関連指針チェック

1. 血小板輸血、FFP、フィブリノゲン関連の確認
2. 抗血小板薬曝露と血小板減少の切り分け
3. 輸血部運用との接続

## 国内脳卒中 GL チェック

1. 急性虚血性脳卒中
2. 脳内出血
3. 抗血栓再開や周術期文脈の確認

## 海外主要 GL チェック

1. 国内資料で不足する論点の補完
2. ただし国内薬事や施設運用の代替にはしない

## CRASH-3 チェック

1. TBI と TXA の時間条件
2. 外傷文脈以外へ機械的に拡張しない

## TICH-2 チェック

1. 自然発症 ICH と TXA 関連 Evidence の確認
2. 海外資料や Evidence の記載を、日本国内での一律運用や通常使用可に直結させない

## ULTRA チェック

1. くも膜下出血や周術期文脈での参照事項を確認
2. 施設実装可能性とは分けて扱う

## Evidence の使い方

1. Evidence は候補の裏付けであり、施設採用品や order 化の裏付けではありません。
2. 一次資料と施設内確認を飛ばして Evidence だけで結論にしません。

## 未確定事項・人間レビュー項目

1. 最新版の改訂日は都度確認が必要です。
2. 論文や guideline の解釈差は人間レビューで吸収してください。

## 統合ポリシー上の安全境界（Runbook Commit 10）

出典は、Integrated_Obsidian_Vault/12_Drug_Label_Source_Hierarchy/ および 16_Guideline_Label_Separation/ にある、確認済みの安全境界要約です。この要約には、数値、用法、同一ライン混注、側管投与の可否は含めません。

### 薬剤ラベル情報の確認順序（Drug label source hierarchy）

1. 国内薬事・製品単位確認は PMDA 関連資料を最優先で見る。RMP / 安全性情報は別軸で確認する。
2. guideline、JAPIC、manufacturer documents は背景整理と照合に用い、国内薬事確認の代替にしない。
3. formulary、薬剤部手順、委員会承認、EHR medication master は facility confirmation として別管理する。
4. 出典分類（source class）の順序は、処方上の優先順位（prescribing hierarchy）ではありません。特定の出典分類に該当する資料があるだけでは、Knowledgeへの反映や薬剤選択を許可しません。

### Guideline と label の分離

1. ガイドライン記載だけで国内薬事、施設採用、EHR/CDS 実装を確定したように見える summary は出さない。
2. ガイドライン、添付文書、保険、施設採用、CDS候補を同一視する利用者向け結論は、安全上未解決の内容として扱い、回答やKnowledge反映の対象から外します（quarantine / unresolved）。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

### 製品単位添付文書（PMDA）— 用法・用量の一次確認

1. 販売名・規格・最新電子添文・適応・用法用量は**製品単位**で確認する（一般名プロファイルと同一視しない）。
2. RMP / IF / 患者向医薬品ガイドは該当製品で確認する。
3. 参考資料や台帳に登録されているだけでは、添付文書の内容が確認済みであるとは扱いません。

### 適用外使用の確認軸

1. 承認範囲を超える使用か（添付文書との照合）。
2. 医師の個別判断の有無と記録。
3. 施設プロトコル・倫理委員会・適用外使用規程の有無（`10`）。
4. 適用外を文献だけで一般化して回答しない。

### CHILD / PARENT の使い分け

- PMDA確認用の作業資料366件（CHILD）には、施設採用や使用可否が未確認の127薬剤候補が含まれます。
- gap v3関連の参考資料191件（PARENT）を含めた557件の台帳行は、確認状況を追跡するためのものです。内容確認なしにKnowledgeへ転記することを許可するものではありません。
