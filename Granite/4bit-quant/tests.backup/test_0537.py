import sqlite3
import pandas as pd
import os
import pytest

def task_func(db_name, table_name, csv_path="data.csv"):
    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
        df.to_csv(csv_path, index=False)
        return os.path.abspath(csv_path)
    finally:
        conn.close()

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test_data.csv"
    expected_output = "test_data.csv"
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

def test_task_func_with_invalid_db_name():
    db_name = "invalid_test.db"
    table_name = "test_table"
    csv_path = "test_data.csv"
    with pytest.raises(Exception):
        task_func(db_name, table_name, csv_path)