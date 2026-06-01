# Human Review Log Template

## Review Record

1. Review date:
2. Reviewer:
3. Trigger:
4. Updated files: package root relative path で記録する。
5. Primary sources checked:
6. Facility confirmations checked:
7. Preview tests rerun:
8. Result:
9. Follow-up needed:

## Preview Review Addendum

1. Review record IDs in `tests/human_reviewed_preview_examples.md`:
2. Sample families reviewed:
3. Model identifier used in Preview:
4. Any PHI or facility-specific leakage detected:
5. Any provenance records updated in `manifest/summary_layer_provenance.csv`:
6. Must-have coverage by review record:
7. Any must-not-have violations detected:
8. Was raw output preserved separately from lightly normalized output:
9. If `pending` was used, which allowed reason applied:
10. If additional secondary naturalized sections were considered, which files were evaluated and what was the decision:
11. Which rows in `manifest/knowledge_chunk_review_crosswalk.csv` changed state during this review:
12. What did `tests/report_preview_promotion_candidates.py` report before any state change:
13. Which rows were dry-run checked with `tests/apply_preview_promotion.py`, and what blocking reasons remained or cleared:
14. Which rows were actually updated by `tests/apply_preview_promotion.py --apply`:
15. Did `tests/validate_review_state_integrity.py` pass before closeout:
16. Which rows changed `release_readiness` or `resolution_status`, and why:
17. Did `tests/validate_release_readiness.py` pass before closeout:
18. Which rows were added or updated in `manifest/knowledge_quarantine_register.csv`:
19. Did `tests/validate_quarantine_integrity.py` pass before closeout:

## Path Recording Note

1. `Updated files` は package root relative path で記録する。例: `tests/pass_fail_criteria.md`、`manifest/summary_layer_provenance.csv`
2. `manifest/summary_layer_provenance.csv` の `source_paths` は package relative link ではなく、repo-root-relative な traceability metadata として扱う。
