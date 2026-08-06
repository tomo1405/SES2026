import sqlite3
import pandas as pd
import os
import pytest

def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    if not os.path.isfile(db_file):
        raise ValueError('db_file does not exist.')

    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    if df[column_name].dtype == 'object':  # Check if the column data type is a string
        matches = df[df[column_name].str.contains(pattern)]
    else:
        matches = pd.DataFrame(columns=df.columns)  # Return an empty DataFrame

    return matches

def test_task_func():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    with sqlite3.connect(db_file) as conn:
        conn.execute('''
            CREATE TABLE test_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value TEXT
            )
        ''')
        conn.execute('''
            INSERT INTO test_table (id, name, value)
            VALUES (1, 'Alice', '10x'), (2, 'Bob', '20y'), (3, 'Charlie', '30z')
        ''')
    matches = task_func(db_file, table_name, column_name, pattern)
    assert matches.shape == (2, 3)
    assert matches.loc[0, 'name'] == 'Alice'
    assert matches.loc[0, 'value'] == '10x'
    assert matches.loc[1, 'name'] == 'Bob'
    assert matches.loc[1, 'value'] == '20y'
    os.remove(db_file)

def test_task_func_empty_df():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    with sqlite3.connect(db_file) as conn:
        conn.execute('''
            CREATE TABLE test_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value TEXT
            )
        ''')
    matches = task_func(db_file, table_name, column_name, pattern)
    assert matches.empty

def test_task_func_invalid_db_file():
    db_file = 'invalid.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    with pytest.raises(ValueError) as e:
        task_func(db_file, table_name, column_name, pattern)
    assert str(e.value) == 'db_file does not exist.'