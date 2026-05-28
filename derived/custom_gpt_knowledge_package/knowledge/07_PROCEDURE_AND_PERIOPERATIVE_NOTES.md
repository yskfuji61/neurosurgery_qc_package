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

# 07 PROCEDURE AND PERIOPERATIVE NOTES

## このファイルの役割

このファイルは、処置予定や周術期タイミングが薬剤判断を大きく変えることを固定します。

## clinician-facing summary

処置予定があるかどうかで、同じ薬剤でも意味が変わります。特に緊急開頭術、EVD、EVT、動脈瘤閉鎖前後では、薬剤の可否だけでなく、いつまでに何を確認すべきかが変わります。

## 実際の考え方

薬剤の話だけで完結させず、処置の時間軸とチーム運用まで含めて考えるのがこのノートの役割です。手術や穿刺が近いほど、検査値や曝露薬の意味は重くなります。

## 緊急開頭術

1. 抗血栓薬曝露、凝固検査、輸血関連準備、薬剤部・輸血部運用を確認します。
2. 手術予定の有無は reversal 判断を大きく変えます。

## EVD

1. 抗凝固薬、抗血小板薬、血小板数、凝固異常を確認します。
2. 手技関連出血リスクと夜間休日体制を分離して扱います。

## EVT

1. rt-PA 後 24 時間条件、抗血栓再開、出血性合併症を確認します。
2. 脳卒中 pathway と脳外科出血対応を混同しません。

## クリッピング

1. 動脈瘤閉鎖前後の時間軸を確認します。
2. 閉鎖前 24 時間条件と周術期運用を飛ばしません。

## コイル塞栓術

1. 抗血小板薬、周術期運用、血管内治療 team の flow を確認します。
2. クリッピングと同じ前提に固定しません。

## シャント関連処置

1. 感染リスク、抗菌薬文脈、抗血栓薬曝露、手技タイミングを確認します。
2. EVD と完全同一のフローにしません。

## 保存的管理

1. ICU / HCU / 一般病棟の別、神経所見観察、浸透圧療法、VTE 予防を確認します。
2. 手術なしだから確認不要とは扱いません。

## ICU / SCU / HCU 管理

1. 高張食塩液、マンニトール、鎮静、血糖管理、看護観察体制を確認します。
2. 一般病棟と同じ order 前提にしません。

## 未確定事項・人間レビュー項目

1. 実際の処置準備フローは施設ごとに異なります。
2. ここで示すのは確認軸であり、手順書そのものではありません。
