from pathlib import Path
import csv, shutil

SRC = Path(__file__).resolve().parents[1]
# このスクリプトは雛形です。実運用では TARGET_ROOT を元Vaultに変更してください。
TARGET_ROOT = Path.cwd() / "TARGET_NEUROSURGERY_VAULT"

print("This is a non-destructive integration helper template.")
print("1. Back up your target vault.")
print("2. Copy 02_DRUG_PROFILES_SAFE_KNOWLEDGE, 03_CLASS_NOTES, 08_VALIDATION_CHECKS, 09_MANIFESTS after manual review.")
print("3. Do not overwrite PMDA resolved files without human audit.")
print(f"Supplement root: {SRC}")
print(f"Target example: {TARGET_ROOT}")
