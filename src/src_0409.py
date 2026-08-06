import sqlite3
import pandas as pd
def task_func(db_file: str, query: str) -> pd.DataFrame:
    with sqlite3.connect(db_file) as conn:
        return pd.read_sql_query(query, conn)