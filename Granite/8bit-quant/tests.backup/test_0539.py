import sqlite3
import pandas as pd
import pytest

def task_func(db_name, table_name):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if "id" in numerical_columns:
        numerical_columns.remove("id")
    if len(numerical_columns) < 2:
        raise ValueError("The table must have at least two numerical columns to plot.")
    ax = df.plot.scatter(x=numerical_columns[0], y=numerical_columns[1])
    return ax

def test_task_func():
    db_name = "example.db"
    table_name = "example_table"
    with sqlite3.connect(db_name) as conn:
        conn.execute('''CREATE TABLE example_table (
            id INTEGER PRIMARY KEY,
            col1 INTEGER,
            col2 REAL,
            col3 TEXT
        )''')
        conn.execute("INSERT INTO example_table VALUES (1, 10, 20.5, 'example')")
    ax = task_func(db_name, table_name)
    assert ax is not None
    numerical_columns = ax.get_xlabel(), ax.get_ylabel()
    assert numerical_columns == ("col1", "col2")