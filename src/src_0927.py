import pandas as pd
import sqlite3
def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    finally:
        conn.close()
    return df