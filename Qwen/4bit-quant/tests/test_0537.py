import pytest
from src_0537 import task_func
import os
import pandas as pd
import sqlite3

# Helper function to create a test database and table
def setup_test_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute(f"INSERT INTO {table_name} VALUES (1, 'Alice')")
    cursor.execute(f"INSERT INTO {table_name} VALUES (2, 'Bob')")
    conn.commit()
    conn.close()

# Helper function to clean up the test database
def teardown_test_db(db_name):
    os.remove(db_name)

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test_data.csv"

    # Setup test database
    setup_test_db(db_name, table_name)

    # Run the function under test
    result = task_func(db_name, table_name, csv_path)

    # Verify the output
    assert os.path.exists(result)
    df = pd.read_csv(csv_path)
    assert df.equals(pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]}))

    # Clean up
    teardown_test_db(db_name)
    os.remove(csv_path)

def test_task_func_non_existent_table():
    db_name = "test.db"
    table_name = "non_existent_table"
    csv_path = "test_data.csv"

    # Setup test database with no tables
    conn = sqlite3.connect(db_name)
    conn.close()

    # Run the function under test and expect it to raise an error
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name, csv_path)

    # Clean up
    os.remove(db_name)