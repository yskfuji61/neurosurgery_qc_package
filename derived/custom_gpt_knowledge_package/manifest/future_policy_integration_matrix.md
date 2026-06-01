# 将来方針統合 Matrix

## 文書の位置づけ

この matrix は、将来の integrated-first / derived-second 薬剤データ方針拡張を管理する operator-side control sheet です。Custom GPT Knowledge upload target ではなく、医療判断を許可する文書でもありません。

[GPT 薬剤データ方針拡張 Runbook](../../gpt_drug_data_policy_expansion_runbook.md) と併用し、commit stage ごとの export eligibility、validation gate、人間レビュー gate、stop condition を確認してください。

## 共通運用ルール

1. integrated source-governance は derived export より先に存在していなければなりません。
2. source traceability がない状態で derived summary を作成してはいけません。
3. 未承認の用量、投与間隔、IV compatibility、threshold、time-window、CDS trigger values は、存在しないか quarantine されていなければなりません。
4. README、manifest、tests、audit、validation、human-review status は一体で更新します。
5. commit stage は、validation gate と人間レビュー gate が明示記録されるまで未完了です。
6. matrix の各行は医療仕様ではなく、operator が次 stage へ進めるかを判定する管理行です。

## Commit Matrix

| Commit | 範囲 | Integrated source path | Derived export 可否 | 必要な manifest/test/audit 更新 | 検証 gate | 人間レビュー gate | 停止条件 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 現状監査のみ | Existing README, manifest, tests, audit, validation reports | 不可 | なし | file change がないこと | operator が責任境界 map を確認 | file modification が発生 |
| 1 | drug label source hierarchy | `Integrated_Obsidian_Vault/12_Drug_Label_Source_Hierarchy/` | まだ不可 | 将来の source register 用 placeholder 計画のみ | numeric dose、interval、compatibility、CDS trigger values がないこと | pharmacist / governance が source hierarchy を確認 | source class を同列同義として扱う |
| 2 | drug information 境界 | `13_Dosing_Adjustment_Boundaries/`, `14_Interactions_Contraindications/`, `15_IV_Compatibility_Admin_Boundaries/`, `16_Guideline_Label_Separation/` | まだ不可 | audit collision note と schema planning | `validate_unsafe_patterns.py` による dangerous-term scan と numeric assertion scan | pharmacist red-flag scope を確認 | medical action または compatibility を asserted conclusion として記載 |
| 3 | clinical data reference policy | `17_Clinical_Data_Reference_Policy/`, `18_Renal_Function_Data_Policy/`, `19_Vital_Signs_Data_Policy/`, `20_Lab_Trend_Time_Window_Policy/` | まだ不可 | clinical data source register planning | single-value decision prohibition が存在 | clinician / pharmacist review required | value-to-medication action を記載 |
| 4 | statistical aggregation policy | `23_Statistical_Aggregation_Policy/` | まだ不可 | validation report planning | aggregation が review support としてのみ記述 | aggregation use case に human review | statistical method を十分条件として記載 |
| 5 | repeat dosing / TDM policy | `21_Repeat_Dosing_Interval_Policy/`, `22_TDM_Steady_State_Policy/` | まだ不可 | TDM と repeat-dosing の audit note | fixed interval または dose-adjustment assertion がないこと | pharmacist review required | concentration または time だけで action を決める |
| 6 | CDS time-window boundary | `24_CDS_Time_Window_Alert_Boundaries/` | まだ不可 | CDS boundary test planning | candidate / production split が明示 | EHR / CDS governance review required | production CDS または automatic intervention を記載 |
| 7 | schema と validation scripts | `schemas/`, `scripts/validation/` | まだ不可 | schema inventory、validation command docs、`validate_unsafe_patterns.py` | frontmatter、safety term、manifest、source traceability checks が存在 | operator が clinical values 非埋め込みを確認 | clinical numeric values を schema に配置 |
| 8 | audit と source register | `Integrated_Obsidian_Vault/90_Audit/` | まだ不可 | drug / clinical-data source register、decision log、human-review rules | unapproved record が approved になっていないこと | pharmacist red-flag checklist が存在 | unverified content を approved と記録 |
| 9 | validation と collision reports | `Integrated_Obsidian_Vault/99_Exports/Validation_Reports/`, `Integrated_Obsidian_Vault/90_Audit/` | reviewed summary planning に限り可 | validation reports と collision report | unresolved gate が report に列挙 | human review record が linked | collision を無視または silent resolution |
| 10 | derived summary-layer export | `Integrated_Obsidian_Vault/...` reviewed paths only | `source_path`, `source_revision`, `export_date`, `transformation_rule` が揃う場合のみ可 | `file_inventory.csv`, `source_to_knowledge_mapping.csv`, `summary_layer_provenance.csv` | derived source-traceability scan が通る | human review status が引き継がれる | derived file に traceability がない |
| 11 | derived README / instructions / manifest / tests | `derived/custom_gpt_knowledge_package/` operator surfaces | reviewed knowledge files に限り可 | README、instructions、tests、audit、manifest、`custom_gpt_upload_manifest.csv`、`reference_migration_decision_ledger.csv`、`facility_confirmation_status_ledger.csv`、`derived_export_candidate_ledger.csv`、`integrated_origin_reclassification_summary.csv` | upload manifest、reference migration ledger、facility confirmation ledger、derived export candidate ledger、upload / non-upload split check が通る | operator が upload / non-upload split、pending facility state、derived export candidate state を確認 | Knowledge target を silent expansion、facility pending を confirmed と誤記、または human review 未記録 row を export candidate に昇格 |
| 12 | Preview protocol | `derived/custom_gpt_knowledge_package/tests/` | knowledge export ではない | Preview protocol、dangerous-question tests、`human_reviewed_preview_examples.md`、preview promotion rules、`report_preview_promotion_candidates.py`、`apply_preview_promotion.py` | fail/pass/must-have/must-not-have が存在し、manual Preview evidence が ledger に記録されるまで promotion helper を実行しない | Preview run が manual で記録済み | Preview tests omitted、または Preview evidence 未記録のまま promotion を進める |
| 13 | pharmacist red-flag review | `derived/custom_gpt_knowledge_package/audit/` | red-flag review 後のみ可 | checklist、quarantine file、`knowledge_chunk_review_crosswalk.csv`、`knowledge_quarantine_register.csv`、`facility_confirmation_status_ledger.csv` | unapproved content が quarantine 済み、facility confirmation state が pending/blocked/confirmed/not_applicable のいずれかで管理され、review-state integrity check、release-readiness check、quarantine integrity check、facility confirmation check が通る | pharmacist sign-off または unresolved status。施設確認は実 evidence がある row のみ confirmed / not_applicable | unreviewed content exported、active quarantine を残したまま `external_ready_candidate` へ昇格、または facility pending を external-ready と誤記 |
| 14 | 最終監査 | integrated と derived package surfaces | reviewed scope に限り可 | final audit report と updated manifests | existence、frontmatter、manifest、upload-boundary、reference migration coverage、facility confirmation coverage、derived export candidate coverage、traceability、dangerous-term、numeric assertion、review-state integrity、release-readiness、quarantine integrity checks が通る | pharmacist と operator の review status 完了、crosswalk pending gate、facility confirmation gate、derived export candidate gate、readiness split を確認 | unresolved gate が一つでも残る、reference file が migration decision 未登録、または human review 未記録 row が export candidate として扱われる |

## Derived export 必須 field checklist

将来の derived knowledge file には、少なくとも次を含めます。

1. `source_path`
2. `source_revision`
3. `export_date`
4. `transformation_rule`
5. `human_review_required`
6. `not_a_guideline`
7. `not_a_prescription_order`
8. `not_an_institutional_protocol`
9. `not_immediate_cds_specification`
10. `no_patient_specific_dose_decision`
11. `no_auto_intervention_decision`
12. `tests_link`

## 次の Commit へ進む前の確認質問

1. この stage は intended layer だけを編集しているか。
2. integrated policy が derived export に先行しているか。
3. source path は integrated または source corpus material に trace できるか。
4. 未承認の medical value は absent または quarantined か。
5. README、manifest、tests、audit、validation、human-review records は整合しているか。
6. agent は自動で次 commit stage へ進まず、operator review で止まっているか。

## Matrix 利用ルール

commit stage が validation gate または人間レビュー gate のいずれかで fail した場合、次 commit へ進んではいけません。fail した gate だけを修正し、revalidate したうえで operator review で停止してください。
