import pytest
from src_0539 import task_func
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Helper function to create a temporary SQLite database with a test table
def create_test_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            num1 REAL,
            num2 INTEGER,
            text_column TEXT
        )
    ''')
    cursor.executemany('INSERT INTO test_table (num1, num2, text_column) VALUES (?, ?, ?)',
                        [(1.5, 10, 'A'), (2.5, 20, 'B'), (3.5, 30, 'C')])
    conn.commit()
    return conn

# Test case for task_func
def test_task_func():
    # Create a temporary SQLite database
    conn = create_test_db()
    
    # Call the function
    ax = task_func(conn, 'test_table')
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'num1'
    assert ax.get_ylabel() == 'num2'
    
    # Clean up
    conn.close()

# Test case for task_func with insufficient numerical columns
def test_task_func_insufficient_columns():
    # Create a temporary SQLite database with only one numerical column
    conn = create_test_db()
    cursor = conn.cursor()
    cursor.execute('ALTER TABLE test_table DROP COLUMN num2')
    conn.commit()
    
    # Call the function and expect a ValueError
    with pytest.raises(ValueError) as excinfo:
        task_func(conn, 'test_table')
    
    assert str(excinfo.value) == "The table must have at least two numerical columns to plot."
    
    # Clean up
    conn.close()