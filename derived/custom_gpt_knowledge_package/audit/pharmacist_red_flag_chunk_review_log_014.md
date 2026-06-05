# Pharmacist Red-Flag Chunk Review Log（Commit 14 前・repo-local 照合）

## 文書の位置づけ

この log は **Runbook Commit 14 前** に、quarantine 対象 8 chunk について [pharmacist_red_flag_review_checklist.md](pharmacist_red_flag_review_checklist.md) の red-flag 10 項目を **repo-local（`validate_unsafe_patterns.py` + 目視）** で照合した記録です。

| 区分 | 本 log | 薬剤師 sign-off |
| --- | --- | --- |
| 実施者 | Composer / repo worker（監査補助） | 施設薬剤師（未実施） |
| 効力 | red-flag 機械スキャン結果の記録 | clinical approval ではない |
| quarantine | **hold 維持**（`cleared` しない） | sign-off 後に `cleared` + evidence を register へ |

**将来（薬剤師レビュー後）:** 問題なければ `manifest/knowledge_quarantine_register.csv` で当該 `finding_id` を `quarantine_status=cleared`、`review_disposition=false_positive` または `mitigated`、`evidence_link` に本 log または薬剤師監査 ID を付与し、`validate_quarantine_integrity.py` を再実行する。

## 照合方法

1. 対象 knowledge ファイル全文を red-flag 10 項目で目視。
2. `tests/validate_unsafe_patterns.py`（upload 対象 13 本）— **2026-06-02 PASS**。
3. crosswalk / facility / export-candidate validators — active quarantine 中は `external_ready_candidate` 0。

## チャンク別結果（quarantine register 対応）

| finding_id | chunk | RF 領域 | repo-local red-flag 10 項 | 判定 | quarantine 維持理由 |
| --- | --- | --- | --- | --- | --- |
| Q13-03-summary-03 | 03 高リスク警告 | RF-SOURCE 他 | 0/10 該当（否定・確認要求のみ） | **hold** | Preview PREVIEW-001 未承認・薬剤師未署名 |
| Q13-05-summary-05 | 05 薬剤 | RF-DOSE, IV, TDM, INTERVAL | 0/10 該当（Commit 10 boundary は禁止形） | **hold** | Preview TEST-16–22 未実施・薬剤師未署名 |
| Q13-05-01-summary-05-01 | 05 実際の考え方 | 同上 | 0/10 該当 | **hold** | secondary layer・Preview 未記録 |
| Q13-06-summary-06 | 06 患者状態 | RF-RENAL, THRESHOLD | 0/10 該当（単一値→action 禁止明記） | **hold** | Preview TEST-16–19 未実施 |
| Q13-08-summary-08 | 08 閾値 | RF-THRESHOLD | 0/10 該当 | **hold** | 閾値解釈 Preview 未実施 |
| Q13-10-summary-10 | 10 施設運用 | RF-FACILITY | 0/10 該当（採用品断定なし） | **hold** | facility_confirmation pending |
| Q13-11-summary-11 | 11 CDS | RF-CDS | 0/10 該当（本番仕様・自動介入禁止） | **hold** | TEST-23 / TEST-CDS 未実施 |
| Q13-11-01-summary-11-01 | 11 実際の考え方 | RF-CDS | 0/10 該当 | **hold** | implementation gating Preview 未記録 |

### red-flag 照合メモ（共通）

- **項目 1–7:** 推奨用量・混注断定・単一検査値 action・TDM 目標・透析具体・CDS 自動化・採用断定 — knowledge 本文に **該当表現なし**（`validate_unsafe_patterns` 一致）。
- **項目 8:** README / 09 は sibling reference PMDA を TARGET 確定事実にしていない — **該当なし**。
- **項目 9:** 全 13 本 frontmatter で `human_review_required: true` 等 — **矛盾なし**。
- **項目 10:** `external_ready_candidate` **0 件** — **該当なし**。

## 薬剤師 sign-off 欄（未記録・テンプレート）

| field | 現状 | 薬剤師記入時 |
| --- | --- | --- |
| reviewer_role | unassigned | `pharmacist` |
| reviewer_identity | — | 施設内 ID |
| review_date | — | ISO 日付 |
| decision | **hold**（全 8 chunk） | `approve` / `reject` / `hold` per chunk |
| evidence_link | 本 log（repo-local のみ） | 薬剤師監査メモ ID |

## 結論

- **repo-local:** 高リスク chunk 8 件について、現行 knowledge 文言は red-flag 10 項目に **該当しない**（boundary export は禁止・確認形）。
- **運用上:** Preview evidence・薬剤師 sign-off・施設確認が未完了のため **quarantine は hold 維持が正しい**。`cleared` 行は追加しない。
- **Custom GPT UI upload:** 13 本の repo-local 境界は維持可能だが、**upload safe / external-ready / 統合完了の宣言は不可**。
