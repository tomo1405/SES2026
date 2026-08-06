import pytest
from src_0537 import task_func
import sqlite3
import pandas as pd
import os

@pytest.fixture
def setup_db(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Bob')")
    conn.commit()
    conn.close()
    return str(db_path)

def test_task_func(setup_db, tmpdir):
    db_name = setup_db
    table_name = "test_table"
    csv_path = tmpdir.join("output.csv")
    
    result = task_func(db_name, table_name, str(csv_path))
    
    assert result == os.path.abspath(str(csv_path))
    
    df = pd.read_csv(str(csv_path))
    expected_df = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob']
    })
    
    pd.testing.assert_frame_equal(df, expected_df)