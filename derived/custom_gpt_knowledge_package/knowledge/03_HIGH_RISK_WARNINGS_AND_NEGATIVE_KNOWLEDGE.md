---
document_type: derived_custom_gpt_knowledge
package_layer: derived
document_role: custom_gpt_rag_knowledge
package_name: neurosurgery_qc_custom_gpt_knowledge_package
source_path: "references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/08_Negative_Knowledge/Layer2薬剤_標準化しない事項.md"
source_revision: integrated-vault-2026-06-01;runbook-commit-10
export_date: 2026-06-02
transformation_rule: direct_guardrail_import_summary_export_commit10
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
# 03 HIGH RISK WARNINGS AND NEGATIVE KNOWLEDGE

## このファイルの役割

このファイルは、Custom GPT が最優先で守るべき高リスク誤読防止規則と誤読を防ぐための注意事項（negative knowledge）を集約するファイルです。

## 先に押さえるべき決定点

このファイルの役割は、単に「だめなこと」を並べることではありません。高リスクの論点で、どこを分けないと危険かを先に示すことです。特に中和薬、止血関連、輸血関連、浸透圧療法、CDS 実装の話題では、短い答えの中でも最初に区別すべき条件があります。

## 臨床での考え始め方

高リスク論点では、まず短絡（shortcut）を止め、その後で分岐軸を整理します。たとえば「脳出血だから PCC」「抗血小板薬を飲んでいるから血小板輸血」といった答え方は速く見えて危険です。実際には薬剤クラス、最終服用時刻、検査値、処置予定、施設運用を分けて考える必要があります。

## 緊急時に先に確認すること

このブロックは、緊急時に確認漏れを避けるための整理です。処方、投与、中止、休薬、再開、用量調整、CDS発火条件をこのKnowledgeだけで判断するためのものではありません。

- 対象病態
- 曝露薬の種類
- 最終服用・最終投与時刻
- 関連する検査値
- 手術、EVD、穿刺、保存的管理などの処置予定
- 禁忌・除外条件
- 施設採用品、在庫、薬剤部手順、輸血部運用、看護観察体制
- 診療科責任医、薬剤部、必要に応じて輸血部・ICU/SCU担当者への確認
- このKnowledgeだけで判断してはいけない事項

## 薬剤名短絡の禁止

薬剤名が出たことだけで、標準候補、推奨、施設運用可能、即時 CDS 実装可能と解釈してはいけません。

## 疾患名短絡の禁止

疾患名が出たことだけで、特定薬剤や特定手技を一律候補化してはいけません。疾患ごとに患者状態、検査値、処置予定、曝露薬、施設運用条件が分離されます。

## 高リスク薬剤・重要な分岐点

### PCC

1. VKA 関連出血と DOAC 関連出血を同列に扱わない。
2. DOAC 関連出血の標準中和薬として機械的に出さない。
3. 特異的中和薬の可否、腎機能、最終服用時刻、手術予定を確認する。
4. 「まず何を考えるか」は、DOAC の種類と特異的中和薬の位置づけ、そして施設で本当に扱えるかの確認である。

### rFVIIa

1. 自然発症脳内出血で一律候補化しない。
2. 高リスク薬剤として、一次資料確認と施設内承認を要する領域として扱う。
3. 早く答えるより、なぜ routine で扱わないのかを先に説明する。

### TXA

1. すべての頭蓋内出血に標準使用できると扱わない。
2. 受傷タイミング、疾患類型、Evidence、施設運用確認を分ける。
3. 臨床上は「どの出血でも同じではない」が出発点になる。

### 血小板輸血

1. 抗血小板薬曝露だけで標準化しない。
2. 血小板減少、出血状況、手術予定、輸血関連指針を別に確認する。
3. 内服歴と検査値を同じ意味で扱わない。

### デスモプレシン

1. 抗血小板薬関連頭蓋内出血で標準候補化しない。
2. 疾患、曝露薬、Evidence、施設手順を分離する。
3. 「使うかどうか」より先に、どういう状況で論点になるかを分ける。

