# Review Change Note

## Knowledge 13 patch round 3（2026-06-05）

- Applied 5 additional human-reviewed Japanese patches to `knowledge/01`, `03`, `04`, `09`, `13` only (no instructions edit).
- Patches: JP-STYLE-01-003 (upload 可否 / Reference corpora / reference-only hold), JP-STYLE-03-003 (rFVIIa routine), JP-STYLE-04-001 (VTE 中核), JP-STYLE-09-001 (TICH-2 routine), JP-STYLE-13-001 (release readiness boundary).
- Deferred without Knowledge body edit: `05` L120 routine, `04` L225 routine, abbreviation bulk apply, Emergency block expansion, standard page structure migration.
- 8/8 targeted validators PASS (post round 3); `external_ready_candidates=0`; upload target **13 files** unchanged.
- **Not** release ready; Preview evidence still pending. See [JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md](JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md).

## Knowledge 13 patch round 2（2026-06-05）

- Applied 4 additional human-reviewed Japanese patches to `knowledge/01`, `03`, `05`, `08` only (no instructions edit).
- Patches: JP-STYLE-01-002 (operator-side / upload safe), JP-STYLE-03-002 (shortcut), JP-STYLE-05-002 (routine L92/L99), JP-STYLE-08-002 (ICU-context confirmation axes).
- Deferred without Knowledge body edit: `05` L120 routine, `03` L76 routine, `04` 中核, `09` routine, `13` release readiness.
- Ledgers and patch proposals updated; `05` L120 / `03` L76 registered as `DEFERRED_HUMAN_REVIEW_REQUIRED`.
- 8/8 targeted validators PASS (post round 2); `external_ready_candidates=0`; upload target **13 files** unchanged.
- **Not** release ready; Preview evidence still pending. See [JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md](JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md).

## Knowledge 13 patch application pass（2026-06-05）

- Applied 5 human-reviewed Japanese patches to `knowledge/01`, `03`, `05`, `08` only (no instructions edit).
- Patches: governance boundary wording, negative knowledge Japanese gloss, emergency quick-check block, antibiogram/de-escalation gloss, threshold「必須」clarification.
- Ledgers and [knowledge_13_japanese_rewrite_patch_proposals_20260605.md](knowledge_13_japanese_rewrite_patch_proposals_20260605.md) updated to `REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW`.
- `validate_unsafe_patterns.py`: negation-boundary markers for emergency block (no clinical content added).
- 8/8 targeted validators PASS; `external_ready_candidates=0`; upload target **13 files** unchanged.
- **Not** release ready; Preview evidence still pending. See [JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md](JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md).

## Knowledge 13 Japanese style application pass（2026-06-05）

- Added Knowledge 13 style prep layer: prework, runbook, plain-language / abbreviation / expression ledgers, patch proposals (proposed-only), role-based readability rules, Japanese Preview quality tests, 4 new validators.
- **Not edited:** `knowledge/*.md` bodies (13 files), `instructions/custom_gpt_instructions.md`; patch proposals are not applied to Knowledge without human review.
- `manifest/custom_gpt_upload_manifest.csv`: all new files `upload_to_custom_gpt=no`; **Knowledge upload remains 13 files only**.
- Decision: **READY_FOR_HUMAN_REVIEW** — not finished clinical document, not facility SOP, not prescription support, not CDS production spec.
- Japanese answer shape: **specified_but_not_empirically_validated**; Knowledge 13 full style application **incomplete**.
- `external_ready_candidates`: **0** maintained.
- See [JAPANESE_KNOWLEDGE_13_STYLE_APPLICATION_COMPLETION_REPORT_20260605.md](JAPANESE_KNOWLEDGE_13_STYLE_APPLICATION_COMPLETION_REPORT_20260605.md).

## Japanese medical document operator-side pass（2026-06-05）

- Added operator-side Japanese medical document layer: `docs/*` (5), `templates/*` (3), `audit/japanese_*` (4), prework + completion reports.
- `manifest/custom_gpt_upload_manifest.csv`: all new files `upload_to_custom_gpt=no`; **Knowledge upload remains 13 files only**.
- `manifest/reference_migration_decision_ledger.csv`: Unicode path metadata fix only.
- `derived/composer25_custom_gpt_update_blueprint_20260605.md`: cross-references to style docs and URL-only / Japanese output policy.
- **Not edited:** `knowledge/*.md`, `instructions/custom_gpt_instructions.md` (no automated clinical rewrite).
- Quality audit decision: **READY_FOR_HUMAN_REVIEW** — not release ready, not clinical approval.
- Japanese answer shape: **specified_but_not_empirically_validated** (Preview approved examples still absent).
- `external_ready_candidates`: **0** maintained.
- See [JAPANESE_MEDICAL_DOCUMENT_COMPLETION_REPORT_20260605.md](JAPANESE_MEDICAL_DOCUMENT_COMPLETION_REPORT_20260605.md).

