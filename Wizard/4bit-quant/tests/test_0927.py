python
import pandas as pd
import sqlite3
import pytest

def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        df[column_name] = df[column_name].replace({'\n': '<br>'}, regex=True)
    finally:
        conn.close()
    return df

def test_task_func():
    # Test case 1: Valid input
    df = task_func('test.db', 'table1', 'column1')
    assert df.shape == (10, 3)
    assert df['column1'][0] == 'This is a test\nThis is another test'
    assert df['column1'][1] == 'This is a test\nThis is another test'
    assert df['column1'][2] == 'This is a test\nThis is another test'
    assert df['column1'][3] == 'This is a test\nThis is another test'
    assert df['column1'][4] == 'This is a test\nThis is another test'
    assert df['column1'][5] == 'This is a test\nThis is another test'
    assert df['column1'][6] == 'This is a test\nThis is another test'
    assert df['column1'][7] == 'This is a test\nThis is another test'
    assert df['column1'][8] == 'This is a test\nThis is another test'
    assert df['column1'][9] == 'This is a test\nThis is another test'

    # Test case 2: Invalid input
    with pytest.raises(sqlite3.OperationalError):
        task_func('invalid.db', 'table1', 'column1')