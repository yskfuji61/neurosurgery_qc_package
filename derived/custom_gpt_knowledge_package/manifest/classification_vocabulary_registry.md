# Classification Vocabulary Registry（Stage 2）

**Operator-side only.** Not Custom GPT Knowledge. Not clinical approval.

## Allowed values（closed set）

| `classification_vocabulary` | Meaning |
|---------------------------|---------|
| `direct_boundary_port` | Structural port to integrated boundary with traceability |
| `adapted_boundary_port` | Adapted governance/boundary language only; no clinical fact import |
| `operator_side_only` | README/manifest/test/audit discipline; never upload target |
| `reference_only` | Keep in reference corpus; no TARGET body copy |
| `quarantine` | Active quarantine; must not clear without evidence |
| `unresolved_do_not_export` | PMDA/facility/preview incomplete; do not export |
| `hold_as_reference_until_integrated_layer_exists` | Drug profiles held until integrated drug-profile layer exists |

## Mapping from `reference_migration_decision_ledger.csv`

| `migration_mode` | Additional rule | `classification_vocabulary` |
|------------------|-----------------|------------------------------|
| `adapted_port` | — | `adapted_boundary_port` |
| `direct_structural_port` | — | `direct_boundary_port` |
| `operator_side_only_port` | — | `operator_side_only` |
| `no_port_unresolved` | — | `unresolved_do_not_export` |
| `no_port_quarantine` | — | `quarantine` |
| `no_port_keep_as_reference_only` | `file_class=drug_profile` or path under `02_DRUG_PROFILES_SAFE_KNOWLEDGE/` | `hold_as_reference_until_integrated_layer_exists` |
| `no_port_keep_as_reference_only` | otherwise | `reference_only` |

## Forbidden interpretations

- `classification_vocabulary` ≠ facility confirmed
- `classification_vocabulary` ≠ PMDA resolved
- `classification_vocabulary` ≠ `export_candidate=yes`
- Ledger 557/557 ≠ integration complete

## Regeneration

```bash
python3 scripts/_apply_stage2_classification_vocabulary.py
python3 tests/validate_classification_vocabulary.py
```
