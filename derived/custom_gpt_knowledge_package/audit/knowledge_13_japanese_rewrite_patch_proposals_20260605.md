# Knowledge 13 Japanese Rewrite Patch Proposals

**Summary:** Rounds 1–4 applied 2026-06-05. Round 5: 2 proposals applied 2026-06-05. Deferred items remain registered below. Knowledge bodies `01`, `09` for round 5 direct edits only.

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

---

## Round 3 — 2026-06-05

### Proposal ID: JP-STYLE-01-003

- 対象ファイル: `knowledge/01_START_HERE_AND_POSITIONING.md`
- 内容: `upload 可否` → Custom GPT Knowledgeへの投入可否；Reference corpora / reference-only / hold の日本語補足
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-03-003

- 対象ファイル: `knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md`
- 内容: rFVIIa 節 `routine` → `一律の候補として扱わない`
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-04-001

- 対象ファイル: `knowledge/04_DISEASE_NOTES.md`
- 内容: VTE 節 `中核ノート` → 重要な確認ノート（実使用は別途確認）
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-09-001

- 対象ファイル: `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md`
- 内容: TICH-2 節 `routine` → 海外資料を国内一律運用に直結させない
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-13-001

- 対象ファイル: `knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md`
- 内容: `release readiness` → 公開可能状態（release readiness）＋境界文補強
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

---

## Round 4 — 2026-06-05

### Proposal ID: JP-STYLE-01-004

- 対象ファイル: `knowledge/01_START_HERE_AND_POSITIONING.md`
- 内容: sibling / reference corpus / source register → PMDA参考資料群・出典登録作業の日本語補足
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-04-002

- 対象ファイル: `knowledge/04_DISEASE_NOTES.md`
- 内容: antibiogram 未確認の一律化 → 施設・地域感受性資料（antibiogram）の日本語補足
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-09-002

- 対象ファイル: `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md`
- 内容: clinician-facing summary 見出し；source class / prescribing hierarchy の日本語補足
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-13-002

- 対象ファイル: `knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md`
- 内容: clinician-facing summary 見出し；package → Knowledge package（文書群）
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

---

## Round 5 — 2026-06-05

### Proposal ID: JP-STYLE-01-005

- 対象ファイル: `knowledge/01_START_HERE_AND_POSITIONING.md`
- 内容: pmda_resolved_count / register / repo-local、127薬剤候補リスト、derived export、統合ガバナンス見出し、CHILD/PARENT 台帳文の平易化
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-09-003

- 対象ファイル: `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md`
- 内容: caution/Evidence、guideline/trial/order、Sibling gap v3、antibiogram、policy boundary、source hierarchy、quarantine/unresolved、CHILD/PARENT の平易化
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## Deferred — not applied in round 5

| 対象 | 表現 | status | 理由 |
|------|------|--------|------|
| `knowledge/05` L120 | ICU 以外で routine 化 | DEFERRED_HUMAN_REVIEW_REQUIRED | スコープ外 |
| `knowledge/04` L225 | routine で固定化 | DEFERRED_HUMAN_REVIEW_REQUIRED | スコープ外 |
| `knowledge/04` L157 | 施設 antibiogram | DEFERRED_HUMAN_REVIEW_REQUIRED | round 5 は 09 L61 のみ |
| `clinician-facing summary` | 全13本横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 5 スコープ外 |
| `knowledge/01` L114 | Integrated policy boundary export 見出し | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-01-005 スコープ外 |
| `knowledge/09` L120 | Integrated governance boundary export | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-09-003 スコープ外 |
| `Integrated governance boundary export` | 他ファイル横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | 02–08, 10–13 本文修正対象外 |
| 略語初出説明 | — | DEFERRED_HUMAN_REVIEW_REQUIRED | 一括反映は別フェーズ |
| Emergency Quick Check | 他ファイル展開 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| 標準ページ構造 | 全面移行 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| Knowledge 13 文体統一 | — | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| `knowledge/13` / `04` | 追加校正 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 5 スコープ外 |

---

## Round 6 — 2026-06-05

### Proposal ID: JP-STYLE-09-005

- 対象ファイル: `knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md`
- 内容: `オーダー化` / `order化` を院内採用・処方指示・電子カルテ入力可否・オーダーセット登録へ分解；`facility confirmation` / `別管理` / `施設確認事項` を採用薬一覧等の個別確認文へ；`統合ポリシー上の安全境界` を混同注意点見出しへ；`Guideline と label の分離` をガイドライン記載と添付文書の混同防止へ；`quarantine / unresolved` を誤用防止の行動文へ；`source class` / `prescribing hierarchy` を資料の種類と処方優先順位の分離へ
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

### Proposal ID: JP-STYLE-01-007

- 対象ファイル: `knowledge/01_START_HERE_AND_POSITIONING.md`
- 内容: `統合ガバナンス上の安全境界` 見出しを `この資料の使用範囲と禁止事項` へ；`運用者向けの安全境界` を `運用者向けの位置づけと禁止事項` へ
- status: REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW
- review_date: 2026-06-05

## Deferred — not applied in round 6

| 対象 | 表現 | status | 理由 |
|------|------|--------|------|
| `knowledge/05` L120 | ICU 以外で routine 化 | DEFERRED_HUMAN_REVIEW_REQUIRED | スコープ外 |
| `knowledge/04` L225 | routine で固定化 | DEFERRED_HUMAN_REVIEW_REQUIRED | スコープ外 |
| `knowledge/04` L157 | 施設 antibiogram | DEFERRED_HUMAN_REVIEW_REQUIRED | スコープ外 |
| `clinician-facing summary` | 全13本横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 6 スコープ外 |
| `knowledge/01` L114 | Integrated policy boundary export 見出し | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-01-007 スコープ外 |
| `knowledge/09` L122 | Integrated governance boundary export | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-09-005 スコープ外 |
| `Integrated governance boundary export` | 他ファイル横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | 02–08, 10–13 本文修正対象外 |
| 略語初出説明 | — | DEFERRED_HUMAN_REVIEW_REQUIRED | 一括反映は別フェーズ |
| Emergency Quick Check | 他ファイル展開 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| 標準ページ構造 | 全面移行 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| Knowledge 13 文体統一 | — | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| `knowledge/13` / `04` | 追加校正 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 6 スコープ外 |
