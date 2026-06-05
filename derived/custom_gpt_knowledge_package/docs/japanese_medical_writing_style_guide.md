# Japanese Medical Writing Style Guide

## Positioning

This guide defines Japanese writing rules for neurosurgery pharmacotherapy RAG, Custom GPT Knowledge, operator-side review packets, and related medical safety documents.

It is not a clinical guideline, prescription order, institutional procedure, or EHR/CDS specification.

## Basic Style

Recommended pattern:

> Aは、Bの文脈で検討されることがある。ただし、実使用の可否は、C、D、Eを確認して判断する。この文書だけで処方、投与、中止、再開、用量調整を判断しない。

Avoid:

- AはBの標準治療である。
- Aを使用すべきである。
- Aが第一選択である。
- Aは禁忌ではないため使用できる。
- 施設判断で使用する。

## Strong-Wording Replacement Rules

Do not use the following words as clinical recommendations without context:

- 標準的
- 第一選択級
- 必須級
- 中核
- 国内重要
- 使用文脈あり
- 施設判断
- 安全情報
- 推奨
- 考慮

| Avoid | Recommended expression |
|---|---|
| 第一選択級 | ガイドラインまたは専門領域で主要な選択肢として扱われることがある。実使用の可否は、国内薬事、施設採用、患者条件を確認して判断する。 |
| 標準的 | 標準治療として扱われる文脈がある。ただし、適応、禁忌、患者条件、施設体制により可否が変わる。 |
| 必須級 | RAG上、誤回答防止のため優先的に整理すべき薬剤である。 |
| 中核 | 当該疾患・治療文脈で重要性が高い。実使用は添付文書、レジメン、施設手順で確認する。 |
| 施設判断 | 施設の承認済み手順、薬剤部手順、診療科責任医、必要に応じて委員会承認を確認して判断する。 |
| 安全情報 | RAG / Custom GPTで扱う安全境界情報。 |
| 海外では推奨 | 海外ガイドラインで言及されることがある。ただし、日本での国内薬事・保険・施設運用とは分けて確認する。 |

## Medical Safety Distinctions

Separate these concepts:

- 適応がある
- 使用経験がある
- ガイドラインに記載がある
- 国内承認がある
- 保険上認められる可能性がある
- 施設採用がある
- 院内手順で許容されている
- 禁忌ではない
- 安全に使える
- 有効性が示唆される
- 有効性が確立している

Required cautions:

- 「禁忌ではない」は「安全に使える」を意味しない。
- 「有効性が示唆される」は「有効性が確立している」を意味しない。
- 「海外ガイドラインで推奨」は「日本で通常使用可」を意味しない。
- 「施設判断」は「個人判断でよい」を意味しない。
- 「RAG上重要」は「臨床的に使用すべき」を意味しない。

## Notation Rules

- Use a half-width space between numbers and units when a value is allowed by the document type. Example: `500 mg`.
- Use consistent units: `mg`, `μg`, `mL`, `mEq`, `mmol/L`, `mg/kg`, `mL/hr`.
- Use these abbreviations consistently: `eGFR`, `CrCl`, `SCr`, `PT-INR`, `aPTT`, `DOAC`, `VKA`, `ICH`, `TBI`, `aSAH`.
- At first appearance, add Japanese explanation:
  - DOAC（直接経口抗凝固薬）
  - VKA（ビタミンK拮抗薬）
  - ICH（脳内出血）
  - TBI（外傷性脳損傷）
  - aSAH（動脈瘤性くも膜下出血）
- Use `腎機能低下時` as the base phrase.
- Use `肝機能障害` as the base phrase.
- Distinguish `中止`, `休薬`, `延期`, `再開`, and `再投与`.
- Distinguish `禁忌`, `投与不可`, `原則禁忌`, `慎重投与`, and `注意`.
- Use `禁忌` only when supported by an electronic label or clear contraindication source.
- If unavailable due to institutional operation, write `施設手順上、投与不可`.

## Review Rule

If a phrase could change clinical meaning, do not auto-rewrite it. Register it in `audit/japanese_expression_risk_ledger.csv` with `HUMAN_REVIEW_REQUIRED`.
