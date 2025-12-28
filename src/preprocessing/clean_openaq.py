import pandas as pd

def clean_openaq(df: pd.DataFrame) -> pd.DataFrame:
    return df[
        (df.get("Country Label", "").astype(str).str.strip().str.lower() == "india") |
        (df.get("Country Code", "").astype(str).str.strip().str.upper() == "IN")
    ].copy()
