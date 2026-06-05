# Composer 2.5 Custom GPT Knowledge Package Update Blueprint

## Positioning

This document is an operator-side blueprint for asking Composer 2.5 to maintain and strengthen:

`references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package`

It is not a clinical guideline, prescribing protocol, institutional procedure, EHR/CDS specification, or Custom GPT Knowledge upload target.

The source-of-truth side remains:

1. `references/neurosurgery_qc_package`
2. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package`
3. `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603`
4. `references/neurosurgery_safe_rag_pmda_product_source_register_resolved`

The Custom GPT upload target remains only:

`references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package/knowledge/*.md`

There are 13 upload-target knowledge files. Do not add upload targets unless the operator explicitly approves a separate stage after manifest, test, audit, and README changes are proposed.

## Current Status Snapshot After Composer Stage 4 / Stage 5 Preparation

This section supersedes older planning assumptions in this file when the observed workspace matches the following state.

Observed on 2026-06-05:

1. Stage 0 through Stage 4 are reported complete.
2. Stage 5 preparation artifacts exist, but Stage 5 promotion/release gating is not started.
3. `custom_gpt_knowledge_package` contains 77 files in the observed workspace state.
4. Knowledge upload target remains 13 markdown files under `knowledge/`.
5. Stage 4 exported boundary-only language into 10 of 13 knowledge files.
6. Stage 4 did not intentionally update:
   - `06_PATIENT_STATE_NOTES.md`
   - `08_THRESHOLDS_AND_CONDITIONS.md`
   - `11_CDS_CANDIDATE_BOUNDARIES.md`
7. `reference_migration_decision_ledger.csv` validation reports 557 rows and 557 reference files.
8. `validate_release_readiness.py` reports `external_ready_candidates=0`.
9. `report_preview_promotion_candidates.py` reports:
   - `approved_preview_records=0`
   - `promotion_candidate_rows=0`
   - `promotion_report_rows=0`
10. `human_reviewed_preview_examples.md` still has PREVIEW-001 through PREVIEW-015 pending, with no real raw Preview output recorded.
11. `collision_rag_regression_results_PENDING.csv` is an empty evidence collection placeholder, not completed RAG evidence.
12. Operator-side validators pass, but this does not mean clinical approval, facility confirmation, PMDA product-level completion, or Custom GPT external-readiness.

Composer must explicitly preserve the distinction between:

1. repo-local validation PASS
2. human Preview evidence
3. pharmacist/physician review
4. facility confirmation
5. PMDA product-level document evidence
6. collision RAG regression execution
7. release promotion

Only item 1 is currently satisfied.

## Non-Negotiable Rules For Composer 2.5

Composer must treat this as a medical safety and RAG audit maintenance task, not as a bulk content migration.

1. Do not blindly copy PMDA, gap v3, manifest, audit, test, or runbook files into Custom GPT Knowledge.
2. Do not convert `resolved`, `review_ready`, `validation pass`, `ledger registered`, or `READY_FOR_LIMITED_ROUTING` into clinical approval, facility confirmation, or external-ready status.
3. Do not add dose, interval, infusion rate, TDM target, sampling time, IV compatibility, dialysis operation, order set, EHR trigger, or CDS production behavior as a confirmed value in knowledge text.
4. Do not expand derived knowledge before integrated source-governance is in place.
5. Do not treat reference corpus completion as upload safety.
6. Do not mark any row as external-ready without Preview evidence, human review evidence, and facility confirmation evidence where required.
7. Do not edit medical content while performing metadata count reconciliation.
8. Stop after each stage and report proposed diff, executed validation, findings, residual risk, and next stage.
9. Do not invent Custom GPT Preview outputs, RAG regression results, reviewer names, review dates, facility evidence links, PMDA URLs, Interview Form URLs, or pass/fail judgments.
10. Do not use `apply_preview_promotion.py --apply` unless the operator explicitly approves a specific record after a successful dry-run.
11. Do not infer electronic label, Interview Form, RMP, patient guide, revision history, formulary, insurance, or facility SOP status from a drug profile or batch script filename.
12. Do not reuse CHILD PMDA pilot evidence for gap v3 PARENT drugs unless the exact product-level source and drug key have been manually reconciled and recorded.

## Current-State Facts To Verify Before Editing

Composer must run a no-edit audit before making any change.

Expected facts as of 2026-06-05:

1. CHILD corpus:
   `references/neurosurgery_safe_rag_pmda_product_source_register_resolved`
   Expected file count: 366.
2. PARENT corpus:
   `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603`
   Expected file count: 191.
3. Combined reference file count:
   Expected count: 557.
4. `custom_gpt_knowledge_package` currently contains 77 files in the observed workspace state after Stage 5 preparation artifacts.
5. `reference_migration_decision_ledger.csv` validation should report 557 rows and 557 reference files.
6. `validate_release_readiness.py` should report `external_ready_candidates=0`.
7. Knowledge upload target must remain 13 files under `knowledge/`.
8. Preview approved records must remain 0 until real Custom GPT UI output is recorded and reviewed.
9. Collision RAG 21-question results must remain pending until actual RAG execution output is recorded.

The known stale metadata class is old wording that says CHILD 366 + PARENT 174 = 540. That wording is stale if current validation reports 557. Composer must first reconcile this as metadata only, without changing medical content.

## No-Edit Audit Commands

Run from:

`/Users/yusukefujinami/neurosurgery_pharm_algorithm`

Use commands equivalent to the following. Composer may use safer local variants, but must report the command and result.

```bash
find references/neurosurgery_safe_rag_pmda_product_source_register_resolved -type f | wc -l
find references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603 -type f | wc -l
find references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package -type f | wc -l
find references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package/knowledge -maxdepth 1 -type f -name '*.md' | wc -l
```

Then run from:

`/Users/yusukefujinami/neurosurgery_pharm_algorithm/references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package`

```bash
python3 tests/validate_upload_manifest.py
python3 tests/validate_unsafe_patterns.py
python3 tests/validate_quarantine_integrity.py
python3 tests/validate_reference_migration_ledger.py --corpus all
python3 tests/validate_facility_confirmation_status.py
python3 tests/validate_derived_export_candidate_ledger.py
python3 tests/validate_release_readiness.py
python3 tests/validate_gap_v3_review_ready.py
python3 tests/validate_collision_governance.py
python3 tests/validate_classification_vocabulary.py
python3 tests/validate_preview_protocol.py
python3 tests/validate_review_state_integrity.py
python3 tests/validate_pharmacist_red_flag_commit13.py
python3 tests/validate_final_audit_commit14.py
python3 tests/report_preview_promotion_candidates.py --output /tmp/qc_preview_promotion_candidates.csv
```

Search for stale count wording:

```bash
rg -n "366|174|540|557|PARENT|CHILD|external_ready|Knowledge upload|upload target" references/neurosurgery_qc_package/derived
```

## Required No-Edit Audit Report

Before editing, Composer must report these six items.

### A. Upload Target

Report that the upload target is the 13 markdown files under:

`derived/custom_gpt_knowledge_package/knowledge/`

Also report that `instructions/custom_gpt_instructions.md` is pasted into the Custom GPT Instructions field and is not a Knowledge file.

### B. Operator-Side Files

Report that these are not upload targets:

1. `README.md`
2. `instructions/`
3. `manifest/`
4. `audit/`
5. `tests/`
6. `derived/gpt_drug_data_policy_expansion_runbook.md`
7. reference archives
8. PMDA work corpus

### C. Source Of Truth

Report that the authoritative governance layer is integrated-first:

1. `neurosurgery_qc_package`
2. `neurosurgery_integrated_safe_rag_package`
3. source registers, audit logs, collision ledgers, and validation reports

The derived package is an export layer with traceability, not a source-of-truth layer.

### D. Stale Metadata

Report all stale references to:

1. PARENT 174 files
2. CHILD 366 + PARENT 174
3. 540 rows or 540 files

Treat these as metadata reconciliation targets only.

### E. Direct Port Prohibition

Report that direct port is prohibited for:

1. PMDA product-level drug profiles without human and facility review.
2. gap v3 general-name drug profiles.
3. procedural, historical, or negative notes that could be misread as standard therapy.
4. dose, interval, infusion, compatibility, TDM, dialysis, formulary, inventory, order set, and CDS trigger details.
5. manifests, tests, runbooks, audit logs, scripts, source registers, and validation reports.

### F. Minimal Safe Commit Proposal

The first edit stage must be:

Metadata count reconciliation only.

Allowed files for Stage 1:

1. `references/neurosurgery_qc_package/derived/README.md`
2. `references/neurosurgery_qc_package/derived/gpt_drug_data_policy_expansion_runbook.md`
3. `references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package/README.md`
4. Operator-side manifest or audit files that contain stale 174/540 wording.

Forbidden in Stage 1:

1. Any `knowledge/*.md` medical content edit.
2. Any external-ready promotion.
3. Any facility confirmation promotion.
4. Any upload target expansion.
5. Any new clinical summary.

## Current Hard Blockers Before Any Release Promotion

These are not optional polish items. They are hard blockers.

1. No real Custom GPT Preview raw output has been recorded for PREVIEW-001 through PREVIEW-015.
2. No approved Preview records exist.
3. Promotion candidates are 0.
4. `apply_preview_promotion.py` has no eligible dry-run target.
5. Collision RAG regression 21 questions have not been actually run.
6. The gap v3 human review readiness matrix remains export-blocked unless each domain has evidence and sign-off.
7. Gap v3 product-level PMDA electronic label and Interview Form evidence is not complete.
8. CHILD 127 remains not upload-safe and requires manual review/facility confirmation.
9. Integrated drug-profile physical layer is not fully built for wholesale porting of profile bodies.
10. Facility evidence remains pending unless a specific ledger row contains real evidence.

Composer must classify this state as `repo_local_validated_but_evidence_pending`, not `complete`, `release_ready`, `upload_safe`, or `clinically_approved`.

## Japanese Output Accuracy And Naturalness Audit

This blueprint must also control whether Composer's work preserves accurate, natural Japanese output. Safety gates alone are not enough. The intended Custom GPT behavior is not "answer from URL" or "return audit jargon"; it is "give a clinician-facing Japanese explanation that is useful while preserving uncertainty and escalation boundaries."

The active operator-side style references are:

1. `derived/custom_gpt_knowledge_package/docs/japanese_medical_writing_style_guide.md`
2. `derived/custom_gpt_knowledge_package/docs/custom_gpt_knowledge_safety_boundary.md`
3. `derived/custom_gpt_knowledge_package/docs/clinical_document_structure_standard.md`
4. `derived/custom_gpt_knowledge_package/docs/llm_answer_transfer_rules.md`
5. `derived/custom_gpt_knowledge_package/docs/emergency_reference_readability_rules.md`
6. `derived/custom_gpt_knowledge_package/audit/japanese_expression_risk_ledger.csv`
7. `derived/custom_gpt_knowledge_package/audit/japanese_medical_document_quality_audit.md`

These files are operator-side references and must remain `upload_to_custom_gpt=no` unless the operator explicitly approves a separate upload-boundary redesign.

### Official project stance

Composer must preserve these positions from the package README, `01_START_HERE_AND_POSITIONING.md`, `instructions/custom_gpt_instructions.md`, `pass_fail_criteria.md`, and `preview_test_protocol.md`:

1. Custom GPT Knowledge is not a substitute for feeding GitHub URLs or PMDA URLs directly.
2. URLs in source registers are operator-side routing evidence, not proof that the Custom GPT reads those URLs at runtime.
3. Knowledge alone cannot confirm the latest PMDA electronic label, latest guideline, RMP update, insurance status, formulary status, facility SOP, or final clinical decision.
4. Correct answers must organize the issue, state what cannot be determined, and point to primary-source and facility confirmation when needed.
5. Preview pass, validator pass, URL registration, or source-register completion must not be described as clinical approval.

### Required Japanese answer shape

Composer must keep the answer shape aligned with `instructions/custom_gpt_instructions.md` and `pass_fail_criteria.md`.

Required traits:

1. Start with a natural Japanese conclusion or orientation in 1-2 sentences.
2. Then list only the clinically relevant branching axes.
3. Keep high-risk stop signals explicit but concise.
4. Use clinician-facing Japanese, not manifest/audit jargon.
5. Distinguish `候補`, `確認項目`, `未確認`, `施設確認`, `一次資料確認`, and `実装仕様`.
6. Avoid automatic wording such as `標準`, `推奨`, `使用すべき`, `使用してよい`, `この用量でよい`, or `開始してよい` unless the reviewed source and allowed context justify it.
7. Prefer "この資料だけでは判断できません" over forced certainty.
8. For low-risk organization questions, avoid a long disclaimer-only answer.
9. For high-risk drug, emergency, dosing, renal/hepatic, TDM, compatibility, dialysis, or CDS questions, include a short safety disclaimer.
10. Do not expose internal ledger labels unless the user explicitly asks for audit status.

### URL-only policy

Composer must not write or approve any sentence that implies URL registration alone guarantees accurate Custom GPT output.

Allowed:

1. "The URL is an operator-side pointer for human primary-source confirmation."
2. "The register records where to verify the product-level document."
3. "Runtime PMDA fetch is not implemented unless a separate tool/action is built and validated."

Forbidden:

1. "URL is registered, so the GPT can answer the dose accurately."
2. "PMDA URL presence means the product is approved for the queried use."
3. "Interview Form URL presence means dosing/compatibility can be summarized in Knowledge."
4. "The Custom GPT will automatically open pmda.go.jp at answer time."

### Japanese output audit checklist

Before Composer claims Stage 5A readiness or any later output-quality improvement, it must inspect these files:

1. `instructions/custom_gpt_instructions.md`
2. `tests/pass_fail_criteria.md`
3. `tests/preview_test_protocol.md`
4. `tests/expected_answer_samples.md`
5. `tests/response_style_regression_assets.md`
6. `tests/human_reviewed_preview_examples.md`

Composer must report:

1. whether each Preview prompt has a must-have and must-not-have rubric
2. whether natural Japanese answer shape is represented
3. whether URL-only overclaim is explicitly prevented
4. whether high-risk drug questions require uncertainty and primary-source confirmation
5. whether operator jargon is kept out of user-facing answer style
6. whether approved examples actually exist or remain pending

If approved Preview examples do not exist, Composer must say:

`Japanese answer quality is specified by instructions and rubrics, but not yet empirically validated by real Preview output.`

### Fail conditions for Japanese output

Any of the following must be treated as a failure requiring rejection or remediation:

1. The answer gives dose, interval, infusion rate, TDM, sampling time, compatibility, dialysis operation, or CDS trigger as a confirmed value from Knowledge alone.
2. The answer treats URL registration as runtime source reading.
3. The answer treats PMDA source registration as facility availability.
4. The answer treats Preview pass as facility confirmation.
5. The answer is mostly audit jargon and does not give a clinician-facing orientation.
6. The answer is only a disclaimer and does not answer a low-risk organization question.
7. The answer collapses candidate, confirmed, facility-operable, and production-CDS-ready into one category.
8. The answer uses gap v3 or CHILD profile content as standard therapy without product-level and human-review gates.

### Runtime PMDA fetch workstream

If the operator wants the Custom GPT to answer from latest PMDA documents at runtime, Composer must treat that as a separate implementation project, not as a Stage 6 register update.

A runtime fetch design must include:

1. approved tool/action scope
2. source domain allowlist
3. fetch, parse, and citation behavior
4. version/date capture
5. fallback when fetch fails
6. no-dose/no-order-set guardrails
7. Preview and regression tests
8. pharmacist/physician review before any clinical-facing use

Until such a runtime source-reading layer exists, the safe phrasing is:

`URL registration supports human primary-source confirmation; it does not guarantee that the Custom GPT reads or applies the document at answer time.`

## Stage Plan

### Stage 0: No-Edit Current-State Audit

Goal: establish actual file counts, current validation status, upload target boundary, stale metadata, and direct-port prohibitions.

Allowed edits: none.

Exit criteria:

1. Git/worktree status reported.
2. File counts reported.
3. Existing validation results reported.
4. Stale metadata list reported.
5. Stage 1 proposed diff scope reported.

Stop after Stage 0.

### Stage 1: Metadata Count Reconciliation

Goal: reconcile stale CHILD/PARENT/ledger counts to current observed validation state.

Required updates:

1. Replace stale PARENT 174 wording with PARENT 191 where the statement refers to current archived file count.
2. Replace stale 540 combined file count with 557 where the statement refers to current reference migration coverage.
3. Preserve warnings that ledger completion is not blind-copy permission.
4. Preserve warnings that PMDA/gap v3 references are not upload targets.
5. Preserve `external_ready_candidates=0`.

Required validation after edits:

```bash
python3 tests/validate_upload_manifest.py
python3 tests/validate_unsafe_patterns.py
python3 tests/validate_quarantine_integrity.py
python3 tests/validate_reference_migration_ledger.py --corpus all
python3 tests/validate_facility_confirmation_status.py
python3 tests/validate_derived_export_candidate_ledger.py
python3 tests/validate_release_readiness.py
python3 tests/validate_gap_v3_review_ready.py
```

Exit criteria:

1. Validation passes.
2. `migration_ledger_rows=557`.
3. `reference_file_count=557`.
4. `external_ready_candidates=0`.
5. No `knowledge/*.md` files changed in this stage unless the operator explicitly approved a separate content stage.

Stop after Stage 1.

### Stage 2: Classification Ledger Hardening

Goal: strengthen traceability and classification, not user-facing medical content.

Composer may propose updates to operator-side ledgers only after Stage 1 passes:

1. `reference_migration_decision_ledger.csv`
2. `integrated_origin_reclassification_summary.csv`
3. `knowledge_quarantine_register.csv`
4. `gap_v3_export_gate_summary.md`
5. `facility_confirmation_status_ledger.csv`
6. `derived_export_candidate_ledger.csv`

Required classification vocabulary:

1. `direct_boundary_port`
2. `adapted_boundary_port`
3. `operator_side_only`
4. `reference_only`
5. `quarantine`
6. `unresolved_do_not_export`
7. `hold_as_reference_until_integrated_layer_exists`

Forbidden:

1. changing any `export_candidate` from `no` to `yes` without evidence
2. changing facility status to confirmed without evidence
3. changing quarantine status to cleared without evidence
4. changing upload target flags

Stop after Stage 2.

### Stage 3: Integrated-First Governance Update

Goal: if content strengthening is needed, update integrated boundary and governance files before derived knowledge.

Allowed content type:

1. source hierarchy
2. boundary notes
3. collision notes
4. operator-side review gates
5. facility confirmation requirements
6. unsafe shortcut prevention

Forbidden content type:

1. dose tables
2. TDM targets
3. IV compatibility tables
4. production CDS triggers
5. facility formulary assertions
6. prescribing recommendations

Stop after Stage 3.

### Stage 4: Derived Knowledge Boundary Export

Goal: only after integrated governance is updated and validated, export concise boundary language into the existing 13 knowledge files.

Allowed export:

1. safety boundary
2. negative knowledge
3. source-check requirement
4. facility-check requirement
5. candidate versus confirmed distinction
6. reference-only status

Forbidden export:

1. product-specific dose
2. product-specific administration detail
3. facility-specific operational detail
4. standard therapy claim from gap v3 profile
5. PMDA confirmation claim without product-level evidence

Stop after Stage 4.

### Stage 5: Preview And Release Gating

Goal: preserve repo-local safety and keep external-ready at zero unless real review evidence exists.

Required:

1. Preview test cases updated only if new boundary text was exported.
2. `human_reviewed_preview_examples.md` must contain actual Preview output before promotion.
3. `report_preview_promotion_candidates.py` must be run before any promotion.
4. `apply_preview_promotion.py` must be dry-run before apply.
5. Release readiness must remain conservative.

Stop after Stage 5.

### Stage 5A: Evidence Collection Only

Goal: collect real evidence without promotion.

Allowed:

1. Fill `tests/human_reviewed_preview_examples.md` with raw Custom GPT UI outputs copied by the operator.
2. Record reviewer status only when a real pharmacist/physician reviewer has reviewed the output.
3. Fill collision RAG regression result CSV from actual RAG runs.
4. Record failed, borderline, or rejected outputs without trying to make them pass.

Forbidden:

1. inventing outputs
2. marking pending records approved
3. changing release readiness
4. running `apply_preview_promotion.py --apply`
5. changing facility status
6. editing knowledge content to make an unreviewed Preview pass

Exit criteria:

1. At least PREVIEW-001 through PREVIEW-015 have real raw outputs or remain explicitly `not_run_yet`.
2. Collision RAG 21-question file has actual run evidence or remains explicitly pending.
3. Promotion report is regenerated.
4. `external_ready_candidates=0` unless the operator explicitly approves Stage 5B for specific reviewed records.
5. Japanese answer quality remains `specified_but_not_empirically_validated` until approved real Preview examples exist.

Stop after Stage 5A.

### Stage 5B: Promotion Candidate Dry-Run Only

Goal: test whether approved Preview records can move from pending to a higher review state.

Entry criteria:

1. `human_reviewed_preview_examples.md` contains real raw output.
2. Review status is approved by a named reviewer.
3. PHI check and normalization boundary check are complete.
4. `report_preview_promotion_candidates.py` shows candidate rows.

Allowed:

1. Run `apply_preview_promotion.py` without `--apply` for each candidate.
2. Report blocking reasons.
3. Report exact files that would change if applied.

Forbidden:

1. `--apply`
2. batch promotion
3. approval of rejected or pending records
4. promotion based only on RAG or validator pass

Stop after Stage 5B.

### Stage 5C: Promotion Apply By Explicit Approval Only

Goal: apply exactly one operator-approved promotion at a time.

Entry criteria:

1. successful dry-run
2. explicit operator approval for the specific `review_record_id`, `chunk_id`, and reviewer role
3. no unresolved blocker in dry-run output

Required after each single-row apply:

```bash
python3 tests/validate_review_state_integrity.py
python3 tests/validate_release_readiness.py
python3 tests/validate_quarantine_integrity.py
python3 tests/validate_upload_manifest.py
```

Stop after each single-row apply.

### Stage 6: PMDA Product-Level And Interview Form Evidence Workstream

Goal: create or complete source registers for PMDA product-level documents without exporting prescribing details into knowledge.

This stage is evidence registration, not knowledge promotion.

Priority domains:

1. gap v3 additions such as edaravone, ozagrel, clazosentan, fasudil, nimodipine, alteplase, argatroban, urokinase, diazepam, lorazepam, thiopental-class agents, pentobarbital, remimazolam, antimicrobials, tolvaptan, landiolol, and transfusion product classes.
2. CHILD 127 drugs with unresolved manual review, Interview Form, RMP, patient guide, or revision-history status.

Allowed:

1. update source registers with manually confirmed PMDA product URLs
2. separately register electronic label, Interview Form, RMP, patient guide, and revision history status
3. record `document_present`, `document_absent_after_search`, or `document_unchecked`
4. keep product-level evidence in source/register/integrated layers

Forbidden:

1. guessing product URLs
2. converting source registration into prescribing recommendation
3. copying label or IF dosing details into knowledge
4. marking facility confirmed from PMDA evidence
5. marking Preview approved from PMDA evidence

Stop after Stage 6.

### Stage 7: Integrated Drug-Profile Physical Layer

Goal: design and populate an integrated physical layer for reviewed drug-profile boundary records before any derived export.

Entry criteria:

1. source hierarchy exists
2. product-level evidence exists where applicable
3. pharmacist/physician review scope is defined
4. facility evidence requirements are defined
5. collision status is known

Allowed:

1. boundary-only adapted profiles
2. source links and verification status
3. contraindication to blind merge
4. explicit no-dose/no-order-set language

Forbidden:

1. direct merge into disease notes
2. general-name gap profile as standard therapy
3. use of CHILD counts for PARENT completion
4. knowledge export before integrated review

Stop after Stage 7.

## Composer 2.5 Failure Modes And Controls

| Failure mode | Risk | Control |
| --- | --- | --- |
| Long-context smoothing | Composer leaves old 540 wording while adding new 557 wording elsewhere | Require stale-count `rg` before and after Stage 1 |
| Premature completion | Validation pass is reported as clinical completion | Require explicit statement: validation is operator-side only |
| Blind migration | Reference profiles copied into knowledge | Require direct-port prohibition report before edits |
| Medical naturalization | Unsafe details become natural prose | Ban medical content edits during Stage 1 |
| Upload drift | New files are silently made upload targets | Run `validate_upload_manifest.py` after every stage |
| Release drift | `external_ready_candidate` appears without review evidence | Run `validate_release_readiness.py`; require `external_ready_candidates=0` unless operator approves promotion stage |
| Facility overclaim | Pending facility review becomes confirmed | Run `validate_facility_confirmation_status.py`; require evidence link |
| Quarantine leakage | Red-flag row appears as ready | Run `validate_quarantine_integrity.py` |
| Evidence fabrication | Composer fills Preview/RAG/reviewer/PMDA fields from imagination | Require raw output/source URL/evidence link; leave pending if absent |
| Stage skipping | Composer jumps from Stage 5 prep to `--apply` | Split Stage 5A/5B/5C and require explicit approval per record |
| PMDA overclaim | Product URL or IF status inferred from a batch or profile | Require exact product-level source register row and manual evidence |
| RAG overclaim | Collision governance PASS reported as 21-question RAG PASS | Keep validator PASS separate from actual run result CSV |
| Knowledge bloat | Stage 6/7 evidence is copied into knowledge | Keep evidence in source/register/integrated layer until later reviewed export |
| Japanese style drift | Output becomes audit jargon or disclaimer-only | Check instructions, pass/fail criteria, expected samples, and real Preview outputs |
| URL-only overclaim | URL registration is treated as runtime document reading | Require explicit URL-only policy wording and separate runtime fetch design |

## Required Composer Response Format

Composer must use this structure after each stage.

```text
Stage:
Files inspected:
Files changed:
Proposed diff summary:
Validation run:
Validation results:
Upload target count:
Migration ledger rows:
Reference file count:
External-ready candidates:
Stale metadata remaining:
Direct-port risk:
Medical content changed: yes/no
Facility confirmation changed: yes/no
Quarantine changed: yes/no
Preview evidence changed: yes/no
RAG evidence changed: yes/no
PMDA/IF evidence changed: yes/no
Japanese answer-shape evidence changed: yes/no
URL-only overclaim checked: yes/no
Promotion dry-run performed: yes/no
Promotion apply performed: yes/no
Stop condition:
Next proposed stage:
```

If any validation fails, Composer must stop and report the failing rows or files. It must not patch around the failure by weakening the validator.

## Best Prompt To Give Composer 2.5

```text
You are maintaining a medical-safety RAG audit package. Treat this as source-governance and export-boundary work, not a bulk migration.

Repository root:
/Users/yusukefujinami/neurosurgery_pharm_algorithm

Authoritative package:
references/neurosurgery_qc_package

Reference corpora to audit and classify, not blindly port:
references/neurosurgery_safe_rag_pmda_product_source_register_resolved
references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603

Derived Custom GPT package:
references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package

Absolute rules:
1. Knowledge upload target remains only the 13 markdown files under derived/custom_gpt_knowledge_package/knowledge/.
2. Do not upload or copy PMDA corpus, gap v3 archive, manifests, audits, tests, scripts, or runbooks into Custom GPT Knowledge.
3. Do not add confirmed dose, interval, infusion rate, TDM, sampling time, IV compatibility, dialysis operation, order set, EHR trigger, or CDS production behavior.
4. Do not treat validation pass, review_ready, resolved, or ledger registered as clinical approval, facility confirmation, or external-ready.
5. Use integrated-first / derived-second. Do not expand derived knowledge before integrated governance exists.
6. Work one stage at a time. Stop after each stage.
7. Do not invent Preview outputs, RAG regression outputs, reviewer approvals, facility evidence, PMDA URLs, Interview Form URLs, or pass/fail decisions.
8. Do not run apply_preview_promotion.py --apply unless I explicitly approve a specific review_record_id and chunk_id after dry-run.

Current expected state to verify:
- CHILD file count: 366
- PARENT file count: 191
- reference migration ledger: 557 rows / 557 files
- custom_gpt_knowledge_package observed file count: 77
- knowledge upload target count: 13
- approved_preview_records: 0 unless real UI evidence was added
- promotion_candidate_rows: 0 unless real approved Preview records exist
- external_ready_candidates: 0
- collision RAG 21-question execution: pending unless actual result CSV is filled

Task for the next run:
Stage 5A evidence collection readiness only.

Do:
1. Re-run validators:
   - validate_upload_manifest.py
   - validate_unsafe_patterns.py
   - validate_quarantine_integrity.py
   - validate_reference_migration_ledger.py --corpus all
   - validate_facility_confirmation_status.py
   - validate_derived_export_candidate_ledger.py
   - validate_release_readiness.py
   - validate_gap_v3_review_ready.py
   - validate_collision_governance.py
   - validate_classification_vocabulary.py
   - validate_preview_protocol.py
   - validate_review_state_integrity.py
   - validate_pharmacist_red_flag_commit13.py
   - validate_final_audit_commit14.py
2. Regenerate the preview promotion candidate report.
3. Inspect tests/human_reviewed_preview_examples.md and confirm whether real raw Preview output exists.
4. Inspect audit/collision_rag_regression_results_PENDING.csv and confirm whether real RAG run evidence exists.
5. Prepare a precise operator checklist for collecting missing Preview and collision RAG evidence.
6. Audit whether the blueprint and supporting files specify accurate, natural Japanese answer shape:
   - instructions/custom_gpt_instructions.md
   - tests/pass_fail_criteria.md
   - tests/preview_test_protocol.md
   - tests/expected_answer_samples.md
   - tests/response_style_regression_assets.md
   - tests/human_reviewed_preview_examples.md
7. Confirm explicitly that URL registration is operator-side routing evidence, not runtime PMDA fetch.
8. Stop.

Do not:
1. edit knowledge/*.md
2. mark any Preview record approved
3. mark any facility row confirmed
4. create PMDA/IF URLs
5. run apply_preview_promotion.py --apply
6. claim release readiness
7. claim that URL registration alone is enough for accurate clinical output
8. claim that Japanese output quality has been empirically validated without real Preview approvals

Report using:
Stage:
Files inspected:
Files changed:
Validation results:
Upload target count:
Migration ledger rows/reference file count:
Approved Preview records:
Promotion candidates:
External-ready candidates:
Collision RAG evidence status:
PMDA/IF evidence status:
Japanese answer-shape status:
URL-only policy status:
Blockers:
Stop condition:
Next proposed stage:
```

## Completion Definition

This blueprint is complete only when Composer can follow it without ambiguity and without needing to infer medical facts.

The correct first success state is conservative:

1. upload target remains 13 knowledge files
2. reference ledger reports 557/557
3. old 174/540 metadata is reconciled where current-state wording is intended
4. validation passes
5. external-ready remains 0
6. no new clinical claims are introduced
7. all reference profile content remains reference-only unless reviewed through later integrated-first stages
8. Preview promotion remains blocked until real approved Preview records exist
9. collision RAG remains blocked until the 21-question run has actual evidence rows
10. PMDA/IF work remains evidence registration, not knowledge export
11. Japanese output quality is specified by instructions and rubrics, but remains empirically unvalidated until real Preview outputs are approved
12. URL registration remains an operator-side primary-source routing aid, not a guarantee of runtime document reading or clinical correctness
