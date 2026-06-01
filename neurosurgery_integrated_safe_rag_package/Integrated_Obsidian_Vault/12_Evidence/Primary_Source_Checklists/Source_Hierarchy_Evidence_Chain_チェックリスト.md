---
note_type: "external_primary_source_checklist"
title: "Source Hierarchy・Evidence Chain チェックリスト"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Source hierarchy / evidence chain"
source_quote_or_summary: "PMDA、RMP、interview form、ガイドライン、JAPIC、manufacturer documents、施設採用品、薬剤部手順、EHR medication master の確認順序と責務分離を整理する。"
gpt_structured_interpretation: "source class の優先順位を prescribing hierarchy と誤認させず、外部一次資料確認と施設内確認を分離するための operator-side checklist。"
evidence_certainty: "原資料上は要外部一次資料確認"
recommendation_strength: "原資料上の候補・非候補を分離。最終判断は外部一次資料確認と施設内承認後"
domestic_regulatory_status: "PMDA電子添文で要確認"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・夜間休日在庫・薬剤部手順・看護体制・委員会承認・EHR medication master を要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
not_to_standardize:
  - "source hierarchy を prescribing hierarchy として扱わない"
  - "海外GL記載を国内薬事確認の代替にしない"
  - "施設採用品や EHR medication master を PMDA 製品単位確認の代替にしない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "PMDA電子添文"
  - "PMDA review report"
  - "RMP / 安全性情報"
  - "患者向医薬品ガイド"
  - "interview form"
  - "Minds / 国内診療ガイドライン"
  - "学会ガイドライン"
  - "JAPIC"
  - "manufacturer documents"
facility_confirmation_items:
  - "採用品"
  - "夜間休日在庫"
  - "薬剤部手順"
  - "委員会承認"
  - "EHR medication master"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "one_claim_per_chunk"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "施設内手順として即時運用しない"
  - "電子カルテ診療支援仕様として即時実装しない"
  - "source class の順序だけで薬剤選択を決めない"
  - "facility confirmation が未了のまま運用可能と判断しない"
audit_status: "draft_needs_human_review"
last_reviewed: "2026-06-01"
---

# Source Hierarchy・Evidence Chain チェックリスト

## 1. 目的

このチェックリストは、Vault 内の薬剤関連記載をどの source class で確認し、どこで施設内確認へ切り替えるかを整理するためのものです。
source hierarchy は確認順序の管理であり、処方や運用の自動決定根拠ではありません。

## 2. Source hierarchy

### 2-1. 国内薬事・製品単位確認の最優先層

- PMDA電子添文
- PMDA review report
- 患者向医薬品ガイド
- interview form
- RMP / 安全性情報

この層は、国内薬事上の位置づけ、製品単位の確認、重大安全性情報、添付文書上の注意事項を確認するための層です。
施設採用品、EHR medication master、海外ガイドラインは、この層の代替にしてはいけません。

### 2-2. 疾患文脈・背景整理の参照層

- Minds / 国内診療ガイドライン
- 学会ガイドライン
- JAPIC
- manufacturer documents

この層は、疾患文脈、背景知識、製品周辺情報、比較の補助に用います。
この層だけで国内適応、施設内標準、即時運用可否を確定してはいけません。

### 2-3. 施設運用確認の必須層

- 採用品
- 夜間休日在庫
- 薬剤部手順
- 委員会承認
- EHR medication master

この層は、施設で実際に扱えるか、誰が確認するか、どの operational surface に載せるかを確認するための層です。
この層は国内薬事確認の代替ではなく、外部一次資料確認の後に分離して扱います。

## 3. 確認軸の分離

- 国内薬事確認: PMDA 製品単位確認を優先する
- 安全性確認: RMP / 安全性情報を分離して確認する
- 疾患文脈確認: ガイドラインや JAPIC を背景整理として扱う
- 施設確認: 採用品、薬剤部手順、委員会承認、EHR medication master を別 ledger で扱う
- 実装確認: CDS candidate と production EHR/CDS specification を分離する

## 4. 標準化しない事項

- source hierarchy を prescribing hierarchy として扱わない
- 海外GL記載を国内薬事確認の代替にしない
- facility confirmation 未了のまま標準候補にしない
- EHR medication master 登録を clinical approval と誤認しない
- source class の存在だけで derived export を許可しない

## 5. 更新対象

- 薬剤ノート
- 薬剤クラスノート
- 疾患ノート
- 患者状態ノート
- 処置ノート
- 条件・閾値ノート
- 陰性知識ノート
- source register
- facility confirmation ledger
- review-state ledger
- RAG JSONL
