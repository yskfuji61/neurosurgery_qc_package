# Japanese Knowledge 13 Patch Application Report

**Date:** 2026-06-05  
**Scope:** Human-reviewed Japanese style patches to Knowledge `01`, `03`, `04`, `05`, `08`, `09`, `13`（round 3 で `04`/`09`/`13` を追加）。

## 1. 対象proposal

Round 1: JP-STYLE-01-001, JP-STYLE-03-001, JP-EMERG-003-001, JP-STYLE-05-001, JP-STYLE-08-001  
Round 2: JP-STYLE-01-002, JP-STYLE-03-002, JP-STYLE-05-002, JP-STYLE-08-002  
Round 3: JP-STYLE-01-003, JP-STYLE-03-003, JP-STYLE-04-001, JP-STYLE-09-001, JP-STYLE-13-001  
Round 4: JP-STYLE-01-004, JP-STYLE-04-002, JP-STYLE-09-002, JP-STYLE-13-002  
Round 5: JP-STYLE-01-005, JP-STYLE-09-003  
Round 6: JP-STYLE-09-005, JP-STYLE-01-007  
Round 7: JP-STYLE-09-006, JP-STYLE-01-008  
Round 8: JP-STYLE-01-009, JP-STYLE-09-007  
Round 9: JP-STYLE-01-010, JP-STYLE-09-008

## 2. 適用したpatch

| proposal_id | file | applied_status | reason |
|---|---|---|---|
| JP-STYLE-01-001 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | validator/ledger と Custom GPT投入承認・実患者使用可否の境界を明確化 |
| JP-STYLE-03-001 | knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | clinician-facing と audit 小見出しに日本語併記 |
| JP-EMERG-003-001 | knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 緊急時確認ブロックを冒頭近くに追加（非処方境界付き） |
| JP-STYLE-05-001 | knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | antibiogram / de-escalation の日本語併記（個別培養結果と分離） |
| JP-STYLE-08-001 | knowledge/08_THRESHOLDS_AND_CONDITIONS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 「必須」を確認項目説明へ言い換え（投与条件に見えないよう） |
| JP-STYLE-01-002 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | operator-side 境界・upload safe の日本語明確化 |
| JP-STYLE-03-002 | knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | shortcut → 短絡（shortcut） |
| JP-STYLE-05-002 | knowledge/05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | routine 表現を一律運用・一律候補へ（L92/L99） |
| JP-STYLE-08-002 | knowledge/08_THRESHOLDS_AND_CONDITIONS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | ICU以外運用可否の確認軸明確化 |
| JP-STYLE-01-003 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | upload 可否・Reference corpora・reference-only/hold の日本語明確化 |
| JP-STYLE-03-003 | knowledge/03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | rFVIIa 節 routine → 一律の候補として扱わない |
| JP-STYLE-04-001 | knowledge/04_DISEASE_NOTES.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | VTE 節 中核 → 重要な確認ノート（実使用は別途確認） |
| JP-STYLE-09-001 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | TICH-2 節 routine → 海外資料を国内一律運用に直結させない |
| JP-STYLE-13-001 | knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | release readiness 日本語補足＋境界文補強 |
| JP-STYLE-01-004 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | PMDA参考資料群・出典登録作業の日本語補足 |
| JP-STYLE-04-002 | knowledge/04_DISEASE_NOTES.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | antibiogram 日本語補足（L162；個別培養結果と分離） |
| JP-STYLE-09-002 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | clinician-facing 見出し；source class / prescribing hierarchy 日本語補足 |
| JP-STYLE-13-002 | knowledge/13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | clinician-facing 見出し；package → Knowledge package（文書群） |
| JP-STYLE-01-005 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 監査語・RAG語の平易化（作業進捗と承認の分離、台帳・派生成果物境界） |
| JP-STYLE-09-003 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 監査語・RAG語の平易化（Evidence・gap v3・出典分類・quarantine 等） |
| JP-STYLE-09-005 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | オーダー化・facility confirmation・安全境界・quarantine・source class の行動文化 |
| JP-STYLE-01-007 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 統合ガバナンス上の安全境界見出しを使用範囲と禁止事項へ；運用者向け安全境界を位置づけと禁止事項へ |
| JP-STYLE-09-006 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | guideline・manufacturer documents・summary の日本語化；Integrated governance 見出しを判断禁止事項へ |
| JP-STYLE-01-008 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | Integrated policy boundary export 見出しを使用範囲と禁止事項へ |
| JP-STYLE-01-009 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 統合Vault側・転記・派生成果物の平易化 |
| JP-STYLE-09-007 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 索引・GL見出し・エビデンス見出しの平易化 |
| JP-STYLE-01-010 | knowledge/01_START_HERE_AND_POSITIONING.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | reference・無断マージ・integrated/collision gate/operator 正本の平易化 |
| JP-STYLE-09-008 | knowledge/09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md | REVISED_AND_APPLIED_AFTER_HUMAN_REVIEW | 本文 Evidence → エビデンス統一；TICH-2・エビデンス節の自然化 |

