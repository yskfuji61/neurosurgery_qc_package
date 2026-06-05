# Custom GPT Knowledge Package

## このパッケージの目的

このパッケージは、[references/neurosurgery_qc_package](../..) に収録されている脳神経外科領域の薬物治療アルゴリズム関連資料を、ChatGPT Custom GPT の Knowledge へ安全にアップロードできる形へ再構成した derived upload package です。

このパッケージは、GitHub URL をそのまま読ませる代替手段ではありません。OpenAI Custom GPT の Knowledge 制約に合わせ、元資料の安全境界、陰性知識、監査思想、一次資料確認要求、施設内確認要求を弱めないことを優先して再構成しています。

この package は source corpus そのものではありません。`references/neurosurgery_qc_package/` 配下の source を直接編集せず、その source から再構成した operator-side export layer として扱います。

将来の薬剤データ、臨床データ参照、CDS 境界拡張は、先に integrated package 側の source-governance、validation、audit、人間レビュー gate を通し、その後に source traceability を保った derived export として反映します。

また、[manifest/future_policy_integration_matrix.md](manifest/future_policy_integration_matrix.md) は operator-side control sheet であり、Knowledge upload target ではありません。

## Sibling reference corpus との関係

Custom GPT（GPT-5.5 運用想定）の **Knowledge 正本は本 package の `knowledge/` 13 ファイルのみ** である。ワークスペース sibling に **二つの reference corpus** がある。いずれも Knowledge へ一括投入する設計ではない（合計 **557** reference files を upload 対象にしない）。

1. **CHILD（PMDA 作業 corpus）:** `references/neurosurgery_safe_rag_pmda_product_source_register_resolved/`（366 files）。127 薬剤 inventory の製品単位 PMDA 解決・safe-boundary プロファイル・pilot batch 証跡。
2. **PARENT（gap v3 残差）:** `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/`（191 files）。神経腫瘍・下垂体・造影/手技等の V3 領域補完。**PMDA 製品単位は未解決**（`UNRESOLVED_DO_NOT_GUESS`）。

reference 側の現状事実（本 package に写し込まない）: CHILD の 127 薬剤は candidate inventory（施設未確定）。CHILD の `09_MANIFESTS/package_summary.json` は reference 内の PMDA 進捗スナップショットであり、TARGET または本 derived package の確定事実・Knowledge 推奨値にはしない。reference の `custom_gpt_upload_safe: false` および `completion_status: NOT_COMPLETE_*` は維持する。CHILD 内で Custom GPT 直接候補とされるのは `09_MANIFESTS/custom_gpt_upload_manifest.csv` の 6 行のみで、いずれも human review pending である。PARENT の `pmda_product_level_verified: false` を true に書き換えない。

本 package への統合は `manifest/reference_migration_decision_ledger.csv` の migration_mode に従う。adapted_port は境界・運用言語の適応であり、医療内容の無批判コピーではない。CHILD 212 + PARENT 123 薬剤プロファイルは integrated drug-profile 層が整うまで hold する。PARENT の V3_RESIDUAL（58 drug_key）は CHILD 127 register と **直交**（盲検マージ禁止）。

**Ledger:** CHILD 366 行 + PARENT 191 行 = **557 行**（`tests/validate_reference_migration_ledger.py --corpus all`）。slice B（25 件 port 適応）と slice C（281 件 non-port 監査完走）に加え、Runbook Commit 11 で A-PMDA batch 由来の reference 追加 56 件を ledger-only 登録済み（`d11_reference_batch_recorded_pending_operator_review`）。初期 PARENT gap v3 登録 174 件は `gap_v3_m0_ledger_recorded_pending_operator_review`；collision/review-ready 等の追補 17 件は `gap_v3_collision_gate_recorded` / `gap_v3_review_ready_recorded`。ledger 完走は blind copy の許可ではない。

**Integrated Phase 2（7 領域）:** `04_Drug_Classes/*_境界と出典階層.md`（神経腫瘍・下垂体・造影・CSF/IIH・血管内治療・痙縮・CNS感染）と `90_Audit/Collisions/gap_v3_*` — 境界のみ。PARENT 正本は [reference_archive](../../reference_archive/)。旧 sibling は削除済み。

