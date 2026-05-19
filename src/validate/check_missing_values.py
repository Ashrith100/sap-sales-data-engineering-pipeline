import pandas as pd


def find_missing_required_values(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = ["vbeln", "posnr", "fkimg", "vrkme", "meins"]

    missing_records = df[
        df[required_columns].isnull().any(axis=1)
    ]

    return missing_records