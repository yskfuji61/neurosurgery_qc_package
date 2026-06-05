# Gap Supplement V2 Final Audit Report

作成日: 2026-06-03

## 結論

V2では、前回V1の36薬剤・noteに加えて、慢性期脳血管障害、脳循環代謝改善薬、頭部外傷後遺症、脳術後意識障害、再評価・承認整理系negative note、末梢循環薬との取り違え防止を追加した。

## 新規追加件数

- 新規追加 profile / note: 29 件
- V1既存 supplement: 36 件
- V2合計 supplement rows: 65 件

## 新規追加の内訳

- active_profile_candidate: 現役profile候補
- active_profile_candidate_current_status_must_verify: 現行販売・薬価・採用確認必須
- historical_negative_note: 旧薬・再評価・承認整理の誤回答防止
- do_not_confuse_note: 末梢循環薬やボセンタン等の取り違え防止

## 未解決事項

このパッケージはPMDA製品単位解決済みパッケージではない。販売名、規格、剤形、添付文書URL、IF、RMP、薬価、経過措置、販売中止、院内採用は人間が確認する必要がある。

## RAG投入時の最低条件

1. PMDA製品単位確認
2. 院内採用品確認
3. 保険適用・査定リスク確認
4. 現代ガイドライン上の位置づけ確認
5. historical/negative noteを処方推奨として出力しないテスト