**Preview / promotion:** `human_reviewed_preview_examples.md` 未記録のまま `apply_preview_promotion.py` 禁止。collision は `unresolved_intentional_hold`（[audit/gap_v3_pharmacist_facility_review_log_20260604.md](audit/gap_v3_pharmacist_facility_review_log_20260604.md)）。

## 重要な位置づけ

このパッケージは、次のいずれでもありません。

1. 正式な診療ガイドライン
2. 正式な処方指示書
3. 施設内手順そのもの
4. 即時実装可能な電子カルテ CDS 仕様

Knowledge にアップロードした後も、最終判断には最新一次資料確認、施設内確認、人間レビューが必要です。

同時に、このパッケージは監査メモだけを返すためのものでもありません。安全境界を維持しつつ、医療者が論点を自然に整理できるよう、Instructions と主要 knowledge ファイルには clinician-facing な summary layer を追加しています。

## 日本語医療文書としての利用上の注意

このパッケージは、医療従事者向けの RAG / Custom GPT 用安全境界資料であり、診療ガイドライン、処方指示、施設内手順、電子カルテ CDS 仕様ではありません。

実患者への適用は、最新の電子添文、国内ガイドライン、施設採用品、薬剤部手順、診療科判断、施設承認を確認する必要があります。

特に以下を混同しないでください。

1. 国内承認
2. 保険上の扱い
3. ガイドライン記載
4. 使用経験
5. 施設採用
6. 施設手順
7. 個別患者への使用可否
8. RAG 上の重要性
9. LLM 回答の安全境界

日本語表現、文書構造、LLM への転用、緊急時参照性については、operator-side の [docs/japanese_medical_writing_style_guide.md](docs/japanese_medical_writing_style_guide.md)、[docs/clinical_document_structure_standard.md](docs/clinical_document_structure_standard.md)、[docs/custom_gpt_knowledge_safety_boundary.md](docs/custom_gpt_knowledge_safety_boundary.md) を参照します。これらは Knowledge upload target ではありません。

## 日本語医療文書品質の現状

このパッケージでは、日本語医療文書としての読みやすさ、誤読耐性、職種横断の情報到達性を改善するため、operator-side のスタイルガイド、構造標準、表現リスク台帳、略語レビュー台帳、Preview 品質テストを整備しています。

ただし、Knowledge 13 本の本文は、現時点ではまだ人間レビュー前の安全境界資料です。医療従事者向け完成文書、施設内正式手順、処方支援文書、看護手順、CDS 本番仕様としては扱いません。

Knowledge 13 本への日本語スタイル完全適用は、[audit/KNOWLEDGE_13_JAPANESE_STYLE_APPLICATION_RUNBOOK_20260605.md](audit/KNOWLEDGE_13_JAPANESE_STYLE_APPLICATION_RUNBOOK_20260605.md) と [audit/knowledge_13_japanese_rewrite_patch_proposals_20260605.md](audit/knowledge_13_japanese_rewrite_patch_proposals_20260605.md) に従い、人間レビュー後に段階的に扱います。

2026-06-05 時点で、人間レビュー基準に沿った日本語補足 patch を **一部適用済み**（`knowledge/01`–`09`, `13` 等）。round 5（2 件）では、`pmda_resolved_count` / `register` / `repo-local`、`candidate_list_not_facility_confirmed`、`derived export` / `source traceability` / `summary layer`、`CHILD` / `PARENT` / `ledger`、`caution` / `Evidence`、`guideline` / `trial` / `order`、`Sibling gap v3 reference`、`user-facing conclusion` / `quarantine` / `unresolved` などの監査語・RAG語を、医療従事者が読める日本語へ修正しました（`01`/`09` のみ）。

round 6（2 件）では、`オーダー化`、`order化`、`safety boundary`、`facility confirmation`、`別管理`、`施設確認事項`、`quarantine` / `unresolved`、`source class` / `prescribing hierarchy` などの曖昧語を、医療従事者が何を確認し、何を判断してはいけないかが分かる表現へ修正しました（`01`/`09` のみ）。

round 7（2 件）では、`guideline`、`manufacturer documents`、`summary`、`Integrated governance boundary export`、`Integrated policy boundary export` などの英語混在・抽象的な表現を、日本語医療文書として読みやすい形へ修正しました（`01`/`09` のみ）。

round 8（2 件）では、`統合Vault側`、`転記`、`派生成果物`、`索引`、`GL`、`Evidence見出し` などの軽微だが読みにくい表現を、日本語医療文書として読みやすい形へ修正しました（`01`/`09` のみ）。

