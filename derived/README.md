# Derived Packages

このディレクトリは、`references/neurosurgery_qc_package/` 配下の source corpus そのものではなく、その source から再構成した derived packages を置くための領域です。

## 運用ルール

1. source of truth は `../` 配下の source corpus と integrated package に置きます。
2. この配下の package は source を直接編集せず、source traceability を残した再輸出物として扱います。
3. OpenAI Custom GPT への upload target や operator-side tests / audit files は、各 derived package の README と manifest に従って確認します。
4. source path を持つ manifest は、package の物理配置ではなく repo 上の source traceability metadata として維持します.

## GPT Drug Data Policy Expansion

将来の薬剤データ、臨床データ参照、CDS 境界拡張は、[gpt_drug_data_policy_expansion_runbook.md](gpt_drug_data_policy_expansion_runbook.md) に従い、integrated-first / derived-second で進めます。

各 commit stage の export eligibility、manifest/test/audit 更新、validation gate、人間レビュー gate は、[custom_gpt_knowledge_package/manifest/future_policy_integration_matrix.md](custom_gpt_knowledge_package/manifest/future_policy_integration_matrix.md) で確認します。

runbook は基準方針文書、matrix は stage ごとの operator-side control sheet であり、いずれも source corpus そのものでも Custom GPT Knowledge upload target でもありません。
