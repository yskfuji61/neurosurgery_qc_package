# GAP-PMDA batch prep (Stage 6)

- **scope:** gap v3 `pmda_product_source_register_gap_supplement.csv` (36 keys)
- **vocabulary:** use `primary_verified_pending_pharmacist` in profile frontmatter; register `source_status` = `verified_primary_source` or `document_absent_domestic_unapproved` only
- **forbidden:** `resolved`, `custom_gpt_upload_safe`, knowledge export, `export_status` changes
- **CHILD transfer:** requires row in `11_INTEGRATION_GUIDES/STAGE6_RECONCILIATION_LOG.md`
- **batch size:** 3–4 keys (primary), then documents slice per batch ID
- **URL rule:** PMDA rdSearch/bookSearch URLs verified on pmda.go.jp before applier run (2026-06-05 web verification for gap-only keys)
