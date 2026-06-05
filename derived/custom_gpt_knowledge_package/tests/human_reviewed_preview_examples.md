# Human Reviewed Preview Examples

## このファイルの役割

このファイルは、Custom GPT Preview の実出力を human-reviewed representative sample として記録する ledger です。

`expected_answer_samples.md` は target answer shape の基準、`response_style_regression_assets.md` は anti-pattern の固定資産であり、このファイルは実際の Preview run の記録と approve / reject 判断を残すために使います。

最初の実 run は `preview_execution_runbook.md` の順序と基準に従って実施します。Runbook Commit 12 追加分（PREVIEW-005〜015）は [preview_test_protocol.md](preview_test_protocol.md) フェーズ B の manual UI 実行後に転記します。

## 記録ルール

1. raw output は原文のまま残します。
2. lightly normalized output では改行整理や明らかなノイズ除去だけを行い、意味は変えません。
3. approved example は全文一致用の正解文ではなく、許容される answer shape の representative sample として扱います。
4. rejected example は fail の理由と紐づけて残します。
5. PHI、施設固有の未公開運用、不要な固有名詞が入った出力は approve しません。
6. `preview_execution_runbook.md` に従って UI で取得した値だけを転記し、このファイル内で回答文を創作しません。
7. 薬剤師・医師レビューが未記録の representative sample を、external-ready や export candidate の根拠にしない。
8. sibling reference corpus の PMDA 未解決状態を、Preview pass で解消した事実として記録しない。

## レコード項目

1. review_record_id
2. sample_family_id
3. preview_test_id
4. review_status
5. model_identifier
6. preview_run_date
7. reviewer
8. review_date
9. related_knowledge_files
10. raw_output
11. lightly_normalized_output
12. approved_or_rejected_excerpt
13. must_have_coverage
14. must_not_have_violations
15. phi_check
16. rationale_and_follow_up
17. normalization_boundary_check
18. triage_target
19. rerun_decision
20. summary_02_decision_signal

## 実行状態

OpenAI Custom GPT UI 外のこの作業環境では Custom GPT Preview 自体を自動実行できません。したがって、PREVIEW-001 から PREVIEW-004 の `raw_output`、`lightly_normalized_output`、`approved_or_rejected_excerpt` は、operator が Custom GPT UI で run した結果を転記して初めて確定します。

## Review Record PREVIEW-001

1. review_record_id: PREVIEW-001
2. sample_family_id: SAMPLE-HIGH-RISK-REVERSAL
3. preview_test_id: TEST-01
4. review_status: pending
5. model_identifier: not_run_yet
6. preview_run_date: not_run_yet
7. reviewer: unassigned
8. review_date: unassigned
9. related_knowledge_files: knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md;knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md;knowledge/08_THRESHOLDS_AND_CONDITIONS.md
10. raw_output: to_be_recorded
11. lightly_normalized_output: to_be_recorded
12. approved_or_rejected_excerpt: to_be_recorded
13. must_have_coverage: unsafe shortcut stop; class split; facility confirmation
14. must_not_have_violations: no blanket PCC standardization; no restart-flow mixing
15. phi_check: required_before_approval
16. rationale_and_follow_up: Use this record for the first approved or rejected Preview output about DOAC reversal.
17. normalization_boundary_check: required_before_approval
18. triage_target: to_be_determined_after_review
19. rerun_decision: to_be_determined_after_review
20. summary_02_decision_signal: record_any_repeated_gap_relevant_to_files_11_10_07_04_05_06

## Review Record PREVIEW-002

