---
document_role: "custom_gpt_rag_knowledge"
package_name: "neurosurgery_qc_custom_gpt_knowledge_package"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
requires_primary_source_check: true
requires_facility_confirmation: true
requires_human_review: true
source_repository: "https://github.com/yskfuji61/neurosurgery_qc_package"
source_scope: "Integrated_Obsidian_Vault and related audit/export files"
rag_chunk_policy: "safety_first_cross_reference_required"
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
