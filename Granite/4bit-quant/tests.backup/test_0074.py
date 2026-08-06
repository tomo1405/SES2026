import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
import pytest

def task_func(db_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    ax = df[['sum', 'mean', 'var']].plot(kind='bar')
    plt.show()

    return df, ax

def test_task_func():
    # Create a temporary database file for testing
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE EmailData
                 (list TEXT)''')
    c.execute("INSERT INTO EmailData VALUES ('[1, 2, 3]')")
    c.execute("INSERT INTO EmailData VALUES ('[4, 5, 6]')")
    conn.commit()
    db_file = ':memory:'

    # Call the function and store the returned values
    df, ax = task_func(db_file)

    # Check the returned values are as expected
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'var' in df.columns
    assert df.shape == (2, 4)

def test_task_func_with_invalid_db_file():
    # Pass an invalid database file path to the function
    with pytest.raises(sqlite3.OperationalError):
        task_func('invalid_db_file.db')