import pytest
from src_0537 import task_func
import os
import pandas as pd
import sqlite3

@pytest.fixture
def setup_db(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = sqlite3.connect(db_path.strpath)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Bob')")
    conn.commit()
    conn.close()
    return db_path.strpath

def test_task_func(setup_db, tmpdir):
    db_name = setup_db
    table_name = "test_table"
    csv_path = tmpdir.join("output.csv").strpath
    
    result_path = task_func(db_name, table_name, csv_path)
    
    assert result_path == os.path.abspath(csv_path)
    
    df_output = pd.read_csv(csv_path)
    expected_df = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob']
    })
    
    pd.testing.assert_frame_equal(df_output, expected_df)

def test_task_func_nonexistent_table(setup_db, tmpdir):
    db_name = setup_db
    table_name = "nonexistent_table"
    csv_path = tmpdir.join("output.csv").strpath
    
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name, csv_path)