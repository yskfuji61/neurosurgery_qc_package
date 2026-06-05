# Stage 6C/D — 薬剤師 IF レビュー・attestation 手順

## 位置づけ

- **対象:** 製品単位 PMDA register（CHILD / gap supplement）。**knowledge 13 件は本手順の対象外。**
- **原則:** [05_PMDA_添付文書遵守と適用外使用ガバナンス.md](../../neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス.md) — 用法・用量は添付文書（電子添文）に従う。適用外は医師判断・施設規程。
- **Composer が行ったこと:** pmda.go.jp から IF URL を取得し register に記録（推測 URL なし）。
- **薬剤師が行うこと:** Review Packet で pmda.go.jp 照合 → attestation CSV 記入 → チャットで `C-00N 承諾`。

## ファイル

| 用途 | パス |
|------|------|
| 神外優先リスト | `STAGE6C_NEURO_PRIORITY_DRUG_LIST_20260605.csv` |
| バッチ割当 | `STAGE6C_BATCH_ASSIGNMENTS.json` |
| 薬剤師 attestation（CHILD） | `CHILD/11_PMDA_RESOLUTION_LOGS/pharmacist_pmda_product_attestation.csv` |
| 薬剤師 attestation（gap） | `gap/11_INTEGRATION_GUIDES/gap_pharmacist_pmda_product_attestation.csv` |
| バッチ Review Packet | `STAGE6C_BATCH_C-00N_REVIEW_PACKET.md` |
| バッチ manifest | `CHILD/09_MANIFESTS/pmda_pilot_batch_C-00N.md` |

## attestation 列の記入

| 列 | 記入 |
|----|------|
| `label_compliance_no_deviation` | 添文・RAG 境界と逸脱なし → `yes` / あり → `no` + `deviation_notes` |
| `if_reviewed` | IF URL を PMDA で確認 → `yes` |
| `guideline_insurance_scope_ok` | 当院運用の範囲で問題なし → `yes`（適用外のみ → `na` 可） |
| `formulary_match` | 当院採用リスト照合が必要な場合のみ `yes`/`no`。本プロジェクトは日本医療全般スコープのため通常 **`na`**（採用医薬品リストは重視しない） |
| `review_date` | レビュー日（YYYY-MM-DD） |

`not_clinical_approval` は常に `true`（臨床承認・upload safe ではない）。

## 承諾後（Composer / オペレーター）

1. `pmda_manual_review_required.csv` の `next_action` 更新（任意）
2. 14 validators 実行
3. `review_change_note.md` 追記

## 禁止

- `facility_confirmation_status_ledger` を evidence なしで一括 `confirmed`
- `external_ready` / Preview 承認 / collision `export_status` 変更
- IF 用量を knowledge に転記
