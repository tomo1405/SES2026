import pytest
from src_0074 import task_func
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

# Mocking the sqlite3 connection and cursor to avoid actual database access
class MockCursor:
    def execute(self, query):
        pass

    def fetchall(self):
        return [
            (1, "[1, 2, 3]"),
            (2, "[4, 5, 6]"),
            (3, "[7, 8, 9]")
        ]

class MockConnection:
    def __init__(self):
        self.cursor = MockCursor()

    def cursor(self):
        return self.cursor

    def close(self):
        pass

@pytest.fixture
def mock_db_file(monkeypatch):
    monkeypatch.setattr(sqlite3, 'connect', lambda db_file: MockConnection())

def test_task_func(mock_db_file):
    db_file = "mock_db.db"
    df, ax = task_func(db_file)

    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(col in df.columns for col in ['id', 'list', 'sum', 'mean', 'var'])

    # Check if the 'list' column is converted to list type
    assert all(isinstance(item, list) for item in df['list'])

    # Check if the sum, mean, and var columns are calculated correctly
    assert df['sum'].tolist() == [6, 15, 24]
    assert df['mean'].tolist() == [2.0, 5.0, 8.0]
    assert df['var'].tolist() == [0.6666666666666666, 0.6666666666666666, 0.6666666666666666]

    # Check if the plot is created
    assert isinstance(ax, plt.Axes)

    # Close the plot to avoid it showing during tests
    plt.close(ax.figure)