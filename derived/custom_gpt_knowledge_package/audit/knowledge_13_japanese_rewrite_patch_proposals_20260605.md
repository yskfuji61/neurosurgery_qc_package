# Knowledge 13 Japanese Rewrite Patch Proposals

No proposal in this file has been applied to `knowledge/*.md`. Each item is `PROPOSED_ONLY`.

## File: `knowledge/01_START_HERE_AND_POSITIONING.md`

### Proposal ID: JP-STYLE-01-001

- 対象箇所: `Integrated governance boundary export`
- 原文: `validation pass・ledger 登録は臨床承認・施設確定・upload safe ではない。`
- 問題点: 英語監査語が混在する。
- 医療安全上のリスク: `upload safe` が実行時安全性の保証に見える。
- 改稿案: `検証PASSや台帳登録は、臨床承認、施設確定、Knowledge投入可否の承認を意味しない。`
- 改稿してよい範囲: 監査語の日本語併記。
- 臨床意味変化リスク: low
- human_review_required: yes
- priority: high
- status: PROPOSED_ONLY

## File: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`

### Proposal ID: JP-STYLE-03-001

- 対象箇所: `negative knowledge`
- 原文: `negative knowledge`
- 問題点: 一般読者に意味が伝わりにくい。
- 医療安全上のリスク: 誤読防止情報の重要性が伝わらない。
- 改稿案: `誤読防止用の陰性知識（negative knowledge）`
- 改稿してよい範囲: 見出し・説明語の日本語併記。
- 臨床意味変化リスク: low
- human_review_required: yes
- priority: medium
- status: PROPOSED_ONLY

## File: `knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`

### Proposal ID: JP-STYLE-05-001

- 対象箇所: 抗菌薬関連 section
- 原文: `de-escalation`, `antibiogram`
- 問題点: 英語臨床語に日本語補足がない。
- 医療安全上のリスク: 抗菌薬の狭域化や施設感受性資料の確認軸が伝わりにくい。
- 改稿案: `抗菌薬の狭域化（de-escalation）`, `施設の薬剤感受性資料（antibiogram）`
- 改稿してよい範囲: 日本語補足の併記のみ。
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: PROPOSED_ONLY

## File: `knowledge/08_THRESHOLDS_AND_CONDITIONS.md`

### Proposal ID: JP-STYLE-08-001

- 対象箇所: `血清 Na・浸透圧・尿量`
- 原文: `必須です`
- 問題点: 何が必須かの範囲が強く読める。
- 医療安全上のリスク: 確認軸が処方条件に見える可能性。
- 改稿案: `確認漏れを避けるため優先的に確認する項目です。`
- 改稿してよい範囲: 確認軸としての言い換え。
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: PROPOSED_ONLY

## Emergency Quick Check Candidate

### Proposal ID: JP-EMERG-003-001

- 対象ファイル: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
- 改稿案:
  - `### 緊急時に先に確認すること`
  - 対象病態
  - 曝露薬
  - 最終服用・投与時刻
  - 検査値
  - 処置予定
  - 禁忌・除外条件
  - 施設採用品・在庫
  - 専門医または責任医確認
  - このKnowledgeだけで判断してはいけない事項
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: PROPOSED_ONLY