## Current ledger state（2026-06-04・operator-side）

- **Reference migration ledger:** **598** rows / **598** reference files（Stage 6/6C 含む）。
- **Upload target:** `knowledge/*.md` **13 files only** — unchanged.
- **`external_ready_candidate`:** 0 維持。

（以下 2026-06-05 節は当時スナップショット。件数は上記が現在。）

## Stage 5A evidence collection readiness 再実行（2026-06-04）

- Stage 6/6C 完了後の **readiness のみ** 再確認（promotion / `--apply` / knowledge 編集なし）。
- 14/14 validators PASS; `migration_ledger_rows=598`; `external_ready_candidates=0`.
- `preview_promotion_candidates_report_20260604.csv` 再生成 — **0** candidates.
- Preview: PREVIEW-001…015 すべて `pending` / `to_be_recorded`（real UI output なし）。
- Collision RAG: 21/21 TEMPLATE、`pass_fail` 未記入。
- Japanese answer shape: **specified_but_not_empirically_validated**（approved Preview 実例なし）。
- URL-only: register は operator-side routing; **runtime PMDA fetch 未実装**; 臨床出力の正確性保証にはならない。
- See [STAGE5A_READINESS_REPORT_20260604.md](STAGE5A_READINESS_REPORT_20260604.md).

## Current ledger state（2026-06-05・operator-side）

- **Reference migration ledger:** CHILD 366 + PARENT 191 + Stage 6/6C artifacts = **598** rows / **598** reference files on disk.
- **Validator:** `validate_reference_migration_ledger.py --corpus all` → `migration_ledger_rows=598`, `reference_file_count=598`（clinical approval ではない）。
- **Upload target:** `knowledge/*.md` **13 files only** — unchanged.
- **`external_ready_candidate`:** 0 維持。

以下の節に **historical** な 540/174 表記が残る場合は当時のスナップショットであり、上記が現在の件数である。

## gap v3 review-ready slice（2026-06-05）

- Added readiness matrix, parking gate audit, regression results TEMPLATE, promotion blockers, integrated REVIEW_READY log, 7 collision checklists (empty).
- `validate_gap_v3_review_ready.py` PASS; gates unchanged (`DO_NOT_EXPORT`, `safe_to_promote=false`).
- **Not** integration complete; **not** pharmacist sign-off.

## metadata count reconciliation（2026-06-05）

- Operator README/runbook/audit: current-state counts aligned to CHILD 366 + PARENT 191 = **557** ledger rows.
- `knowledge/*.md` unchanged. `external_ready_candidate=0` maintained.

## Stage 2 classification ledger hardening（2026-06-05）

- Added `classification_vocabulary` to migration ledger (557 rows) and operator ledgers (quarantine, facility, export candidate, crosswalk, integrated summary).
- `validate_classification_vocabulary.py` PASS. **No** export_candidate / facility / quarantine promotion.
- See [STAGE2_CLASSIFICATION_LEDGER_AUDIT_REPORT_20260605.md](STAGE2_CLASSIFICATION_LEDGER_AUDIT_REPORT_20260605.md).

## Stage 3 integrated governance（2026-06-05）

- **添付文書遵守:** 用法・用量・使用方法は製品単位最新電子添文（PMDA）に沿う。reference から数値断定禁止。
- **適用外使用:** 医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- Integrated: `00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス.md` + 7 boundary hubs + 7 collisions + pituitary REFERENCE_HUB routing.
- `knowledge/*.md` **unchanged**. No promotion.
- See [STAGE3_INTEGRATED_GOVERNANCE_AUDIT_REPORT_20260605.md](STAGE3_INTEGRATED_GOVERNANCE_AUDIT_REPORT_20260605.md).

## Stage 4 knowledge boundary export（2026-06-05）

- Exported Stage 3 governance into **10/13** `knowledge/*.md` (boundary / negative knowledge / checklists only).
- Fixed stale **306** → **366** CHILD file count in `01_START_HERE`.
- `validate_unsafe_patterns.py` PASS. Upload target remains **13**. No promotion.
- See [STAGE4_KNOWLEDGE_BOUNDARY_EXPORT_AUDIT_REPORT_20260605.md](STAGE4_KNOWLEDGE_BOUNDARY_EXPORT_AUDIT_REPORT_20260605.md).

