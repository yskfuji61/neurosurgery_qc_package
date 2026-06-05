# Neurosurgery Safe RAG Gap Supplement Package

作成日: 2026-06-03

## 目的
このパッケージは、既存ZIP `neurosurgery_safe_rag_pmda_product_source_register_resolved(1).zip` に不足していた、脳外・脳卒中・神経集中治療で重要な薬剤を補うための追加パッケージです。

## 重要な結論
このパッケージは「完成済み処方データベース」ではありません。PMDA製品単位URL、販売名、製造販売業者、剤形、規格、院内採用品は未解決です。したがってCustom GPT/RAGに入れる場合は、回答範囲を安全境界・確認事項・薬剤位置づけに限定してください。

## 追加対象
- Sランク: エダラボン、オザグレル、ファスジル、クラゾセンタン、アルテプラーゼ、アルガトロバン
- Aランク: ウロキナーゼ、ニモジピン、ジアゼパム、ロラゼパム、フェノバルビタール、チオペンタール、チアミラール、ビタミンK、クリオプレシピテート、赤血球濃厚液、アンピシリン、セフォタキシム、トルバプタン、フルドロコルチゾン等
- Bランク: ICU/麻酔/感染/循環/電解質の補助薬剤

## ファイル構成
- `09_MANIFESTS/neurosurgery_gap_drug_supplement_master.csv`: 追加薬剤一覧
- `01_SOURCE_REGISTERS/pmda_product_source_register_gap_supplement.csv`: PMDA製品単位確認用source register
- `02_DRUG_PROFILES_SAFE_KNOWLEDGE/`: 追加薬剤profile
- `03_CLASS_NOTES/`: 領域別class note
- `08_VALIDATION_CHECKS/`: RAG誤回答テスト
- `12_RESEARCH_EVIDENCE/`: 参照ソース台帳
- `scripts/apply_gap_supplement.py`: 元Vaultへ統合する補助スクリプト

## 使用禁止
患者個別の投与可否、用量決定、禁忌判定、処方提案、院内手順の代替には使わないでください。


---

## V2追加内容

慢性期脳血管障害、脳循環代謝改善薬、頭部外傷後遺症、脳術後意識障害、historical/negative note、末梢循環薬との取り違え防止、ボセンタンとクラゾセンタンの取り違え防止を追加。
