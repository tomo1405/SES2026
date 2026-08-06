import os
import sqlite3

import pandas as pd
import pytest
from src_0409 import task_func


# Fixture to create a temporary SQLite database and populate it with test data
@pytest.fixture
def temp_db():
    db_file = 'temp_test.db'
    conn = sqlite3.connect(db_file)
    try:
        # Create a test table
        conn.execute('CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        # Insert some test data
        conn.execute("INSERT INTO test_table (name) VALUES ('Alice')")
        conn.execute("INSERT INTO test_table (name) VALUES ('Bob')")
        conn.commit()
        yield db_file
    finally:
        # Close the connection and remove the database file
        conn.close()
        os.remove(db_file)

def test_task_func(temp_db):
    query = "SELECT * FROM test_table"
    result_df = task_func(temp_db, query)
    
    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['id', 'name']
    assert list(result_df.columns) == expected_columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(result_df) == 2
    
    # Check if the DataFrame contains the correct data
    expected_data = {'id': [1, 2], 'name': ['Alice', 'Bob']}
    assert result_df.to_dict(orient='list') == expected_data