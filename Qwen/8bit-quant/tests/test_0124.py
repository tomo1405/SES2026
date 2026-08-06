import pytest
from src_0124 import task_func
import pandas as pd
import os
import glob

# Mocking functions and data for testing
class MockGlob:
    def __init__(self, results):
        self.results = results

    def glob(self, pattern):
        return self.results

class MockPdReadCsv:
    def __init__(self, data):
        self.data = data

    def read_csv(self, file):
        return pd.DataFrame(self.data)

@pytest.fixture
def mock_glob(monkeypatch):
    def mock_glob_results(pattern):
        return ['./data_files/file1.csv', './data_files/file2.csv']
    monkeypatch.setattr(glob, 'glob', mock_glob_results)

@pytest.fixture
def mock_pd_read_csv(monkeypatch):
    def mock_read_csv(file):
        return pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func_with_valid_input(mock_glob, mock_pd_read_csv):
    my_list = [1, 2]
    result = task_func(my_list)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 4  # 2 rows per file * 2 files

def test_task_func_with_empty_list(mock_glob, mock_pd_read_csv):
    my_list = []
    result = task_func(my_list)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2  # 2 rows per file * 1 file (since 12 is appended to my_list)

def test_task_func_with_no_files_found():
    my_list = [1]
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(my_list, file_dir='./non_existent_dir/')
    assert str(excinfo.value) == "No files with extension '.csv' found in directory './non_existent_dir/'."

def test_task_func_with_non_list_input():
    my_list = "not a list"
    with pytest.raises(TypeError) as excinfo:
        task_func(my_list)
    assert str(excinfo.value) == "my_list must be a list."