import sqlite3
import warnings

import pandas as pd
import pytest
from src_1069 import task_func


# Mocking setup
class MockConnection:
    def __init__(self, data):
        self.data = data

    def cursor(self):
        return self

    def execute(self, query):
        pass

    def fetchall(self):
        return self.data

    def close(self):
        pass

@pytest.fixture
def mock_db(monkeypatch):
    def mock_connect(db_path):
        # Example data for testing
        data = [
            (1, 'Alice'),
            (2, 'Bob')
        ]
        columns = ['id', 'name']
        mock_conn = MockConnection(data)
        monkeypatch.setattr(sqlite3, 'connect', lambda _: mock_conn)
        return mock_conn

    return mock_connect

def test_task_func_success(mock_db):
    db_path = "test.db"
    query = "SELECT * FROM users"
    expected_data = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob']
    })

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = task_func(db_path, query, warn_large_dataset=False)

    assert result.equals(expected_data)
    assert len(w) == 0

def test_task_func_large_dataset_warning(mock_db):
    db_path = "test.db"
    query = "SELECT * FROM large_table"
    large_data = [(i, f'User{i}') for i in range(10001)]
    columns = ['id', 'name']
    mock_conn = mock_db(db_path)
    monkeypatch.setattr(mock_conn, 'fetchall', lambda: large_data)

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = task_func(db_path, query, warn_large_dataset=True)

    assert len(result) == 10001
    assert len(w) == 1
    assert str(w[-1].message) == "The data contains more than 10000 rows."

def test_task_func_error(mock_db):
    db_path = "test.db"
    query = "SELECT * FROM non_existent_table"
    mock_conn = mock_db(db_path)
    monkeypatch.setattr(mock_conn, 'execute', lambda q: None)
    monkeypatch.setattr(mock_conn, 'fetchall', lambda: [])

    with pytest.raises(Exception) as excinfo:
        task_func(db_path, query, warn_large_dataset=False)

    assert "Error fetching data from the database:" in str(excinfo.value)