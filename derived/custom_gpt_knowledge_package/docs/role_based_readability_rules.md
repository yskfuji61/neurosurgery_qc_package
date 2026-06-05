# Role-Based Readability Rules

## Purpose

Help pharmacists, physicians, nurses, residents, and clinical informatics staff reach the information they need without converting Knowledge into orders, protocols, or CDS specifications.

## Role-Based Information Design

| Role | Needed information | Allowed in Knowledge | Forbidden in Knowledge |
|---|---|---|---|
| 薬剤師 | 薬事、相互作用、腎機能・肝機能、施設確認事項 | 確認軸・注意点 | 個別用量・個別処方判断 |
| 医師 | 病態別の論点、除外条件、専門医確認 | 論点整理・確認条件 | 処方指示・投与決定 |
| 看護師 | 観察体制、連絡が必要な論点 | 観察体制を確認すべきという境界 | 看護手順・観察頻度・投与速度 |
| 研修医 | 上級医へ相談すべき論点 | 相談が必要な領域の明示 | 独自判断を促す指示 |
| 医療情報担当者 | CDS候補と本番仕様の境界 | 要件定義・承認・監査が必要という境界 | 実装条件・発火条件の確定 |

## Expression Rules

- Do not write `看護師は〜する`; write `看護体制・観察体制の確認が必要`.
- Do not write `研修医は〜すべき`; write `上級医・専門医確認が必要な論点`.
- Do not write `CDSを発火させる`; write `CDS候補として扱うには、要件定義、責任者承認、監査ログ設計、受入テストが必要`.

## Review Boundary

Role-based readability improves navigation. It does not approve clinical use, prescribing, nursing operation, or CDS implementation.
