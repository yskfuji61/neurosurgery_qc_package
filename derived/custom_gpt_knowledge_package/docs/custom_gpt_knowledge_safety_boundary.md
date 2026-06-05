# Custom GPT Knowledge Safety Boundary

## Positioning

This document defines what may and may not be included in Custom GPT Knowledge for this package.

It is not a clinical guideline, prescription order, institutional procedure, or EHR/CDS specification.

## Allowed Knowledge Content

Custom GPT Knowledge may include:

- document positioning
- domestic regulatory confirmation status
- PMDA / MHLW / guideline source-register pointers
- unresolved items
- misread-prevention notes
- forbidden answer patterns
- conditions requiring specialist confirmation
- conditions requiring facility confirmation
- "not a clinical guideline"
- "not a prescription order"
- "not an institutional procedure"
- "not an EHR/CDS specification"
- LLM answer cautions

## Forbidden Knowledge Content

Custom GPT Knowledge must not include:

- dose tables
- dosing intervals
- infusion rates
- TDM targets
- sampling timing
- IV compatibility conclusions
- dialysis-specific concrete doses
- institutional formulary status
- inventory
- nursing operation
- EHR/CDS trigger conditions
- order sets
- override conditions
- individual physician prescribing decisions
- individual pharmacist inquiry decisions
- unapproved local operations

## Forbidden Answer Patterns

The LLM must not answer:

- この患者にはAを投与してください。
- Aが第一選択です。
- 禁忌ではないので使えます。
- 海外ガイドラインで推奨されているため、日本でも使用できます。
- 施設判断でよいです。
- この用量で開始してください。
- この速度で投与してください。
- この条件ならCDSを発火させてください。

## Recommended Answer Pattern

> Aは、Bの文脈で検討されることがある。ただし、実使用の可否は、国内電子添文、国内ガイドライン、患者背景、禁忌、腎機能・肝機能、相互作用、施設採用品、施設手順を確認して判断する。この文書だけで処方、投与、中止、再開、用量調整は判断しない。

## URL Register Boundary

URL registration is an operator-side routing aid. It does not guarantee that the Custom GPT reads PMDA, MHLW, or guideline URLs at answer time.

Runtime source fetch requires a separate tool/action design, validation, citation policy, failure handling, and human review.
