import pytest
from src_0927 import task_func
import pandas as pd
import sqlite3

# Helper function to create a temporary SQLite database and table
def create_temp_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE test_table (id INTEGER PRIMARY KEY, text_column TEXT)')
    cursor.execute("INSERT INTO test_table (text_column) VALUES ('Hello\nWorld')")
    cursor.execute("INSERT INTO test_table (text_column) VALUES ('Foo\nBar')")
    conn.commit()
    conn.close()
    return ':memory:'

def test_task_func():
    db_path = create_temp_db()
    table_name = 'test_table'
    column_name = 'text_column'
    
    df = task_func(db_path, table_name, column_name)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'text_column' in df.columns
    
    # Check if newline characters are replaced with '<br>'
    assert df.loc[0, 'text_column'] == 'Hello<br>World'
    assert df.loc[1, 'text_column'] == 'Foo<br>Bar'

def test_task_func_nonexistent_table():
    db_path = create_temp_db()
    table_name = 'nonexistent_table'
    column_name = 'text_column'
    
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_path, table_name, column_name)

def test_task_func_nonexistent_column():
    db_path = create_temp_db()
    table_name = 'test_table'
    column_name = 'nonexistent_column'
    
    with pytest.raises(KeyError):
        task_func(db_path, table_name, column_name)