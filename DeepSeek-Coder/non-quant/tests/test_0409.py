import pytest
from src_0409 import task_func
import sqlite3
import pandas as pd

def test_task_func():
    # Create a sample database and query
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER, value TEXT)")
    cursor.execute("INSERT INTO test_table VALUES (1, 'test')")
    conn.commit()

    # Query the database
    result = task_func(":memory:", "SELECT * FROM test_table")

    # Check the result
    assert len(result) == 1
    assert result.iloc[0]['id'] == 1
    assert result.iloc[0]['value'] == 'test'

    # Clean up
    conn.close()