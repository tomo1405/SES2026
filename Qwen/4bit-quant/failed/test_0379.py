import pytest
from src_0379 import task_func
import pandas as pd
import os
import glob

# Mocking os.path.exists and glob.glob for testing
class MockPath:
    def __init__(self, exists=True):
        self.exists = exists

    def exists(self, path):
        return self.exists

class MockGlob:
    def __init__(self, files):
        self.files = files

    def glob(self, pattern):
        return self.files

def test_task_func_directory_not_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda path: False)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func()
    assert str(excinfo.value) == "The directory './data/' does not exist."

def test_task_func_no_csv_files(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda path: True)
    monkeypatch.setattr(glob, 'glob', lambda pattern: [])
    with pytest.raises(ValueError) as excinfo:
        task_func()
    assert str(excinfo.value) == "No CSV files found in the directory './data/'."

def test_task_func_with_empty_csv_file(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda path: True)
    monkeypatch.setattr(glob, 'glob', lambda pattern: ['./data/empty.csv'])
    with pytest.raises(pd.errors.EmptyDataError) as excinfo:
        task_func()
    assert str(excinfo.value) == "Error when reading file './data/empty.csv'."

def test_task_func_with_valid_csv_files(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda path: True)
    monkeypatch.setattr(glob, 'glob', lambda pattern: ['./data/file1.csv', './data/file2.csv'])
    
    # Mocking pd.read_csv to return predefined DataFrames
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8], 'E': [9, 10]})

    def mock_read_csv(file):
        if file == './data/file1.csv':
            return df1
        elif file == './data/file2.csv':
            return df2
        else:
            raise ValueError("Unexpected file")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

    result = task_func()
    expected_output = """\
+-----------+------+---------+
|   File    | Rows | Columns |
+-----------+------+---------+
| file1.csv |    2 |       2 |
| file2.csv |    2 |       3 |
+-----------+------+---------+"""

    assert result == expected_output