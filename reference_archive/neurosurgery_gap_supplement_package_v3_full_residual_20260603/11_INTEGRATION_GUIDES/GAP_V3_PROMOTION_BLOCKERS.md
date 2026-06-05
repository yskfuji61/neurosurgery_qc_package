# Gap V3 Promotion Blockers（operator / pharmacist）

**This document is not clinical approval.** It blocks premature export and promotion while collision gates remain active.

## Current state (not integration complete)

- Gap V3 **collision governance gate** is in place; **full V3 body integration is not complete**.
- All **7** rows in `09_MANIFESTS/collision_resolution_ledger.csv` have `export_status=DO_NOT_EXPORT`.
- All **139** rows in `09_MANIFESTS/reference_profile_parking_register.csv` have `export_allowed=no`.
- `gap_v3_human_review_readiness_matrix.csv`: all rows `safe_to_promote=false`.

## Human / facility / clinical gaps (as of review-ready slice)

| Gate | Status |
|------|--------|
| Pharmacist sign-off | **NOT_SIGNED_OFF** (repo-local logs are not sign-off) |
| Facility evidence (formulary / SOP) | **NO_FACILITY_EVIDENCE** |
| Specialist review | **NOT_COMPLETED** |
| PMDA product-level resolution (V3 profiles) | **UNRESOLVED** for held domains |
| RAG collision regression (21 prompts) | **NOT_RUN** — definition + TEMPLATE only |
| Preview evidence | **None** — do not promote |
| `custom_gpt_upload_safe` | Must remain **false** |
| `external_ready_candidate` | Must remain **0** |

## Forbidden without evidence

1. **`apply_preview_promotion.py --apply`** — no Preview run recorded in `human_reviewed_preview_examples.md`.
2. Changing `export_status` on collision ledger rows to export-ready values.
3. Setting `safe_to_promote=true` in readiness matrix.
4. Copying CHILD `package_summary.json` PMDA counts into V3 or integrated layer.
5. Merging `02_DRUG_PROFILES_SAFE_KNOWLEDGE/**/*.md` into disease note bodies (including `脳腫瘍周術期.md`).
6. Treating procedural / intraventricular / ITB / botulinum / 5-ALA / ICG / contrast notes as universal hospital standard orders.
7. Recommending **bosentan** for SAH vasospasm instead of **clazosentan** context routing.
8. Promoting **chronic/historical** circulation drugs as acute stroke first-line therapy.

## Conditions before any `export_status` change (all required)

1. **Pharmacist sign-off** with named reviewer, date, and scope (collision_id list).
2. **Facility evidence links** (formulary, SOP, committee minutes, or approved pathway PDF) per domain.
3. **PMDA product-level URLs** per drug key (no filename inference; no CHILD count promotion).
4. **Specialist review** where ledger `owner_role` includes endocrinology, ID, radiology, neuro-ICU, rehab, etc.
5. **RAG regression results file** copied from `collision_regression_results_TEMPLATE.csv` to `collision_regression_results_YYYYMMDD.csv` with all 21 rows `pass_fail` filled by human reviewer (no fabricated PASS).
6. **Ledger row update only** — no bulk profile port to integrated disease notes.
7. Re-run: `validate_collision_governance.py`, `validate_gap_v3_review_ready.py`, `validate_reference_migration_ledger.py --corpus all`.

## `safe_to_promote=true` (current answer: none)

No collision row may set `safe_to_promote=true` until **all** conditions above are met for that row. As of review-ready delivery: **no row qualifies**.

## Rollback

```bash
# Remove review-ready slice (from repo root)
rm references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv
rm references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/reference_parking_gate_audit.csv
rm references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/suspicious_allowlist_entries.csv
rm references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/08_VALIDATION_CHECKS/collision_regression_results_TEMPLATE.csv
rm references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/11_INTEGRATION_GUIDES/GAP_V3_PROMOTION_BLOCKERS.md
# Revert checklist append on collision MDs (git checkout) if needed
```

Collision gate from prior slice (`collision_resolution_ledger.csv`, deny/allow lists) is independent; deleting only review-ready files does not remove DO_NOT_EXPORT defaults.

## Related paths

- `09_MANIFESTS/collision_resolution_ledger.csv`
- `09_MANIFESTS/gap_v3_human_review_readiness_matrix.csv`
- `08_VALIDATION_CHECKS/collision_regression_tests.csv`
- `08_VALIDATION_CHECKS/collision_regression_results_TEMPLATE.csv`
- `10_FINAL_REPORTS/GAP_V3_REVIEW_READY_AUDIT_REPORT_*.md`
- Integrated: `90_Audit/gap_v3_pharmacist_facility_review_log_*_REVIEW_READY.md`
