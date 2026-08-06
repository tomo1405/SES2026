import pytest
from src_0927 import task_func
import pandas as pd
import sqlite3

def test_task_func():
    # Create a temporary database for testing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            text_column TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO test_table (text_column) VALUES ('Hello\nWorld')
    ''')
    conn.commit()

    # Call the function
    result = task_func(':memory:', 'test_table', 'text_column')

    # Check the result
    assert not result.empty
    assert 'Hello<br>World' in result['text_column'].values[0]

    # Clean up
    conn.close()