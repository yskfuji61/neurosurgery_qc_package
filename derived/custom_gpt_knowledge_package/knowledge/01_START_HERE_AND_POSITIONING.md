---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/final_qc_manifest.json"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: boundary_preservation_summary_export_commit10
included_for_custom_gpt: true
operator_side_only: false
human_review_required: true
not_a_guideline: true
not_a_prescription_order: true
not_immediate_cds_specification: true
no_patient_specific_dose_decision: true
no_auto_intervention_decision: true
requires_primary_source_check: true
requires_facility_confirmation: true
requires_human_review: true
source_repository: "https://github.com/yskfuji61/neurosurgery_qc_package"
source_scope: "Integrated_Obsidian_Vault and related audit/export files"
rag_chunk_policy: safety_first_cross_reference_required
tests_link: "derived/custom_gpt_knowledge_package/tests/pass_fail_criteria.md"
not_an_institutional_procedure: true
---
# 01 START HERE AND POSITIONING

## このファイルの役割

このファイルは、Custom GPT が最初に参照すべき位置づけファイルです。Knowledge 全体の境界、禁止解釈、参照順、誤読防止の最重要原則を固定します。

## まずどう使うか

この Knowledge は、医療者が論点を整理し、危険な短絡を避け、確認漏れを減らすための補助資料として使います。最初から長い注意文として読むのではなく、まず論点を絞り、その後で high-risk の注意点と確認事項を重ねる使い方を想定します。

## 臨床での考え始め方

最初に考えるべきなのは「何のための判断か」です。止血、中和、再開、周術期感染対策、発作対応、頭蓋内圧管理、CDS 検討では、必要な情報も危険な短絡も異なります。したがって、いきなり薬剤名や疾患名に飛びつくのではなく、目的、患者状態、処置予定、施設運用を先に分けてから読む前提にします。

## Vault 全体の位置づけ

この Knowledge は、脳神経外科領域の薬物治療アルゴリズム関連資料を、Custom GPT の Knowledge として安全に参照できるように再編したものです。元資料は公開参考資料、施設内手順作成用ベース資料、RAG 安全設計・監査資料の性格を持ちます。

## 正式ガイドラインではない

Knowledge 上の記載は、正式な診療ガイドラインではありません。診療推奨を確定する根拠として単独では用いてはいけません。

## 処方指示ではない

Knowledge 上の記載は、処方指示や投与指示ではありません。薬剤名だけで「使うべき」「投与する」と解釈してはいけません。

## 施設内手順ではない

Knowledge 上の記載は、承認済み施設内手順ではありません。対象施設の採用品、在庫、手順、看護体制、委員会承認を経ずに標準運用として扱ってはいけません。

## 即時 CDS 仕様ではない

Knowledge 上の CDS 候補は、即時実装可能な電子カルテ仕様ではありません。High Constraint Input Control、要件定義、責任者承認、監査ログ設計、受入テストが別途必要です。

## 回答時に必ず分離すべき 5 軸

回答時は少なくとも次の 5 軸を分離します。

1. 疾患・臨床状況
2. 薬剤・薬効分類
3. 患者状態・検査値・曝露薬
4. 処置予定・周術期タイミング
5. 一次資料確認・施設内確認・CDS 候補境界

必要に応じて、国内薬事、保険、施設運用、委員会承認、AI 誤読リスクを独立軸として追加します。

## 一次資料確認と施設内確認が必要な理由

Knowledge だけでは、次の事項を確定できません。

1. 最新 PMDA 電子添文での薬事上の位置づけ
2. 国内外ガイドラインの最新版
3. RMP・安全性情報の更新
4. 保険適用と査定運用
5. 施設採用品、夜間休日在庫、薬剤部手順、輸血部運用、看護観察体制、委員会承認

## この Knowledge をどう読むべきか

1. まず `03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md` を見て、禁止短絡を確認します。
2. 次に `02_INDEX_AND_NAVIGATION.md` から、質問に対応するカテゴリを特定します。
3. 疾患、薬剤、患者状態、処置、閾値、Evidence、施設運用、CDS 候補を横断参照します。
4. 最後に、最新資料や施設運用で追加確認が必要な部分だけを短く残して答えます。

## 誤読防止の最重要原則

1. 薬剤名だけで標準候補化しない。
2. 疾患名だけで薬剤選択しない。
3. 候補、推奨、国内薬事、保険、施設内運用、CDS 実装可能性を混同しない。
4. Knowledge にないことは推測せず、「確認できない」と言う。
5. 高リスク薬剤と陰性知識を、一般的な連想より優先する。

## 検索補助語

検索補助語です。医学的同一性を断定するものではありません。

1. Custom GPT Knowledge
2. RAG package
3. Obsidian Vault
4. negative knowledge
5. not a guideline
6. not immediate CDS specification

## 未確定事項・人間レビュー項目

1. この位置づけ文だけでは個別薬剤や個別疾患の可否を決められません。
2. 実回答では関連する `04` から `13` の横断参照が必要です。

## この資料の使用範囲と禁止事項（Runbook Commit 10）

この節では、本資料をどの範囲で使えるか、また何をこの資料だけで判断してはいけないかを整理します。処方、施設運用、Custom GPT Knowledgeへの投入可否を確定する根拠にはなりません。

1. ワークスペース内のPMDA参考資料群（reference corpus、366 files）は、製品単位の出典登録作業に用いる正本であり、本Knowledge 13本の代替ではない。
2. PMDA参考資料群で記録している確認件数（`pmda_resolved_count`）や出典登録の更新は、このリポジトリ内での作業進捗を示すものです。Custom GPT Knowledgeへの投入承認、施設採用品の確定、または実患者への使用可否を意味しません。
3. 127薬剤の一覧は、施設採用や使用可否が未確認の候補リストとして扱います。薬剤プロファイル212件は、統合済みの薬剤プロファイルとして整理されるまでは、Knowledgeへそのまま転記しません。
4. 元資料から作成した内容をKnowledgeに反映できるのは、出典を確認でき、人間レビューが必要であることを明記した要約ファイルに限ります（Commit 10）。
## この資料の使用範囲と禁止事項（Stage 4 — 2026-06-05）

出典: integrated `00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス` および gap v3 collision gate（operator 正本）。**検証PASSや台帳登録は、臨床承認、施設確定、Custom GPT Knowledgeへの投入承認、または実患者への使用可否を意味しない。**

1. **参考資料群（Reference corpora：Knowledge投入対象外）:** PMDA確認用の作業資料366件（CHILD）と、gap v3関連の参考資料191件（PARENT）は、合計557件の参考資料として台帳管理されています。ただし、これらは本Knowledge 13本の代替ではなく、Custom GPT Knowledgeへ一括投入する対象でもありません。
2. **添付文書遵守:** 用法・用量・投与間隔・投与速度・用法区分は、当該製品の最新電子添文（PMDA 製品単位）で確認できる場合に限り記載可能。reference 一般名プロファイルから数値を推測・補完しない。
3. **適用外使用:** 添付文書の承認範囲を超える使用を、医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
4. **Gap v3:** 神経腫瘍・下垂体・造影/手技・CSF/IIH・血管内・痙縮・CNS 感染などは **参考資料扱い / 投入保留（reference-only / hold）**。疾患ノート本文への無断マージ禁止。
