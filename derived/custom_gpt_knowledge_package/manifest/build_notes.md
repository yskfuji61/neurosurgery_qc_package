# build_notes

## このファイルの役割

このファイルは、この derived package をどの source から、どの範囲で、どの安全方針に基づいて再構成したかを記録するための build log です。

## 走査したディレクトリ

1. `references/neurosurgery_qc_package/`
2. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/`
3. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/00_Index/`
4. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/02_Diseases/`
5. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/03_Drugs/`
6. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/04_Drug_Classes/`
7. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/05_Patient_States/`
8. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/06_Procedures/`
9. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/08_Negative_Knowledge/`
10. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/10_Operationalization/`
11. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/11_CDS_Candidates/`
12. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/12_Evidence/`
13. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/13_Thresholds_Conditions/`
14. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/90_Audit/`
15. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/91_AI_Error_Tests/`
16. `references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/99_Exports/`

## RAG 対象にしたファイル

1. 既存 4 本の Upload Bundle
2. package manifest / integration manifest / package README
3. negative knowledge の中核ファイル
4. CDS readiness と High Constraint Input Control 候補
5. Evidence checklist / facility checklist / AI error tests / audit templates
6. validation report と master CSV の一部

## RAG 対象外にしたファイル

1. `_extracted_sources/` 配下の生 source 一式
2. JSONL RAG seed
3. YAML masters
4. 施設別の確定値として誤読されうる情報源
5. 即時実装仕様と誤認されうる非承認データ

## 統合方針

1. OpenAI Custom GPT の Knowledge へアップロードする対象は `knowledge/` の 13 本だけに固定する。
2. 既存 4 本 bundle を、そのままではなく、疾患・薬効分類・患者状態・処置・閾値・Evidence・施設運用・CDS 境界・AI test・監査更新へ再分解する。
3. 既存 source の安全境界、陰性知識、監査思想を弱めない。
4. `Knowledge上は`、`要一次資料確認`、`要施設内確認`、`未確認` を使い分け、医療判断や処方指示に読める断定を避ける。
5. 監査語彙がそのまま表層回答へ漏れないよう、high-traffic knowledge files と instructions に clinician-facing な summary layer を追加する。

## 回答自然性レイヤーの方針

1. safety boundary は削除せず、答えの順番と表現を変える。
2. 一般整理質問では、自然な全体像を先に出す。
3. 高リスク薬剤や CDS 質問では、短い結論の直後に強い制約を出す。
4. 内部語は対外説明用の自然文へ言い換える。
5. clinician-facing summary は front matter の長文 key ではなく、本文冒頭の短い summary として追加する。
6. expected answer samples と response style regression assets を tests 配下に置き、自然化前後の差分を audit ではなく回答品質テストとして管理する。

## Preview review と provenance の方針

