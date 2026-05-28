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

# 06 PATIENT STATE NOTES

## このファイルの役割

このファイルは、疾患名や薬剤名ではなく、患者状態が判断を分岐させることを固定するためのノートです。

## clinician-facing summary

患者状態は、薬剤や疾患の説明を現実の判断へ変える部分です。腎機能、血小板数、凝固異常、妊娠可能性、夜間休日運用などが入ると、同じ疾患名でも扱いは変わります。

## 実際の考え方

実務では、疾患と薬剤だけで答えを出すのではなく、「この患者でその前提が成り立つか」を確認します。このノートは、その確認軸を落とさないために使います。

## 抗凝固薬曝露

1. 薬剤名、最終服用時刻、腎機能、関連凝固検査を確認します。
2. 薬剤クラス不明のまま reversal を提示しません。

## 抗血小板薬曝露

1. 単剤か DAPT か、最終内服時刻、血小板数、処置予定を確認します。
2. 曝露のみで輸血候補を固定しません。

## 血栓溶解薬曝露

1. 投与時刻、24 時間画像、出血合併症の有無を確認します。
2. 虚血性脳卒中後管理と ICH 管理をそのまま混ぜません。

## 腎機能低下

1. CrCl / eGFR、尿量、AKI の有無を確認します。
2. ダビガトラン、LMWH、アシクロビル、バンコマイシンなどで特に重要です。

## 肝機能低下

1. 凝固、代謝、薬物相互作用の影響を確認します。
2. 抗てんかん薬や鎮静関連で特に重要です。

## 妊娠可能性

1. バルプロ酸などの候補化前に確認します。
2. 一般論で省略しません。

## 血小板減少

1. 抗血小板薬曝露とは別概念として扱います。
2. 輸血関連指針、出血状況、手術予定を確認します。

## 凝固異常

1. PT-INR、aPTT、ACT、関連薬剤曝露を確認します。
2. 検査値だけで薬剤クラスを推定しません。

## 低フィブリノゲン血症

1. フィブリノゲン値と輸血関連の確認を行います。
2. 出血重症度と処置予定を分離して扱います。

## 血栓症高リスク

1. VTE 予防と therapeutic anticoagulation 再開を分離します。
2. 再開日を機械的に固定しません。

## けいれんリスク

1. 予防投与か治療投与かを分離します。
2. 術後、腫瘍、外傷、出血の文脈で必要な薬剤が変わります。

## 夜間休日運用

1. 在庫、呼出体制、輸血部、薬剤部、看護観察体制を確認します。
2. 日中前提のフローを夜間休日へ自動延長しません。

## 未確定事項・人間レビュー項目

1. 患者状態ノートは、単独で治療候補を出すためのものではありません。
2. 実回答では必ず疾患、薬剤、処置、閾値、施設運用を併記してください。
