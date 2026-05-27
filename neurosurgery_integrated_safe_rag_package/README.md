# Neurosurgery Integrated Safe RAG Package

## Important Clinical and Licensing Notice

This package is a source-available, evaluation-only asset for medical-document RAG safety hardening, auditability, validation, and governance design. It is not open source software.

This package and its contents must not be treated as any of the following:

1. a formal clinical guideline
2. a prescription order
3. an institutional procedure
4. an immediately deployable EHR or CDS specification
5. a patient-care-ready medical AI asset
6. a commercially reusable RAG or LLM knowledge package

Without the Licensor's prior written permission, you may not use this package for:

1. commercial use
2. redistribution
3. public derivative publication
4. SaaS or API delivery
5. RAG service operation
6. embedding generation or vector database construction
7. LLM training, fine-tuning, benchmark construction, or evaluation dataset creation
8. medical AI product integration
9. hospital system, EHR, or CDS integration
10. institutional deployment or customer delivery

See the repository root [LICENSE](../LICENSE), [NOTICE](../NOTICE), and [COMMERCIAL_LICENSE.md](../COMMERCIAL_LICENSE.md) for the governing terms.

## これは何か

このパッケージは、脳神経外科領域の薬物治療関連文書を、そのまま診療や運用に使うためのものではなく、医療文書を RAG / LLM / 知識ベースへ投入する前に、安全境界、誤読リスク、監査可能性、ガバナンス要件を明示するための統合パッケージです。

これは「脳神経外科薬物治療そのものの正本」ではなく、以下のための source-available evaluation asset です。

1. 医療文書 RAG 安全化
2. 医療文書監査と validation
3. frontmatter と chunk の安全設計
4. negative knowledge の明示
5. CDS candidate の隔離と誤実装防止
6. upload bundle と RAG ingest governance の整備

## このパッケージの中核価値

このパッケージの価値は、単なる Vault 統合ではありません。主に次の構造化価値を含みます。

1. required keys を持つ frontmatter 設計
2. not_a_guideline、not_a_prescription_order、not_an_institutional_procedure、not_immediate_cds_specification を核にした境界設計
3. safety_principles に基づく誤読抑止
4. negative knowledge による危険な短絡の抑制
5. audit report、validation report、collision report を含む監査補助構造
6. upload bundles と RAG投入ガイドを含む ingest governance
7. CDS candidate を即時実装仕様から切り離す設計
8. 医療安全、薬事、保険、施設運用、承認を同一視しない表現設計

このため、本パッケージは、医療 AI プロダクト設計、病院 DX ガバナンス、医療文書ナレッジベース設計、RAG 安全化監査、商用医療 AI の内部評価に対して高い実務価値を持ちます。
ただし、その価値は著作者に留保されており、現行版では評価目的以外の利用は許可されていません。

## 想定読者

このパッケージは、主に以下の読者を想定しています。

1. 医療 AI 企業の安全設計担当
2. 病院 DX 担当、情報部門、医療安全担当
3. 薬剤部、看護部、委員会事務局の評価担当
4. 法務、知財、規制、ガバナンス担当
5. 採用担当、技術面接担当、プロダクト戦略担当
6. 医療文書の RAG / LLM 安全化を調査する研究者

## 統合されているもの

このパッケージは、以下の Vault を統合したものです。

1. Minimal Safety Knowledge Vault
2. Core Expansion Knowledge Vault
3. Priority Individual Notes Vault
4. Layer 2 Indexed Drug Vault
5. Validation Audit Operations Vault

## 主な追加物

1. `Integrated_Obsidian_Vault/`
2. `99_Exports/Unified_RAG/unified_safe_rag_seed.jsonl`
3. `99_Exports/Validation_Reports/yaml_frontmatter_required_keys_audit.csv`
4. `99_Exports/Validation_Reports/integrated_file_inventory.csv`
5. `99_Exports/Upload_Bundles/Custom_GPT_Project_Knowledge_RAG投入ガイド.md`
6. `90_Audit/Collision_Report.md`

## 何に使ってはいけないか

このパッケージは、README だけを読んだ段階でも、少なくとも以下には使ってはいけません。

