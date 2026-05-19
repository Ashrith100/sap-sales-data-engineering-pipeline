from sqlalchemy import create_engine
import pandas as pd


def load_dataframe_to_postgres(df: pd.DataFrame, database_name: str, table_name: str) -> None:
    engine = create_engine(
        f"postgresql+psycopg2://localhost/{database_name}"
    )

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded data into PostgreSQL table '{table_name}' in database '{database_name}'")