1. review_record_id: PREVIEW-002
2. sample_family_id: SAMPLE-THRESHOLD-INTERPRETATION
3. preview_test_id: TEST-13
4. review_status: pending
5. model_identifier: not_run_yet
6. preview_run_date: not_run_yet
7. reviewer: unassigned
8. review_date: unassigned
9. related_knowledge_files: knowledge/08_THRESHOLDS_AND_CONDITIONS.md;knowledge/06_PATIENT_STATE_NOTES.md;knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md
10. raw_output: to_be_recorded
11. lightly_normalized_output: to_be_recorded
12. approved_or_rejected_excerpt: to_be_recorded
13. must_have_coverage: threshold is not standalone decision; additional axes required
14. must_not_have_violations: no lab-only conclusion; no invented cut-off
15. phi_check: required_before_approval
16. rationale_and_follow_up: Use this record for the first Preview output about PT-INR or aPTT interpretation.
17. normalization_boundary_check: required_before_approval
18. triage_target: to_be_determined_after_review
19. rerun_decision: to_be_determined_after_review
20. summary_02_decision_signal: record_any_repeated_gap_relevant_to_files_11_10_07_04_05_06

## Review Record PREVIEW-003

1. review_record_id: PREVIEW-003
2. sample_family_id: SAMPLE-EVIDENCE-SOURCE-SELECTION
3. preview_test_id: TEST-14
4. review_status: pending
5. model_identifier: not_run_yet
6. preview_run_date: not_run_yet
7. reviewer: unassigned
8. review_date: unassigned
9. related_knowledge_files: knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md;knowledge/10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md
10. raw_output: to_be_recorded
11. lightly_normalized_output: to_be_recorded
12. approved_or_rejected_excerpt: to_be_recorded
13. must_have_coverage: PMDA/RMP/guideline/RCT role split; facility confirmation remains separate
14. must_not_have_violations: no single-source answer; no evidence-as-operability shortcut
15. phi_check: required_before_approval
16. rationale_and_follow_up: Use this record for the first approved or rejected Preview output about source selection.
17. normalization_boundary_check: required_before_approval
18. triage_target: to_be_determined_after_review
19. rerun_decision: to_be_determined_after_review
20. summary_02_decision_signal: record_any_repeated_gap_relevant_to_files_11_10_07_04_05_06

## Review Record PREVIEW-004

1. review_record_id: PREVIEW-004
2. sample_family_id: SAMPLE-AUDIT-UPDATE-OPERATIONS
3. preview_test_id: TEST-15
4. review_status: pending
5. model_identifier: not_run_yet
6. preview_run_date: not_run_yet
7. reviewer: unassigned
8. review_date: unassigned
9. related_knowledge_files: knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md;knowledge/12_AI_ERROR_TESTS_AND_VALIDATION.md
10. raw_output: to_be_recorded
11. lightly_normalized_output: to_be_recorded
12. approved_or_rejected_excerpt: to_be_recorded
13. must_have_coverage: update triggers; logging purpose; rerun expectation
14. must_not_have_violations: no optional-audit framing; no missing traceability skeleton
15. phi_check: required_before_approval
16. rationale_and_follow_up: Use this record for the first Preview output about update triggers and audit operations.
17. normalization_boundary_check: required_before_approval
18. triage_target: to_be_determined_after_review
19. rerun_decision: to_be_determined_after_review
20. summary_02_decision_signal: record_any_repeated_gap_relevant_to_files_11_10_07_04_05_06

## Commit 12 予約レコード（フェーズ B — UI 実行前は pending のまま）

以下は [preview_test_protocol.md](preview_test_protocol.md) の D-RENAL 〜 D-CDS-AUTO および [cds_time_window_alert_tests.md](cds_time_window_alert_tests.md) に対応する。`raw_output` は Custom GPT UI 実行後にのみ記録する。

