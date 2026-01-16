import pandas as pd

def min_max_normalize(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())


def build_composite_risk_index(
    df: pd.DataFrame,
    crime_col: str,
    accident_col: str,
    disaster_col: str,
) -> pd.DataFrame:
    """
    Phase 5: Build Composite Risk Index (CRI)

    Assumptions:
    - All inputs are country–year aligned
    - Higher value = higher risk
    """

    df_out = df.copy()

    for col in [crime_col, accident_col, disaster_col]:
        df_out[f"{col}_norm"] = (
            df_out
            .groupby("year")[col]
            .transform(min_max_normalize)
        )

    df_out["composite_risk_index"] = (
        df_out[f"{crime_col}_norm"]
        + df_out[f"{accident_col}_norm"]
        + df_out[f"{disaster_col}_norm"]
    ) / 3

    return df_out
