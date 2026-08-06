import os
import sqlite3

import pandas as pd
import pytest
from src_0409 import task_func


@pytest.fixture
def setup_database(tmpdir):
    db_file = os.path.join(tmpdir, "test.db")
    conn = sqlite3.connect(db_file)
    try:
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO test_table (name) VALUES ('Alice')")
        conn.execute("INSERT INTO test_table (name) VALUES ('Bob')")
        conn.commit()
    finally:
        conn.close()
    return db_file

def test_task_func(setup_database):
    db_file = setup_database
    query = "SELECT * FROM test_table"
    result_df = task_func(db_file, query)
    expected_df = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob']
    })
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_no_data(setup_database):
    db_file = setup_database
    query = "SELECT * FROM non_existent_table"
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_file, query)

def test_task_func_empty_result(setup_database):
    db_file = setup_database
    query = "SELECT * FROM test_table WHERE id > 2"
    result_df = task_func(db_file, query)
    expected_df = pd.DataFrame(columns=['id', 'name'])
    pd.testing.assert_frame_equal(result_df, expected_df)