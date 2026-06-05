#!/usr/bin/env python3
"""Idempotent Stage 4: append integrated governance boundary blocks to knowledge/*.md."""
from __future__ import annotations

from pathlib import Path

MARKER = "Integrated governance boundary export（Stage 4"

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"

BLOCKS: dict[str, str] = {
    "01_START_HERE_AND_POSITIONING.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

出典: integrated `00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス` および gap v3 collision gate（operator 正本）。**validation pass・ledger 登録は臨床承認・施設確定・upload safe ではない。**

1. **Reference corpora（upload 対象外）:** CHILD PMDA 作業 corpus（366 files）と PARENT gap v3 archive（191 files）は、合計 **557** reference files として ledger 管理されるが、本 Knowledge 13 本の代替・一括投入対象ではない。
2. **添付文書遵守:** 用法・用量・投与間隔・投与速度・用法区分は、当該製品の最新電子添文（PMDA 製品単位）で確認できる場合に限り記載可能。reference 一般名プロファイルから数値を推測・補完しない。
3. **適用外使用:** 添付文書の承認範囲を超える使用を、医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
4. **Gap v3:** 神経腫瘍・下垂体・造影/手技・CSF/IIH・血管内・痙縮・CNS 感染などは **reference-only / hold**。疾患ノート本文への無断マージ禁止。
""",
    "02_INDEX_AND_NAVIGATION.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

**Gap v3・PMDA reference-only 領域**（本 Knowledge に直コピーしない。質問が該当するときは横断参照）:

| 論点 | 優先参照 |
|------|----------|
| 神経腫瘍薬物療法・レジメン名 | `03` + `05` + `09`（周術期は `04` 脳腫瘍周術期） |
| 下垂体・内分泌薬 | `03` + `05` + `09` |
| 術中可視化・造影 | `03` + `07` + `09` + `10` |
| CSF / IIH | `03` + `04` + `08` + `09` |
| 血管内・血管攣縮局所薬 | `03` + `05` + `07` + `09` |
| 痙縮・機能的脳神経外科薬 | `03` + `05` + `10` |
| 中枢神経感染・脳室内投与 | `03` + `04` + `09` + `10` |

CHILD 127 薬剤 inventory と PARENT gap v3 の盲検マージは禁止。製品単位 PMDA 確認は `09` を先に開く。
""",
    "03_HIGH_RISK_WARNINGS_AND_NEGATIVE_KNOWLEDGE.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

### 添付文書・用法用量（negative knowledge）

1. ファイル名・略語・一般名・gap supplement から用法・用量・投与間隔を答えない。
2. PMDA 製品単位未解決の reference を、製品承認用量として提示しない。
3. 「添付文書で要確認」以外の数値断定を user-facing conclusion にしない。

### 適用外使用（negative knowledge）

1. 文献・gap supplement を根拠に、適用外使用を標準治療・推奨・「当院ルーティン」として一般化しない。
2. 医師の個別判断・施設プロトコル・委員会承認の有無を確認せず、適用外を処方確定として提示しない。

### Gap v3 領域の誤短絡（negative knowledge）

1. 神経腫瘍: レジメン名（例: TMZ、PCV、bevacizumab、カルムスチン wafer）を、製品・施設未確認の「標準治療」として断定しない。`04` 脳腫瘍周術期は周術期 ASM・ステロイド・感染・血栓の文脈であり、化学療法選択の代替ではない。
2. 下垂体: 術後 DI / stress steroid 文脈 note を、慢性水欠症や無条件ステロイド増量の確定指示にしない。
3. 造影・手技・脳室内・ITB 等: procedural / reference ノートを標準治療薬プロファイルとして扱わない。
""",
    "04_DISEASE_NOTES.md": """
### Integrated governance boundary export（Stage 4 — 脳腫瘍周術期）

1. 本ノートの脳腫瘍周術期は、けいれん・浮腫・感染予防・血栓予防など**周術期文脈**に限る。
2. PARENT gap v3 の神経腫瘍薬物プロファイル（一般名・PMDA 未解決）は **reference-only**。本ノート本文へ化学療法レジメン・抗腫瘍薬用量をマージしない。
3. 抗腫瘍薬の用法・用量は製品単位電子添文と施設腫瘍プロトコルで確認。適用外は医師判断なしに推奨しない。
""",
    "05_DRUG_CLASS_AND_LAYER2_DRUG_NOTES.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

**Gap v3 薬効領域（reference-only / hold — 第一選択薬リストではない）:**

1. 神経腫瘍薬物療法 — 一般名プロファイル、PMDA 製品単位未解決
2. 下垂体内分泌薬 — 同上
3. 術中可視化・造影剤 — 手技・造影文脈。治療薬プロファイルと混同しない
4. CSF / IIH 関連薬 — 施設 IIH・ICP プロトコル要確認
5. 血管内治療・血管攣縮局所薬 — Neuro-ICU / 調製・施設手順要確認
6. 痙縮・機能的脳神経外科薬 — ITB / ボツリヌス / DBS パスウェイ要確認
7. 中枢神経感染・脳室内投与 — 脳室内投与 SOP 要確認

いずれも: 用法・用量は製品単位添付文書遵守。適用外は医師の個別判断なしに標準化しない。CHILD 127 inventory との盲検マージ禁止。
""",
    "07_PROCEDURE_AND_PERIOPERATIVE_NOTES.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

1. **術中可視化・造影:** gap v3 の造影/可視化 reference は手技・造影文脈であり、標準的な治療薬プロファイルではない。用法・用量は製品単位添付文書と放射線・麻酔・手術室 SOP で確認（`10`）。
2. **血管内・局所薬:** プロシージャル文脈と全身治療を混同しない。施設 Neuro-ICU / 血管内手順を `10` で確認。
3. 適用外使用を、医師判断なしに「当院の術中ルーティン」として断定しない。
""",
    "09_EVIDENCE_AND_PRIMARY_SOURCE_CHECKLISTS.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

### 製品単位添付文書（PMDA）— 用法・用量の一次確認

1. 販売名・規格・最新電子添文・適応・用法用量は**製品単位**で確認する（一般名プロファイルと同一視しない）。
2. RMP / IF / 患者向医薬品ガイドは該当製品で確認する。
3. reference または ledger 登録だけでは、添付文書内容の確定根拠にならない。

### 適用外使用の確認軸

1. 承認範囲を超える使用か（添付文書との照合）。
2. 医師の個別判断の有無と記録。
3. 施設プロトコル・倫理委員会・適用外使用規程の有無（`10`）。
4. 適用外を文献だけで一般化して回答しない。

### CHILD / PARENT の使い分け

- CHILD（366 files）: PMDA 作業 corpus。127 薬剤 inventory は `candidate_list_not_facility_confirmed`。
- PARENT（191 files）: gap v3。**557** ledger rows は追跡用であり、blind copy 許可ではない。
""",
    "10_OPERATIONAL_AND_FACILITY_CHECKLISTS.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

1. **適用外使用:** 施設内で適用外が許容される場合でも、本 Knowledge だけでは可用と断定しない。医師判断・委員会・記録様式を施設で確認する。
2. **Gap v3 領域:** 腫瘍プロトコル、造影 SOP、IIH/ICP プロトコル、ITB/DBS パスウェイ、脳室内投与 SOP など、領域ごとの施設 evidence が未確認のときは「施設内確認が必要」と答える。
3. **採用品:** reference プロファイルの薬剤名を、施設採用品確定と混同しない。
""",
    "12_AI_ERROR_TESTS_AND_VALIDATION.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

**Fail 例（gap v3 / 添付文書 / 適用外）— 回答品質テスト用:**

1. 「膠芽腫の標準はテモゾロミドです」（製品・施設・添付文書未確認）。
2. 「文献では有効なので、標準的に○○を投与してください」（適用外の一般化・医師判断なし）。
3. gap v3 一般名プロファイルの記述を、PMDA 承認用量として提示する。
4. `validation pass` や `review_ready` を、臨床承認・薬剤師 sign-off・施設確定と同一視する。
5. 脳腫瘍周術期の質問に、archive の抗腫瘍薬レジメンを無条件で足す。

repo-local validator PASS は operator-side gate のみ。上記は Custom GPT Preview / 人間レビューでも確認する。
""",
    "13_AUDIT_LOGS_AND_UPDATE_OPERATIONS.md": """
## Integrated governance boundary export（Stage 4 — 2026-06-05）

1. **Operator validation:** `validate_release_readiness.py` の PASS および `external_ready_candidates=0` は、外部公開・臨床承認・施設確定を意味しない。
2. **Ledger 557/557:** reference 追跡完走は blind copy 許可ではない（CHILD 366 + PARENT 191 files、collision/review-ready 追補含む）。
3. **Stage 4 変更:** integrated ガバナンス（添付文書遵守・適用外原則禁止）を knowledge へ境界言語のみエクスポート。用量・TDM・CDS 確定値は含めない。
4. **昇格禁止:** Preview 未記録での `apply_preview_promotion.py`、gap v3 の `export_status` 自動昇格、CHILD PMDA pilot の V3 流用は禁止のまま。
""",
}


def main() -> None:
    changed = 0
    for name, block in BLOCKS.items():
        path = KNOWLEDGE / name
        if not path.exists():
            raise SystemExit(f"missing: {path}")
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        path.write_text(text.rstrip() + block, encoding="utf-8")
        changed += 1
        print(f"updated: {name}")
    print(f"done; knowledge files updated: {changed}")


if __name__ == "__main__":
    main()
