---
drug_key: isoxsuprine
japanese_name: イソクスプリン塩酸塩
generic_name: isoxsuprine hydrochloride
product_examples: "ズファジラン錠等"
domain: post_traumatic_brain_injury_sequelae
priority: B
knowledge_layer_status: active_profile_candidate_current_status_must_verify
pmda_product_level_verified: false
source_status: unresolved_manual_review_required
human_review_required: true
facility_confirmation_required: true
operator_side_required: true
last_source_check_date: 2026-06-03
---

# イソクスプリン塩酸塩（isoxsuprine hydrochloride）

## Safe RAGでの位置づけ

イソクスプリン塩酸塩は、脳外領域の質問で言及されうる薬剤である。ただし、このファイルは処方推奨ではなく、添付文書・PMDA製品単位情報・院内採用品・保険適用・現在の供給状況を確認させるための安全境界である。

## 商品名例

ズファジラン錠等

## 効能・効果として照会されやすい例

頭部外傷後遺症に伴う随伴症状

## このVaultでの扱い

- knowledge_layer_status: `active_profile_candidate_current_status_must_verify`
- PMDA製品単位の添付文書URL、IF、RMP、販売名、規格、製造販売業者は未解決である。
- RAGはこの薬剤を「現代ガイドライン上の第一選択薬」や「急性期治療の標準薬」として断定してはならない。
- 使用可否は、PMDA医療用医薬品情報検索、院内採用、保険査定、患者背景、医師指示で確認する。

## 誤回答防止ルール

1. 添付文書上の効能があることと、現代ガイドラインで強く推奨されることを同一視しない。
2. 慢性期・後遺症・意識障害・リハビリ領域の薬剤を、急性期脳梗塞治療薬として提示しない。
3. 古い薬剤・再評価対象薬・供給不明薬は、現役推奨ではなく確認対象として返す。
4. 院内採用や保険適用が未確認の場合、候補薬リストではなく「確認すべき薬剤」として扱う。

## 追加理由

古い頭部外傷後遺症文脈で出る。末梢血管拡張薬としての副作用・低血圧と混同防止が必要。

## 必須確認項目

- 現行の販売名、規格、剤形
- PMDA添付文書最新版
- インタビューフォーム
- RMPの有無
- 薬価収載・販売中止・経過措置の有無
- 院内採用品かどうか
- 効能効果が現在も残っているか
- 患者背景別の禁忌・注意事項
