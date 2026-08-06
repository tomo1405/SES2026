import sqlite3
import pandas as pd
import pytest
from src_0409 import task_func

def test_task_func():
    db_file = 'test_db.sqlite'
    query = 'SELECT * FROM test_table'
    expected_df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})

    with sqlite3.connect(db_file) as conn:
        conn.execute('''
            CREATE TABLE test_table (
                col1 INTEGER,
                col2 TEXT
            )
        ''')
        conn.execute('INSERT INTO test_table VALUES (1, "a")')
        conn.execute('INSERT INTO test_table VALUES (2, "b")')
        conn.execute('INSERT INTO test_table VALUES (3, "c")')

    actual_df = task_func(db_file, query)

    assert actual_df.equals(expected_df)