## Stage 5 preparation only（2026-06-05）

- Full validator suite PASS; `external_ready_candidates=0`; upload **13** knowledge files.
- `report_preview_promotion_candidates.py` → `approved_preview_records=0`（Preview 未実走）。
- `apply_preview_promotion.py` **未実行**（`--apply` 禁止遵守）。
- Prepared: [preview_evidence_collection_checklist.md](preview_evidence_collection_checklist.md), [collision_rag_regression_evidence_collection.md](collision_rag_regression_evidence_collection.md), [collision_rag_regression_results_PENDING.csv](collision_rag_regression_results_PENDING.csv).
- See [STAGE5_READINESS_AND_BLOCKERS_20260605.md](STAGE5_READINESS_AND_BLOCKERS_20260605.md).

## Stage 5A evidence collection readiness（2026-06-05）

- Re-ran 14 validators — all PASS; `557/557`; `external_ready_candidates=0`.
- Regenerated [preview_promotion_candidates_report_20260605.csv](preview_promotion_candidates_report_20260605.csv) — 0 approved / 0 candidates.
- Preview: **no real raw_output** (PREVIEW-001..004 `to_be_recorded`; 005..015 `not_run_yet`).
- Collision RAG: **21/21 pending** (`collision_rag_regression_results_PENDING.csv`).
- New: [STAGE5A_EVIDENCE_COLLECTION_OPERATOR_CHECKLIST.md](STAGE5A_EVIDENCE_COLLECTION_OPERATOR_CHECKLIST.md), [STAGE5A_READINESS_REPORT_20260605.md](STAGE5A_READINESS_REPORT_20260605.md).
- **Not done:** knowledge edits, approve, facility confirmed, PMDA/IF URLs, `--apply`, release readiness claim.

## Stage 6 PMDA/IF product-level registration（2026-06-05）

- **Parallel with Stage 5A** (Preview/RAG human evidence still pending).
- Gap supplement: **36/36** keys updated in `pmda_product_source_register_gap_supplement.csv` + new `pmda_document_source_register_gap_supplement.csv` (210 document rows).
- Applier: `reference_archive/.../08_VALIDATION_CHECKS/_apply_gap_stage6_all_batches.py`; batch MD `pmda_pilot_batch_GAP-001` … `GAP-013`.
- **CHILD→gap reconciliation:** 26 keys copied with log in `STAGE6_RECONCILIATION_LOG.md` (user-approved).
- **Gap-only web-verified primary (2026-06-05):** edaravone, ozagrel, clazosentan, fasudil, thiopental, thiamylal, pentobarbital, remimazolam, fludrocortisone.
- **nimodipine:** `document_absent_domestic_unapproved` — no PMDA product URL (国内未承認).
- **CHILD C-001:** IF audit notes only (`pmda_pilot_batch_C-001.md`); no Interview Form URLs invented.
- Profile frontmatter: `primary_verified_pending_pharmacist` or `document_absent_domestic_unapproved`; **`pmda_product_level_verified` remains false**.
- **Not done:** knowledge export, facility confirmed, pharmacist sign-off, Preview approve, `--apply`, `custom_gpt_upload_safe`.
- See [STAGE6_NO_EDIT_AUDIT_20260605.md](STAGE6_NO_EDIT_AUDIT_20260605.md), [STAGE6_CHILD_GAP_RECONCILIATION_MATRIX_20260605.csv](STAGE6_CHILD_GAP_RECONCILIATION_MATRIX_20260605.csv), [STAGE6_COMPLETION_REPORT_20260605.md](STAGE6_COMPLETION_REPORT_20260605.md).

## Stage 6C/D IF individual URLs & pharmacist attestation（2026-06-05）

- **PMDA/IF evidence changed:** yes — CHILD `interview_form` **104** `document_present`, **19** `document_absent_after_search`; GAP **31** present / **4** absent.
- **Pharmacist attestation:** **17** batches (`C-002` … `C-018`) signed **2026-06-05** — CHILD **115/123** `yes`, gap **35/35** `yes`; **`formulary_match=na`**（日本全般スコープ、当院採用リストは対象外）。**C-001**（8 keys）のみ `pending`。
- Pipeline: `_stage6c_pipeline.py`; applier stub `_apply_child_stage6_C00N.py`; operator guide `STAGE6C_PHARMACIST_IF_REVIEW_OPERATOR_GUIDE.md`.
- **Not done:** knowledge export, facility confirmed, pharmacist sign-off (`label_compliance_no_deviation=yes`), Preview approve, `--apply`, `custom_gpt_upload_safe`.
- **Unchanged:** `gap_v3_pharmacist_facility_review_log` NOT sign-off; `external_ready_candidate=0`.
- See [STAGE6C_D_COMPLETION_REPORT_20260605.md](STAGE6C_D_COMPLETION_REPORT_20260605.md).

