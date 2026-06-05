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

このファイルは、Knowledge 内の候補や caution を最終確認するための一次資料・Evidence チェックリストをまとめます。

## clinician-facing summary

このファイルは、候補をそのまま正当化するための一覧ではなく、何を確認したいときにどの資料を見るべきかを整理するためのガイドです。PMDA、RMP、国内外 guideline、RCT は役割が異なるため、確認目的を分けて参照する前提で使います。

## このファイルを開く場面

薬剤や対応の候補が見えてきたあとに、「国内薬事はどうか」「安全性情報は更新されていないか」「この論点は guideline や trial でどこまで支えられるか」を確認したい場面で開きます。Evidence は重要ですが、施設採用品や order 化の代わりにはなりません。

## Sibling gap v3 reference（PMDA 未解決）

ワークスペース sibling の `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` は、神経腫瘍・下垂体・造影/手技などの **一般名ベース gap supplement** である。PMDA 製品単位（販売名・添付文書 URL・RMP 等）は **未解決** のまま推測で埋めない。本 Knowledge 13 本にそのまま取り込む設計ではない。確認が必要なときは、製品単位 PMDA ページと施設採用品を先に確認し、reference プロファイルは人間監査後の索引としてのみ使う。CHILD（127 薬剤 PMDA 作業 corpus）との inventory 盲検マージは禁止する。

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
3. 施設 antibiogram の必要性

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

## Integrated policy boundary export（Runbook Commit 10）

出典: `Integrated_Obsidian_Vault/12_Drug_Label_Source_Hierarchy/` および `16_Guideline_Label_Separation/` の reviewed boundary summary。数値・用法・同一ライン混注・側管投与の可否は含めない。

### Drug label source hierarchy（確認順序のみ）

1. 国内薬事・製品単位確認は PMDA 関連資料を最優先で見る。RMP / 安全性情報は別軸で確認する。
2. guideline、JAPIC、manufacturer documents は背景整理と照合に用い、国内薬事確認の代替にしない。
3. formulary、薬剤部手順、委員会承認、EHR medication master は facility confirmation として別管理する。
4. source class の順序は prescribing hierarchy ではない。source class の存在だけで derived export や薬剤選択を許可しない。

### Guideline と label の分離

1. ガイドライン記載だけで国内薬事、施設採用、EHR/CDS 実装を確定したように見える summary は出さない。
2. ガイドライン、label、保険、施設採用、CDS candidate を同一視する user-facing conclusion は quarantine / unresolved として扱う。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

### 製品単位添付文書（PMDA）— 用法・用量の一次確認

1. 販売名・規格・最新電子添文・適応・用法用量は**製品単位**で確認する（一般名プロファイルと同一視しない）。
2. RMP / IF / 患者向医薬品ガイドは該当製品で確認する。
3. reference または ledger 登録だけでは、添付文書内容の確定根拠にならない。

### 適用外使用の確認軸

1. 承認範囲を超える使用か（添付文書との照合）。
2. 医師の個別判断の有無と記録。
3. 施設プロトコル・倫理委員会・適用外使用規程の有無（`10`）。
4. 適用外を文献だけで一般化して回答しない。

### CHILD / PARENT の使い分け

- CHILD（366 files）: PMDA 作業 corpus。127 薬剤 inventory は `candidate_list_not_facility_confirmed`。
- PARENT（191 files）: gap v3。**557** ledger rows は追跡用であり、blind copy 許可ではない。
