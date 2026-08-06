import ast
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0074 import task_func


# Mocking dependencies
class MockCursor:
    def execute(self, query):
        pass

class MockConnection:
    def __init__(self):
        self.cursor = MockCursor()

    def cursor(self):
        return self.cursor

    def close(self):
        pass

def mock_read_sql_query(query, conn):
    data = {
        'id': [1, 2],
        'list': ['[1, 2, 3]', '[4, 5, 6]']
    }
    return pd.DataFrame(data)

@pytest.fixture
def setup_mock():
    original_connect = sqlite3.connect
    original_read_sql_query = pd.read_sql_query

    sqlite3.connect = lambda db_file: MockConnection()
    pd.read_sql_query = mock_read_sql_query

    yield

    sqlite3.connect = original_connect
    pd.read_sql_query = original_read_sql_query

def test_task_func(setup_mock, monkeypatch):
    # Mocking ast.literal_eval to avoid actual evaluation
    monkeypatch.setattr(ast, 'literal_eval', lambda x: eval(x))

    # Mocking plt.show to avoid actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)

    db_file = 'mock_db.db'
    df, ax = task_func(db_file)

    # Check if DataFrame columns are correctly calculated
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'var' in df.columns

    # Check if the values are correctly computed
    assert df['sum'].tolist() == [6, 15]
    assert df['mean'].tolist() == [2.0, 5.0]
    assert df['var'].tolist() == [0.6666666666666666, 0.6666666666666666]

    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)