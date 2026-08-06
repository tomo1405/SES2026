import pytest
from src_0883 import task_func
import os
import sqlite3
import pandas as pd

# Helper function to create a temporary SQLite database for testing
def create_temp_db():
    db_file = 'temp_test.db'
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, value TEXT)''')
    cursor.execute("INSERT INTO test_table (name, value) VALUES ('test1', '123x')")
    cursor.execute("INSERT INTO test_table (name, value) VALUES ('test2', 'abc')")
    conn.commit()
    conn.close()
    return db_file

# Helper function to remove the temporary SQLite database after testing
def remove_temp_db(db_file):
    os.remove(db_file)

def test_task_func_valid_data():
    db_file = create_temp_db()
    try:
        result = task_func(db_file, 'test_table', 'value')
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert result['name'].iloc[0] == 'test1'
    finally:
        remove_temp_db(db_file)

def test_task_func_no_matches():
    db_file = create_temp_db()
    try:
        result = task_func(db_file, 'test_table', 'name', pattern='xyz')
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    finally:
        remove_temp_db(db_file)

def test_task_func_non_string_column():
    db_file = create_temp_db()
    try:
        # Modify the table to have a non-string column
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE test_table ADD COLUMN number INTEGER")
        cursor.execute("UPDATE test_table SET number = 1")
        conn.commit()
        conn.close()

        result = task_func(db_file, 'test_table', 'number')
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    finally:
        remove_temp_db(db_file)

def test_task_func_invalid_db_file():
    with pytest.raises(ValueError, match='db_file does not exist'):
        task_func('non_existent.db', 'test_table', 'value')

def test_task_func_invalid_table_name():
    db_file = create_temp_db()
    try:
        with pytest.raises(sqlite3.OperationalError):
            task_func(db_file, 'non_existent_table', 'value')
    finally:
        remove_temp_db(db_file)

def test_task_func_invalid_column_name():
    db_file = create_temp_db()
    try:
        result = task_func(db_file, 'test_table', 'non_existent_column')
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    finally:
        remove_temp_db(db_file)