修正は日本語表現の自然化と禁止事項の明確化に限定しています。用量、投与速度、投与可否、抗菌薬選択、VTE予防薬、抗凝固再開時期、施設採用品、看護運用、CDS発火条件は追加していません。詳細は [audit/JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md](audit/JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md)。Preview 実出力の承認は未完了であり、医療従事者向け完成文書ではありません。

## パッケージ構成

### Knowledge にアップロードするファイル

Knowledge にアップロードする対象は、[knowledge](knowledge) 配下の 13 ファイルだけです。

1. [knowledge/01_START_HERE_AND_POSITIONING.md](knowledge/01_START_HERE_AND_POSITIONING.md)
2. [knowledge/02_INDEX_AND_NAVIGATION.md](knowledge/02_INDEX_AND_NAVIGATION.md)
3. [knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md](knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md)
4. [knowledge/04_DISEASE_NOTES.md](knowledge/04_DISEASE_NOTES.md)
5. [knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md](knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md)
6. [knowledge/06_PATIENT_STATE_NOTES.md](knowledge/06_PATIENT_STATE_NOTES.md)
7. [knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md](knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md)
8. [knowledge/08_THRESHOLDS_AND_CONDITIONS.md](knowledge/08_THRESHOLDS_AND_CONDITIONS.md)
9. [knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md](knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md)
10. [knowledge/10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md](knowledge/10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md)
11. [knowledge/11_CDS_CANDIDATE_BOUNDARIES.md](knowledge/11_CDS_CANDIDATE_BOUNDARIES.md)
12. [knowledge/12_AI_ERROR_TESTS_AND_VALIDATION.md](knowledge/12_AI_ERROR_TESTS_AND_VALIDATION.md)
13. [knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md](knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md)

### 運用補助ファイル

1. [instructions/custom_gpt_instructions.md](instructions/custom_gpt_instructions.md)
2. [tests/preview_test_cases.md](tests/preview_test_cases.md)
3. [tests/preview_test_protocol.md](tests/preview_test_protocol.md)（Runbook Commit 12・8 領域 must-have / must-not-have）
4. [tests/cds_time_window_alert_tests.md](tests/cds_time_window_alert_tests.md)（Commit 12・CDS / time-window 専用）
5. [tests/pass_fail_criteria.md](tests/pass_fail_criteria.md)
6. [tests/expected_answer_samples.md](tests/expected_answer_samples.md)
7. [tests/human_reviewed_preview_examples.md](tests/human_reviewed_preview_examples.md)
8. [tests/preview_execution_runbook.md](tests/preview_execution_runbook.md)
9. [tests/response_style_regression_assets.md](tests/response_style_regression_assets.md)
10. [audit/rag_export_audit_checklist.md](audit/rag_export_audit_checklist.md)
11. [audit/update_trigger_checklist.md](audit/update_trigger_checklist.md)
12. [audit/human_review_log_template.md](audit/human_review_log_template.md)
13. [audit/review_change_note.md](audit/review_change_note.md)
14. [audit/pharmacist_red_flag_review_checklist.md](audit/pharmacist_red_flag_review_checklist.md)（Commit 13・薬剤師 red-flag）
15. [audit/unapproved_content_quarantine.md](audit/unapproved_content_quarantine.md)（Commit 13・quarantine 規程）
16. [audit/pharmacist_red_flag_chunk_review_log_014.md](audit/pharmacist_red_flag_chunk_review_log_014.md)（Commit 14・repo-local red-flag 照合）
17. [audit/runbook_commit_14_final_audit_report.md](audit/runbook_commit_14_final_audit_report.md)（Commit 14・最終監査）
18. [manifest/file_inventory.csv](manifest/file_inventory.csv)
19. [manifest/source_to_knowledge_mapping.csv](manifest/source_to_knowledge_mapping.csv)
20. [manifest/summary_layer_provenance.csv](manifest/summary_layer_provenance.csv)
21. [manifest/build_notes.md](manifest/build_notes.md)
22. [manifest/commit_message_body.md](manifest/commit_message_body.md)
23. [manifest/future_policy_integration_matrix.md](manifest/future_policy_integration_matrix.md)
24. [manifest/custom_gpt_upload_manifest.csv](manifest/custom_gpt_upload_manifest.csv)
25. [tests/validate_upload_manifest.py](tests/validate_upload_manifest.py)
26. [manifest/knowledge_chunk_review_crosswalk.csv](manifest/knowledge_chunk_review_crosswalk.csv)
27. [tests/validate_unsafe_patterns.py](tests/validate_unsafe_patterns.py)
28. [tests/validate_preview_protocol.py](tests/validate_preview_protocol.py)
29. [manifest/knowledge_quarantine_register.csv](manifest/knowledge_quarantine_register.csv)
30. [tests/validate_quarantine_integrity.py](tests/validate_quarantine_integrity.py)
31. [tests/validate_pharmacist_red_flag_commit13.py](tests/validate_pharmacist_red_flag_commit13.py)
32. [tests/validate_final_audit_commit14.py](tests/validate_final_audit_commit14.py)
33. [tests/report_preview_promotion_candidates.py](tests/report_preview_promotion_candidates.py)
34. [tests/apply_preview_promotion.py](tests/apply_preview_promotion.py)
35. [tests/validate_review_state_integrity.py](tests/validate_review_state_integrity.py)
36. [tests/validate_release_readiness.py](tests/validate_release_readiness.py)
37. [manifest/reference_migration_decision_ledger.csv](manifest/reference_migration_decision_ledger.csv)
38. [tests/validate_reference_migration_ledger.py](tests/validate_reference_migration_ledger.py)
39. [manifest/facility_confirmation_status_ledger.csv](manifest/facility_confirmation_status_ledger.csv)
40. [tests/validate_facility_confirmation_status.py](tests/validate_facility_confirmation_status.py)
41. [manifest/derived_export_candidate_ledger.csv](manifest/derived_export_candidate_ledger.csv)
42. [manifest/integrated_origin_reclassification_summary.csv](manifest/integrated_origin_reclassification_summary.csv)
43. [tests/validate_derived_export_candidate_ledger.py](tests/validate_derived_export_candidate_ledger.py)

