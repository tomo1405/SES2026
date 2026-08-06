import sqlite3
import pandas as pd
import os
import pytest
from src_0883 import task_func

def test_task_func_with_valid_input():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'test_column'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE test_table
                 (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
    c.execute("INSERT INTO test_table VALUES (1, 'Test1', 100), (2, 'Test2', 200), (3, 'Test3', 300)")
    conn.commit()
    conn.close()
    matches = task_func(db_file, table_name, column_name, pattern='\d+[xX]')
    assert len(matches) == 1
    assert matches.iloc[0]['name'] == 'Test2'
    os.remove(db_file)

def test_task_func_with_invalid_db_file():
    with pytest.raises(ValueError) as excinfo:
        task_func('invalid_file.db', 'test_table', 'test_column', pattern='\d+[xX]')
    assert 'db_file does not exist.' in str(excinfo.value)

def test_task_func_with_invalid_table_name():
    db_file = 'test.db'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE test_table
                 (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
    c.execute("INSERT INTO test_table VALUES (1, 'Test1', 100), (2, 'Test2', 200), (3, 'Test3', 300)")
    conn.commit()
    conn.close()
    with pytest.raises(ValueError) as excinfo:
        task_func(db_file, 'invalid_table', 'test_column', pattern='\d+[xX]')
    assert 'no such table: invalid_table' in str(excinfo.value)
    os.remove(db_file)

def test_task_func_with_invalid_column_name():
    db_file = 'test.db'
    table_name = 'test_table'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE test_table
                 (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
    c.execute("INSERT INTO test_table VALUES (1, 'Test1', 100), (2, 'Test2', 200), (3, 'Test3', 300)")
    conn.commit()
    conn.close()
    with pytest.raises(ValueError) as excinfo:
        task_func(db_file, table_name, 'invalid_column', pattern='\d+[xX]')
    assert "Column 'invalid_column' does not exist" in str(excinfo.value)
    os.remove(db_file)

def test_task_func_with_invalid_pattern():
    db_file = 'test.db'
    table_name = 'test_table'
    column_name = 'name'
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE test_table
                 (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
    c.execute("INSERT INTO test_table VALUES (1, 'Test1', 100), (2, 'Test2', 200), (3, 'Test3', 300)")
    conn.commit()
    conn.close()
    matches = task_func(db_file, table_name, column_name, pattern='\d')
    assert len(matches) == 0
    os.remove(db_file)