## 3. 適用しなかったpatch

| proposal_id | file | status | reason |
|---|---|---|---|
| — | knowledge/05 L120 ICU 以外 routine 化 | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-05-002 スコープ外 |
| — | knowledge/04 L225 routine で固定化 | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-04-002 は L162 のみ |
| — | knowledge/04 L157 施設 antibiogram | DEFERRED_HUMAN_REVIEW_REQUIRED | JP-STYLE-04-002 スコープ外 |
| — | clinician-facing summary 全13本横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 5 スコープ外 |
| JP-STYLE-01-008 | knowledge/01 L122 Stage 4 見出し | NO_CHANGE_NEEDED_AFTER_REVIEW | Round 6（01-007）で既に日本語化済み |
| — | knowledge/09 L33 clinician-facing summary 見出し | DEFERRED_HUMAN_REVIEW_REQUIRED | round 7 スコープ外 |
| — | knowledge/09 L105 guideline（未確定事項節） | DEFERRED_HUMAN_REVIEW_REQUIRED | round 7 スコープ外 |
| — | knowledge/09 L111 Drug label source hierarchy 英語小見出し | DEFERRED_HUMAN_REVIEW_REQUIRED | round 7 スコープ外 |
| — | knowledge/01 L120 転記しません | DEFERRED_HUMAN_REVIEW_REQUIRED | round 8 スコープ外（禁止境界文） |
| — | knowledge/01 L87 Evidence（横断参照リスト） | DEFERRED_HUMAN_REVIEW_REQUIRED | round 9 スコープ外 |
| — | knowledge/09 L140 転記禁止境界文 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 8 スコープ外 |
| — | Integrated governance boundary export 他ファイル横断 | DEFERRED_HUMAN_REVIEW_REQUIRED | 02–13 本文修正対象外 |
| — | Knowledge 13 文体統一 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| — | knowledge/13 / 04 追加校正 | DEFERRED_HUMAN_REVIEW_REQUIRED | round 5 スコープ外 |
| — | abbreviation_first_use_review_ledger 一括反映 | DEFERRED_HUMAN_REVIEW_REQUIRED | 略語初出説明の本文挿入は別フェーズ |
| — | Emergency Quick Check 他ファイル展開 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| — | 標準ページ構造への全面移行 | DEFERRED_HUMAN_REVIEW_REQUIRED | 別フェーズ |
| — | plain language ledger 未レビュー GLOBAL 行 | NEEDS_REVIEW | round 5 外は据え置き |

## 4. 医療安全上の確認