上記の運用補助ファイルは、Knowledge にアップロードする対象ではなく、integrated-first / derived-second の運用、監査、manifest 整合、Preview review を支える operator-side files です。

## Knowledge 13 ファイルの説明

1. `01` は package 全体の位置づけと最優先の安全境界を固定します。
2. `02` は索引と横断参照の導線を固定します。
3. `03` は高リスク誤読、陰性知識、標準化禁止事項を集約します。
4. `04` は疾患ノートを統合します。
5. `05` は薬効分類と Layer 2 薬剤索引を統合します。
6. `06` は患者状態ノートを統合します。
7. `07` は処置・周術期ノートを統合します。
8. `08` は閾値・条件ノートを統合します。
9. `09` は一次資料と Evidence チェックリストを統合します。
10. `10` は施設運用・施設内確認チェックリストを統合します。
11. `11` は CDS 候補と即時実装仕様の境界を固定します。
12. `12` は AI 誤回答テストと Validation を統合します。
13. `13` は監査ログ、更新トリガー、更新運用を統合します。

## Custom GPT での使い方

1. [instructions/custom_gpt_instructions.md](instructions/custom_gpt_instructions.md) の内容を Custom GPT の Instructions 欄に貼り付けます。
2. `python tests/validate_upload_manifest.py` を実行し、Knowledge upload target が `knowledge/` 配下の 13 ファイルだけであることを確認します。
3. `python tests/validate_unsafe_patterns.py` を実行し、dangerous-term と numeric assertion の gate が upload target 上で通るか確認します。
4. `python tests/validate_quarantine_integrity.py` を実行し、quarantine register の row が `external_ready_candidate` と衝突していないか確認します。
5. `python tests/validate_reference_migration_ledger.py` を実行し、reference repo の全ファイルが `manifest/reference_migration_decision_ledger.csv` に 1 件ずつ migration decision として登録されていることを確認します。
6. `python tests/validate_facility_confirmation_status.py` を実行し、`manifest/facility_confirmation_status_ledger.csv` が `manifest/knowledge_chunk_review_crosswalk.csv` の全 chunk を cover し、facility pending を confirmed と誤記していないことを確認します。
7. `python tests/validate_derived_export_candidate_ledger.py` を実行し、`manifest/derived_export_candidate_ledger.csv` が `manifest/summary_layer_provenance.csv` の全 summary chunk を cover し、human review 未記録 row を export candidate に誤昇格していないことを確認します。
8. [knowledge](knowledge) 配下の 13 ファイルだけを Knowledge へアップロードします。
9. [tests/expected_answer_samples.md](tests/expected_answer_samples.md) と [tests/pass_fail_criteria.md](tests/pass_fail_criteria.md) を開き、[tests/preview_execution_runbook.md](tests/preview_execution_runbook.md) の順序で PREVIEW-001 から PREVIEW-004 を実行します。
10. [tests/preview_test_cases.md](tests/preview_test_cases.md) を使って Preview で誤回答テストを実行します。
11. [tests/human_reviewed_preview_examples.md](tests/human_reviewed_preview_examples.md) に raw output と approve / reject を記録します。実 Preview 実績がまだない場合は、ここで止まり、promotion workflow に進みません。
12. `python tests/report_preview_promotion_candidates.py --output /tmp/qc_preview_promotion_candidates.csv` を実行し、approved Preview 実績から `external_ready_candidate` に上げられる row があるかを確認します。approved 実績がない場合は `0 candidate` が正しい結果です。
13. candidate が `yes` の row だけに対して `python tests/apply_preview_promotion.py --record-id <PREVIEW-ID> --chunk-id <summary-XX> --reviewer-role <role>` を dry-run し、blocking reason が消えていることを確認します。
14. dry-run が通った row だけに対して `python tests/apply_preview_promotion.py --record-id <PREVIEW-ID> --chunk-id <summary-XX> --reviewer-role <role> --apply` を実行し、`review_state`、`review_evidence_link`、`release_readiness`、`resolution_status` を更新します。
15. `python tests/validate_review_state_integrity.py` を実行し、`human_reviewed_preview_examples.md` と `knowledge_chunk_review_crosswalk.csv` の review state が矛盾していないか確認します。
16. `python tests/validate_release_readiness.py` を実行し、`repo_local_only`、`pending_preview_review`、`quarantined_red_flag`、`external_ready_candidate` が混同されていないか確認します。
17. [tests/response_style_regression_assets.md](tests/response_style_regression_assets.md) で anti-pattern へ戻っていないか確認します。
18. [manifest/summary_layer_provenance.csv](manifest/summary_layer_provenance.csv) で summary layer の根拠を確認します。
19. [manifest/knowledge_chunk_review_crosswalk.csv](manifest/knowledge_chunk_review_crosswalk.csv) で section ごとの review state、release readiness、pending gate を確認します。
20. [manifest/knowledge_quarantine_register.csv](manifest/knowledge_quarantine_register.csv) で red-flag finding の disposition を確認します。
21. [audit](audit) 配下のチェックリストで export 前監査と更新監査を行います。

