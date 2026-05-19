import pandas as pd


def export_clean_data(df: pd.DataFrame, output_path: str) -> None:
    df.to_csv(output_path, index=False)
    print(f"Clean data exported to {output_path}")