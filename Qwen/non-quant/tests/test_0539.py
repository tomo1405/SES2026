import pytest
from src_0539 import task_func
import pandas as pd
import sqlite3
from io import StringIO

# Helper function to create an in-memory SQLite database and table
def create_test_db():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            col1 REAL,
            col2 INTEGER,
            col3 TEXT
        )
    ''')
    cursor.executemany('INSERT INTO test_table (col1, col2, col3) VALUES (?, ?, ?)', [
        (1.1, 1, 'A'),
        (2.2, 2, 'B'),
        (3.3, 3, 'C')
    ])
    connection.commit()
    return connection

def test_task_func_with_valid_data():
    connection = create_test_db()
    db_name = ':memory:'
    table_name = 'test_table'
    ax = task_func(db_name, table_name)
    assert isinstance(ax, pd.plotting._matplotlib.scatter.ScatterPlot)
    connection.close()

def test_task_func_with_insufficient_numerical_columns():
    connection = create_test_db()
    cursor = connection.cursor()
    cursor.execute('ALTER TABLE test_table DROP COLUMN col2')
    connection.commit()
    db_name = ':memory:'
    table_name = 'test_table'
    with pytest.raises(ValueError, match="The table must have at least two numerical columns to plot."):
        task_func(db_name, table_name)
    connection.close()

def test_task_func_with_nonexistent_table():
    db_name = ':memory:'
    table_name = 'nonexistent_table'
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name)

def test_task_func_with_empty_table():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE empty_table (
            id INTEGER PRIMARY KEY,
            col1 REAL,
            col2 INTEGER
        )
    ''')
    connection.commit()
    db_name = ':memory:'
    table_name = 'empty_table'
    with pytest.raises(ValueError, match="The table must have at least two numerical columns to plot."):
        task_func(db_name, table_name)
    connection.close()