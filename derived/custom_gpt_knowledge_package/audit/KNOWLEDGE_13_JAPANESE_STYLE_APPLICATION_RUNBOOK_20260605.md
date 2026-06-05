# Knowledge 13 Japanese Style Application Runbook

## Purpose

Bring the 13 Knowledge files closer to natural, readable, misread-resistant Japanese medical documents that can safely support Custom GPT answer behavior.

This runbook does not authorize clinical rewriting, dosing, prescribing, facility-operation claims, or release promotion.

## Target Files

1. `knowledge/01_START_HERE_AND_POSITIONING.md`
2. `knowledge/02_INDEX_AND_NAVIGATION.md`
3. `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
4. `knowledge/04_DISEASE_NOTES.md`
5. `knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`
6. `knowledge/06_PATIENT_STATE_NOTES.md`
7. `knowledge/07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md`
8. `knowledge/08_THRESHOLDS_AND_CONDITIONS.md`
9. `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md`
10. `knowledge/10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md`
11. `knowledge/11_CDS_CANDIDATE_BOUNDARIES.md`
12. `knowledge/12_AI_ERROR_TESTS_AND_VALIDATION.md`
13. `knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md`

## Order Of Work

1. Dangerous-expression scan.
2. Abbreviation first-use scan.
3. English clinical/audit term scan.
4. Emergency readability scan.
5. Candidate only: auto-rewrite-safe expressions.
6. Mark clinical-meaning changes as `HUMAN_REVIEW_REQUIRED`.
7. Reflect needed scenarios in Preview test cases.
8. Apply to Knowledge text only after human review.

## Auto-Rewrite Candidate Scope

Candidate expressions:

| Current expression | Candidate Japanese |
|---|---|
| operator-side | 運用者向け |
| boundary export | 安全境界の転記 |
| upload safe | Knowledge投入可否 |
| reference-only / hold | 参考資料扱い / 投入保留 |
| negative knowledge | 誤読防止用の陰性知識 |
| routine | 定型化 / 一律運用 |
| workflow | 運用フロー |
| order set | オーダーセット |
| reversal | 中和・拮抗・代替対応 |
| de-escalation | 狭域化 |
| antibiogram | 施設の薬剤感受性資料 |

If a replacement may change clinical meaning, do not rewrite automatically.

## Do-Not-Auto-Rewrite Scope

Do not automatically rewrite:

- indication
- dose
- dosing interval
- infusion rate
- use/non-use decision
- hold/stop/restart
- contraindication judgment
- renal/hepatic adjustment
- insurance
- formulary
- inventory
- nursing operation
- CDS trigger
- specialist consultation necessity

## Completion Criteria

Do not mark this work above `READY_FOR_HUMAN_REVIEW` until all are true:

1. dangerous-word scan completed
2. abbreviation definition gaps registered
3. English/audit terms registered
4. auto-rewrite candidates separated from human-review-required rows
5. Preview Japanese quality tests executed
6. human review records exist

## Current Status

READY_FOR_HUMAN_REVIEW. Not release ready.
