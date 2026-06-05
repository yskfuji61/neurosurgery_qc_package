# DRAFT: PARENT / CHILD Reference Corpus Diff Report

> **Superseded for current-state counts (2026-06-05):** Phase 0 expected PARENT 174 / combined 540 ledger rows. Current validation: PARENT **191** files, combined ledger **557/557**. This DRAFT remains historical Phase 0 diff only.

**Status:** operator-side DRAFT (Phase 0)  
**Generated:** 2026-06-04  
**PARENT:** `references/neurosurgery_qc_package/reference_archive/neurosurgery_gap_supplement_package_v3_full_residual_20260603`  
**CHILD:** `references/neurosurgery_safe_rag_pmda_product_source_register_resolved`  
**TARGET:** `references/neurosurgery_qc_package`

---

## 1. Top-level directory diff

| Category | Directories |
|----------|-------------|
| **PARENT only** | `11_INTEGRATION_GUIDES`, `scripts` |
| **CHILD only** | `04_OPERATOR_SIDE_ONLY`, `05_QUARANTINE`, `06_CUSTOM_GPT_UPLOAD_SET`, `11_PMDA_RESOLUTION_LOGS`, `13_PMDA_PRODUCT_REGISTER` |
| **Common** | `00_START_HERE`, `01_SOURCE_REGISTERS`, `02_DRUG_PROFILES_SAFE_KNOWLEDGE`, `03_CLASS_NOTES`, `07_VSCODE_AGENT_INTEGRATION`, `08_VALIDATION_CHECKS`, `09_MANIFESTS`, `10_FINAL_REPORTS`, `12_RESEARCH_EVIDENCE` |

| Corpus | File count (machine) |
|--------|----------------------|
| PARENT | 174 |
| CHILD | 366 |

---

## 2. `02_DRUG_PROFILES_SAFE_KNOWLEDGE/` taxonomy

PARENT uses **clinical-domain** folders (19). CHILD uses **pharmacologic-class** folders (9) plus `pmda_unresolved_profiles`.

### PARENT (19 domains)

`acute_ischemic_stroke`, `antimicrobials_cns_infection`, `chronic_post_stroke_symptoms`, `consciousness_recovery_neurorehab`, `csf_iih`, `endocrine_electrolyte`, `healthcare_associated_cns_infection`, `historical_reassessment_negative_notes`, `neuro_oncology`, `neurocritical_care_anesthesia`, `perioperative_visualization_contrast`, `peripheral_circulation_do_not_confuse`, `pituitary_endocrine`, `post_traumatic_brain_injury_sequelae`, `reversal_hemostasis_blood_products`, `sah_vasospasm`, `spasticity_functional_neurosurgery`, `status_epilepticus`, `vasospasm_endovascular_procedural`

### CHILD (9 + unresolved)

`antiepileptics`, `antimicrobials_tdm`, `antithrombotics`, `chronic_prevention_supportive`, `hyperosmolar_icp_bp`, `pmda_unresolved_profiles`, `reversal_hemostasis_blood_products`, `sedation_analgesia_delirium`, `steroids_endocrine_metabolic`

### Overlap note

Only `reversal_hemostasis_blood_products` shares the same folder name. Taxonomies are **not merge-compatible** without explicit crosswalk.

| Metric | PARENT | CHILD |
|--------|--------|-------|
| Markdown profiles under `02/` | 123 | 212 |

---

## 3. `drug_key` set operations

Sources:

- V3_ALL: `PARENT/09_MANIFESTS/neurosurgery_gap_drug_supplement_master_V3_ALL.csv`
- V3_RESIDUAL: `PARENT/09_MANIFESTS/neurosurgery_gap_drug_supplement_master_V3_RESIDUAL.csv`
- CHILD: `CHILD/01_SOURCE_REGISTERS/pmda_product_source_register.csv`

| Set | Count |
|-----|-------|
| V3_ALL | 122 |
| V3_RESIDUAL | 58 |
| CHILD register | 127 |
| V3_ALL ∩ CHILD | 17 |
| V3_RESIDUAL ∩ CHILD | **0** |
| V3_ALL only | 105 |
| V3_RESIDUAL only | 58 |
| CHILD only (vs V3_ALL) | 110 |

### Sample: V3_RESIDUAL only (10)

`5-HT3 receptor antagonists`, `DBS perioperative antiparkinson medication note`, `EVD VP shunt infection note`, `HBV reactivation prophylaxis/monitoring`, `acetazolamide`, `adrenal insufficiency stress steroid note`, `amikacin`, `aminolevulinic acid`, `baclofen`, `bevacizumab`

### Sample: CHILD only vs V3_ALL (10)

`NSAIDs`, `acetaminophen`, `activated prothrombin complex concentrate`, `acyclovir`, `adrenaline`, `alteplase`, `amlodipine`, `amphotericin B`, `andexanet alfa`, `apixaban`

