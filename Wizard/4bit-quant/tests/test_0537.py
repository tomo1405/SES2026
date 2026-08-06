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
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 2: Invalid input (db_name is None)
    db_name = None
    table_name = "test_table"
    csv_path = "test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 3: Invalid input (table_name is None)
    db_name = "test.db"
    table_name = None
    csv_path = "test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 4: Invalid input (csv_path is None)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = None
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 5: Invalid input (csv_path is empty string)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = ""
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 6: Invalid input (csv_path is a directory)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "."
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 7: Invalid input (csv_path is a file)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 8: Invalid input (db_name does not exist)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 9: Invalid input (table_name does not exist)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output

    # Test case 10: Invalid input (csv_path is not writable)
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "/root/test.csv"
    expected_output = None
    actual_output = task_func(db_name, table_name, csv_path)
    assert actual_output == expected_output