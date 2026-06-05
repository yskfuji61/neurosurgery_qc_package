# Japanese Medical Document Quality Audit

## Scope

This audit evaluates whether the package has operator-side rules for natural, accurate, misread-resistant Japanese medical documents.

## Scoring Axes

| Axis | Current evaluation | Main problem | Medical safety risk | Improvement policy | Completion condition | Human review |
|---|---|---|---|---|---|---|
| 自然な日本語 | Partly defined in instructions | Style rules were distributed across files | Audit jargon may leak into clinician-facing answers | Add style guide and templates | Preview examples approved by humans | yes |
| 医療文書としての正確性 | Strong safety boundary | URL registration may be overread | Users may think GPT reads PMDA at runtime | Add URL-only boundary | Runtime/fetch status explicitly stated | yes |
| 誤読されにくさ | Good negative knowledge | Strong terms need ledger | Recommendation-like terms may be overread | Add risk ledger | Reviewed or justified terms | yes |
| 情報到達性 | README and indexes exist | New docs need manifest registration | Operator may miss style rules | Add docs/templates and manifest rows | Manifest validator PASS | no |
| 見出し設計 | Knowledge files structured | Drug/disease templates absent | Future pages may drift | Add templates | New pages follow templates | yes |
| 表記統一 | Partly present | No central notation guide | Abbreviations and terms may vary | Add notation rules | Style review pass | yes |
| 現場実用性 | Safety-first | Facility checklist needed | Facility availability may be inferred | Add checklist template | Evidence-linked facility review | yes |
| 緊急時の参照性 | Present in tests | Not centralized | Critical cautions may be buried | Add emergency readability rules | Emergency sections follow structure | yes |
| Custom GPTでの検索適性 | 13-file target maintained | New docs are operator-side only | Accidental upload drift | Manifest rows set to no | Upload manifest PASS | no |
| LLM回答への転用適性 | Instructions strong | Transfer rules implicit | Source facts may become unsafe answers | Add transfer rules | Preview output review | yes |

## Overall Findings

### このまま医療従事者向け日本語文書として読ませてよいか

Operator-side review use is acceptable. Clinical-facing release still requires human review and Preview evidence.

### このままCustom GPT Knowledgeに入れてよいか

No new files in this pass should be uploaded to Knowledge. Knowledge upload target remains the existing 13 files only.

### Unified style rule

Use the pattern:

> Aは、Bの文脈で検討されることがある。ただし、実使用の可否は、国内電子添文、国内ガイドライン、患者背景、禁忌、腎機能・肝機能、相互作用、施設採用品、施設手順を確認して判断する。この文書だけで処方、投与、中止、再開、用量調整は判断しない。

### Highest-priority expression risks

1. Recommendation-like words such as `推奨`, `標準的`, and `第一選択`.
2. Ambiguous governance words such as `施設判断`.
3. Evidence-strength words such as `有効性が示唆される`.
4. Domestic applicability phrases such as `海外では推奨`.

## Final Audit Decision

READY_FOR_HUMAN_REVIEW
