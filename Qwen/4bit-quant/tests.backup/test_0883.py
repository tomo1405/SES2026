import pytest
from src_0883 import task_func
import os
import pandas as pd
import sqlite3

@pytest.fixture
def setup_db(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, value TEXT)''')
    cursor.execute("INSERT INTO test_table (value) VALUES ('123x'), ('456y'), ('789x')")
    conn.commit()
    conn.close()
    return str(db_path)

def test_task_func_valid_pattern(setup_db):
    db_file = setup_db
    table_name = "test_table"
    column_name = "value"
    pattern = '\d+[xX]'
    
    result_df = task_func(db_file, table_name, column_name, pattern)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 2
    assert all(result_df['value'].isin(['123x', '789x']))

def test_task_func_invalid_pattern(setup_db):
    db_file = setup_db
    table_name = "test_table"
    column_name = "value"
    pattern = '[a-zA-Z]+'
    
    result_df = task_func(db_file, table_name, column_name, pattern)
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.empty

def test_task_func_nonexistent_column(setup_db):
    db_file = setup_db
    table_name = "test_table"
    column_name = "nonexistent_column"
    pattern = '\d+[xX]'
    
    with pytest.raises(KeyError):
        task_func(db_file, table_name, column_name, pattern)

def test_task_func_nonexistent_table(setup_db):
    db_file = setup_db
    table_name = "nonexistent_table"
    column_name = "value"
    pattern = '\d+[xX]'
    
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_file, table_name, column_name, pattern)

def test_task_func_nonexistent_db():
    db_file = "nonexistent.db"
    table_name = "test_table"
    column_name = "value"
    pattern = '\d+[xX]'
    
    with pytest.raises(ValueError, match='db_file does not exist'):
        task_func(db_file, table_name, column_name, pattern)