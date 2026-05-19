import pandas as pd


def create_validation_summary(total_rows: int, duplicate_count: int, missing_count: int) -> pd.DataFrame:
    summary = {
        "metric": [
            "total_rows",
            "duplicate_records",
            "missing_required_value_records"
        ],
        "value": [
            total_rows,
            duplicate_count,
            missing_count
        ]
    }

    return pd.DataFrame(summary)


def save_validation_summary(summary_df: pd.DataFrame, output_path: str) -> None:
    summary_df.to_csv(output_path, index=False)