### アンデキサネット アルファ / イダルシズマブ / プロタミン

1. 薬剤名対応関係を混同しない。
2. 施設採用品、夜間休日在庫、薬剤部手順、理由記録を要確認とする。
3. 適応整理と実際の可用性を一つの答えに潰さない。

### マンニトール / 高張食塩液

1. 一般病棟で標準単独運用できると扱わない。
2. Na、浸透圧、尿量、看護観察体制、病棟制約を必須確認とする。
3. 薬剤の話だけでなく、監視体制の話として扱う。

## VKA 関連出血と DOAC 関連出血を同列に扱わない

抗凝固薬関連出血では、少なくとも次を分離します。

1. VKA
2. ダビガトラン
3. Xa 阻害薬
4. ヘパリン系

中和薬、代替薬、理由記録、施設運用可否は別軸です。

## 自然発症 ICH で rFVIIa を一律候補化しない

Knowledge 上は高リスク誤読領域です。一般論や薬剤名連想で候補化してはいけません。

## TXA を全頭蓋内出血に一律候補化しない

外傷性脳損傷、自然発症 ICH、抗血栓薬関連出血、くも膜下出血を一つの横断カテゴリとして扱ってはいけません。

## 抗血小板薬曝露だけで血小板輸血を標準化しない

薬剤曝露と血小板数低下は別の状態です。処置予定、出血状況、輸血部運用を分けて確認します。

## CDS 候補と即時実装仕様を混同しない

`11_CDS_CANDIDATE_BOUNDARIES.md` を優先し、候補、表示、理由記録、入力拘束、実装仕様を分離してください。

## 国内薬事、保険、施設採用品、在庫、運用を推測しない

Knowledge 上に確定値がない場合は、次のように扱います。

1. 国内薬事: 要 PMDA 電子添文確認
2. 保険・査定: 要施設方針確認
3. 採用品・在庫: 要施設内確認
4. 運用手順: 要薬剤部、輸血部、看護、委員会確認

## 検索補助語

検索補助語です。医学的同一性を断定するものではありません。

1. PCC / prothrombin complex concentrate
2. rFVIIa / recombinant factor VIIa
3. TXA / tranexamic acid
4. DDAVP / desmopressin
5. andexanet alfa
6. idarucizumab

## 未確定事項・人間レビュー項目

1. 高リスク薬剤の最終運用可否は対象施設ごとに異なります。
2. 本ファイルは誤読防止を優先しており、個別運用判断は `04` から `10` と一次資料を併用して確認する必要があります。
## Integrated governance boundary export（Stage 4 — 2026-06-05）

### 添付文書・用法用量（誤読防止用の陰性知識 / negative knowledge）

1. ファイル名・略語・一般名・gap supplement から用法・用量・投与間隔を答えない。
2. PMDA 製品単位未解決の reference を、製品承認用量として提示しない。
3. 「添付文書で要確認」以外の数値断定を user-facing conclusion にしない。

### 適用外使用（誤読防止用の陰性知識 / negative knowledge）

1. 文献・gap supplement を根拠に、適用外使用を標準治療・推奨・「当院ルーティン」として一般化しない。
2. 医師の個別判断・施設プロトコル・委員会承認の有無を確認せず、適用外を処方確定として提示しない。

### Gap v3 領域の誤短絡（誤読防止用の陰性知識 / negative knowledge）

1. 神経腫瘍: レジメン名（例: TMZ、PCV、bevacizumab、カルムスチン wafer）を、製品・施設未確認の「標準治療」として断定しない。`04` 脳腫瘍周術期は周術期 ASM・ステロイド・感染・血栓の文脈であり、化学療法選択の代替ではない。
2. 下垂体: 術後 DI / stress steroid 文脈 note を、慢性水欠症や無条件ステロイド増量の確定指示にしない。
3. 造影・手技・脳室内・ITB 等: procedural / reference ノートを標準治療薬プロファイルとして扱わない。
