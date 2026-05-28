# Custom GPT Knowledge Package

## このパッケージの目的

このパッケージは、[references/neurosurgery_qc_package](../..) に収録されている脳神経外科領域の薬物治療アルゴリズム関連資料を、ChatGPT Custom GPT の Knowledge へ安全にアップロードできる形へ再構成した derived upload package です。

このパッケージは、GitHub URL をそのまま読ませる代替手段ではありません。OpenAI Custom GPT の Knowledge 制約に合わせ、元資料の安全境界、陰性知識、監査思想、一次資料確認要求、施設内確認要求を弱めないことを優先して再構成しています。

この package は source corpus そのものではありません。`references/neurosurgery_qc_package/` 配下の source を直接編集せず、その source から再構成した operator-side export layer として扱います。

## 重要な位置づけ

このパッケージは、次のいずれでもありません。

1. 正式な診療ガイドライン
2. 正式な処方指示書
3. 施設内手順そのもの
4. 即時実装可能な電子カルテ CDS 仕様

Knowledge にアップロードした後も、最終判断には最新一次資料確認、施設内確認、人間レビューが必要です。

同時に、このパッケージは監査メモだけを返すためのものでもありません。安全境界を維持しつつ、医療者が論点を自然に整理できるよう、Instructions と主要 knowledge ファイルには clinician-facing な summary layer を追加しています。

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
3. [tests/pass_fail_criteria.md](tests/pass_fail_criteria.md)
4. [tests/expected_answer_samples.md](tests/expected_answer_samples.md)
5. [tests/human_reviewed_preview_examples.md](tests/human_reviewed_preview_examples.md)
6. [tests/preview_execution_runbook.md](tests/preview_execution_runbook.md)
7. [tests/response_style_regression_assets.md](tests/response_style_regression_assets.md)
8. [audit/rag_export_audit_checklist.md](audit/rag_export_audit_checklist.md)
9. [audit/update_trigger_checklist.md](audit/update_trigger_checklist.md)
10. [audit/human_review_log_template.md](audit/human_review_log_template.md)
11. [audit/review_change_note.md](audit/review_change_note.md)
12. [manifest/file_inventory.csv](manifest/file_inventory.csv)
13. [manifest/source_to_knowledge_mapping.csv](manifest/source_to_knowledge_mapping.csv)
14. [manifest/summary_layer_provenance.csv](manifest/summary_layer_provenance.csv)
15. [manifest/build_notes.md](manifest/build_notes.md)
16. [manifest/commit_message_body.md](manifest/commit_message_body.md)

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
2. [knowledge](knowledge) 配下の 13 ファイルだけを Knowledge へアップロードします。
3. [tests/preview_test_cases.md](tests/preview_test_cases.md) を使って Preview で誤回答テストを実行します。
4. [tests/pass_fail_criteria.md](tests/pass_fail_criteria.md) を基準に合否判定を行います。
5. [tests/expected_answer_samples.md](tests/expected_answer_samples.md) で target answer shape を確認します。
6. [tests/human_reviewed_preview_examples.md](tests/human_reviewed_preview_examples.md) に raw output と approve / reject を記録します。
7. [tests/preview_execution_runbook.md](tests/preview_execution_runbook.md) の順序で PREVIEW-001 から PREVIEW-004 を実行します。
8. [tests/response_style_regression_assets.md](tests/response_style_regression_assets.md) で anti-pattern へ戻っていないか確認します。
9. [manifest/summary_layer_provenance.csv](manifest/summary_layer_provenance.csv) で summary layer の根拠を確認します。
10. [audit](audit) 配下のチェックリストで export 前監査と更新監査を行います。

## Preview review と provenance の考え方

`expected_answer_samples.md` は representative answer shape の基準であり、実際の Preview 実出力そのものを保存する場所ではありません。Preview 実出力は `human_reviewed_preview_examples.md` に分けて記録し、raw output、lightly normalized output、approved / rejected 判断、review rationale を残します。

また、`source_to_knowledge_mapping.csv` は source file と knowledge file の対応を残す file-level inventory です。clinician-facing summary layer のような自然化 section の由来追跡は、`summary_layer_provenance.csv` で別管理します。これにより、既存の mapping を壊さずに summary layer の provenance を辿れます。

`manifest/` 配下の source path は、package の物理配置ではなく repo 上の source traceability を残すための metadata です。したがって、この package が `references/neurosurgery_qc_package/derived/` 配下に置かれていても、manifest の source path は source corpus を指す基準として維持します。

現在の provenance pilot では、04、05、06、07、10、11 について clinician-facing summary だけでなく `実際の考え方` section も secondary naturalized section として追跡対象にしています。

## 今回の作成物一覧

このパッケージは、Knowledge upload 用 13 ファイルに加えて、manifest、instructions、tests、audit を含みます。元ファイルは削除も上書きもしていません。

## 未確認事項

1. 最新 PMDA 電子添文の個別更新内容は本パッケージ内では確定していません。
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
