# COLLISION RESOLUTION FINAL AUDIT REPORT

**Date:** 2026-06-04  
**Scope:** Gap V3 seven-domain collision governance (not full body merge)

## 1. Collisions processed

| collision_id | domain | final_status | export_status |
|--------------|--------|--------------|---------------|
| GAP-V3-COLLISION-NEURO-ONC-001 | neuro_oncology | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-PITUITARY-001 | pituitary_endocrine | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-PERIOP-VIS-CONTRAST-001 | perioperative_visualization_contrast | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-CSF-IIH-001 | csf_iih | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-VASOSPASM-ENDOVASCULAR-001 | vasospasm_endovascular | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-SPASTICITY-FUNCTIONAL-001 | spasticity_functional | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |
| GAP-V3-COLLISION-CNS-INFECTION-INTRAVENTRICULAR-001 | healthcare_associated_cns_infection | HOLD_REFERENCE_ONLY | DO_NOT_EXPORT |

## 2. Integrated (routing / gate only)

- 7× `04_Drug_Classes/*_境界と出典階層.md` — append: export deny, PMDA promotion conditions, routing, forbidden answers
- `02_Diseases/下垂体・間脳下垂体疾患_REFERENCE_HUB.md` — new routing hub (not treatment body)
- `00_Index/04_Gap_V3_Reference_Parked_Index.md` — parked/hold navigation
- 7× `90_Audit/Collisions/gap_v3_*.md` — collision_id + export_status frontmatter

## 3. Held (not merged)

- 123× `02_DRUG_PROFILES_SAFE_KNOWLEDGE/**/*.md` — virtual parking; physical paths unchanged
- 16× `03_CLASS_NOTES/*.md` — procedural / class reference-only
- `02_Diseases/脳腫瘍周術期.md` — **unchanged** (no oncology chemo merge)

## 4. Export prohibited

See `09_MANIFESTS/export_denylist.csv` — includes:

- All archive drug profiles glob
- All class notes
- RAG_OUTPUT patterns: bosentan-for-SAH, chronic-as-acute, historical-as-active
- Intraventricular vancomycin as universal order
- CHILD package_summary promotion to V3

## 5. PMDA product resolution required

Domains: `neuro_oncology/`, `pituitary_endocrine/`, `sah_vasospasm/`, plus any profile with `pmda_product_level_verified: false` in archive.

High-priority keys (non-exhaustive): temozolomide, bevacizumab, carmustine_wafer, cabergoline, octreotide, clazosentan.

## 6. Facility protocol confirmation required

Domains: perioperative_visualization_contrast, csf_iih, vasospasm_endovascular_procedural, spasticity_functional_neurosurgery, healthcare_associated_cns_infection.

## 7. Human review required

- Pharmacist sign-off on all 7 collisions (repo-local 2026-06-04 recorded; **not** clinical approval)
- Facility formulary / pathway evidence before any export_status change
- Preview evidence before `apply_preview_promotion.py`

## 8. Remaining risks

- RAG may still hallucinate standard therapy if boundary hubs not retrieved
- 17-key overlap between V3_ALL and CHILD register naming mismatch
- Integrated drug-profile layer still absent for physical port

## 9. Next minimal tasks

1. Run `collision_regression_tests.csv` against target RAG (manual or scripted)
2. Pharmacist + facility evidence → update `collision_resolution_ledger.csv` row-level only
3. PMDA pilot batches for oncology/pituitary subset (do not copy CHILD counts)

## 10. Rollback

```bash
# From repo root — restore specific paths if needed
git checkout -- references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/09_MANIFESTS/collision_resolution_ledger.csv
git checkout -- references/neurosurgery_qc_package/neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/04_Drug_Classes/
# Remove new files if rollback full slice:
# rm .../02_Diseases/下垂体・間脳下垂体疾患_REFERENCE_HUB.md
# rm .../00_Index/04_Gap_V3_Reference_Parked_Index.md
```

Deleting `collision_resolution_ledger.csv` removes domain-level gate (file-level migration ledger **557** rows unchanged).

## 11. Self-audit checklist (§6)

| Check | Yes/No |
|-------|--------|
| PMDA未解決を解決済みとして扱っていない | Yes |
| V3 profileを疾患ノート本文に直接マージしていない | Yes |
| procedural noteを標準処方・標準治療として扱っていない | Yes |
| 施設未確認noteをexportしていない | Yes |
| CHILD解決状況をV3に流用していない | Yes |
| ボセンタンをクラゾセンタン代替として扱っていない | Yes |
| chronic/historicalを急性期標準として扱っていない | Yes |
| 脳室内投与を全施設標準として扱っていない | Yes |
| allowlistは保守的か | Yes |
| denylistは十分か | Yes |
| collision_regression_tests.csv 作成済み (21件) | Yes |
| final audit report 作成済み | Yes |
| rollback方法明記 | Yes |

**Gate status:** Collision governance artifacts complete. **Not** "full integration complete" — reference profiles remain hold.

## 12. Artifact paths

- `09_MANIFESTS/collision_resolution_ledger.csv`
- `09_MANIFESTS/export_denylist.csv` / `export_allowlist.csv`
- `09_MANIFESTS/reference_profile_parking_register.csv`
- `08_VALIDATION_CHECKS/collision_regression_tests.csv`
- `02_DRUG_PROFILES_SAFE_KNOWLEDGE/README_REFERENCE_PROFILE_PARKING.md`
- `derived/custom_gpt_knowledge_package/tests/validate_collision_governance.py`
