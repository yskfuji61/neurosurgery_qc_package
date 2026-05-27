# neurosurgery_qc_package

## 重要

このリポジトリ名およびパッケージ名は `neurosurgery_qc_package` ですが、これを「そのまま使える QC 済み正本」と解釈してはいけません。

このリポジトリは、脳神経外科領域の知識VaultとRAG投入用成果物を品質確認済みの形で束ねた公開参考パッケージです。以下のいずれとしても扱ってはいけません。

1. 正式な診療ガイドライン
2. 正式な処方指示
3. 正式な施設内手順
4. 即時実装可能な電子カルテ / CDS 仕様

さらに、次の安全原則を外して利用してはいけません。

1. 公開参考資料を施設内ガイドラインとして扱わない
2. 候補を処方指示として扱わない
3. 薬剤名だけで標準候補と判断しない
4. 疾患名だけで薬剤選択しない
5. 国内薬事・保険・施設運用をエビデンスと同一視しない
6. 診療支援候補を即時実装仕様として扱わない

最終判断には、最新電子添文、国内診療ガイドライン、施設内採用品、薬剤部手順、夜間休日在庫、看護観察体制、委員会承認、人間による最終レビューが必要です。

実体の説明と収録物は [neurosurgery_integrated_safe_rag_package/README.md](neurosurgery_integrated_safe_rag_package/README.md) を参照してください。

## License and Commercial Use

このリポジトリは OSS ではありません。現行版は、評価限定の source-available ライセンスで公開されています。

著作者の事前書面許諾なく、以下を行ってはいけません。

1. 商用利用
2. 再配布
3. 派生物の公開又は配布
4. SaaS 化、API 化、RAG サービス化
5. embedding 生成、vector DB 化、LLM 学習、fine-tuning、評価データセット化
6. 医療 AI 製品、院内システム、電子カルテ、CDS への組込み

詳細は [LICENSE](LICENSE)、[NOTICE](NOTICE)、[COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) を参照してください。

過去に Apache License 2.0 で配布された特定の旧版がある場合、その旧版に対して有効に取得された権利は遡及的には取り消されません。境界は [NOTICE](NOTICE) を参照してください。