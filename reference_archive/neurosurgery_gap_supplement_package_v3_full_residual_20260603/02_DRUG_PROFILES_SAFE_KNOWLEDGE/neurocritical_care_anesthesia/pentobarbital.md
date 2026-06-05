---
drug_key: pentobarbital
japanese_name: ペントバルビタール
english_name: pentobarbital
generic_name: pentobarbital
synonyms: "pentobarbital|barbiturate coma"
drug_class: バルビツレート・難治性ICP/難治性てんかん重積
domain: neurocritical_care
priority: B
gap_type: complete_absent
pmda_product_level_verified: false
source_status: primary_verified_pending_pharmacist
knowledge_layer_status: custom_gpt_safe_boundary_only
human_review_required: true
facility_confirmation_required: true
operator_side_required: true
last_source_check_date: 2026-06-05
---

# ペントバルビタール（pentobarbital）

## 1. この薬剤を追加する理由
海外/集中治療文献でバルビツレート昏睡として出る。国内採用・適応は別確認が必要。

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

1. 「この薬剤はneurocritical_care文脈で重要だが、製品単位のPMDA確認と院内採用品確認が未完了」と明示する。
2. 適応・位置づけは、疾患文脈とセットで説明する。
3. 他剤との置換可能性を断定せず、違いを確認する。
4. 患者個別判断では、医師指示、画像所見、発症時刻、出血リスク、腎肝機能、併用薬を確認するよう促す。
5. 最新添付文書・院内プロトコルの確認が必要と締める。

## 6. 主な参照ソース
- TBI_NEUROCRITICAL_REVIEW_2019: 頭部外傷の病態と治療  \
  URL: https://www.nms.ac.jp/sh/jmanms/pdf/015020071.pdf  \
  使用箇所: 重症頭部外傷ICP管理、浸透圧療法、鎮静・神経集中治療薬剤カテゴリの不足確認  \
  限界: 総説であり薬剤添付文書や国内ガイドライン最新版の代替ではない。

## 7. PMDA検索クエリ候補

```text
ペントバルビタール OR pentobarbital OR pentobarbital OR pentobarbital|barbiturate coma
```

## 8. 統合時の注意
このファイルはgap supplementであり、元Vaultの既存profileを無条件に上書きしない。既存薬剤と重複する場合は、`gap_type`、`priority`、`domain`、`source_status`を比較し、薬剤師レビューで昇格・統合・除外を決める。