1. 正式な診療ガイドラインとしての利用
2. 処方指示書としての利用
3. 施設内承認済み手順としての利用
4. 即時実装可能な電子カルテ / CDS 仕様としての利用
5. 患者診療における直接判断材料としての利用
6. 医療機関への未承認導入
7. 顧客向け納品物への組込み
8. 医療 AI 製品の即時知識ベース化
9. RAG サービスや LLM 学習用途への投入
10. vector DB、embedding、evaluation dataset、prompt library への転用

## 医療安全上の境界

このパッケージに含まれる情報は、臨床的に完成した推奨ではありません。
また、Integrated Safe RAG Package という名称は、患者ケアや院内本番運用にそのまま使えることを意味しません。

最終判断には、少なくとも以下が必要です。

1. 最新電子添文
2. 国内診療ガイドライン
3. 施設内採用品の確認
4. 薬剤部手順の確認
5. 夜間休日在庫の確認
6. 看護観察体制の確認
7. 委員会承認
8. 資格ある人間による最終レビュー

このパッケージの構造化内容、warning、negative knowledge、CDS candidate、audit 情報は、医療判断責任を代替しません。

## Source-Available / Evaluation-Only / Commercial Reservation

このパッケージは OSS ではありません。
現行版は、評価限定の source-available ライセンスで公開されています。

著作者の事前書面許諾なく、以下はすべて禁止されます。

1. 商用利用
2. 再配布
3. 派生物の公開又は配布
4. 顧客向け成果物への組込み
5. SaaS 化
6. API 化
7. RAG サービス化
8. embedding 生成
9. vector DB 化
10. LLM 学習
11. fine-tuning
12. benchmark 又は評価データセット化
13. prompt collection 化
14. knowledge base 化
15. 医療 AI 製品への組込み
16. 病院システム、電子カルテ、CDS への連携
17. 院内導入又は本番運用

商用利用、導入、共同開発、再配布、AI/RAG/LLM 利用、医療 AI 組込みを希望する場合は、repository root の [COMMERCIAL_LICENSE.md](../COMMERCIAL_LICENSE.md) を参照してください。

## 旧 Apache 2.0 版について

このパッケージの過去の一部版が Apache License 2.0 で配布されていた可能性があります。
その場合でも、現行版が Apache 2.0 であることを意味しません。

整理すると以下です。

1. 過去に Apache License 2.0 で適法に取得された特定の旧版については、その旧版に対する権利が直ちに遡及取消されるわけではありません
2. ただし、現行版および現行ライセンス付きで配布される版には、Apache 2.0 は適用されません
3. 境界と解釈は repository root の [NOTICE](../NOTICE) と [LICENSE](../LICENSE) を優先してください

## 差別化ポイント

このパッケージは、単なる medical prompt 集でも、単なる guideline summary でもありません。
差別化ポイントは以下です。

1. medical-document RAG safety hardening を主目的にしていること
2. negative knowledge を前面に出していること
3. not_to_interpret_as を構造的に持つこと
4. audit と validation の両方を package に含むこと
5. CDS candidate を候補として隔離していること
6. 医療安全、規制、保険、施設運用、承認を同一視しない設計であること
7. upload bundles と RAG ingest governance まで含めた統合パッケージであること

## 参考ファイル

1. `integration_manifest.json`
2. `Integrated_Obsidian_Vault/`
3. `Integrated_Obsidian_Vault/99_Exports/`
4. `Integrated_Obsidian_Vault/90_Audit/`
5. `Integrated_Obsidian_Vault/08_Negative_Knowledge/`
6. `Integrated_Obsidian_Vault/11_CDS_Candidates/`

## Related Repository-Level Documents

1. [LICENSE](../LICENSE)
2. [NOTICE](../NOTICE)
3. [COMMERCIAL_LICENSE.md](../COMMERCIAL_LICENSE.md)
4. [../README.md](../README.md)

## Contact

商用利用、共同開発、RAG/LLM 利用、病院導入、EHR/CDS 連携、再配布、派生物公開に関する問い合わせは、repository root の [COMMERCIAL_LICENSE.md](../COMMERCIAL_LICENSE.md) の窓口を参照してください。
