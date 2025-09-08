from __future__ import annotations
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"

RAW_FILE = RAW_DIR / "Dataset_INE_Graduados_ESO_43698.csv"
CLEAN_FILE = PROCESSED_DIR / "ine_43698_clean.csv"