1. `tests/expected_answer_samples.md` は target answer shape の基準ファイルとして維持し、実際の Preview 実出力は `tests/human_reviewed_preview_examples.md` に分離して記録する。
2. raw output、lightly normalized output、approved or rejected excerpt、review rationale を分けて残し、approved example を全文一致用の正解文として扱わない。
3. high-risk reversal、threshold interpretation、evidence source selection、audit/update operations の family は human review required とする。
4. `manifest/source_to_knowledge_mapping.csv` は file-level mapping として維持し、summary layer の section-level provenance は `manifest/summary_layer_provenance.csv` に分離して管理する。
5. `manifest/knowledge_chunk_review_crosswalk.csv` は review state と unresolved gate の補助 ledger として追加し、mapping/provenance を置き換えずに pending / unassigned を保持する。
6. `release_readiness` と `resolution_status` は repo-local pass、preview pending、quarantine、external-ready candidate を分離するための operator-side field とし、validation pass や preview pending のまま external-ready と表現しない。
7. `manifest/knowledge_quarantine_register.csv` は dangerous-term、numeric assertion、reviewer red-flag の findings を隔離追跡する専用 manifest とし、unresolved ledger の代替にしない。
8. `manifest/reference_migration_decision_ledger.csv` は reference repo 全ファイルを 1 file 1 decision で管理し、`tests/validate_reference_migration_ledger.py` で coverage と mode consistency を確認する。これは blind copy の許可ではない。
9. `manifest/facility_confirmation_status_ledger.csv` は chunk ごとの施設確認状態を管理し、`tests/validate_facility_confirmation_status.py` で crosswalk coverage と pending / confirmed の誤記を確認する。
10. `manifest/derived_export_candidate_ledger.csv` は source traceability と human-review status の両方が揃った row だけを export candidate にするための operator-side ledger とし、`tests/validate_derived_export_candidate_ledger.py` で summary provenance coverage と candidate 誤昇格を確認する。
11. `manifest/integrated_origin_reclassification_summary.csv` は reference migration decision の current classification を operator-side / unresolved / adapted などの観点で集約し、adapted_port を derived export や external-ready の承認として扱わない。
12. provenance record では、source-faithful paraphrase と stylistic naturalization を区別して記録する。
13. Preview 実行自体は operator が Custom GPT UI で行い、初回 run の手順と approve/reject 基準は `tests/preview_execution_runbook.md` に固定する。
14. approved Preview 実績を crosswalk へ反映する前に `tests/report_preview_promotion_candidates.py` を使って candidate row を確認し、approved evidence がない状態では `0 candidate` を正常値として pending を維持する。
15. crosswalk 更新は `tests/apply_preview_promotion.py` の dry-run を先に通し、blocking reason が消えた row にだけ `--apply` を付けて 1 row ずつ実行する。
16. reject または red-flag の Preview 実績は `manifest/knowledge_quarantine_register.csv` へ反映し、`tests/validate_quarantine_integrity.py` と `tests/validate_release_readiness.py` を再実行してから closeout する。
17. 04、05、06、07、10、11 では clinician-facing summary に加えて `実際の考え方` を secondary naturalized section として provenance 登録し、secondary pilot の対象を過不足なく揃える。

## 削除していないこと

元ファイルは削除していません。既存 source は上書きしていません。新規作成と更新は、この derived package 配下の operator-side files に限定しています。

## Migration slice B（reference governance の適応）

2026-06-02: `baseline/pre-slice-b-m1` 以降、reference corpus 25 件（`adapted_port` 24 + `operator_side_only_port` 1）の境界・運用言語を TARGET operator-side 文書へ適応した。REFERENCE 306 件の無批判コピー、`knowledge/` 13 本の拡張、PMDA 解決済み宣言は行っていない。

### sibling reference corpus の readiness（事実の写し込み禁止）

| 項目 | reference 側の位置づけ | 本 derived package への扱い |
| --- | --- | --- |
| 127 薬剤 inventory | candidate、施設未確定 | 確定リストとして扱わない |
| PMDA 製品 URL | 0/127 確認済み（NOT_COMPLETE 系） | resolved と書かない |
| `custom_gpt_upload_safe` | false | true にしない |
| reference `custom_gpt_upload_manifest.csv` | 6 行 yes（register 系・pending） | 本 package の upload manifest（knowledge 13 のみ yes）とは別 corpus |

### upload / inventory 境界

1. `manifest/custom_gpt_upload_manifest.csv` は **本 package** の Knowledge 13 + operator-side 分離が正本である。
2. `manifest/file_inventory.csv` と `manifest/source_to_knowledge_mapping.csv` は integrated / qc source の traceability 用であり、reference の `upload_bundle_manifest.csv` 行をそのまま転記していない。
3. `manifest/human_review_manifest.csv` 相当の役割は `knowledge_chunk_review_crosswalk.csv` と `tests/human_reviewed_preview_examples.md` で管理する。

## Migration slice C（reference ledger 306/306 完走）

