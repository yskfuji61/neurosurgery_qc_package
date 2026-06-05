# Step 1 Inventory Snapshot

**Date:** 2026-06-04  
**Purpose:** Gap V3 collision governance — readonly baseline before gate artifacts.

## Layer inventory

| Layer | Root | File count | Notes |
|-------|------|------------|-------|
| PARENT archive | `reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603/` | 191 (2026-06-05; was 174 at snapshot) | PMDA product-level unresolved |
| integrated | `neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault/` | 261+ | Safe RAG body |
| CHILD sibling | `references/neurosurgery_safe_rag_pmda_product_source_register_resolved/` | 366 | 127-drug register; orthogonal to V3_RESIDUAL |
| derived ledger | `derived/custom_gpt_knowledge_package/manifest/reference_migration_decision_ledger.csv` | 557 rows (2026-06-05) | 366 CHILD + 191 PARENT paths |

## Archive structure (present)

- `00_START_HERE/` — yes
- `01_SOURCE_REGISTERS/` — yes (pmda v3 residual, gap supplement CSVs)
- `02_DRUG_PROFILES_SAFE_KNOWLEDGE/` — 123 `.md` profiles
- `03_CLASS_NOTES/` — 16 class notes
- `08_VALIDATION_CHECKS/v3_residual_rag_safety_tests.csv` — yes
- `09_MANIFESTS/` — V3_ALL, V3_RESIDUAL, package_file_manifest_v3
- `10_FINAL_REPORTS/` — GAP_SUPPLEMENT_V3 audit reports
- `11_INTEGRATION_GUIDES/V3統合手順.md` — yes

## Integrated (present)

- `90_Audit/Collisions/gap_v3_*.md` — **7** files
- `04_Drug_Classes/*_境界と出典階層.md` — **7** files
- `02_Diseases/脳腫瘍周術期.md` — present; **no oncology chemo hub**

## Missing before this work (now to create)

- `09_MANIFESTS/collision_resolution_ledger.csv`
- `09_MANIFESTS/export_denylist.csv` / `export_allowlist.csv`
- `09_MANIFESTS/reference_profile_parking_register.csv`
- `08_VALIDATION_CHECKS/collision_regression_tests.csv`
- `10_FINAL_REPORTS/COLLISION_RESOLUTION_FINAL_AUDIT_REPORT.md`
- `02_Diseases/下垂体・間脳下垂体疾患_REFERENCE_HUB.md`

## Intentional non-changes

- `02_Diseases/脳腫瘍周術期.md` — no PARENT drug profile merge
- No physical relocation of `02_DRUG_PROFILES_SAFE_KNOWLEDGE/*.md`
