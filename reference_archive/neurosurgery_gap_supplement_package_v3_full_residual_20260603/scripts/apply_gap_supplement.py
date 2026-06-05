#!/usr/bin/env python3
"""
Apply neurosurgery gap supplement to an existing Vault directory.
This script copies supplement files and creates proposed merged CSVs without deleting original files.

Usage:
  python scripts/apply_gap_supplement.py --vault /path/to/neurosurgery_safe_rag_pmda_product_source_register_resolved --supplement /path/to/neurosurgery_gap_supplement_package
"""
import argparse, shutil
from pathlib import Path
import pandas as pd

COPY_DIRS = [
    '02_DRUG_PROFILES_SAFE_KNOWLEDGE', '03_CLASS_NOTES', '08_VALIDATION_CHECKS', '12_RESEARCH_EVIDENCE'
]

def copytree_merge(src: Path, dst: Path):
    for p in src.rglob('*'):
        rel = p.relative_to(src)
        out = dst / rel
        if p.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            if out.exists():
                # never overwrite silently
                out = out.with_name(out.stem + '__gap_supplement' + out.suffix)
            shutil.copy2(p, out)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--vault', required=True)
    ap.add_argument('--supplement', required=True)
    args=ap.parse_args()
    vault=Path(args.vault)
    sup=Path(args.supplement)
    assert vault.exists(), f'Vault not found: {vault}'
    assert sup.exists(), f'Supplement not found: {sup}'

    for d in COPY_DIRS:
        if (sup/d).exists(): copytree_merge(sup/d, vault/d)

    # Merge manifests as proposed, not authoritative
    orig = vault/'09_MANIFESTS/drug_inventory_master.csv'
    add = sup/'09_MANIFESTS/neurosurgery_gap_drug_supplement_master.csv'
    out = vault/'09_MANIFESTS/drug_inventory_master_PROPOSED_WITH_GAP_SUPPLEMENT.csv'
    if orig.exists() and add.exists():
        df_orig=pd.read_csv(orig)
        df_add=pd.read_csv(add)
        common_cols=list(df_orig.columns)
        for col in common_cols:
            if col not in df_add.columns: df_add[col]=''
        merged=pd.concat([df_orig, df_add[common_cols]], ignore_index=True)
        merged=merged.drop_duplicates(subset=['drug_key'], keep='first')
        merged.to_csv(out, index=False, encoding='utf-8-sig')
        print(f'Wrote proposed merged manifest: {out}')

    orig_src = vault/'01_SOURCE_REGISTERS/pmda_product_source_register.csv'
    add_src = sup/'01_SOURCE_REGISTERS/pmda_product_source_register_gap_supplement.csv'
    out_src = vault/'01_SOURCE_REGISTERS/pmda_product_source_register_PROPOSED_WITH_GAP_SUPPLEMENT.csv'
    if orig_src.exists() and add_src.exists():
        df_orig=pd.read_csv(orig_src)
        df_add=pd.read_csv(add_src)
        common=list(df_orig.columns)
        for col in common:
            if col not in df_add.columns: df_add[col]=''
        merged=pd.concat([df_orig, df_add[common]], ignore_index=True)
        merged=merged.drop_duplicates(subset=['drug_key'], keep='first')
        merged.to_csv(out_src,index=False,encoding='utf-8-sig')
        print(f'Wrote proposed merged source register: {out_src}')

if __name__=='__main__':
    main()
