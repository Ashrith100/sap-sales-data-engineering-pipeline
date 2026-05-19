import pandas as pd


def find_invalid_business_values(df: pd.DataFrame) -> pd.DataFrame:
    invalid_records = df[
        (df["fkimg"] < 0)
    ]

    return invalid_records