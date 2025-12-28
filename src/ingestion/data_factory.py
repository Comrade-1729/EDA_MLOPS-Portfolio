import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2] / "datasets"

def load_data(subdir: str, filename: str) -> pd.DataFrame:
    return pd.read_csv(
        BASE_DIR / subdir / filename,
        engine="python",          # fixes tokenizing error
        sep=";",                  # IMPORTANT
        on_bad_lines="skip"       # skip malformed rows
    )