## Preview review と provenance の考え方

`expected_answer_samples.md` は representative answer shape の基準であり、実際の Preview 実出力そのものを保存する場所ではありません。Preview 実出力は `human_reviewed_preview_examples.md` に分けて記録し、raw output、lightly normalized output、approved / rejected 判断、review rationale を残します。

また、`source_to_knowledge_mapping.csv` は source file と knowledge file の対応を残す file-level inventory です。clinician-facing summary layer のような自然化 section の由来追跡は、`summary_layer_provenance.csv` で別管理します。これにより、既存の mapping を壊さずに summary layer の provenance を辿れます。

`knowledge_chunk_review_crosswalk.csv` は、`source_to_knowledge_mapping.csv` と `summary_layer_provenance.csv` を置き換えるものではありません。section 単位で `review_state`、`reviewer_role`、`review_evidence_link`、`blockers` に加えて `release_readiness` と `resolution_status` を横断管理し、review 実績がない section や quarantine 対象を external-ready と混同しないための operator-side 補助 ledger です。

`knowledge_quarantine_register.csv` は dangerous-term、numeric assertion、red-flag review の findings を operator-side で隔離追跡するための register です。`knowledge_chunk_review_crosswalk.csv` の代替ではなく、quarantined row が `external_ready_candidate` へ誤昇格しないようにする補助 manifest として扱います。

`reference_migration_decision_ledger.csv` は、`neurosurgery_safe_rag_pmda_product_source_register_resolved` の全ファイルを 1 件ずつ migration decision として扱う operator-side ledger です。これは全ファイルを無批判に Knowledge へコピーするための表ではなく、direct / adapted / operator-side / unresolved / quarantine / reference-only の判断を残すための表です。

