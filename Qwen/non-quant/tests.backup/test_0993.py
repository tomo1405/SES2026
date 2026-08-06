import pytest
from src_0993 import task_func
import sqlite3
import os

# Mocking sys.path.append to avoid side effects
class MockSysPath:
    def __init__(self):
        self.paths = []

    def append(self, path):
        self.paths.append(path)

@pytest.fixture
def mock_sys_path(monkeypatch):
    mock_path = MockSysPath()
    monkeypatch.setattr(sys, 'path', mock_path)
    return mock_path

@pytest.fixture
def temp_db_file(tmpdir):
    db_file = tmpdir.join("test_database.db")
    return str(db_file)

def test_task_func_default_args(mock_sys_path, temp_db_file):
    result = task_func(database=temp_db_file)
    assert result == "path/to/whatever"
    assert mock_sys_path.paths == ["path/to/whatever"]

    # Check if the database was created and the table was populated
    conn = sqlite3.connect(temp_db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM paths")
    rows = cur.fetchall()
    conn.close()
    assert rows == [("path/to/whatever",)]

def test_task_func_custom_args(mock_sys_path, temp_db_file):
    custom_path = "custom/path"
    custom_db = temp_db_file
    result = task_func(path_to_append=custom_path, database=custom_db)
    assert result == custom_path
    assert mock_sys_path.paths == [custom_path]

    # Check if the database was created and the table was populated with custom path
    conn = sqlite3.connect(custom_db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM paths")
    rows = cur.fetchall()
    conn.close()
    assert rows == [(custom_path,)]