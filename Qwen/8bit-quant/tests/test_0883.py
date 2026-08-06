import sqlite3

import pandas as pd
import pytest
from src_0883 import task_func


# Mocking setup
@pytest.fixture
def mock_db_file(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute('''INSERT INTO test_table (name) VALUES ('item1'), ('item2'), ('item10x'), ('item20X')''')
    conn.commit()
    conn.close()
    return str(db_path)

def test_task_func_existing_file(mock_db_file):
    result = task_func(mock_db_file, 'test_table', 'name', '\d+[xX]')
    assert result.equals(pd.DataFrame({'id': [3, 4], 'name': ['item10x', 'item20X']}))

def test_task_func_nonexistent_file():
    with pytest.raises(ValueError) as excinfo:
        task_func('nonexistent.db', 'test_table', 'name')
    assert str(excinfo.value) == 'db_file does not exist.'

def test_task_func_column_not_string(mock_db_file):
    result = task_func(mock_db_file, 'test_table', 'id', '\d+')
    assert result.empty

def test_task_func_no_matches(mock_db_file):
    result = task_func(mock_db_file, 'test_table', 'name', 'abc')
    assert result.empty

def test_task_func_empty_table(tmpdir):
    db_path = tmpdir.join("empty_test.db")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE empty_table (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()
    result = task_func(str(db_path), 'empty_table', 'name', '\d+[xX]')
    assert result.empty