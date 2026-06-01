---
note_type: "source_hierarchy_guidance"
title: "Drug Label Source Hierarchy"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "脳神経外科領域における施設内薬物治療アルゴリズム"
source_section: "Drug label source hierarchy"
source_quote_or_summary: "薬剤関連情報の source class、確認順序、facility confirmation への切り替え条件を整理する。"
gpt_structured_interpretation: "source hierarchy は確認順序を管理する operator-side governance であり、処方判断、施設運用、EHR/CDS 実装を直接決めるものではない。"
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
  - "source class の存在だけで derived export を許可しない"
undetermined_from_source:
  - "国内薬事上の最終位置づけ"
  - "保険・査定上の最終扱い"
  - "施設内標準化可否"
  - "電子カルテ診療支援としての実装可否"
external_primary_source_check_items:
  - "PMDA electronic package insert"
  - "PMDA review report"
  - "RMP / 安全性情報"
  - "患者向医薬品ガイド"
  - "interview form"
  - "Minds / 国内診療ガイドライン"
  - "学会ガイドライン"
  - "JAPIC"
  - "manufacturer documents"
facility_confirmation_items:
  - "formulary status / 採用品"
  - "night-holiday stock"
  - "pharmacy procedure"
  - "committee approval"
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

# Drug Label Source Hierarchy

## 1. 目的

この文書は、薬剤関連情報を確認するときの source class、確認順序、facility confirmation への切り替え条件を整理するための canonical note です。
source hierarchy は確認順序の管理であり、処方、調製、投与、施設運用、EHR/CDS 実装の自動決定根拠ではありません。

## 2. Source class の基本原則

1. 国内薬事・製品単位確認は、PMDA 関連資料を最優先で確認する。
2. safety signal は RMP / 安全性情報として分離して確認する。
3. guideline、JAPIC、manufacturer documents は背景整理と照合に用いるが、国内薬事確認の代替にしない。
4. formulary status、pharmacy procedure、committee approval、EHR medication master は facility confirmation として別に扱う。
5. source class の順序は prescribing hierarchy ではない。

## 3. 国内薬事・製品単位確認層

この層は、国内薬事上の位置づけ、製品単位の確認、添付文書上の注意事項、安全性情報への接続を確認するための層です。

- PMDA electronic package insert
- PMDA review report
- 患者向医薬品ガイド
- interview form
- RMP / 安全性情報

施設採用品、EHR medication master、海外GL、manufacturer documents は、この層の代替ではありません。
PMDA 製品単位確認が未了の薬剤は、resolved / confirmed / approved として扱ってはいけません。

## 4. 疾患文脈・背景整理層

この層は、疾患文脈、背景知識、比較、用語整理を補助するための層です。

- Minds / 国内診療ガイドライン
- 学会ガイドライン
- JAPIC
- manufacturer documents

この層だけで国内適応、施設内運用可否、Custom GPT upload 可否、derived export 可否を確定してはいけません。

## 5. 施設運用確認層

この層は、施設で扱えるか、誰が確認するか、どの operational surface に載せるかを確認するための層です。

- formulary status / 採用品
- night-holiday stock
- pharmacy procedure
- committee approval
- EHR medication master

この層は国内薬事確認の代替ではありません。
EHR medication master に登録があることは、clinical approval、facility-ready、external-ready、production CDS specification の成立を意味しません。

## 6. 参照先 checklist

- `12_Evidence/Primary_Source_Checklists/Source_Hierarchy_Evidence_Chain_チェックリスト.md`
- `12_Evidence/Primary_Source_Checklists/PMDA電子添文チェックリスト.md`
- `12_Evidence/Primary_Source_Checklists/RMP_安全性情報チェックリスト.md`
- `10_Operationalization/Formulary_Stock/施設採用品_夜間休日在庫チェックリスト.md`
- `10_Operationalization/Pharmacy_Workflow/薬剤部調製_払い出しチェックリスト.md`

## 7. 標準化しない事項

- source hierarchy を prescribing hierarchy として扱わない。
- source class の存在だけで薬剤選択、施設運用、derived export を決めない。
- 海外GL記載を国内薬事確認の代替にしない。
- PMDA 製品単位確認前に confirmed / approved と書かない。
- facility confirmation 未了のまま facility-ready または external-ready と扱わない。
- EHR medication master を production EHR/CDS specification として扱わない。

## 8. Human review required

この文書は source class と evidence chain の operator-side governance です。
薬剤師、臨床担当者、施設運用担当者、EHR/CDS governance reviewer の確認が完了するまで、derived export や external-ready 判定の根拠にしてはいけません。
