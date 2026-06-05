# Clinical Document Structure Standard

## Common Opening Boundary

Every drug or disease page should begin with this boundary:

> このページは、医療従事者向けのRAG / Custom GPT用安全境界資料である。診療ガイドライン、処方指示、施設内手順、電子カルテCDS仕様ではない。実患者への適用は、最新の電子添文、国内ガイドライン、施設採用品、薬剤部手順、診療科判断、施設承認を確認する。

## Drug Page Structure

1. このページでしてよいこと・してはいけないこと
2. 結論
3. 対象となる患者・病態
4. 使う場面
5. 使わない場面
6. 国内薬事・保険・施設採用の確認状況
7. 用法用量の扱い
8. 腎機能・肝機能で注意する点
9. 禁忌・原則避ける場面
10. 相互作用
11. モニタリング
12. 似た薬剤・似た病態との違い
13. 根拠
14. 限界・未確定事項
15. 施設確認事項
16. LLM回答時の注意
17. 最終更新日
18. 更新トリガー

## Disease Page Structure

1. このページでしてよいこと・してはいけないこと
2. 結論
3. 対象患者
4. 初期確認事項
5. 緊急時に確認する事項
6. 薬物治療候補
7. 使わない、または慎重に扱う治療
8. 国内ガイドライン・国内薬事との関係
9. 施設確認事項
10. 似た病態との違い
11. 根拠
12. 限界・未確定事項
13. LLM回答時の注意
14. 最終更新日
15. 更新トリガー

## Emergency Readability

- Separate emergency-facing information from background explanation.
- Put conclusion, contraindications, exclusions, confirmation items, and specialist-consult triggers near the top.
- Put long explanation later.
- Do not bury contraindications, cautions, or unresolved items inside prose.
- Use bullets or tables for branching conditions.
- Improve visibility for dose, route, time, lab value, and administration condition when these are allowed in source documents.
- Do not include concrete dose or infusion-speed values in Custom GPT Knowledge upload files.
