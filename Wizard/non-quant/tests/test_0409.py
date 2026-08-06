python
import sqlite3
import pandas as pd
import pytest

def task_func(db_file: str, query: str) -> pd.DataFrame:
    with sqlite3.connect(db_file) as conn:
        return pd.read_sql_query(query, conn)

def test_task_func():
    # Test case 1: Valid input
    df = task_func('test.db', 'SELECT * FROM table')
    assert isinstance(df, pd.DataFrame)

    # Test case 2: Invalid input (empty query)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', '')

    # Test case 3: Invalid input (invalid query)
    with pytest.raises(sqlite3.OperationalError):
        task_func('test.db', 'SELECT * FROM invalid_table')