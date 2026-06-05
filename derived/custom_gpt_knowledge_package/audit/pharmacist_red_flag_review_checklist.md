# Pharmacist Red-Flag Review Checklist（Runbook Commit 13）

## 文書の位置づけ

この checklist は **derived Custom GPT package** の operator-side 薬剤師レビュー用 scaffold です。

- Custom GPT Knowledge upload 対象ではない。
- 診療ガイドライン・処方指示・施設内手順・EHR/CDS 本番仕様ではない。
- checklist 完了 ≠ 薬剤師承認済み clinical approval。

integrated 正本: `neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/90_Audit/Pharmacist_Red_Flag_Review_Checklist.md`

## 適用範囲（red-flag 必須 domain）

| domain_id | 内容 | 主な knowledge ファイル |
| --- | --- | --- |
| RF-DOSE | 用量・投与量の断定 | `knowledge/05_*`, `knowledge/07_*` |
| RF-INTERVAL | 固定間隔・反復投与 | `knowledge/05_*`, `knowledge/07_*` |
| RF-IV | IV compatibility / 調製 / 投与経路 | `knowledge/05_*`, `knowledge/07_*` |
| RF-TDM | TDM・濃度→action | `knowledge/05_*`, `knowledge/08_*` |
| RF-RENAL | eGFR/CrCl・透析具体 | `knowledge/06_*`, `knowledge/08_*` |
| RF-THRESHOLD | 閾値単独判断 | `knowledge/08_*` |
| RF-FACILITY | 採用品・在庫・手順の断定 | `knowledge/10_*` |
| RF-CDS | CDS 本番化・自動介入 | `knowledge/11_*`, `knowledge/12_*` |
| RF-SOURCE | 製品単位 PMDA / 一次資料欠落 | `knowledge/09_*` |

## Red-flag 項目（1 つでも該当 → hold）

1. 数値付き用量・投与間隔・投与速度が **推奨** として読める。
2. 混注・側管・同一ルートが **可否断定** されている（施設・添文確認なし）。
3. 単一検査値・単回バイタルから **投与・変更・中止** へ直結している。
4. TDM / トラフ / ピークだけで **増減・目標** が書かれている。
5. 透析・CRRT・AKI/CKD が **具体運用** として確定している。
6. CDS / アラートが **本番仕様・自動投与** として読める。
7. 採用品・在庫・夜間休日運用が **可用断定** されている。
8. sibling reference の PMDA 進捗を **解決済み** と user-facing に書いている。
9. `human_review_required` / `facility_confirmation_required` が frontmatter と矛盾する。
10. Preview evidence 未記録なのに `external_ready_candidate` へ昇格しようとしている。

## レビュー記録（薬剤師 sign-off 前はすべて pending）

| field | 必須状態 |
| --- | --- |
| `reviewer_role` | `pharmacist` または governance 委任者を **記録**（未記録のまま approve 禁止） |
| `reviewer_identity` | 監査ログまたは施設内 ID（generated text に創作しない） |
| `review_date` | ISO 日付 |
| `review_scope` | chunk_id / knowledge_file / section_id |
| `decision` | `approve` / `reject` / `hold`（人間のみ） |
| `source_scope` | PMDA 製品単位確認済み / class_note / 国内未販売 / pending |
| `facility_scope` | `confirmed` / `not_applicable` / `pending_facility_review` / `blocked` |
| `evidence_link` | `tests/human_reviewed_preview_examples.md` の record ID、または quarantine finding_id |

### Sign-off 状態（Commit 14 時点）

| 項目 | 状態 |
| --- | --- |
| repo-local red-flag 照合 | **済み** — [pharmacist_red_flag_chunk_review_log_014.md](pharmacist_red_flag_chunk_review_log_014.md)（8 chunk・10 項 0 該当） |
| 薬剤師 sign-off | **未記録**（`reviewer_role=unassigned`） |
| quarantine register | **hold 維持**（`cleared` 0 件 — sign-off 後に evidence 付きで更新） |
| package 全体 | **hold** — repo-local boundary export のみ可 |
| external-ready | **禁止**（active quarantine 8） |

## 承認前ゲート（すべて PASS 後のみ chunk 昇格）

1. [pass_fail_criteria.md](../tests/pass_fail_criteria.md) の must-not-have 0 件（Preview 実績がある family）。
2. [validate_unsafe_patterns.py](../tests/validate_unsafe_patterns.py) gate PASS。
3. [knowledge_quarantine_register.csv](../manifest/knowledge_quarantine_register.csv) で当該 chunk の active quarantine なし、または `cleared` + evidence。
4. [validate_facility_confirmation_status.py](../tests/validate_facility_confirmation_status.py) — `confirmed` は実 evidence 後のみ。
5. [validate_derived_export_candidate_ledger.py](../tests/validate_derived_export_candidate_ledger.py) — export candidate 誤昇格なし。

## 停止条件

- red-flag 該当 chunk を `cleared` にせず external-ready へ進めない。
- quarantine 未登録の reject / Preview fail を silent にしない。
- partial approval の範囲（file / section）を記録せずに approve しない。

## 関連 operator ファイル

- [unapproved_content_quarantine.md](unapproved_content_quarantine.md)
- [manifest/knowledge_quarantine_register.csv](../manifest/knowledge_quarantine_register.csv)
- [manifest/knowledge_chunk_review_crosswalk.csv](../manifest/knowledge_chunk_review_crosswalk.csv)
- [rag_export_audit_checklist.md](rag_export_audit_checklist.md)
