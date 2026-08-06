import sqlite3
import pandas as pd
import pytest

def task_func(db_file: str, query: str) -> pd.DataFrame:
    with sqlite3.connect(db_file) as conn:
        return pd.read_sql_query(query, conn)

def test_task_func():
    db_file = "example.db"
    query = "SELECT * FROM table"
    expected_output = pd.DataFrame({
        "column1": [1, 2, 3],
        "column2": ["a", "b", "c"]
    })
    actual_output = task_func(db_file, query)
    assert actual_output.equals(expected_output)