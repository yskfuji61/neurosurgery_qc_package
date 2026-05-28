# RAG Export Audit Checklist

## export 前チェック

1. Knowledge upload 対象が `knowledge/` 配下の 13 ファイルだけになっている。
2. `README.md` に upload 対象が明記されている。
3. 各 knowledge ファイルに共通 YAML front matter が入っている。
4. `03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md` が高リスク誤読を網羅している。
5. `11_CDS_CANDIDATE_BOUNDARIES.md` が CDS 境界を明示している。
6. `12_AI_ERROR_TESTS_AND_VALIDATION.md` と `tests/` が整合している。
7. `manifest/source_to_knowledge_mapping.csv` が source path を追跡できる。
8. 元 source files を編集していない。
9. high-traffic knowledge files の冒頭に clinician-facing な summary または自然文導入がある。
10. instructions が risk-based 出力モードと内部語の言い換え方針を含む。
11. `tests/expected_answer_samples.md` と `tests/response_style_regression_assets.md` が存在し、現行 test suite と整合する。
12. `tests/human_reviewed_preview_examples.md` が存在し、human review required の family を記録できる。
13. `manifest/summary_layer_provenance.csv` が存在し、pilot summary sections の provenance を追跡できる。
14. `tests/preview_execution_runbook.md` が存在し、PREVIEW-001 から PREVIEW-004 の実 run 手順が固定されている。
15. `manifest/summary_layer_provenance.csv` に 04、05、06、07、10、11 の `実際の考え方` section が secondary naturalized section として登録されている。
16. Preview review の approved 判定に must-have 100% 充足、must-not-have 0 件、PHI / 施設固有未公開情報 0 件の gate がある。
17. `pending` を使う条件が `model_identifier`、leakage 判定、normalized 境界の不確定に限定されている。

## export 後チェック

1. Preview で 10 テストを再実行した。
2. fail 回答がない。
3. disclaimer が消えていない。
4. 一次資料確認と施設内確認が回答から落ちていない。
5. 一般整理質問で、冒頭が長い免責のみになっていない。
6. 高リスク質問で、短い結論の直後に必要な制約が入っている。
7. 閾値、Evidence、validation、audit の質問でも package 全体の文体が揃っている。
8. human review required の Preview run には review record が残っている。
9. summary layer を含む質問について、根拠 section を `manifest/summary_layer_provenance.csv` で辿れる。
10. approved record で `raw_output` と `lightly_normalized_output` の区別が保たれている。
11. secondary naturalized section を追加しなかった file も含めて、Preview review 後の decision log が残っている。
