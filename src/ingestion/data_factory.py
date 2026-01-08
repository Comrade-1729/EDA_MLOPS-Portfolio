from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = PROJECT_ROOT / "datasets"

def load_data(subdir: str, filename: str) -> pd.DataFrame:
    """
    Load CSV from datasets/ directory.
    subdir example: 'raw/climate' or 'processed/health'
    """
    return pd.read_csv(
        DATASETS_DIR / subdir / filename,
        engine="python",
        sep=";",
        on_bad_lines="skip"
    )
