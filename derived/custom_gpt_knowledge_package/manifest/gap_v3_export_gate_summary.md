# Gap V3 Export Gate Summary（operator-side）

**Not a Custom GPT Knowledge upload target.**

## Archive canonical manifests

| File | Rows / purpose |
|------|----------------|
| `reference_archive/.../09_MANIFESTS/collision_resolution_ledger.csv` | 7 domain collisions |
| `reference_archive/.../09_MANIFESTS/export_denylist.csv` | Export prohibitions |
| `reference_archive/.../09_MANIFESTS/export_allowlist.csv` | Conservative allow (routing only) |
| `reference_archive/.../09_MANIFESTS/reference_profile_parking_register.csv` | 139 profiles virtual parking |
| `reference_archive/.../09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv` | 7 rows; all `safe_to_promote=false` |
| `reference_archive/.../09_MANIFESTS/reference_parking_gate_audit.csv` | Parking rule audit |
| `reference_archive/.../09_MANIFESTS/suspicious_allowlist_entries.csv` | Allowlist human review queue |
| `reference_archive/.../08_VALIDATION_CHECKS/collision_regression_tests.csv` | 21 regression prompts (definition) |
| `reference_archive/.../08_VALIDATION_CHECKS/collision_regression_results_TEMPLATE.csv` | Run template (`pass_fail` blank) |
| `reference_archive/.../11_INTEGRATION_GUIDES/GAP_V3_PROMOTION_BLOCKERS.md` | Promotion/export blockers |
| `reference_archive/.../10_FINAL_REPORTS/COLLISION_RESOLUTION_FINAL_AUDIT_REPORT.md` | Collision gate audit |
| `reference_archive/.../10_FINAL_REPORTS/GAP_V3_REVIEW_READY_AUDIT_REPORT_20260605.md` | Review-ready audit |

## Integrated (review workflow)

| File | Purpose |
|------|---------|
| `Integrated_Obsidian_Vault/90_Audit/Collisions/gap_v3_*.md` | Checklists (unchecked) |
| `Integrated_Obsidian_Vault/90_Audit/gap_v3_pharmacist_facility_review_log_20260605_REVIEW_READY.md` | Review-ready operator log (not sign-off) |

## Stage 2 classification（operator-side）

| Artifact | Purpose |
|----------|---------|
| `manifest/classification_vocabulary_registry.md` | Closed-set vocabulary + mapping rules |
| `manifest/reference_migration_decision_ledger.csv` | Column `classification_vocabulary` on 557 rows |
| `manifest/integrated_origin_reclassification_summary.csv` | Vocabulary breakdown by scope |
| `tests/validate_classification_vocabulary.py` | No promotion; export_candidate stays no |

## Validators

```bash
python3 tests/validate_classification_vocabulary.py
python3 tests/validate_collision_governance.py
python3 tests/validate_gap_v3_review_ready.py
```

## Policy

- All 7 V3 domain profiles: **DO_NOT_EXPORT** until PMDA + facility gates cleared
- `apply_preview_promotion.py` — blocked without Preview evidence
- `custom_gpt_upload_safe` — not set true by this work
- **Review-ready ≠ integration complete**
