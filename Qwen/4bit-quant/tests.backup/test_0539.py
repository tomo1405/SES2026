import pytest
from src_0539 import task_func
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

@pytest.fixture
def create_test_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE test_table (
                        id INTEGER PRIMARY KEY,
                        column1 REAL,
                        column2 INTEGER,
                        non_numeric TEXT)''')
    cursor.executemany('INSERT INTO test_table (column1, column2, non_numeric) VALUES (?, ?, ?)',
                         [(1.0, 1, 'a'), (2.0, 2, 'b'), (3.0, 3, 'c')])
    conn.commit()
    conn.close()
    return db_path

def test_task_func(create_test_db):
    db_path = create_test_db
    ax = task_func(db_path, 'test_table')
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'column1'
    assert ax.get_ylabel() == 'column2'

def test_task_func_insufficient_numerical_columns(create_test_db):
    db_path = create_test_db
    with pytest.raises(ValueError, match="The table must have at least two numerical columns to plot."):
        task_func(db_path, 'test_table')

def test_task_func_non_existent_table(create_test_db):
    db_path = create_test_db
    with pytest.raises(sqlite3.OperationalError, match="no such table: non_existent_table"):
        task_func(db_path, 'non_existent_table')

def test_task_func_no_numerical_columns(create_test_db):
    db_path = create_test_db
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE no_numeric_table (
                        id INTEGER PRIMARY KEY,
                        non_numeric TEXT)''')
    cursor.executemany('INSERT INTO no_numeric_table (non_numeric) VALUES (?)', [('a',), ('b',), ('c',)])
    conn.commit()
    conn.close()
    with pytest.raises(ValueError, match="The table must have at least two numerical columns to plot."):
        task_func(db_path, 'no_numeric_table')