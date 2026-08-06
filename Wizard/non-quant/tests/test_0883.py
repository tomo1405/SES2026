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
    # Test case 1: Valid input
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    expected_output = pd.DataFrame({'id': [1, 2, 3], 'name': ['John', 'Mary', 'Bob'], 'age': ['30', '25', '40'], 'gender': ['M', 'F', 'M']})
    with sqlite3.connect(db_file) as conn:
        expected_output.to_sql(table_name, conn, if_exists='replace')
    output = task_func(db_file, table_name, column_name, pattern)
    assert output.equals(expected_output)

    # Test case 2: Invalid input - db_file does not exist
    db_file = 'invalid.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    with pytest.raises(ValueError):
        task_func(db_file, table_name, column_name, pattern)

    # Test case 3: Invalid input - column_name does not exist in the table
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'invalid_column'
    pattern = '\d+[xX]'
    with pytest.raises(KeyError):
        task_func(db_file, table_name, column_name, pattern)

    # Test case 4: Invalid input - column_name is not a string
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'id'
    pattern = '\d+[xX]'
    with pytest.raises(TypeError):
        task_func(db_file, table_name, column_name, pattern)

    # Test case 5: Invalid input - pattern is not a string
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = 123
    with pytest.raises(TypeError):
        task_func(db_file, table_name, column_name, pattern)

    # Test case 6: Invalid input - pattern is not a valid regex pattern
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = 'invalid_pattern'
    with pytest.raises(re.error):
        task_func(db_file, table_name, column_name, pattern)