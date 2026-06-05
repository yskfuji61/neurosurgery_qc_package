# Reference Profile Parking Policy（仮想バケット）

**物理パスは変更しない。** `reference_migration_decision_ledger.csv`（**557** 行・CHILD 366 + PARENT 191）の `reference_path` を維持する。

## 仮想バケット

| Bucket | 意味 | 実体の例 |
|--------|------|----------|
| `_HOLD_PMDA_UNRESOLVED` | PMDA 製品単位未解決 | `neuro_oncology/`, `pituitary_endocrine/`, `sah_vasospasm/` |
| `_HOLD_FACILITY_PROTOCOL_REQUIRED` | 施設プロトコル未確認 | `perioperative_visualization_contrast/`, `vasospasm_endovascular_procedural/`, `spasticity_functional_neurosurgery/`, `healthcare_associated_cns_infection/` |
| `_PROCEDURAL_REFERENCE_ONLY` | 手技・文脈 note | `03_CLASS_NOTES/*procedural*`, `*intraventricular*`, `造影剤_*` |
| `_PARKED_REFERENCE_ONLY` | historical / chronic / do-not-confuse | `historical_reassessment_negative_notes/`, `chronic_post_stroke_symptoms/`, `peripheral_circulation_do_not_confuse/` |

## 台帳

- ファイル単位: `09_MANIFESTS/reference_profile_parking_register.csv`
- 領域単位: `09_MANIFESTS/collision_resolution_ledger.csv`
- export: `09_MANIFESTS/export_denylist.csv`（本文 export 禁止）

## 標準 export 対象ではない

この README および `02_DRUG_PROFILES_SAFE_KNOWLEDGE/**/*.md` は Custom GPT Knowledge や疾患ノート本文への無批判コピー対象ではない。
