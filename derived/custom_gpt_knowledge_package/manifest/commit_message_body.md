# Commit Message

## Commit Title

Clarify operator-facing wording for derived package review docs

## Commit Body

4ファイル限定で derived Custom GPT package の operator-facing wording を整理し、Preview 実行環境と path 意味の誤読を防いだ。

Preview manual-only の説明は、package 配置の制約ではなく OpenAI Custom GPT UI 外の作業環境制約として明確化した。

あわせて tests/pass_fail_criteria.md では manifest 参照が package-relative document link であることを明確化し、audit/human_review_log_template.md では Updated files の package root relative 記録ルールと source_paths の repo-root-relative traceability metadata という意味を固定した。

今回は audit/rag_export_audit_checklist.md と instructions/custom_gpt_instructions.md を含む追加変更は行っていない。

package 全体で error は出ていない。
