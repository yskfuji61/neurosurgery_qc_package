# Derived Packages

このディレクトリは、`references/neurosurgery_qc_package/` 配下の source corpus そのものではなく、その source から再構成した derived packages を置くための領域です。

## 運用ルール

1. source of truth は `../` 配下の source corpus と integrated package に置きます。
2. この配下の package は source を直接編集せず、source traceability を残した再輸出物として扱います。
3. OpenAI Custom GPT への upload target や operator-side tests / audit files は、各 derived package の README と manifest に従って確認します。
4. source path を持つ manifest は、package の物理配置ではなく repo 上の source traceability metadata として維持します.
5. reference repo 全ファイルの扱いは、各 file を無批判に copy することではなく、`custom_gpt_knowledge_package/manifest/reference_migration_decision_ledger.csv` で 1 file 1 migration decision として管理します。
6. 施設確認状態は `custom_gpt_knowledge_package/manifest/facility_confirmation_status_ledger.csv` で chunk ごとに管理し、実 evidence がない row を `confirmed` または `not_applicable` として扱ってはいけません。
7. derived export 候補は `custom_gpt_knowledge_package/manifest/derived_export_candidate_ledger.csv` で別管理し、source traceability と human-review status が揃わない row を export candidate にしてはいけません。
8. integrated-origin の再分類状態は `custom_gpt_knowledge_package/manifest/integrated_origin_reclassification_summary.csv` で要約し、adapted_port を derived export や external-ready の自動承認として扱ってはいけません。

## GPT Drug Data Policy Expansion

将来の薬剤データ、臨床データ参照、CDS 境界拡張は、[gpt_drug_data_policy_expansion_runbook.md](gpt_drug_data_policy_expansion_runbook.md) に従い、integrated-first / derived-second で進めます。

各 commit stage の export eligibility、manifest/test/audit 更新、validation gate、人間レビュー gate は、[custom_gpt_knowledge_package/manifest/future_policy_integration_matrix.md](custom_gpt_knowledge_package/manifest/future_policy_integration_matrix.md) で確認します。

runbook は基準方針文書、matrix は stage ごとの operator-side control sheet であり、いずれも source corpus そのものでも Custom GPT Knowledge upload target でもありません。

`custom_gpt_knowledge_package` では、Preview 実績が `tests/human_reviewed_preview_examples.md` に記録される前に promotion helper を実行してはいけません。approved Preview evidence がある場合だけ `tests/report_preview_promotion_candidates.py` で candidate row を確認し、`tests/apply_preview_promotion.py` を dry-run 後に 1 row ずつ apply します。reject または red-flag は `manifest/knowledge_quarantine_register.csv` で隔離し、repo-local pass と external-ready を混同しないでください。

同じく、`custom_gpt_knowledge_package` では `tests/validate_reference_migration_ledger.py` と `tests/validate_facility_confirmation_status.py` を operator-side gate として扱います。Preview approved は reference migration completeness や facility confirmation の代替ではありません。real Preview evidence または facility evidence がない chunk は `repo_local_only` / `pending_facility_review` のまま維持します。

`tests/validate_derived_export_candidate_ledger.py` は、`manifest/derived_export_candidate_ledger.csv` が `manifest/summary_layer_provenance.csv` の chunk coverage と export_candidate gate を壊していないことを確認する operator-side validator です。candidate ledger は Knowledge upload target ではなく、human review 未記録 row を external-ready へ進めないための管理表です。
