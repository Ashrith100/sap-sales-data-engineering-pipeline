from extract.read_file import read_excel_file
from transform.clean_columns import clean_column_names
from validate.check_duplicates import find_duplicates
from validate.check_missing_values import find_missing_required_values


def main():
    file_path = "data/raw/vbrp_jksample.xlsx"

    df = read_excel_file(file_path)

    print("File loaded successfully.")

    df = clean_column_names(df)

    print(f"\nRows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    duplicates = find_duplicates(df)

    print(f"\nDuplicate Records Found: {len(duplicates)}")

    if not duplicates.empty:
        print(duplicates[["vbeln", "posnr"]].head())

    missing_values = find_missing_required_values(df)

    print(f"\nRecords Missing Required Values: {len(missing_values)}")

    if not missing_values.empty:
        print(
            missing_values[
                ["vbeln", "posnr", "fkimg", "vrkme", "meins"]
            ].head()
        )


if __name__ == "__main__":
    main()