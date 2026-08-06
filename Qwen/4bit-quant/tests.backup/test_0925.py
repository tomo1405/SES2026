import pytest
from src_0925 import task_func
import pandas as pd
import os
import sys

# Mocking os.path.exists to simulate file existence
class MockPath:
    def __init__(self, exists):
        self.exists = exists

    def exists(self, path):
        return self.exists

# Mocking sys.exit to prevent actual exit during tests
class MockExit:
    def __init__(self):
        self.exited = False

    def __call__(self, code):
        self.exited = True

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    mock_path = MockPath(exists=True)
    monkeypatch.setattr(os, 'path', mock_path)

@pytest.fixture
def mock_sys_exit(monkeypatch):
    mock_exit = MockExit()
    monkeypatch.setattr(sys, 'exit', mock_exit)
    return mock_exit

def test_task_func_file_not_exists(monkeypatch, capsys):
    mock_path = MockPath(exists=False)
    monkeypatch.setattr(os, 'path', mock_path)
    mock_exit = MockExit()
    monkeypatch.setattr(sys, 'exit', mock_exit)

    with pytest.raises(SystemExit):
        task_func('non_existent_file.csv', 'test_column')

    captured = capsys.readouterr()
    assert "File does not exist: non_existent_file.csv" in captured.out
    assert mock_exit.exited is True

def test_task_func_column_not_exists(mock_os_path_exists, mock_sys_exit, capsys):
    df = pd.DataFrame({'test_column': [1, 2, 3]})
    monkeypatch.setattr(pd, 'read_csv', lambda x: df)

    result_df = task_func('existing_file.csv', 'non_existent_column')

    captured = capsys.readouterr()
    assert "Column 'non_existent_column' does not exist in the DataFrame. No changes were made." in captured.out
    assert result_df.equals(df)

def test_task_func_column_exists(mock_os_path_exists, mock_sys_exit):
    df = pd.DataFrame({'test_column': ['a\nb', 'c\nd', 'e']})
    monkeypatch.setattr(pd, 'read_csv', lambda x: df)

    expected_df = pd.DataFrame({'test_column': ['a<br>b', 'c<br>d', 'e']})

    result_df = task_func('existing_file.csv', 'test_column')

    assert result_df.equals(expected_df)