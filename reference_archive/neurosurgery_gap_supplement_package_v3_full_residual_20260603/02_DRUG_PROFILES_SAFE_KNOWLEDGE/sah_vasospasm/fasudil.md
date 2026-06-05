---
drug_key: fasudil
japanese_name: ファスジル塩酸塩
english_name: fasudil hydrochloride
generic_name: fasudil hydrochloride
synonyms: "エリル|fasudil|Rho kinase inhibitor"
drug_class: Rhoキナーゼ阻害薬・SAH術後脳血管攣縮薬
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

# ファスジル塩酸塩（fasudil hydrochloride）

## 1. この薬剤を追加する理由
SAH術後脳血管攣縮で国内実務上重要。低血圧・頭蓋内出血・投与期間の安全境界を個別化すべき。

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

## 7. PMDA検索クエリ候補

```text
ファスジル塩酸塩 OR fasudil hydrochloride OR fasudil hydrochloride OR エリル|fasudil|Rho kinase inhibitor
```

## 8. 統合時の注意
このファイルはgap supplementであり、元Vaultの既存profileを無条件に上書きしない。既存薬剤と重複する場合は、`gap_type`、`priority`、`domain`、`source_status`を比較し、薬剤師レビューで昇格・統合・除外を決める。
