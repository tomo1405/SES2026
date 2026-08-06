python
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
    # Test case 1: db_file does not exist
    with pytest.raises(ValueError):
        task_func('non_existent_file.db', 'table_name', 'column_name')

    # Test case 2: column data type is not a string
    df = pd.DataFrame({'column_name': [1, 2, 3]})
    conn = sqlite3.connect(':memory:')
    df.to_sql('table_name', conn, index=False)
    matches = task_func(conn, 'table_name', 'column_name')
    assert matches.empty

    # Test case 3: column data type is a string and there are matches
    df = pd.DataFrame({'column_name': ['1x', '2X', '3x']})
    conn = sqlite3.connect(':memory:')
    df.to_sql('table_name', conn, index=False)
    matches = task_func(conn, 'table_name', 'column_name')
    assert matches.shape == (2, 2)

    # Test case 4: column data type is a string and there are no matches
    df = pd.DataFrame({'column_name': ['abc', 'def', 'ghi']})
    conn = sqlite3.connect(':memory:')
    df.to_sql('table_name', conn, index=False)
    matches = task_func(conn, 'table_name', 'column_name')
    assert matches.empty