- 用量を追加していない。
- 投与速度を追加していない。
- 投与間隔を追加していない。
- TDM目標を追加していない。
- 採血タイミングを追加していない。
- 混注可否を追加していない。
- 透析時具体用量を追加していない。
- 施設採用品、在庫、看護運用を確定していない。
- EHR/CDS発火条件を追加していない（否定境界文での言及のみ）。
- 処方指示、投与指示、休薬・再開指示を追加していない。
- validator PASS や台帳登録を臨床承認として扱っていない。
- 抗菌薬広域化・ICU運用の施設確定は追加していない（08-002 の看護観察体制・責任医・薬剤部は確認軸のみ）。
- ICU以外での運用可否を確定していない。
- 抗菌薬選択・広域化可否・狭域化実施条件を確定していない。
- VTE予防薬や抗凝固再開時期を確定していない（04-001 は確認ノート表現のみ）。
- 海外GL記載から国内一律運用・通常使用可への変換を追加していない。
- release ready、clinical approved、facility approved への昇格をしていない（13-001 は否定境界のみ）。
- PMDA参考資料群を Knowledge 本文の代替または一括投入対象にしていない（01-004）。
- 出典分類を処方優先順位に変換していない（09-002 は否定境界のみ）。
- clinician-facing summary の日本語化は見出し補足のみであり、臨床内容を変更していない（09-002 / 13-002）。
- 台帳登録や作業進捗を Custom GPT 投入承認・施設採用・実患者使用可否として扱っていない（01-005）。
- Evidence だけで施設採用品、処方、オーダー化を確定していない（09-003）。
- エビデンスだけで院内採用、処方指示、電子カルテ上の入力可否、オーダーセット登録を確定していない（09-005）。
- 採用薬一覧、薬剤部手順、委員会承認、電子カルテ薬剤マスタのいずれか一つだけで使用可否を判断していない（09-005）。
- CDS候補を本番仕様にしていない（09-005）。
- 内容確認なしに Knowledge へ転記することを許可していない（09-003）。
- ガイドライン記載だけで国内薬事、施設採用、EHR/CDS実装が確定したように見える回答や要約を作成していない（09-006）。
- 参考資料を、人間レビューなしに Knowledge へ直接取り込む対象にしていない（09-007）。
- 参考資料の一般名プロファイルから数値を推測・補完する表現を追加していない（01-010）。
- 疾患ノート本文へ、内容確認なしに統合することを許可していない（01-010）。
- エビデンスだけで院内採用、処方指示、電子カルテ上の入力可否、オーダーセット登録を確定していない（09-008；09-005 と整合）。

## 5. Knowledge upload target

- `upload_to_custom_gpt=yes` は **13 本固定**（増加なし）。
- 新規 docs/audit/tests/templates は `upload_to_custom_gpt=no`。
- 今回の patch は既存 Knowledge 本文の日本語補足・安全境界強化であり、upload target を増やさない。

## 6. 残存リスク

- Preview 実出力の承認は未完了。
- 医療従事者向け完成文書ではない。
- 施設内手順ではない。
- 処方支援文書ではない。
- 看護手順ではない。
- CDS 本番仕様ではない。
- 実患者への適用可否は、最新電子添文、国内ガイドライン、患者背景、施設採用品、施設手順、責任医・薬剤部確認が必要。
- Knowledge 13 本への日本語スタイル完全適用は未完了（05-L120、04-L225 routine、略語一括、Emergency 他ファイル展開、標準ページ構造全面移行は残存）。
- 略語初出説明の一括反映は未完了。
- 他ファイルへの Emergency Quick Check Block 展開は未完了。
- 薬剤別・病態別の標準ページ構造への全面移行は未完了。
- `clinician-facing summary` の全 13 本横断統一は未完了。
- Knowledge 13 本全体の文体統一は未完了。
- Preview 実出力の日本語品質承認は未完了。

## 7. Validator結果

**Run date:** 2026-06-05（repo-local；round 9 適用後に再実測）

| Validator | Result | Notes |
|---|---|---|
| validate_upload_manifest.py | PASS | upload_manifest_findings=0 |
| validate_japanese_expression_ledger.py | PASS | japanese_expression_ledger_findings=0 |
| validate_abbreviation_first_use_ledger.py | PASS | abbreviation_first_use_ledger_findings=0 |
| validate_plain_language_rewrite_ledger.py | PASS | plain_language_rewrite_ledger_findings=0 |
| validate_japanese_preview_quality_tests.py | PASS | japanese_preview_quality_tests_findings=0 |
| validate_unsafe_patterns.py | PASS | gate PASS; 09 L39/L99 否定境界 = REVIEW_CONTEXT；01 L129「統合しない」は新規 RED なし |
| validate_release_readiness.py | PASS | external_ready_candidates=0 |
| validate_review_state_integrity.py | PASS | review_state_findings=0 |

**Summary:** 8/8 PASS; `external_ready_candidates=0`; `upload_to_custom_gpt=yes` = 13 rows.

## 8. 最終判定

**READY_FOR_PREVIEW_TESTING**

（`release ready` / 臨床承認 / 施設確定ではない。Preview 実出力の日本語品質承認が次ゲート。）