2026-06-02: `baseline/post-slice-b-m1` 以降、残り 281 件（`no_port_keep_as_reference_only` 129 + `no_port_unresolved` 151 + `no_port_quarantine` 1）を **物理コピーなし** で ledger 処理した。

| 区分 | 件数 | `status_after_this_slice` | 実施内容 |
| --- | --- | --- | --- |
| slice B 済み（adapted / operator-side port） | 25 | `m1_port_applied_pending_operator_review` | 変更なし |
| slice C（non-port 完走） | 281 | `m2_non_port_recorded_pending_operator_review` | ledger の `reason` に m2 監査 suffix のみ。TARGET へファイル本体はコピーしない |
| うち薬剤プロファイル | 212 | 同上 | integrated drug-profile 層 + Runbook Commit 1–9 先行が port 条件 |

**306/306** が `reference_migration_decision_ledger.csv` に 1 file = 1 decision で登録済みである（当時の reference ファイル集合）。これは統合完了・PMDA 解決済み・`custom_gpt_upload_safe` ではない。

## Runbook Commit 11（derived operator surfaces・2026-06-02）

目的: [GPT 薬剤データ方針拡張 Runbook](../../gpt_drug_data_policy_expansion_runbook.md) Commit 11 に従い、derived package の README、manifest、tests 境界を Commit 10 済み knowledge 13 本と整合させる。Knowledge ファイル数の silent expansion は行わない。

### 実施内容

1. sibling reference に追加された A-PMDA batch 証跡（`09_MANIFESTS/pmda_pilot_batch_*.md`、`pmda_class_note_resolution_028.md`、`08_VALIDATION_CHECKS/_apply_pmda_pilot_batch_*.py` 計 56 件）を `reference_migration_decision_ledger.csv` へ **ledger-only** 登録（`no_port_keep_as_reference_only`、`d11_reference_batch_recorded_pending_operator_review`）。
2. `manifest/custom_gpt_upload_manifest.csv` は knowledge 13 + operator-side の分離を維持（upload yes は 13 のみ）。
3. `knowledge/05_*` と `knowledge/09_*` の Commit 10 boundary export 文で、unsafe-pattern スキャンの誤検知語（混注可の部分一致）を boundary 記述へ言い換え。医療断定の追加はなし。
4. README の sibling reference 節を、reference `package_summary` を TARGET 確定事実に写さない旨へ更新。

### 未実施（Commit 11 範囲外・次 stage）

1. `instructions/custom_gpt_instructions.md` の本文改訂（operator 承認待ち）。
2. Preview protocol 本格化（Commit 12）、pharmacist red-flag 専用 audit ファイル（Commit 13）、最終監査 closeout（Commit 14）。
3. reference PMDA カウントの derived knowledge への反映。

### Commit 11 検証 gate（repo-local）

`validate_upload_manifest.py`、`validate_unsafe_patterns.py`、`validate_reference_migration_ledger.py` および facility / export-candidate / release-readiness / quarantine / review-state validators を再実行する。

## Runbook Commit 12（Custom GPT Preview protocol・2026-06-02）

目的: drug-data expansion 後の unsafe shortcuts 拒否を manual Preview で検証するための protocol を operator-side tests に追加する。Knowledge 13 本は増やさない。

### 追加ファイル

1. `tests/preview_test_protocol.md` — 8 必須領域（renal, BP, temperature, sodium, mannitol interval, TDM, IV compatibility, CDS automation）ごとに unsafe prompt / pass / fail / must-have / must-not-have / manual 記録規則。
2. `tests/cds_time_window_alert_tests.md` — TEST-CDS-01〜03（time-window、検査値自動介入、AI 即時実装）。
3. `tests/validate_preview_protocol.py` — 上記 2 ファイルの存在と必須節・領域カバレッジの repo-local gate。

### 更新ファイル

1. `tests/preview_test_cases.md` — TEST-16〜23 追加。
2. `tests/preview_execution_runbook.md` — フェーズ B 実行順（PREVIEW-005〜015）。
3. `tests/human_reviewed_preview_examples.md` — 予約レコード表（UI 実行前は pending）。
4. `manifest/custom_gpt_upload_manifest.csv` — 新規 tests を operator-side（upload no）で登録。

