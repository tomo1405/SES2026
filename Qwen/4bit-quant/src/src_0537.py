import sqlite3
import pandas as pd
import os
def task_func(db_name, table_name, csv_path="data.csv"):
    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
        df.to_csv(csv_path, index=False)
        return os.path.abspath(csv_path)
    finally:
        conn.close()