import pytest
from src_0646 import task_func
import pandas as pd
import os

# Mocking os.path.exists and os.stat to control file existence and size
class MockOsModule:
    def __init__(self, file_exists=True, file_size=10):
        self.file_exists = file_exists
        self.file_size = file_size

    def path(self, filename):
        class Path:
            def exists(self, filename):
                return self.exists

        return Path()

    def stat(self, filename):
        class StatResult:
            def __init__(self, st_size):
                self.st_size = st_size

        return StatResult(self.file_size)

# Mocking pandas.read_csv to control DataFrame returned
def mock_read_csv(filename):
    return pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# Mocking built-in open function to control file operations
def mock_open(filename, mode):
    if mode == 'w':
        return type('MockFile', (object,), {'truncate': lambda: None})()
    else:
        raise ValueError("Unsupported mode")

@pytest.fixture
def patch_os(monkeypatch):
    mock_os = MockOsModule()
    monkeypatch.setattr(os, 'path', mock_os.path)
    monkeypatch.setattr(os, 'stat', mock_os.stat)

@pytest.fixture
def patch_pandas(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

@pytest.fixture
def patch_open(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func_file_not_found(patch_os, patch_pandas, patch_open):
    mock_os = MockOsModule(file_exists=False)
    with pytest.raises(FileNotFoundError, match="No such file: 'nonexistent.csv'"):
        task_func('nonexistent.csv')

def test_task_func_empty_file(patch_os, patch_pandas, patch_open):
    mock_os = MockOsModule(file_size=0)
    result_df = task_func('empty.csv')
    assert result_df.empty

def test_task_func_non_empty_file(patch_os, patch_pandas, patch_open):
    result_df = task_func('non_empty.csv')
    expected_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    pd.testing.assert_frame_equal(result_df, expected_df)