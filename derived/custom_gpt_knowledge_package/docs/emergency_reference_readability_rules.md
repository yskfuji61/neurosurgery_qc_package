# Emergency Reference Readability Rules

## Purpose

This document defines readability rules for urgent-reference medical documents. It does not authorize emergency treatment, prescribing, dosing, or CDS implementation.

## Top-Of-Page Order

1. Scope and non-guideline boundary
2. Immediate orientation
3. Stop conditions
4. Must-confirm items
5. Specialist or facility contact triggers
6. Source and facility confirmation status
7. Background explanation

## Readability Rules

- Use short headings.
- Prefer bullets and compact tables for branching conditions.
- Do not hide "未確認", "禁忌", "原則避ける", or "施設確認" in long prose.
- Keep "can discuss as a candidate" separate from "can use".
- Keep emergency confirmation items separate from background pharmacology.
- Do not include concrete dose, infusion speed, TDM target, or CDS trigger values in Custom GPT Knowledge upload files.

## High-Risk Phrases

Avoid:

- すぐ投与する
- 第一選択として使う
- この条件で発火する
- 禁忌ではないため使用できる

Use:

- 緊急度が高い論点であり、患者状態、禁忌、国内電子添文、施設手順、専門職確認を分けて確認する。

## Emergency Quick Check Block

For high-risk Knowledge files, consider adding this block near the top after human review:

### 緊急時に先に確認すること

- 対象病態
- 曝露薬
- 最終服用・投与時刻
- 検査値
- 処置予定
- 禁忌・除外条件
- 施設採用品・在庫
- 専門医または責任医確認
- このKnowledgeだけで判断してはいけない事項

This block must not include dose, infusion speed, or CDS trigger conditions.

## Priority Files

Prioritize proposal review for:

1. `03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
2. `04_DISEASE_NOTES.md`
3. `05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`
4. `06_PATIENT_STATE_NOTES.md`
5. `07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md`
6. `08_THRESHOLDS_AND_CONDITIONS.md`
7. `11_CDS_CANDIDATE_BOUNDARIES.md`
