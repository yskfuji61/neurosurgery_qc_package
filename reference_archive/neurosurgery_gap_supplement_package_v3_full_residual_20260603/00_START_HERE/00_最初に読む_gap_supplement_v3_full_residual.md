# Neurosurgery Safe RAG Gap Supplement V3 Full Residual（20260603）

このパッケージは、V2で補完済みの急性期脳梗塞、SAH術後血管攣縮、神経集中治療、慢性期脳血管障害、頭部外傷後遺症、historical / negative note に加えて、V2監査で残った追加漏れを補うV3統合パッケージである。

## V3で追加した主領域

1. 脳腫瘍・神経腫瘍薬物療法
2. 下垂体・間脳下垂体疾患薬
3. 脳室炎・シャント感染・脳室内投与系note
4. SAH血管攣縮の血管内治療・局所投与note
5. 造影剤・術中可視化薬・手技関連薬
6. 痙縮・機能的脳神経外科薬
7. CSF/IIH関連薬
8. 支持療法・誤回答防止note

## 重要な限界

これはPMDA製品単位解決済みパッケージではない。販売名、規格、添付文書URL、RMP、IF、患者向医薬品ガイド、審査報告書、再審査報告書、販売中止・経過措置・薬価削除は、推測で埋めず UNRESOLVED_DO_NOT_GUESS とした。

## 使い方

- `09_MANIFESTS/neurosurgery_gap_drug_supplement_master_V3_ALL.csv` を統合候補の全体台帳として使う。
- `01_SOURCE_REGISTERS/pmda_product_source_register_v3_residual.csv` をPMDA製品単位解決作業の入力にする。
- `02_DRUG_PROFILES_SAFE_KNOWLEDGE/` のMarkdownはRAG投入前の人間監査対象である。
- `08_VALIDATION_CHECKS/v3_residual_rag_safety_tests.csv` で誤回答テストを行う。