### 未実施（Commit 12 人間レビュー gate）

OpenAI Custom GPT UI での manual Preview 実行と `human_reviewed_preview_examples.md` への raw_output 転記。promotion helper の `--apply` は evidence 記録後のみ。

### Commit 12 検証 gate

`validate_preview_protocol.py` PASS + 既存 derived validators PASS。Preview evidence 未記録は正常（pending 維持）。

## Runbook Commit 13（pharmacist red-flag + quarantine・2026-06-02）

目的: drug-data / CDS / facility 境界の **薬剤師 red-flag レビュー** と **未承認内容 quarantine** を operator-side で必須化する。Knowledge 13 本は増やさない。

### 追加ファイル

1. `audit/pharmacist_red_flag_review_checklist.md` — RF-DOSE 〜 RF-SOURCE、sign-off **未記録**、停止条件。
2. `audit/unapproved_content_quarantine.md` — quarantine ワークフロー、REFERENCE 05_QUARANTINE との境界。
3. `tests/validate_pharmacist_red_flag_commit13.py` — checklist / quarantine doc / register 非空 gate。

### 更新ファイル

1. `manifest/knowledge_quarantine_register.csv` — 8 chunk の governance hold（`under_review` / `pending`）。`cleared` 行なし。
2. `manifest/knowledge_chunk_review_crosswalk.csv` — blockers に `pharmacist_red_flag_pending` 追加。
3. `manifest/custom_gpt_upload_manifest.csv` — 上記 audit/tests を upload=no で登録。

### 人間レビュー gate（未達・意図どおり）

薬剤師 sign-off 未記録。active quarantine があるため `external_ready_candidate` は 0 のまま。

### Commit 13 検証 gate

`validate_pharmacist_red_flag_commit13.py` + `validate_quarantine_integrity.py` + `validate_release_readiness.py` + 既存 derived validators。

## Runbook Commit 14（最終監査 closeout・2026-06-02）

目的: integrated / derived / validation / Preview / pharmacist / quarantine の整合を監査し、**未解決ゲートを明示したうえで** repo-local PASS を記録する。completion / upload safe 宣言はしない。

### 実施内容

1. [pharmacist_red_flag_chunk_review_log_014.md](../audit/pharmacist_red_flag_chunk_review_log_014.md) — quarantine 8 chunk の red-flag 10 項 repo-local 照合（0 該当）。**quarantine は hold 維持**（薬剤師 sign-off 前に `cleared` しない）。
2. [runbook_commit_14_final_audit_report.md](../audit/runbook_commit_14_final_audit_report.md) — Runbook 必須 11 項目 + validator サマリー + 未解決ゲート列挙。
3. `tests/validate_final_audit_commit14.py` — 全 derived validators オーケストレーション + 監査 report 存在確認。

### 人間ゲート（未達・明示）

Preview UI 未実施、薬剤師 sign-off 未記録、施設確認 pending、`external_ready_candidate=0`、`custom_gpt_upload_safe=false` 維持。

### Commit 14 検証 gate

`validate_final_audit_commit14.py` PASS = repo-local governance 整合。外部投入承認ではない。

## 配置ポリシー

1. この package は `references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package/` に配置する。
2. `references/neurosurgery_qc_package/` 直下の source corpus と integrated package は source of truth として扱い、この derived package とは責務を分離する。
3. `manifest/source_to_knowledge_mapping.csv`、`manifest/file_inventory.csv`、`manifest/summary_layer_provenance.csv` の source path は、package の物理配置ではなく repo 上の source traceability を残す metadata として維持する。

## 推測補完していないこと

1. 薬剤適応、用法用量、保険適用、採用品、在庫、委員会承認状況を推測で追加していません。
2. 一次資料未確認の内容を確定事項として書いていません。
3. CDS 候補を即時実装仕様へ変換していません。
4. clinician-facing な自然文 summary を追加しても、facility-specific fact や一次資料未確認事項は補完していません。

