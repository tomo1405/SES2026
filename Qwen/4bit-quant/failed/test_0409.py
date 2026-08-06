import pytest
from src_0409 import task_func
import pandas as pd
import sqlite3

@pytest.fixture
def db_file(tmp_path):
    # Create a temporary SQLite database file
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Bob')")
    conn.commit()
    conn.close()
    return db_path

def test_task_func(db_file):
    query = "SELECT * FROM test_table"
    result_df = task_func(db_file, query)
    
    # Define the expected DataFrame
    expected_df = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob']
    })
    
    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_nonexistent_table(db_file):
    query = "SELECT * FROM non_existent_table"
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_file, query)

def test_task_func_with_invalid_query(db_file):
    query = "SELECT * FROM test_table WHERE invalid_column = 'value'"
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_file, query)