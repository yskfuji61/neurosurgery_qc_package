# VS Code / Cursor Agent 統合指示

## 目的
既存Vaultへgap supplementを統合する。ただし、元ファイルを破壊的に上書きしない。

## 手順
1. 元Vaultとこのsupplementを同じworkspaceに置く。
2. `python scripts/apply_gap_supplement.py --vault <元Vault> --supplement <このsupplement>` を実行する。
3. `_PROPOSED_WITH_GAP_SUPPLEMENT.csv` を薬剤師がレビューする。
4. PMDA製品単位URL、販売名、剤形、規格、製造販売業者を手動確認する。
5. Custom GPT投入前に `08_VALIDATION_CHECKS` の誤回答テストを実施する。

## Agentへの禁止事項
- PMDA URLを推測で埋めない。
- 添付文書確認前に用量を確定しない。
- 国内薬事・保険・院内採用品を未確認で「使用可能」と断定しない。
- gap supplementのprofileを臨床判断の根拠として単独利用しない。
