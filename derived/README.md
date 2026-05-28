# Derived Packages

このディレクトリは、`references/neurosurgery_qc_package/` 配下の source corpus そのものではなく、その source から再構成した derived packages を置くための領域です。

## 運用ルール

1. source of truth は `../` 配下の source corpus と integrated package に置きます。
2. この配下の package は source を直接編集せず、source traceability を残した再輸出物として扱います。
3. OpenAI Custom GPT への upload target や operator-side tests / audit files は、各 derived package の README と manifest に従って確認します。
4. source path を持つ manifest は、package の物理配置ではなく repo 上の source traceability metadata として維持します.
