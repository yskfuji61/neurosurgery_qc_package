# Collision regression results — operator instructions

## Files

| File | Role |
|------|------|
| `collision_regression_tests.csv` | **Definition only** (21 prompts) — do not add pass/fail here |
| `collision_regression_results_TEMPLATE.csv` | Empty run slots (`pass_fail` blank) |
| `collision_regression_results_YYYYMMDD.csv` | **Copy from TEMPLATE** after a real RAG run |

## How to run (human)

1. Copy `collision_regression_results_TEMPLATE.csv` → `collision_regression_results_YYYYMMDD.csv`.
2. Set `run_id`, `run_date`, `rag_system_name`, `rag_system_version`.
3. Execute each `prompt` against your target RAG (same corpus retrieval policy as production candidate).
4. Fill `actual_answer_summary` (short, factual).
5. Set `pass_fail` to `PASS` or `FAIL` only after human review — **do not pre-fill PASS**.
6. If `forbidden_behavior_observed=yes`, set `remediation_required=yes` and note in `remediation_note`.
7. Store logs under `evidence_link_or_log_path` (file path or ticket URL).

## Gate

- `validate_gap_v3_review_ready.py` checks TEMPLATE exists; it does **not** treat empty `pass_fail` as PASS.
- Export / promotion remains blocked until pharmacist + facility evidence + ledger update per `11_INTEGRATION_GUIDES/GAP_V3_PROMOTION_BLOCKERS.md`.
