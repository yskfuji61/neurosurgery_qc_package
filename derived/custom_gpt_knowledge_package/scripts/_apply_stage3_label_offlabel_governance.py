#!/usr/bin/env python3
"""Idempotent Stage 3 append: label compliance + off-label governance to integrated boundaries and collisions."""
from __future__ import annotations

from pathlib import Path

MARKER = "## 添付文書遵守・適用外使用ガバナンス（Stage 3）"
COLLISION_INSERT_BEFORE = "## Human / Facility Review Checklist"

BOUNDARY_APPEND = """
---

## 添付文書遵守・適用外使用ガバナンス（Stage 3）

**正本:** [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

### 用法・用量・使用方法

- 具体的な用法・用量・投与間隔・投与速度・用法区分は、当該製品の**最新電子添文（PMDA 製品単位、施設で参照する版）**が確認できる場合に限り記載可能。
- 本境界ハブ・PARENT reference・一般名プロファイルから数値用量・固定閾値・投与ルートを推測・補完・断定しない。
- PMDA 製品単位が未解決の場合は「添付文書で要確認」への routing のみ。

### 適用外使用（添付文書の承認範囲を超える使用）

- 適用外使用を、医師の個別判断なしに標準治療・推奨治療・標準オーダー・「当院ルーティン」として提示しない（**原則禁止**）。
- gap supplement・文献・一般名ノートを根拠に、適用外を一般化・正常化しない。
- 適用外の可能性に言及する場合は処方確定ではなく、**医師の判断**・**施設プロトコル／委員会承認**・**製品単位添付文書との照合**を要する旨を併記する。

### 禁止回答例（本ドメイン）

- ファイル名・略語・一般名から用量・投与間隔を答える。
- 「文献では有効なので標準的に投与」のような適用外の一般化。
- PMDA 未解決プロファイルの記述を製品承認用量として提示する。

### AI / operator gate

- [ ] 回答に数値用量が含まれる場合、出典が当該製品電子添文（製品単位 URL 確認済み）である。
- [ ] 適用外に該当しうる内容は、医師判断・施設確認を案内しており、単独で処方確定していない。
"""

COLLISION_BLOCK = """
## 添付文書・適用外ガバナンス（Stage 3）

- **用法・用量・使用方法:** 製品単位の最新電子添文（PMDA）遵守。未解決 reference から数値・ルートを断定しない。
- **適用外使用:** 医師の個別判断なしに標準治療・推奨・標準オーダーとして提示しない（原則禁止）。
- **正本:** [[00_Index/05_PMDA_添付文書遵守と適用外使用ガバナンス]]

"""


def append_if_missing(path: Path, block: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text or (path.name.startswith("gap_v3_") and "## 添付文書・適用外ガバナンス（Stage 3）" in text):
        return False
    path.write_text(text.rstrip() + block, encoding="utf-8")
    return True


def insert_collision_block(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "## 添付文書・適用外ガバナンス（Stage 3）" in text:
        return False
    if COLLISION_INSERT_BEFORE not in text:
        raise SystemExit(f"anchor not found in {path}")
    updated = text.replace(COLLISION_INSERT_BEFORE, COLLISION_BLOCK + COLLISION_INSERT_BEFORE, 1)
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    qc = Path(__file__).resolve().parents[3]
    vault = qc / "neurosurgery_integrated_safe_rag_package/Integrated_Obsidian_Vault"
    boundaries = sorted((vault / "04_Drug_Classes").glob("*_境界と出典階層.md"))
    collisions = sorted((vault / "90_Audit/Collisions").glob("gap_v3_*_reference_collision.md"))
    changed = 0
    for p in boundaries:
        if append_if_missing(p, BOUNDARY_APPEND):
            changed += 1
            print(f"boundary: {p.name}")
    for p in collisions:
        if insert_collision_block(p):
            changed += 1
            print(f"collision: {p.name}")
    print(f"done; files updated: {changed}")


if __name__ == "__main__":
    main()
