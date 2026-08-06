import pandas as pd
import sqlite3
import pytest

def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    finally:
        conn.close()
    return df

def test_task_func():
    db_path = "path/to/database.db"
    table_name = "example_table"
    column_name = "example_column"
    expected_df = pd.DataFrame({
        'column1': ['value1', 'value2'],
        'column2': ['value3', 'value4']
    })
    actual_df = task_func(db_path, table_name, column_name)
    assert actual_df.equals(expected_df)

if __name__ == "__main__":
    pytest.main()