# Commit Message

## Commit Title

Align migration, facility, and preview governance across operator-side docs

## Commit Body

derived Custom GPT package の operator-side 文書群を横断して、Preview evidence -> candidate report -> dry-run -> apply -> closeout の順序規律を揃えた。

README、runbook、matrix では、実 Preview 実績が `tests/human_reviewed_preview_examples.md` に記録される前に `report_preview_promotion_candidates.py` や `apply_preview_promotion.py` へ進まないことに加え、`reference_migration_decision_ledger.csv` と `facility_confirmation_status_ledger.csv` を operator-side gate として扱うことを明記した。

`derived_export_candidate_ledger.csv` と `integrated_origin_reclassification_summary.csv` を追加し、source traceability と human-review status が揃っていない summary chunk を export candidate にしないこと、adapted_port や Preview pending state を external-ready と混同しないことを operator-side で見える化した。

audit/human_review_log_template.md、audit/rag_export_audit_checklist.md、audit/update_trigger_checklist.md、tests/preview_execution_runbook.md、tests/pass_fail_criteria.md には candidate report、dry-run、`--apply`、quarantine 再検証、reference migration completeness、facility pending state の確認点を追加し、review_change_note.md と build_notes.md も現行の運用順へ合わせて更新した。

今回、instructions/custom_gpt_instructions.md への追加変更は行っていない。

repo-local validation として `report_preview_promotion_candidates.py`、`validate_quarantine_integrity.py`、`validate_release_readiness.py`、`validate_review_state_integrity.py`、`validate_unsafe_patterns.py`、`validate_upload_manifest.py`、`validate_reference_migration_ledger.py`、`validate_facility_confirmation_status.py`、`validate_derived_export_candidate_ledger.py` は PASS を維持している。実 Preview evidence はまだ未投入のため、approved preview records と external_ready_candidate は 0 件のままであり、facility confirmation 18 rows も pending のまま維持している。
