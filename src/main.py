from extract.read_file import read_excel_file
from transform.clean_columns import clean_column_names
from validate.check_duplicates import find_duplicates


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


if __name__ == "__main__":
    main()