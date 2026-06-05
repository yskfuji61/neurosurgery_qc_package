# Japanese Knowledge 13 Style Application Prework

## Scope

Target: the 13 files under `knowledge/`.

This prework records style-readiness issues before any direct rewrite of the Knowledge upload files. It does not approve clinical content, facility operation, prescribing, dosing, or release readiness.

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

## Current Structure

All 13 files have a stable title and section structure. Many files already contain a `clinician-facing summary` section and safety-boundary language. However, some section labels and embedded terms remain audit-oriented or English-heavy, for example `operator-side`, `boundary export`, `reference-only`, `hold`, `validation pass`, `clinician-facing summary`, and `negative knowledge`.

## Style Guide Application Status

The style guide is now defined, but the Knowledge 13 files have not been fully rewritten under it. This pass does not rewrite clinical content.

## Abbreviation Definition Gaps

Important abbreviations appear across the 13 files, including DOAC, VKA, ICH, TBI, aSAH, EVD, EVT, CDS, RAG, PMDA, RMP, TDM, PT-INR, aPTT, CrCl, eGFR, DAPT, VTE, CNS, CSF, IIH, ITB, DBS, DI, GL, and SOP.

Because Custom GPT retrieval can occur at chunk level, key abbreviations should be reviewed per file. Candidate definitions are tracked in `abbreviation_first_use_review_ledger.csv`.

## English Clinical And Audit Terms

Detected terms include `operator-side`, `boundary export`, `upload safe`, `reference-only`, `hold`, `negative knowledge`, `clinician-facing summary`, `source corpus`, `derived export`, `migration ledger`, `blind copy`, `routine`, `workflow`, `order set`, `reversal`, `de-escalation`, `antibiogram`, `shortcut`, `validation`, and `release ready`.

These are useful for audit precision but may reduce Japanese readability. Candidate rewrites are tracked in `japanese_plain_language_rewrite_ledger.csv`.

## Strong Expressions

Detected expressions include `標準候補`, `標準治療`, `標準的`, `第一選択`, `推奨`, `必須`, and `中核`. Many appear as prohibited-answer examples or protective boundary language. They should not be mechanically rewritten. File-specific rows are added to `japanese_expression_risk_ledger.csv`.

## Emergency Readability Gap

High-risk files do not yet have a consistent `緊急時に先に確認すること` block. Candidate blocks should be proposed before editing Knowledge text.

Priority files:

1. `03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
2. `04_DISEASE_NOTES.md`
3. `05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`
4. `06_PATIENT_STATE_NOTES.md`
5. `07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md`
6. `08_THRESHOLDS_AND_CONDITIONS.md`
7. `11_CDS_CANDIDATE_BOUNDARIES.md`

## Auto-Rewrite Candidate Scope

Candidate only:

- English/audit term with no clinical meaning change
- heading translation with English retained in parentheses
- safety-boundary explanation
- abbreviation definition

## Human Review Required Scope

Human review is required for anything affecting:

- indication
- dose
- interval
- administration speed
- use/non-use decision
- contraindication
- renal/hepatic adjustment
- insurance
- formulary
- facility operation
- CDS trigger
- specialist consultation

## Clinical Content Not Edited In This Pass

No drug candidate, disease candidate, dose, contraindication, insurance statement, facility adoption, procedure timing, restart/hold decision, or CDS condition was edited.
