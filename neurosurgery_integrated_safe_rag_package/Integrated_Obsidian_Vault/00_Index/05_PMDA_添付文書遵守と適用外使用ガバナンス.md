---
note_type: "governance_index"
title: "PMDA_添付文書遵守と適用外使用ガバナンス"
not_a_guideline: true
not_a_prescription_order: true
not_an_institutional_procedure: true
not_immediate_cds_specification: true
source_document: "Neurosurgery Safe RAG integrated governance (Stage 3)"
source_section: "label compliance and off-label use routing"
source_quote_or_summary: "Operator-side rules: dosing, route, frequency, and administration method must align with product-specific electronic package inserts (PMDA). Use beyond approved labeling is not presented as standard care without explicit physician judgment and facility policy confirmation."
gpt_structured_interpretation: "Governance index only. No numeric doses, no TDM targets, no order sets, no CDS triggers. Routes AI and humans to PMDA product-level labels and blocks off-label generalization."
evidence_certainty: "operator_policy_not_clinical_source"
recommendation_strength: "no_clinical_recommendation_in_this_note"
domestic_regulatory_status: "PMDA_electronic_package_insert_required_per_product"
insurance_risk: "施設方針・理由記録を要確認"
institutional_operability: "採用品・専門医・委員会承認・プロトコルを要確認"
facility_candidate: "原資料からは確定できない"
cds_candidate: "即時実装仕様ではない"
human_review_required: true
not_to_standardize:
  - "添付文書の承認範囲を超える用法を標準治療として標準化しない"
  - "一般名・gap supplement・文献を製品単位添付文書と同一視しない"
  - "reference profile から数値用量を補完しない"
undetermined_from_source:
  - "各製品の最新版電子添文の全文"
  - "施設内適用外使用の承認プロセスの最終形"
  - "保険・査定上の適用外の扱い"
external_primary_source_check_items:
  - "PMDA医薬品医療機器総合機構 個別製品ページ（製品単位）"
  - "最新電子添文（施設で参照する版）"
  - "RMP / IF / 患者向医薬品ガイド（該当時）"
facility_confirmation_items:
  - "施設内採用品・規格"
  - "適用外使用に関する院内規程・委員会承認の有無"
  - "専門科・薬剤部の確認記録"
required_human_review: true
ai_misread_risk: "high"
rag_chunk_policy: "governance_routing_preferred_over_reference_profiles"
not_to_interpret_as:
  - "正式な診療ガイドラインとして扱わない"
  - "正式な処方指示として扱わない"
  - "適用外使用の推奨・一般化として扱わない"
  - "数値用量・投与間隔の確定値として扱わない"
audit_status: "draft_needs_human_review"
stage3_governance_slice: "2026-06-05"
last_reviewed: "2026-06-05"
---

# PMDA 添付文書遵守と適用外使用ガバナンス（Stage 3）

## 位置づけ

本ノートは **integrated 正本の operator / RAG ガバナンス** である。臨床推奨・処方確定・施設 SOP の代替ではない。

- Gap V3 boundary hubs: [[00_Index/04_Gap_V3_Reference_Parked_Index]]
- Collision 監査: `90_Audit/Collisions/gap_v3_*_reference_collision.md`
- Derived Custom GPT `knowledge/*.md` への用量エクスポートは **Stage 4 以降**（本 Stage では未実施）

## 用法・用量・使用方法（添付文書遵守）

| 原則 | 内容 |
|------|------|
| 一次根拠 | 具体的な**用法・用量・投与間隔・投与速度・用法区分・適応**は、当該製品の**最新電子添文（PMDA 製品単位、施設で参照する版）**に沿って確認された場合に限り記載可能 |
| 未解決 | PMDA 製品単位が未解決の reference / 一般名プロファイルから数値・ルート・間隔を**推測・補完・断定しない** |
| routing | 未確認時は「**添付文書（製品単位）で要確認**」と施設採用品・専門医確認へ誘導するのみ |
| 禁止 | ファイル名・略語・レジメン名・gap supplement 本文から用量表を生成しない |

## 適用外使用（添付文書の承認範囲を超える使用）

| 原則 | 内容 |
|------|------|
| 原則禁止 | 適用外使用を、**医師の個別判断なしに**標準治療・推奨治療・標準オーダー・「当院ルーティン」として提示しない |
| 文献・gap | 文献・参考資料・PARENT gap supplement を根拠に、適用外を**一般化・正常化**しない |
| 言及の条件 | 適用外の可能性に言及する場合は**処方確定ではなく**、**医師の判断**・**施設プロトコル／委員会承認**・**製品単位添付文書との照合**を併記する |
| 昇格 | `export_status` / `export_candidate` の変更は、PMDA 解決・薬剤師・施設 evidence の後の operator 作業のみ |

## 禁止回答例（全ドメイン共通）

- 「○○mg を1日○回」など、製品単位添付文書未確認の数値断定
- 「文献では有効なので標準的に投与」などの適用外の一般化
- PARENT 一般名プロファイルの記述を製品承認用量として提示
- CHILD PMDA inventory 件数や pilot 結果を V3 profile 用量の根拠にする

## AI / operator gate（チェックリスト）

- [ ] 数値用量・投与間隔を含む回答の出典が、当該製品の電子添文（製品単位 URL 確認済み）である
- [ ] 適用外に該当しうる内容は、医師判断・施設確認を案内しており、単独で処方確定していない
- [ ] `脳腫瘍周術期.md` 等の疾患ノートへ oncology レジメン・用量を誤マージしていない
- [ ] `apply_preview_promotion.py` 未実行・Preview 捏造なし

## 関連 boundary（各ハブ末尾に同趣旨の節あり）

[[04_Drug_Classes/神経腫瘍薬物療法_境界と出典階層]] · [[04_Drug_Classes/下垂体内分泌薬_境界と出典階層]] · [[04_Drug_Classes/術中可視化・造影剤_境界と出典階層]] · [[04_Drug_Classes/CSF_IIH関連薬_境界と出典階層]] · [[04_Drug_Classes/血管内治療・血管攣縮局所薬_境界と出典階層]] · [[04_Drug_Classes/痙縮・機能的脳神経外科薬_境界と出典階層]] · [[04_Drug_Classes/中枢神経感染・脳室内投与_境界と出典階層]]
