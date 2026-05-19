from reports.validation_summary import (
    create_validation_summary,
    save_validation_summary
)

from extract.read_file import read_excel_file
from transform.clean_columns import clean_column_names
from validate.check_duplicates import find_duplicates
from validate.check_missing_values import find_missing_required_values
from load.load_to_sqlite import load_dataframe_to_sqlite
from export.export_clean_data import export_clean_data
from utils.logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("Pipeline started")

    file_path = "data/raw/vbrp_jksample.xlsx"

    df = read_excel_file(file_path)

    logger.info(f"Loaded dataset with {len(df)} rows")

    print("File loaded successfully.")

    df = clean_column_names(df)

    print(f"\nRows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    duplicates = find_duplicates(df)

    logger.info(f"Duplicate records found: {len(duplicates)}")

    print(f"\nDuplicate Records Found: {len(duplicates)}")

    if not duplicates.empty:
        print(duplicates[["vbeln", "posnr"]].head())

    missing_values = find_missing_required_values(df)

    logger.info(f"Missing required value records: {len(missing_values)}")

    print(f"\nRecords Missing Required Values: {len(missing_values)}")

    if not missing_values.empty:
        print(
            missing_values[
                ["vbeln", "posnr", "fkimg", "vrkme", "meins"]
            ].head()
        )

    summary_df = create_validation_summary(
        total_rows=len(df),
        duplicate_count=len(duplicates),
        missing_count=len(missing_values)
    )

    save_validation_summary(
        summary_df,
        "reports/validation_summary.csv"
    )

    logger.info("Validation summary report generated")

    print("\nValidation summary saved to reports/validation_summary.csv")

    export_clean_data(
        df=df,
        output_path="data/processed/clean_vbrp.csv"
    )

    logger.info("Clean CSV export completed")

    load_dataframe_to_sqlite(
        df=df,
        database_name="sap_sales.db",
        table_name="billing_items"
    )

    logger.info("SQLite load completed")

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()