`facility_confirmation_status_ledger.csv` は、chunk ごとの施設確認状態を管理する operator-side ledger です。実 facility evidence がない row は `pending_facility_review` のまま維持し、validation pass を `confirmed` や external-ready の代替として扱ってはいけません。

`derived_export_candidate_ledger.csv` は、summary layer provenance の各 chunk について、source traceability と human-review status が揃っているかを別管理する operator-side ledger です。`export_candidate=yes` は Knowledge upload や external-ready を意味せず、Preview evidence と facility confirmation が未了の row は `repo_local_only` のまま扱います。

`integrated_origin_reclassification_summary.csv` は、reference migration decision の現在の分類を operator-side / unresolved / adapted などの観点で集約する operator-side summary です。これは reclassification の監査補助であり、reference file の blind copy や derived export の承認ではありません。

`manifest/` 配下の source path は、package の物理配置ではなく repo 上の source traceability を残すための metadata です。したがって、この package が `references/neurosurgery_qc_package/derived/` 配下に置かれていても、manifest の source path は source corpus を指す基準として維持します。

現在の provenance pilot では、04、05、06、07、10、11 について clinician-facing summary だけでなく `実際の考え方` section も secondary naturalized section として追跡対象にしています。

## 今回の作成物一覧

このパッケージは、Knowledge upload 用 13 ファイルに加えて、manifest、instructions、tests、audit を含みます。元ファイルは削除も上書きもしていません。

## Operator-side 隔離（reference OPERATOR_SIDE_ONLY 適応）

Custom GPT Knowledge へ昇格してはいけない典型（確認手順・参照先・未解決表示・安全境界のみ昇格可）:

1. 製品別用量、腎機能別用量、透析条件別運用、投与速度、希釈、投与経路
2. TDM 目標値、採血時刻、混注・側管・同一ルート可否
3. 院内採用品、在庫、看護部運用、EHR/CDS 発火条件、Override、オーダーセット

これらは sibling reference の `04_OPERATOR_SIDE_ONLY/` に置き、本 package の `manifest/custom_gpt_upload_manifest.csv` では `upload_to_custom_gpt=no` として維持する。

## 使用禁止（reference corpus 由来の境界の反映）

次の用途に本 package または Knowledge だけを使ってはいけない。

1. AI による処方・投与・中止・増量・減量の決定
2. 院内手順・EHR/CDS 本番仕様としての即時流用
3. 用量表・TDM 表・混注表としての使用
4. sibling reference corpus 上で PMDA 未確認の薬剤を確認済みと扱うこと
5. 海外ガイドライン記載を国内承認・保険情報の代替とすること

## 未確認事項

1. 最新 PMDA 電子添文の個別更新内容は本パッケージ内では確定していません（sibling reference corpus でも PMDA 製品単位 0/127）。
2. 国内保険適用と査定運用の施設別差異は本パッケージ内では確定していません。
3. 施設採用品、夜間休日在庫、薬剤部手順、輸血部運用、看護観察体制、委員会承認状況は施設別確認が必要です。
4. 電子カルテ CDS 即時実装仕様、order set、alert 条件、監査ログ仕様は本パッケージ内では確定していません。

## 人間レビューが必要な事項

1. 高リスク薬剤に関する陰性知識が、対象施設の実運用と矛盾しないか。
2. 疾患別・薬効分類別に引用した caution が一次資料と整合するか。
3. Evidence チェックリストと施設内確認チェックリストの優先順が対象施設に適合するか。
4. Preview テストで不合格回答が出た場合の修正文面が十分か。

## 次に Custom GPT 画面で行うべき操作

1. 新しい Custom GPT を作成します。
2. Instructions 欄に [instructions/custom_gpt_instructions.md](instructions/custom_gpt_instructions.md) の全文を貼り付けます。
3. Knowledge には [knowledge](knowledge) 配下の 13 ファイルだけをアップロードします。
4. Preview で [tests/preview_test_cases.md](tests/preview_test_cases.md) の質問を順に実行します。
5. [tests/pass_fail_criteria.md](tests/pass_fail_criteria.md) で合否判定を行います。
6. export 前に [audit/rag_export_audit_checklist.md](audit/rag_export_audit_checklist.md) を確認します。
