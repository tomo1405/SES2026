import pytest
from src_0927 import task_func
import pandas as pd
import sqlite3
import io

# Helper function to create an in-memory SQLite database for testing
def create_test_db():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            text_column TEXT
        )
    ''')
    cursor.executemany('INSERT INTO test_table (text_column) VALUES (?)', [
        ('Hello\nWorld',),
        ('Foo\nBar',),
        ('Baz\nQux',),
    ])
    connection.commit()
    return connection

def test_task_func():
    # Create an in-memory database and populate it with test data
    test_db = create_test_db()
    db_path = test_db.filename
    table_name = 'test_table'
    column_name = 'text_column'

    # Call the function under test
    result_df = task_func(db_path, table_name, column_name)

    # Define the expected output
    expected_data = {
        'id': [1, 2, 3],
        'text_column': ['Hello<br>World', 'Foo<br>Bar', 'Baz<br>Qux']
    }
    expected_df = pd.DataFrame(expected_data)

    # Assert that the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Clean up the in-memory database
    test_db.close()

def test_task_func_nonexistent_table():
    # Create an in-memory database without any tables
    test_db = create_test_db()
    db_path = test_db.filename
    table_name = 'nonexistent_table'
    column_name = 'text_column'

    # Expect a ValueError because the table does not exist
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_path, table_name, column_name)

    # Clean up the in-memory database
    test_db.close()

def test_task_func_nonexistent_column():
    # Create an in-memory database and populate it with test data
    test_db = create_test_db()
    db_path = test_db.filename
    table_name = 'test_table'
    column_name = 'nonexistent_column'

    # Expect a KeyError because the column does not exist
    with pytest.raises(KeyError):
        task_func(db_path, table_name, column_name)

    # Clean up the in-memory database
    test_db.close()