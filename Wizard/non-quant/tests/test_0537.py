python
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
    # Test case 1: Valid input
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test.csv"
    expected_output = os.path.abspath(csv_path)
    task_func(db_name, table_name, csv_path)
    assert os.path.exists(expected_output)

    # Test case 2: Invalid input (non-existent database)
    db_name = "nonexistent.db"
    table_name = "test_table"
    csv_path = "test.csv"
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name, csv_path)

    # Test case 3: Invalid input (non-existent table)
    db_name = "test.db"
    table_name = "nonexistent_table"
    csv_path = "test.csv"
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name, csv_path)

    # Test case 4: Invalid input (invalid CSV path)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "/invalid/path/test.csv"
    with pytest.raises(FileNotFoundError):
        task_func(db_name, table_name, csv_path)

    # Test case 5: Invalid input (invalid CSV path)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test.csv"
    os.remove(csv_path)
    task_func(db_name, table_name, csv_path)
    assert os.path.exists(expected_output)