# Review Change Note

## Migration slice B（2026-06-02）

`baseline/pre-slice-b-m1` 以降、reference corpus 25 件（adapted_port + operator_side_only_port）の governance パターンを TARGET operator-side 文書へ適応。REFERENCE の PMDA 0/127 や `custom_gpt_upload_safe: false` を TARGET の完了事実として写していない。`knowledge/` 13 本は未変更。

レビュー重点: runbook / README の sibling reference 節、quarantine カテゴリ、safe answer shape、instructions の禁止短絡、ledger 25 行の `m1_port_applied_pending_operator_review`。

## Prior closeout note

今回の変更は、Preview evidence -> candidate report -> dry-run -> apply -> closeout の順序規律に加えて、reference migration completeness、facility confirmation state、derived export candidate state の gate を operator-side 文書全体で揃えるための限定差分です。レビューでは、実 Preview 実績が未記録のまま promotion helper に進めないこと、active quarantine を残した row を `external_ready_candidate` に上げないこと、reference repo 全ファイルが migration decision ledger で 1 file 1 decision として管理されていること、facility evidence がない row を `confirmed` または `not_applicable` にしないこと、human review 未記録 row を `derived_export_candidate_ledger.csv` で `export_candidate=yes` にしないこと、closeout 記録面で candidate report と dry-run/apply と validation の証跡が追えることを見てください。

主な確認対象は次のとおりです。

1. `README.md` の Custom GPT 実行順が Preview 実績記録後に candidate report / dry-run / apply へ進む順になっているか。
2. `tests/preview_execution_runbook.md` と `derived/gpt_drug_data_policy_expansion_runbook.md` が同じ停止条件と 1 row apply 規律を持っているか。
3. `manifest/future_policy_integration_matrix.md` の Commit 12 / 13 が Preview evidence 未記録時の停止条件と quarantine 衝突条件を反映しているか。
4. `audit/human_review_log_template.md` と `audit/rag_export_audit_checklist.md` が candidate report、dry-run、apply、quarantine 再検証の証跡を残せる形になっているか。
5. `derived/README.md` と package `README.md` が、`reference_migration_decision_ledger.csv` / `validate_reference_migration_ledger.py` と `facility_confirmation_status_ledger.csv` / `validate_facility_confirmation_status.py` を operator-side gate として同じ意味で説明しているか。
6. `tests/pass_fail_criteria.md` と `tests/preview_execution_runbook.md` が、Preview approved を facility confirmed や reference migration completeness の代替として扱っていないか。
7. `manifest/derived_export_candidate_ledger.csv` と `manifest/integrated_origin_reclassification_summary.csv` が operator-side artifact として登録され、Knowledge upload target や external-ready 承認として扱われていないか。
8. full validation suite に `validate_reference_migration_ledger.py`、`validate_facility_confirmation_status.py`、`validate_derived_export_candidate_ledger.py` が含まれ、repo-local pass と external-ready が分離して報告されるか。

今回、real Preview evidence と facility evidence は未投入です。したがって `tests/apply_preview_promotion.py --apply`、`manifest/knowledge_chunk_review_crosswalk.csv` の external-ready 昇格、`manifest/facility_confirmation_status_ledger.csv` の `confirmed` / `not_applicable` 更新は行いません。

今回、human-review evidence も未投入です。したがって `manifest/derived_export_candidate_ledger.csv` の各 row は `export_candidate=no` のまま維持し、source traceability があることだけを理由に derived export や external-ready へ進めません。

今回、`instructions/custom_gpt_instructions.md` への追加変更はありません。

touch したファイルの diagnostics では error は出ていません。
