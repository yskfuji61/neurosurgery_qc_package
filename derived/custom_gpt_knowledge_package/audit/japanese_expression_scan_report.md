# Japanese Expression Scan Report

## Scope

Scan target:

- `references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package`
- `references/neurosurgery_qc_package/derived/composer25_custom_gpt_update_blueprint_20260605.md`

Search terms:

`標準的`, `第一選択`, `第一選択級`, `必須`, `必須級`, `中核`, `国内重要`, `使用文脈`, `施設判断`, `安全情報`, `推奨`, `考慮`, `禁忌ではない`, `有効性が示唆`, `海外では推奨`, `通常使用可`, `投与すべき`, `使用できる`, `適応あり`, `保険上認められる`

## Summary

Many hits are intentional must-not-have examples, audit labels, or safety-boundary phrases. They should not be mechanically rewritten.

No automatic clinical-content rewrite was performed in this pass.

## Representative Findings

| File | Expression | Context | Risk | Auto rewrite | Human review |
|---|---|---|---|---|---|
| `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md` | 標準候補 / 推奨 | Warning not to infer standard candidate or recommendation from drug name | Low; used as negative knowledge | no | no |
| `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md` | 適用外使用を標準治療・推奨として一般化しない | Explicit prohibition | Low; protective wording | no | no |
| `knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md` | 標準的な治療薬プロファイルではない | Boundary statement for contrast/visualization | Low; protective wording | no | no |
| `knowledge/04_DISEASE_NOTES.md` | 中核ノート | May be read as clinical centrality if isolated | Medium | no | yes |
| `knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md` | 第一選択薬リストではない | Protective wording | Low | no | no |
| `knowledge/08_THRESHOLDS_AND_CONDITIONS.md` | 必須です | Could sound mandatory without context | Medium | no | yes |
| `tests/preview_test_protocol.md` | 推奨 | Mostly appears in must-not-have or review-record suggestions | Low to medium | no | review if promoted |
| `audit/collision_rag_regression_results_PENDING.csv` | 全例推奨 / 第一選択 | Unsafe test prompts | Low; intentionally adversarial | no | no |
| `scripts/_apply_stage4_knowledge_boundary_export.py` | 標準治療・推奨 | Historical helper script with embedded safety text | Low; not upload target | no | no |
| `composer25_custom_gpt_update_blueprint_20260605.md` | 推奨 / 標準 | Describes avoided expressions | Low; operator-side | no | no |

## Required Handling

1. If the phrase appears as a prohibited answer example, leave it unchanged.
2. If the phrase appears in a user-facing knowledge paragraph and could imply clinical recommendation, register it in `japanese_expression_risk_ledger.csv`.
3. If clinical meaning could change, do not auto-rewrite.
4. If the phrase is in tests or adversarial prompts, do not rewrite unless the test intent is unclear.

## Current Decision

- automatic_rewrites_performed: 0
- clinical_content_changed: no
- human_review_required_for_selected_hits: yes
- custom_gpt_upload_target_changed: no

## Knowledge 13 Follow-Up

The follow-up scan for the 13 Knowledge files found three broad classes:

1. Protective wording or prohibited-answer examples that should remain unchanged unless a reviewer approves clearer Japanese.
2. Audit/English terms that can be made easier to read by Japanese parenthetical explanation.
3. Strong expressions that require human review before any direct Knowledge rewrite.

New tracking artifacts:

- `japanese_plain_language_rewrite_ledger.csv`
- `abbreviation_first_use_review_ledger.csv`
- `knowledge_13_japanese_rewrite_patch_proposals_20260605.md`
- `japanese_medical_output_quality_preview_tests.md`

No direct Knowledge rewrite was performed.