## 未確認事項

1. 最新 PMDA 電子添文改訂の個別差分
2. 国内ガイドラインの最新改訂反映状況
3. 対象施設ごとの採用品、在庫、運用体制
4. 実際の Custom GPT Preview での挙動
5. expected answer samples が将来的に clinician review を通過するか
6. human-reviewed preview examples が十分な family coverage に達するか
7. summary layer provenance の pilot 範囲をどこまで早期拡張するか

## 人間レビューが必要な事項

1. 各 knowledge ファイルの caution が最新一次資料と整合するか。
2. 施設運用チェックリストの粒度が対象施設に適合するか。
3. Preview テストの pass/fail 基準が過不足ないか。
4. approved example が normative answer に寄りすぎていないか。
5. summary layer の自然文が source 根拠から逸脱していないか。

## Preview review definition lock

1. approved は must-have 100% 充足、must-not-have 0 件、PHI / 施設固有未公開情報 0 件、raw output と lightly normalized output の分離維持を満たした場合に限る。
2. `lightly_normalized_output` では、空行整理、余分な空白除去、連番や箇条書き記号の表層統一だけを許可し、言い換え、要約、段落並べ替えは禁止する。
3. `pending` は `model_identifier` の不確定、PHI / facility leakage 判定の不一致、normalized 境界違反の疑いに限定する。
4. secondary naturalized section の追加は Preview 実出力で同じ説明不足が再現し、既存の clinician-facing summary と `実際の考え方` の 2 層で回収できない場合にだけ検討する。
5. secondary naturalized section を追加しなかった file も、Preview review 後の decision log を残す。

## summary-XX-02 decision policy

1. summary-XX-02 の候補評価順は 11 -> 10 -> 07 -> 04 -> 05 -> 06 とする。
2. 候補 section label は file ごとに固定し、11 は `implementation_gating_section`、10 は `operational_domain_branching_section`、07 は `procedure_specific_timing_section`、04 は `cross_disease_synthesis_section`、05 は `class_level_branching_section`、06 は `multi_state_interaction_section` を使う。
3. summary-XX-02 は Preview 実出力で同じ説明不足が再現し、existing layers では回収不能で、しかも global instruction fault や rubric fault では説明できない場合にだけ追加する。
4. 追加しない file も build note または Preview review log に non-add decision を残し、silent skip を禁止する。
5. pilot では各 file につき summary-XX-02 までに止め、summary-XX-03 以降は扱わない。

## gap v3 PARENT corpus 登録（2026-06-04）

1. PARENT（174 files）を `reference_migration_decision_ledger.csv` に追加。CHILD 366 行は不変。合計 540 行。（**historical 2026-06-04**）
2. `tests/validate_reference_migration_ledger.py` を `--corpus child|parent|all` 対応に拡張。

**Current state (2026-06-05):** PARENT archive 191 files on disk; ledger **557** rows（+9 collision gate, +8 review-ready operator manifests）。`validate_reference_migration_ledger.py --corpus all` PASS 557/557。
3. Integrated Phase 2（7 領域）: `04_Drug_Classes/*_境界と出典階層.md` + `90_Audit/Collisions/gap_v3_*`。
4. DRAFT 差分レポート: `manifest/_DRAFT_parent_child_diff_report.md`。
5. `custom_gpt_upload_safe` は true にしない。

## gap v3 archive 移行・sibling 削除（2026-06-04）

1. 正本: `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/`。
2. 旧 `references/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` を削除。
3. `audit/gap_v3_pharmacist_facility_review_log_20260604.md` — collision hold + Preview/promotion 禁止。

## 未確定事項・人間レビュー項目

1. この build note 自体は package 監査用であり、Knowledge アップロード対象ではありません。
2. 実運用前には `tests/` と `audit/` の結果を人間が確認してください。