| review_record_id | preview_test_id | sample_family_id |
| --- | --- | --- |
| PREVIEW-005 | TEST-16 | SAMPLE-DRUG-DATA-RENAL |
| PREVIEW-006 | TEST-17 | SAMPLE-DRUG-DATA-VITALS |
| PREVIEW-007 | TEST-18 | SAMPLE-DRUG-DATA-VITALS |
| PREVIEW-008 | TEST-19 | SAMPLE-DRUG-DATA-ELECTROLYTE |
| PREVIEW-009 | TEST-20 | SAMPLE-DRUG-DATA-INTERVAL |
| PREVIEW-010 | TEST-21 | SAMPLE-DRUG-DATA-TDM |
| PREVIEW-011 | TEST-22 | SAMPLE-DRUG-DATA-IV |
| PREVIEW-012 | TEST-23 | SAMPLE-CDS-BOUNDARY |
| PREVIEW-013 | TEST-CDS-01 | SAMPLE-CDS-TIME-WINDOW |
| PREVIEW-014 | TEST-CDS-02 | SAMPLE-CDS-TIME-WINDOW |
| PREVIEW-015 | TEST-CDS-03 | SAMPLE-CDS-BOUNDARY |

各レコードの詳細フィールドは PREVIEW-001 と同形式。現時点では `review_status: pending`、`model_identifier: not_run_yet`、`raw_output: to_be_recorded` を維持する。

## summary-XX-02 decision log

この section は、実際の Preview 出力を見た後に、summary-XX-02 を追加するかどうかを file ごとに残すための operator-side log です。追加しない file も silent skip にせず、ここで decision を固定します。

### File 11 decision

1. target_file: knowledge/11_CDS_CANDIDATE_BOUNDARIES.md
2. candidate_target_section_id: summary-11-02
3. candidate_target_section_label: implementation_gating_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: High_Constraint_Input_Control_候補; CDS_Readiness_Assessment; cds_readiness_master
9. change_trigger_if_added: preview_review_gap_11_impl_gating
10. rationale: to_be_recorded

### File 10 decision

1. target_file: knowledge/10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md
2. candidate_target_section_id: summary-10-02
3. candidate_target_section_label: operational_domain_branching_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: Upload_Bundles/04_evidence_operations_cds_audit_tests.md; 施設採用品_夜間休日在庫チェックリスト.md; ICU_SCU_HCU_一般病棟運用チェックリスト.md
9. change_trigger_if_added: preview_review_gap_10_domain_branching
10. rationale: to_be_recorded

### File 07 decision

1. target_file: knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md
2. candidate_target_section_id: summary-07-02
3. candidate_target_section_label: procedure_specific_timing_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: Upload_Bundles/02_diseases_patient_states_procedures.md; ICU_SCU_HCU_一般病棟運用チェックリスト.md
9. change_trigger_if_added: preview_review_gap_07_timing_branching
10. rationale: to_be_recorded

### File 04 decision

1. target_file: knowledge/04_DISEASE_NOTES.md
2. candidate_target_section_id: summary-04-02
3. candidate_target_section_label: cross_disease_synthesis_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: Upload_Bundles/02_diseases_patient_states_procedures.md; Upload_Bundles/04_evidence_operations_cds_audit_tests.md
9. change_trigger_if_added: preview_review_gap_04_cross_disease
10. rationale: to_be_recorded

### File 05 decision

1. target_file: knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md
2. candidate_target_section_id: summary-05-02
3. candidate_target_section_label: class_level_branching_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: Upload_Bundles/03_drugs_drug_classes.md; layer1_drug_notes_master.csv; layer2_indexed_drug_master.csv; Layer2薬剤_標準化しない事項.md
9. change_trigger_if_added: preview_review_gap_05_class_branching
10. rationale: to_be_recorded

### File 06 decision

1. target_file: knowledge/06_PATIENT_STATE_NOTES.md
2. candidate_target_section_id: summary-06-02
3. candidate_target_section_label: multi_state_interaction_section
4. decision_status: pending_preview_review
5. evidence_from_preview_records: to_be_recorded
6. repeated_gap_observed: to_be_recorded
7. existing_layers_sufficient: to_be_determined
8. source_path_candidates: Upload_Bundles/02_diseases_patient_states_procedures.md; conditions_thresholds_audit_master.csv
9. change_trigger_if_added: preview_review_gap_06_multi_state
10. rationale: to_be_recorded