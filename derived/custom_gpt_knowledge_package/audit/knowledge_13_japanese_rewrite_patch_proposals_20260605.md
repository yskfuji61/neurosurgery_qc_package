# Knowledge 13 Japanese Rewrite Patch Proposals

**Summary:** Round 1: 5 proposals applied 2026-06-05. Round 2: 4 additional proposals applied 2026-06-05. Deferred items remain registered below. Knowledge bodies `01`, `03`, `05`, `08` only for direct edits.

See [JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md](JAPANESE_KNOWLEDGE_13_PATCH_APPLICATION_REPORT_20260605.md).

## File: `knowledge/01_START_HERE_AND_POSITIONING.md`

### Proposal ID: JP-STYLE-01-001

- 対象箇所: `Integrated governance boundary export`
- 原文: `validation pass・ledger 登録は臨床承認・施設確定・upload safe ではない。`
- 適用後: `検証PASSや台帳登録は、臨床承認、施設確定、Custom GPT Knowledgeへの投入承認、または実患者への使用可否を意味しない。`
- 臨床意味変化リスク: low
- human_review_required: yes
- priority: high
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## File: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`

### Proposal ID: JP-STYLE-03-001

- 対象箇所: role section; Integrated governance subheadings
- 原文: `negative knowledge`
- 適用後（clinician-facing）: `誤読を防ぐための注意事項（negative knowledge）`
- 適用後（audit subheadings）: `（誤読防止用の陰性知識 / negative knowledge）`
- 臨床意味変化リスク: low
- human_review_required: yes
- priority: medium
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-EMERG-003-001

- 対象ファイル: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
- 適用後: `## 緊急時に先に確認すること` ブロック（確認軸9項目＋非処方境界文）
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## File: `knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`

### Proposal ID: JP-STYLE-05-001

- 対象箇所: 抗菌薬関連 section
- 原文: `de-escalation`, `antibiogram`
- 適用後: `抗菌薬の狭域化（de-escalation）`, `施設・地域の薬剤感受性傾向をまとめた資料（antibiogram）`
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## File: `knowledge/08_THRESHOLDS_AND_CONDITIONS.md`

### Proposal ID: JP-STYLE-08-001

- 対象箇所: `血清 Na・浸透圧・尿量`
- 原文: `必須です`
- 適用後: `浸透圧療法や高張食塩液関連では、処方・投与判断の根拠ではなく、確認漏れを避けるために優先して確認する項目です。`
- 臨床意味変化リスク: medium
- human_review_required: yes
- priority: high
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

---

## Round 2 — 2026-06-05

### Proposal ID: JP-STYLE-01-002

- 対象ファイル: `knowledge/01_START_HERE_AND_POSITIONING.md`
- 内容: `operator-side 境界` → 運用者向けの安全境界；`upload safe` → Custom GPT Knowledgeへの投入承認
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-03-002

- 対象ファイル: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
- 内容: `shortcut` → `短絡（shortcut）`
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-05-002

- 対象ファイル: `knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md`
- 内容: `routine` 表現を一律運用・一律候補の日本語へ
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-08-002

- 対象ファイル: `knowledge/08_THRESHOLDS_AND_CONDITIONS.md`
- 内容: ICU以外運用可否の確認軸を明確化（検査値単独に見えないよう）
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## Deferred — not applied in round 2

| 対象 | 表現 | status | 理由 |
|------|------|--------|------|
| `knowledge/05` L120 | ICU 以外で routine 化 | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-05-002 スコープ外 |
| `knowledge/03` L76 | routine で扱わない | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-03-002 は shortcut のみ |
| `knowledge/04` | 中核 | DEFERRED_HUMAN_REVIEW_REQUIRED | 直接本文修正対象外 |
| `knowledge/09` | routine | DEFERRED_HUMAN_REVIEW_REQUIRED | 直接本文修正対象外 |
| `knowledge/13` | release readiness | DEFERRED_HUMAN_REVIEW_REQUIRED | 直接本文修正対象外 |
| 略語初出説明 | — | DEFERRED_HUMAN_REVIEW_REQUIRED | 一括反映は別フェーズ |
| Emergency Quick Check | 他ファイル展開 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