## gap v3 follow-up: Phase 2 拡張・薬剤師/施設レビュー・archive 移行（2026-06-04）

### 実施

1. Phase 2 追加 5 領域: 造影・CSF/IIH・血管内治療・痙縮・CNS 感染（境界ハブ + collision 各 1）
2. 既存 2 collision に repo-local 薬剤師/施設レビュー表を追記（`unresolved_intentional_hold` 維持）
3. [gap_v3_pharmacist_facility_review_log_20260604.md](gap_v3_pharmacist_facility_review_log_20260604.md) — Preview/promotion 禁止の明文化
4. PARENT を `reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` へ集約。ledger 174 行・integrated `source_path` を更新
5. ワークスペース sibling `references/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` **削除**

### Hold / gate（変更なし）

- `apply_preview_promotion.py` — Preview evidence なしでは実行しない
- `external_ready_candidate` — 0
- 123+212 薬剤プロファイル — integrated 層待ち

### Validators

`validate_reference_migration_ledger.py --corpus all` PASS (540/540)（**historical 2026-06-04**）、upload_manifest、unsafe_patterns、release_readiness、facility_confirmation PASS。

---

## gap v3 PARENT / CHILD dual-reference（2026-06-04）

### Port したもの（adapted_port / integrated boundary のみ）

1. `manifest/reference_migration_decision_ledger.csv` — PARENT 174 行追加（CHILD 366 行不変、合計 540）。（**historical 2026-06-04**）
2. `tests/validate_reference_migration_ledger.py` — `--corpus child|parent|all`、二重 `REFERENCE_ROOTS`。
3. `derived/README.md` — sibling 二層（CHILD + PARENT）の説明。
4. `derived/gpt_drug_data_policy_expansion_runbook.md` — Sibling 節を CHILD/PARENT に分割。
5. `manifest/build_notes.md` — gap v3 登録エントリ。
6. `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md` — PARENT（PMDA 未解決）の 1 節。
7. Integrated pilot:
   - `neurosurgery_integrated_safe_rag_package/.../04_Drug_Classes/神経腫瘍薬物療法_境界と出典階層.md`
   - `neurosurgery_integrated_safe_rag_package/.../04_Drug_Classes/下垂体内分泌薬_境界と出典階層.md`
   - `90_Audit/Collisions/gap_v3_neuro_oncology_reference_collision.md`
   - `90_Audit/Collisions/gap_v3_pituitary_endocrine_reference_collision.md`
8. `manifest/_DRAFT_parent_child_diff_report.md` — Phase 0 機械差分。

### Intentionally hold

1. PARENT `02_DRUG_PROFILES_SAFE_KNOWLEDGE/**/*.md`（123）— `no_port_keep_as_reference_only`、integrated drug-profile 層待ち。
2. CHILD 212 薬剤プロファイル — 既存 hold 維持。
3. CHILD `package_summary.json` の PMDA 数値 — TARGET / knowledge へ non-promotion。
4. `custom_gpt_upload_safe: true` — 設定しない。
5. PARENT `pmda_product_level_verified: false` — true に書き換えない。
6. V3 残り 6 領域（造影/手技、痙縮、CSF/IIH 等）— integrated 本文 port なし（ledger のみ）。

### 残 gate

1. Operator review: `gap_v3_m0_ledger_recorded_pending_operator_review`（540 行）。（**historical** — current ledger 557）
2. Pharmacist / facility confirmation — collision メモ `unresolved_intentional_hold`。
3. Preview evidence — 未投入のまま promotion / external-ready 禁止。
4. `validate_reference_migration_ledger.py --corpus all` — repo-local PASS は external-ready ではない。

### Validators（2026-06-04 実行）

- `validate_reference_migration_ledger.py --corpus all` — PASS（540/540）（**historical 2026-06-04**）
- `validate_upload_manifest.py` — PASS
- `validate_unsafe_patterns.py` — PASS
- `validate_release_readiness.py` — PASS
- `check_integrated_policy_controls.py` — PASS（新規 integrated 4 ファイル含む）

## Migration slice B（2026-06-02）

