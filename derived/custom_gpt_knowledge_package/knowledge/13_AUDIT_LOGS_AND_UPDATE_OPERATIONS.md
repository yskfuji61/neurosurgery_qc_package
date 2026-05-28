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

# 13 AUDIT LOGS AND UPDATE OPERATIONS

## このファイルの役割

このファイルは、Knowledge package の更新契機、監査ログ、人間レビュー運用をまとめます。

## clinician-facing summary

このファイルは、運用台帳を置くためだけの場所ではありません。Knowledge package を安全に使い続けるには、一次資料更新、施設運用変更、Preview fail、AI 誤答事例を検知した時点で見直しが必要であり、その変更理由を追跡できる状態を保つために使います。

## なぜ更新と監査が必要か

この package は静的な完成物ではなく、情報更新と回答品質の変化に影響を受けます。監査ログは形式的な記録ではなく、どの変更が safety boundary や回答品質に影響したかを後から説明するための証跡です。

## 更新トリガー

1. PMDA 電子添文改訂
2. RMP / 安全性情報更新
3. 国内外 guideline 更新
4. 輸血療法関連指針更新
5. 施設採用品変更
6. 夜間休日在庫変更
7. 薬剤部・輸血部・看護手順変更
8. 委員会承認状況変更
9. Preview テスト不合格
10. AI 誤回答事例の新規発見

## 更新時の最低作業

1. 該当一次資料を確認する
2. 該当 knowledge ファイルを修正する
3. `tests/preview_test_cases.md` を再実行する
4. `audit/` 配下のチェックリストを更新する
5. 人間レビュー記録を残す

## 監査ログに残す項目

1. 更新日
2. 更新理由
3. 更新対象ファイル
4. 確認した一次資料
5. 施設内確認先
6. 人間レビュー担当
7. Preview 再試験結果

## 問題発見時の扱い

1. 断定的誤回答が出た場合は即修正対象とする
2. 一次資料未確認のまま候補化した場合は fail とする
3. 施設未確認情報を可用と書いた場合は fail とする

## package 運用の原則

1. 元ファイルは直接編集しない
2. 再輸出物はこの derived package 配下で完結させる
3. source path と mapping を残す

## 未確定事項・人間レビュー項目

1. 監査頻度と責任者は対象チームで定義が必要です。
2. 実運用開始前に preview 再試験と監査ログ確認が必要です。
