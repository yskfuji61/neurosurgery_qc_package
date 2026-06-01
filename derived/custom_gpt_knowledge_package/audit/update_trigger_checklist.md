# Update Trigger Checklist

## 更新契機

1. PMDA 電子添文改訂
2. RMP / 安全性情報更新
3. 国内外 guideline 更新
4. 施設採用品変更
5. 夜間休日在庫変更
6. 薬剤部、輸血部、看護、病棟運用変更
7. 委員会承認状況変更
8. Preview fail 発生
9. 実運用で危険誤答を発見

## 更新時の最低確認

1. 関連 knowledge ファイルを特定した。
2. 一次資料を確認した。
3. 施設内確認先を記録した。
4. Preview 再試験を実施した。
5. 人間レビュー記録を残した。
6. Preview 実績を `tests/human_reviewed_preview_examples.md` に記録した。
7. approved Preview 実績がある場合だけ `tests/report_preview_promotion_candidates.py` を実行し、candidate 結果を確認した。
8. candidate が `yes` の row だけ `tests/apply_preview_promotion.py` の dry-run を行い、必要時だけ `--apply` を実行した。
9. reject または red-flag が出た場合は `manifest/knowledge_quarantine_register.csv` を更新した。
10. 更新後に `tests/validate_review_state_integrity.py`、`tests/validate_release_readiness.py`、必要時は `tests/validate_quarantine_integrity.py` を再実行した。
11. `tests/validate_reference_migration_ledger.py` を再実行し、reference file coverage と migration decision completeness を壊していないことを確認した。
12. `tests/validate_facility_confirmation_status.py` を再実行し、facility pending / blocked / confirmed state を誤更新していないことを確認した。
