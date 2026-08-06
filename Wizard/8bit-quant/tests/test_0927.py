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
    assert df.shape == (3, 3)
    assert df['column1'][1] == 'This is a test\nwith newline character'
    assert df['column1'][2] == 'This is another test\nwith newline character'

    # Test case 2: Invalid input (empty db_path)
    with pytest.raises(sqlite3.OperationalError):
        task_func('', 'table1', 'column1')

    # Test case 3: Invalid input (empty table_name)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', '', 'column1')

    # Test case 4: Invalid input (empty column_name)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', 'table1', '')

    # Test case 5: Invalid input (non-existent db_path)
    with pytest.raises(sqlite3.OperationalError):
        task_func('nonexistent.db', 'table1', 'column1')

    # Test case 6: Invalid input (non-existent table_name)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', 'nonexistent', 'column1')

    # Test case 7: Invalid input (non-existent column_name)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', 'table1', 'nonexistent')