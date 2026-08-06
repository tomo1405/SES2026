import pytest
from src_0074 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import sqlite3

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE EmailData (list TEXT)")
    cursor.execute("INSERT INTO EmailData (list) VALUES (?)", ("[1, 2, 3]",))
    conn.commit()
    yield conn
    conn.close()

@pytest.fixture
def df_with_data():
    df = pd.DataFrame({
        'list': [[1, 2, 3], [4, 5, 6]]
    })
    return df

def test_task_func(db_connection, df_with_data):
    df, ax = task_func('dummy_db_file')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'var' in df.columns
    assert ax is not None
    plt.close()