`baseline/pre-slice-b-m1` 以降、reference corpus 25 件（adapted_port + operator_side_only_port）の governance パターンを TARGET operator-side 文書へ適応。REFERENCE の PMDA 0/127 や `custom_gpt_upload_safe: false` を TARGET の完了事実として写していない。`knowledge/` 13 本は未変更。

レビュー重点: runbook / README の sibling reference 節、quarantine カテゴリ、safe answer shape、instructions の禁止短絡、ledger 25 行の `m1_port_applied_pending_operator_review`。

## Prior closeout note

今回の変更は、Preview evidence -> candidate report -> dry-run -> apply -> closeout の順序規律に加えて、reference migration completeness、facility confirmation state、derived export candidate state の gate を operator-side 文書全体で揃えるための限定差分です。レビューでは、実 Preview 実績が未記録のまま promotion helper に進めないこと、active quarantine を残した row を `external_ready_candidate` に上げないこと、reference repo 全ファイルが migration decision ledger で 1 file 1 decision として管理されていること、facility evidence がない row を `confirmed` または `not_applicable` にしないこと、human review 未記録 row を `derived_export_candidate_ledger.csv` で `export_candidate=yes` にしないこと、closeout 記録面で candidate report と dry-run/apply と validation の証跡が追えることを見てください。

主な確認対象は次のとおりです。

1. `README.md` の Custom GPT 実行順が Preview 実績記録後に candidate report / dry-run / apply へ進む順になっているか。
2. `tests/preview_execution_runbook.md` と `derived/gpt_drug_data_policy_expansion_runbook.md` が同じ停止条件と 1 row apply 規律を持っているか。
3. `manifest/future_policy_integration_matrix.md` の Commit 12 / 13 が Preview evidence 未記録時の停止条件と quarantine 衝突条件を反映しているか。
4. Runbook Commit 11（2026-06-02）: reference A-PMDA batch 56 件の ledger-only 登録と knowledge 13 固定を `manifest/build_notes.md` で確認したか。
5. Runbook Commit 12（2026-06-02）: `tests/preview_test_protocol.md` と `tests/cds_time_window_alert_tests.md` が 8 領域 + TEST-CDS をカバーし、`validate_preview_protocol.py` が PASS か。UI Preview 未実行のまま approve していないか。
6. Runbook Commit 13（2026-06-02）: `audit/pharmacist_red_flag_review_checklist.md` / `unapproved_content_quarantine.md` が存在し、`knowledge_quarantine_register.csv` に active hold がある間 `external_ready_candidate` に昇格していないか。
7. Runbook Commit 14（2026-06-02）: `runbook_commit_14_final_audit_report.md` が未解決ゲートを明示し、`validate_final_audit_commit14.py` が PASS か。薬剤師 sign-off 前に quarantine を `cleared` にしていないか。
4. `audit/human_review_log_template.md` と `audit/rag_export_audit_checklist.md` が candidate report、dry-run、apply、quarantine 再検証の証跡を残せる形になっているか。
5. `derived/README.md` と package `README.md` が、`reference_migration_decision_ledger.csv` / `validate_reference_migration_ledger.py` と `facility_confirmation_status_ledger.csv` / `validate_facility_confirmation_status.py` を operator-side gate として同じ意味で説明しているか。
6. `tests/pass_fail_criteria.md` と `tests/preview_execution_runbook.md` が、Preview approved を facility confirmed や reference migration completeness の代替として扱っていないか。
7. `manifest/derived_export_candidate_ledger.csv` と `manifest/integrated_origin_reclassification_summary.csv` が operator-side artifact として登録され、Knowledge upload target や external-ready 承認として扱われていないか。
8. full validation suite に `validate_reference_migration_ledger.py`、`validate_facility_confirmation_status.py`、`validate_derived_export_candidate_ledger.py` が含まれ、repo-local pass と external-ready が分離して報告されるか。

今回、real Preview evidence と facility evidence は未投入です。したがって `tests/apply_preview_promotion.py --apply`、`manifest/knowledge_chunk_review_crosswalk.csv` の external-ready 昇格、`manifest/facility_confirmation_status_ledger.csv` の `confirmed` / `not_applicable` 更新は行いません。

今回、human-review evidence も未投入です。したがって `manifest/derived_export_candidate_ledger.csv` の各 row は `export_candidate=no` のまま維持し、source traceability があることだけを理由に derived export や external-ready へ進めません。

今回、`instructions/custom_gpt_instructions.md` への追加変更はありません。

touch したファイルの diagnostics では error は出ていません。
