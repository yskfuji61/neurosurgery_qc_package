---
drug_key: clazosentan
japanese_name: クラゾセンタンナトリウム
english_name: clazosentan sodium
generic_name: clazosentan sodium
synonyms: "ピヴラッツ|Pivlaz|endothelin receptor antagonist"
drug_class: エンドセリン受容体拮抗薬・SAH術後脳血管攣縮薬
domain: sah_vasospasm
priority: S
gap_type: complete_absent
pmda_product_level_verified: false
source_status: primary_verified_pending_pharmacist
knowledge_layer_status: custom_gpt_safe_boundary_only
human_review_required: true
facility_confirmation_required: true
operator_side_required: true
last_source_check_date: 2026-06-05
---

# クラゾセンタンナトリウム（clazosentan sodium）

## 1. この薬剤を追加する理由
2020年代以降のSAH術後血管攣縮管理で重要度が高い。肝機能・肺水腫/体液貯留・対象患者選択の確認が必要。

## 2. Safe RAGで許可する回答範囲
このファイルは、処方指示、投与量決定、禁忌判定の自動化、院内プロトコル代替には使わない。回答してよいのは、次の範囲に限定する。

- 脳外・脳卒中・神経集中治療における薬剤の位置づけ
- 既存Vaultで漏れていた理由と補完すべき文脈
- 薬剤師・医師が確認すべき安全論点
- PMDA製品単位確認、院内採用品確認、施設プロトコル確認が必要であること
- 他薬剤・他疾患文脈との混同を避けるための注意喚起

## 3. 禁止する回答

- 患者個別の投与可否を断定する
- 用量・投与速度・投与期間を、最新添付文書や院内プロトコル確認なしに確定する
- 国内薬事、保険、院内採用を未確認のまま「使える」と表現する
- 同じカテゴリの薬剤を同等薬として機械的に置換する
- 出血、腎機能、肝機能、意識障害、画像所見、手術前後、感染症、妊娠授乳などの確認を省略する

## 4. 薬剤師・医師レビュー必須チェック

- 最新のPMDA添付文書、RMP、インタビューフォーム、審査報告書を確認したか
- 院内採用品、剤形、規格、採用中止、供給制限を確認したか
- 疾患文脈が一致しているか。例：急性期脳梗塞、SAH術後血管攣縮、TBI、髄膜炎、ICU鎮静など
- 禁忌、慎重投与、腎機能・肝機能、出血リスク、相互作用、検査値監視を確認したか
- 施設内プロトコル、診療科方針、医師指示、保険適用、レセプト査定リスクを確認したか

## 5. RAG回答時の安全テンプレート

この薬剤について回答する場合は、原則として次の順番で答える。

1. 「この薬剤はsah_vasospasm文脈で重要だが、製品単位のPMDA確認と院内採用品確認が未完了」と明示する。
2. 適応・位置づけは、疾患文脈とセットで説明する。
3. 他剤との置換可能性を断定せず、違いを確認する。
4. 患者個別判断では、医師指示、画像所見、発症時刻、出血リスク、腎肝機能、併用薬を確認するよう促す。
5. 最新添付文書・院内プロトコルの確認が必要と締める。

## 6. 主な参照ソース
- JSTS_STROKE_GL_2021_REV2025: 脳卒中治療ガイドライン2021〔改訂2025〕  \
  URL: https://www.jsts.gr.jp/img/guideline2021_kaitei2025_kaiteikoumoku.pdf  \
  使用箇所: SAH遅発性脳血管攣縮薬（クラゾセンタン、ファスジル、オザグレル）およびrt-PA等の脳卒中急性期項目の根拠確認  \
  限界: 改訂項目PDFであり全文全章ではない。実運用では最新版本文・添付文書・院内採用品を併用確認。
- PMDA_CLAZOSENTAN_PIVLAZ_REVIEW: ピヴラッツ点滴静注液150mg 審査報告/関連資料  \
  URL: https://www.pmda.go.jp/drugs/2022/P20210112001/150923000_30400AMX00012_B100_1.pdf  \
  使用箇所: クラゾセンタンのSAH術後脳血管攣縮関連、安全性論点、対象患者制限の確認  \
  限界: 審査資料であり添付文書最新版ではない。肝機能・併用薬・年齢等は添付文書で再確認。

## 7. PMDA検索クエリ候補

```text
クラゾセンタンナトリウム OR clazosentan sodium OR clazosentan sodium OR ピヴラッツ|Pivlaz|endothelin receptor antagonist
```

## 8. 統合時の注意
このファイルはgap supplementであり、元Vaultの既存profileを無条件に上書きしない。既存薬剤と重複する場合は、`gap_type`、`priority`、`domain`、`source_status`を比較し、薬剤師レビューで昇格・統合・除外を決める。
