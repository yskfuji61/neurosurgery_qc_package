# Neurosurgery Safe RAG Gap Supplement Package V2

作成日: 2026-06-03

## 目的

このV2は、前回の急性期脳梗塞、SAH術後脳血管攣縮、神経集中治療、抗発作、感染、止血・反転薬補完に加えて、慢性期脳血管障害、脳循環代謝改善薬、頭部外傷後遺症、脳術後意識障害、再評価・承認整理系のnegative note、末梢循環改善薬との取り違え防止を追加した統合パッケージである。

## 重要な設計判断

この領域の薬剤は、添付文書上の効能があること、現在販売されていること、現代ガイドラインで推奨されること、院内採用があること、処方すべきであることが一致しない。したがって、全薬剤を同じprofileとして扱わず、以下に分けた。

1. active_profile_candidate
2. active_profile_candidate_current_status_must_verify
3. historical_negative_note
4. do_not_confuse_note
5. current_status_high_risk_verify_before_use

## 絶対ルール

PMDA製品単位のURL、添付文書、IF、RMP、販売名、規格、製造販売業者は未解決のものを含む。RAG投入前に `01_SOURCE_REGISTERS/pmda_product_source_register_chronic_historical_supplement.csv` を使って製品単位確認を行うこと。
