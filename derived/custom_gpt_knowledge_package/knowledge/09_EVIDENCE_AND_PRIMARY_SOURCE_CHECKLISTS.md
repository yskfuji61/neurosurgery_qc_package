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

# 09 EVIDENCE AND PRIMARY SOURCE CHECKLISTS

## このファイルの役割

このファイルは、Knowledge 内の候補や caution を最終確認するための一次資料・Evidence チェックリストをまとめます。

## clinician-facing summary

このファイルは、候補をそのまま正当化するための一覧ではなく、何を確認したいときにどの資料を見るべきかを整理するためのガイドです。PMDA、RMP、国内外 guideline、RCT は役割が異なるため、確認目的を分けて参照する前提で使います。

## このファイルを開く場面

薬剤や対応の候補が見えてきたあとに、「国内薬事はどうか」「安全性情報は更新されていないか」「この論点は guideline や trial でどこまで支えられるか」を確認したい場面で開きます。Evidence は重要ですが、施設採用品や order 化の代わりにはなりません。

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
2. routine 標準化には直結させない

## ULTRA チェック

1. くも膜下出血や周術期文脈での参照事項を確認
2. 施設実装可能性とは分けて扱う

## Evidence の使い方

1. Evidence は候補の裏付けであり、施設採用品や order 化の裏付けではありません。
2. 一次資料と施設内確認を飛ばして Evidence だけで結論にしません。

## 未確定事項・人間レビュー項目

1. 最新版の改訂日は都度確認が必要です。
2. 論文や guideline の解釈差は人間レビューで吸収してください。
