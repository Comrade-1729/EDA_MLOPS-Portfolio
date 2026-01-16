import pandas as pd

def aggregate_disaster_emdat_country_year(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Phase 4 aggregation for EM-DAT disaster data.

    Aggregation rules (explicit):
    - Count of disaster events per country–year
    - Sum of total deaths per country–year
    - Sum of total affected per country–year
    """

    df_agg = (
        df.groupby(["iso3", "country", "year"], as_index=False)
          .agg(
              disaster_event_count=("event_id", "nunique"),
              disaster_deaths=("disaster_deaths", "sum"),
              disaster_affected=("disaster_affected", "sum"),
          )
    )

    return df_agg