### Sample: intersection V3_ALL ∩ CHILD (10)

`albumin`, `amiodarone`, `ampicillin`, `atracurium`, `atracurium besylate`, `azithromycin`, `cefazolin`, `cefotaxime`, `ceftazidime`, `ceftriaxone`

**Implication:** V3_RESIDUAL (~58) is orthogonal to the 127 CHILD inventory keys. V3_ALL shares 17 keys with CHILD but uses different naming for many equivalents (e.g. `alteplase recombinant` vs `alteplase`). **Blind merge by drug_key is prohibited.**

---

## 4. CHILD files missing from TARGET ledger

Validator output (2026-06-04):

```
migration_ledger_findings=0
migration_ledger_rows=366
reference_file_count=366
migration_ledger_gate=PASS
```

**Missing from ledger: 0** (366/366).

### Future detection procedure

When CHILD gains files:

```bash
cd references/neurosurgery_qc_package/derived/custom_gpt_knowledge_package
python3 tests/validate_reference_migration_ledger.py
# missing_reference_path findings list gaps
```

After Phase 1, the same validator will cover PARENT (557 total rows expected; **current state 2026-06-05**).

---

## 5. PARENT → `reference_migration_decision_ledger` draft policy

174 files; **0** currently in ledger. Phase 1 adds one row per file without modifying existing CHILD rows.

| file_class | Path pattern | migration_mode | target_decision | Key flags |
|------------|--------------|----------------|-----------------|-----------|
| governance | `00_START_HERE/*` | `adapted_port` | `adapt_boundary_language_into_existing_docs` | `upload_safe=no`, `operator_side_only=yes`, `human_review_required=yes` |
| integration | `11_INTEGRATION_GUIDES/*` | `adapted_port` | `adapt_integration_rules_into_runbook` | same |
| class_note | `03_CLASS_NOTES/*` | `adapted_port` | `adapt_class_boundary_into_integrated_or_derived` | `facility_confirmation_required=yes` for clinical context |
| manifest | `09_MANIFESTS/*` | `no_port_keep_as_reference_only` | `keep_manifest_as_reference_inventory` | `unresolved_needed=yes` |
| source_register | `01_SOURCE_REGISTERS/*` | `no_port_keep_as_reference_only` | `keep_pmda_unresolved_register_as_reference` | `unresolved_needed=yes` |
| drug_profile | `02_DRUG_PROFILES_SAFE_KNOWLEDGE/**/*.md` (123) | `no_port_keep_as_reference_only` | `hold_as_reference_until_target_integrated_drug_profile_layer_exists` | mirror CHILD L35 pattern |
| validation | `08_VALIDATION_CHECKS/*` | `no_port_keep_as_reference_only` | `keep_reference_validation_as_history` | do not copy scripts to TARGET |
| scripts | `scripts/*` | `no_port_keep_as_reference_only` | `keep_reference_scripts_as_history` | operator-side only |
| audit_report | `10_FINAL_REPORTS/*` | `no_port_keep_as_reference_only` | `keep_audit_report_as_reference_history` | |
| research | `12_RESEARCH_EVIDENCE/*` | `no_port_unresolved` | `keep_evidence_targets_unresolved` | `unresolved_needed=yes` |
| vscode | `07_VSCODE_AGENT_INTEGRATION/*` | `operator_side_only_port` | `keep_agent_integration_as_operator_side` | |
| status_after_this_slice | (all PARENT rows) | — | — | `gap_v3_m0_ledger_recorded_pending_operator_review` |

**Phase 2 pilot (integrated):** only `neuro_oncology`, `pituitary_endocrine` domain boundaries—not bulk profile port.

---

## 6. Prohibited actions checklist

From PARENT `00_START_HERE/00_最初に読む_gap_supplement_v3_full_residual.md` (L16–18) and `11_INTEGRATION_GUIDES/V3統合手順.md` (L11–16):

- [ ] Do **not** guess or fill PMDA URLs, product names, or package inserts.
- [ ] Do **not** treat procedural / visualization notes as standard therapeutic drug profiles.
- [ ] Do **not** promote historical / negative notes to active first-line recommendations.
- [ ] Do **not** conflate domestic regulatory, insurance, in-hospital operations, and guideline recommendations.
- [ ] Do **not** copy CHILD `package_summary.json` `pmda_resolved_count` into TARGET as resolved fact.
- [ ] Do **not** set `custom_gpt_upload_safe: true` on TARGET from reference snapshots.
- [ ] Do **not** bulk-upload 174 PARENT or 366 CHILD files to Custom GPT Knowledge (13-file rule stands).
- [ ] Do **not** blind-merge V3_ALL and CHILD inventories despite 17 key overlaps (naming mismatch risk).

---

## Phase 0 gate

- **Files changed in TARGET:** this DRAFT only.
- **Next:** Phase 1 GO — validator dual-root + 174 PARENT ledger rows.
