import sqlite3
import pandas as pd
import os
import pytest
from src_0883 import task_func

def test_task_func_with_valid_input():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {table_name} ({column_name} TEXT)")
    c.execute(f"INSERT INTO {table_name} VALUES ('1x'), ('2X'), ('3x4'), ('5X6')")
    conn.commit()
    conn.close()
    matches = task_func(db_file, table_name, column_name, pattern)
    assert len(matches) == 4
    assert matches[column_name].iloc[0] == '1x'
    assert matches[column_name].iloc[1] == '2X'
    assert matches[column_name].iloc[2] == '3x4'
    assert matches[column_name].iloc[3] == '5X6'
    os.remove(db_file)

def test_task_func_with_invalid_db_file():
    db_file = 'invalid_file.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    with pytest.raises(ValueError) as excinfo:
        task_func(db_file, table_name, column_name, pattern)
    assert 'db_file does not exist.' in str(excinfo.value)

def test_task_func_with_invalid_column_type():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    pattern = '\d+[xX]'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {table_name} ({column_name} INTEGER)")
    c.execute(f"INSERT INTO {table_name} VALUES (1), (2), (3), (4)")
    conn.commit()
    conn.close()
    matches = task_func(db_file, table_name, column_name, pattern)
    assert len(matches) == 0
    os.remove(db_file)