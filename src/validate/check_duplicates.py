import pandas as pd


def find_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    duplicates = df[
        df.duplicated(subset=["vbeln", "posnr"], keep=False)
    ]

    return duplicates