#!/usr/bin/env python3
"""Apply Stage 6 gap PMDA primary + document register rows. Run from gap archive root."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-06-05"
CHILD_REG = (
    Path(__file__).resolve().parents[3].parent
    / "neurosurgery_safe_rag_pmda_product_source_register_resolved"
    / "01_SOURCE_REGISTERS"
    / "pmda_product_source_register.csv"
)
GAP_REG = ROOT / "01_SOURCE_REGISTERS/pmda_product_source_register_gap_supplement.csv"
GAP_DOC_REG = ROOT / "01_SOURCE_REGISTERS/pmda_document_source_register_gap_supplement.csv"
RECON_LOG = ROOT / "11_INTEGRATION_GUIDES/STAGE6_RECONCILIATION_LOG.md"
PROFILE_ROOT = ROOT / "02_DRUG_PROFILES_SAFE_KNOWLEDGE"
MANIFEST_DIR = ROOT / "09_MANIFESTS"
CHILD_SUMMARY = (
    Path(__file__).resolve().parents[3].parent
    / "neurosurgery_safe_rag_pmda_product_source_register_resolved"
    / "09_MANIFESTS"
    / "package_summary.json"
)

DOC_TYPES = [
    "electronic_label",
    "interview_form",
    "rmp",
    "rmp_material",
    "patient_guide",
    "revision_history",
]

# gap-only: PMDA pages verified via pmda.go.jp fetch 2026-06-05 (operator-side)
GAP_ONLY = {
    "edaravone": {
        "product_name": "ラジカット点滴静注バッグ30mg",
        "generic_name_pmda": "エダラボン",
        "manufacturer": "田辺ファーマ株式会社",
        "formulation": "点滴静注バッグ",
        "strength": "30mg/袋（100mL）",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/1190401G1026?user=1",
        "batch": "GAP-001",
        "note_extra": "脳梗塞急性期代表製品。院内採用品・剤形（注/バッグ）要確認。",
    },
    "ozagrel": {
        "product_name": "カタクロット注射液40mg",
        "generic_name_pmda": "オザグレルナトリウム",
        "manufacturer": "丸石製薬株式会社",
        "formulation": "注射液",
        "strength": "40mg/2mL",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/3999411H3026?user=1",
        "batch": "GAP-001",
        "note_extra": "SAH/脳梗塞文脈で院内採用品・適応確認必須。",
    },
    "clazosentan": {
        "product_name": "ピヴラッツ点滴静注液150mg",
        "generic_name_pmda": "クラゾセンタンナトリウム",
        "manufacturer": "ネクセラファーマジャパン株式会社",
        "formulation": "点滴静注液",
        "strength": "150mg",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/2190418A1023?user=1",
        "batch": "GAP-001",
        "note_extra": "SAH術後脳血管攣縮。ボセンタンと混同禁止。",
    },
    "fasudil": {
        "product_name": "エリル点滴静注液30mg",
        "generic_name_pmda": "ファスジル塩酸塩水和物",
        "manufacturer": "旭化成ファーマ株式会社",
        "formulation": "点滴静注液",
        "strength": "30mg",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/2190414A1033?user=1",
        "batch": "GAP-002",
        "note_extra": "SAH術後脳血管攣縮。",
    },
    "nimodipine": {
        "product_name": "",
        "generic_name_pmda": "ニモジピン",
        "manufacturer": "",
        "formulation": "",
        "strength": "",
        "pmda_product_url": "",
        "batch": "GAP-002",
        "source_status": "document_absent_domestic_unapproved",
        "note_extra": "国内未承認（PMDA製品単位ページなし）。国際標準比較・文献索引のみ。",
    },
    "thiopental": {
        "product_name": "ラボナール注射用0.5g",
        "generic_name_pmda": "注射用チオペンタールナトリウム",
        "manufacturer": "ニプロ株式会社",
        "formulation": "注射用（溶解後静注）",
        "strength": "0.5g/管",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/1115400X2023?user=1",
        "batch": "GAP-005",
        "note_extra": "ICP/バルビツレートコマ代表。0.3g規格も同一rdSearch。",
    },
    "thiamylal": {
        "product_name": "イソゾール注射用0.5g",
        "generic_name_pmda": "注射用チアミラールナトリウム",
        "manufacturer": "日医工株式会社",
        "formulation": "注射用",
        "strength": "0.5g",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/1115403D3043?user=1",
        "batch": "GAP-005",
        "note_extra": "チトゾール等別販売名あり。院内採用品確認。",
    },
    "pentobarbital": {
        "product_name": "ラボナ錠50mg",
        "generic_name_pmda": "ペントバルビタールカルシウム",
        "manufacturer": "田辺ファーマ株式会社",
        "formulation": "錠剤",
        "strength": "50mg",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/1125006F1030?user=1",
        "batch": "GAP-005",
        "note_extra": "難治性ICP/てんかん重積ではIV製剤が施設方針と異なる場合あり。錠剤は代表primary。",
    },
    "remimazolam": {
        "product_name": "アネレム静注用20mg",
        "generic_name_pmda": "レミマゾラムベシル酸塩",
        "manufacturer": "ムンディファーマ株式会社",
        "formulation": "静注用粉末",
        "strength": "20mg",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/1119403F1024?user=1",
        "batch": "GAP-005",
        "note_extra": "50mg規格も同一rdSearch。",
    },
    "fludrocortisone": {
        "product_name": "フロリネフ錠0.1mg",
        "generic_name_pmda": "フルドロコルチゾン酢酸エステル",
        "manufacturer": "サンドファーマ株式会社",
        "formulation": "錠剤",
        "strength": "0.1mg",
        "pmda_product_url": "https://www.pmda.go.jp/PmdaSearch/rdSearch/02/2452003F1035?user=1",
        "batch": "GAP-005+",
        "note_extra": "CSW/低Na文脈。",
    },
}

BATCH_KEYS = {
    "GAP-001": ["edaravone", "ozagrel", "clazosentan"],
    "GAP-002": ["fasudil", "nimodipine", "alteplase"],
    "GAP-003": ["argatroban", "urokinase", "clobazam"],
    "GAP-004": ["diazepam", "lorazepam", "phenobarbital"],
    "GAP-005": ["thiopental", "thiamylal", "pentobarbital", "remimazolam"],
    "GAP-006": ["ketamine", "rocuronium", "sugammadex", "vitamin_k"],
    "GAP-007": ["ampicillin", "cefotaxime", "sulbactam_ampicillin", "metronidazole"],
    "GAP-008": ["levofloxacin", "tolvaptan", "furosemide", "levothyroxine"],
    "GAP-009": ["landiolol", "esmolol", "nitroglycerin", "nitroprusside"],
    "GAP-010": ["fresh_frozen_plasma", "platelet_transfusion", "red_blood_cell_concentrate"],
    "GAP-011": ["albumin"],
    "GAP-013": ["cryoprecipitate"],
}


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def child_batches() -> dict[str, list[str]]:
    data = json.loads(CHILD_SUMMARY.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = {}
    for b in data.get("pilot_batches", []):
        for k in b.get("resolved_drug_keys", []):
            out.setdefault(k, []).append(b["batch_id"])
    return out


def find_profile(key: str) -> Path | None:
    for p in PROFILE_ROOT.rglob(f"{key}.md"):
        return p
    return None


def update_profile_frontmatter(path: Path, source_status: str) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return
    end = text.find("\n---", 3)
    if end < 0:
        return
    fm = text[3:end]
    fm = re.sub(r"^source_status:.*$", f"source_status: {source_status}", fm, flags=re.M)
    fm = re.sub(
        r"^last_source_check_date:.*$",
        f"last_source_check_date: {DATE}",
        fm,
        flags=re.M,
    )
    if "pmda_product_level_verified: true" in fm:
        fm = re.sub(
            r"^pmda_product_level_verified: true$",
            "pmda_product_level_verified: false",
            fm,
            flags=re.M,
        )
    new_text = f"---{fm}{text[end:]}"
    path.write_text(new_text, encoding="utf-8")


def product_note(batch: str, extra: str = "") -> str:
    base = (
        f"pilot {batch}: PMDA primary verified {DATE} (operator-side pmda.go.jp check). "
        "IF/RMP/患者向けガイドは未個別確認。薬剤師・院内採用品・施設確認 pending。"
    )
    return f"{base} {extra}".strip()


def main() -> None:
    child = {r["drug_key"]: r for r in csv.DictReader(CHILD_REG.open(encoding="utf-8-sig"))}
    batches = child_batches()
    recon_rows: list[str] = []

    fields, gap_rows = read_csv(GAP_REG)
    doc_rows: list[dict] = []
    applied: dict[str, dict] = {}

    for r in gap_rows:
        key = r["drug_key"]
        batch_id = "GAP-?"
        for bid, keys in BATCH_KEYS.items():
            if key in keys:
                batch_id = bid
                break
        if key in GAP_ONLY:
            g = GAP_ONLY[key]
            batch_id = g.get("batch", batch_id)
            if g.get("source_status") == "document_absent_domestic_unapproved":
                r["source_status"] = "document_absent_domestic_unapproved"
                r["last_source_check_date"] = DATE
                r["notes"] = (
                    f"pilot {batch_id}: domestic product-level PMDA page absent ({DATE}). "
                    f"{g.get('note_extra', '')} Pharmacist/facility review pending."
                )
            else:
                r["pmda_product_url"] = g["pmda_product_url"]
                r["product_name"] = g["product_name"]
                r["generic_name_pmda"] = g["generic_name_pmda"]
                r["manufacturer"] = g["manufacturer"]
                r["formulation"] = g["formulation"]
                r["strength"] = g["strength"]
                r["approval_or_listing_status"] = "marketed_pmda_label_present"
                r["source_status"] = "verified_primary_source"
                r["last_source_check_date"] = DATE
                r["notes"] = product_note(batch_id, g.get("note_extra", ""))
                el_url = g["pmda_product_url"]
                for dt in DOC_TYPES:
                    doc_rows.append(
                        {
                            "drug_key": key,
                            "product_name": g["product_name"],
                            "manufacturer": g["manufacturer"],
                            "document_type": dt,
                            "document_url": el_url if dt == "electronic_label" else "",
                            "document_status": "document_present"
                            if dt == "electronic_label"
                            else "document_unchecked",
                            "last_source_check_date": DATE,
                            "notes": f"pilot {batch_id}: electronic_label from primary rdSearch {DATE}."
                            if dt == "electronic_label"
                            else f"pilot {batch_id}: 未個別確認。",
                        }
                    )
            applied[key] = {"batch": batch_id, "source": "gap_only_web_verify"}
        elif key in child and child[key].get("pmda_product_url"):
            c = child[key]
            cb = "|".join(batches.get(key, []))
            recon_rows.append(
                f"| {DATE} | {key} | {cb} | {c.get('product_name','')} | {c.get('pmda_product_url','')} | yes | CHILD primary copied; verify gap clinical context | Composer |"
            )
            for col in (
                "pmda_product_url",
                "product_name",
                "generic_name_pmda",
                "manufacturer",
                "formulation",
                "strength",
            ):
                if c.get(col):
                    r[col] = c[col]
            r["approval_or_listing_status"] = c.get(
                "approval_or_listing_status", "marketed_pmda_label_present"
            )
            r["source_status"] = "verified_primary_source"
            r["last_source_check_date"] = DATE
            r["notes"] = (
                product_note(batch_id)
                + f" Reconciled from CHILD pilot {cb}."
            )
            el_url = c.get("pmda_product_url", "")
            for dt in DOC_TYPES:
                doc_rows.append(
                    {
                        "drug_key": key,
                        "product_name": c.get("product_name", ""),
                        "manufacturer": c.get("manufacturer", ""),
                        "document_type": dt,
                        "document_url": el_url if dt == "electronic_label" else "",
                        "document_status": "document_present"
                        if dt == "electronic_label"
                        else "document_unchecked",
                        "last_source_check_date": DATE,
                        "notes": f"pilot {batch_id}: electronic_label from CHILD primary {DATE}.",
                    }
                )
            if key == "cryoprecipitate":
                r["notes"] += (
                    " CHILD A-PMDA-010: 院内作製クリオ；原料FFP代表URL。gap文脈は院内作製プロトコル確認 pending。"
                )
            applied[key] = {"batch": batch_id, "source": "child_reconcile"}
        # alteplase handled in overlap branch

        prof = find_profile(key)
        if prof:
            st = r.get("source_status", "unresolved")
            if st == "verified_primary_source":
                update_profile_frontmatter(prof, "primary_verified_pending_pharmacist")
            elif st == "document_absent_domestic_unapproved":
                update_profile_frontmatter(prof, "document_absent_domestic_unapproved")

    write_csv(GAP_REG, fields, gap_rows)
    doc_fields = [
        "drug_key",
        "product_name",
        "manufacturer",
        "document_type",
        "document_url",
        "document_status",
        "last_source_check_date",
        "notes",
    ]
    write_csv(GAP_DOC_REG, doc_fields, doc_rows)

    log = RECON_LOG.read_text(encoding="utf-8")
    if recon_rows:
        log = log.rstrip() + "\n" + "\n".join(recon_rows) + "\n"
        RECON_LOG.write_text(log, encoding="utf-8")

    for batch_id, keys in BATCH_KEYS.items():
        lines = [
            f"# PMDA pilot batch {batch_id}",
            "",
            f"- **batch_id:** `{batch_id}`",
            f"- **resolution_date:** {DATE}",
            f"- **scope:** gap supplement primary register",
            "",
            "| drug_key | product_name | pmda_product_url | source |",
            "| --- | --- | --- | --- |",
        ]
        for k in keys:
            info = applied.get(k, {})
            row = next((x for x in gap_rows if x["drug_key"] == k), {})
            lines.append(
                f"| {k} | {row.get('product_name','')} | {row.get('pmda_product_url','')} | {info.get('source','')} |"
            )
        (MANIFEST_DIR / f"pmda_pilot_batch_{batch_id}.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

    print(f"gap_register_updated={len(applied)}")
    print(f"gap_document_rows={len(doc_rows)}")
    print(f"reconciliation_rows={len(recon_rows)}")


if __name__ == "__main__":
    main()
