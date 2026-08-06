import pytest
from src_0124 import task_func
import pandas as pd
import os
import glob

# Mocking the glob and os modules to control file operations
class MockGlob:
    def __init__(self, files):
        self.files = files

    def glob(self, pattern):
        return [file for file in self.files if pattern in file]

class MockOs:
    def path(self):
        pass

@pytest.fixture
def mock_glob(monkeypatch):
    mock_files = [
        './data_files/file1.csv',
        './data_files/file2.csv',
        './data_files/file3.csv'
    ]
    monkeypatch.setattr(glob, 'glob', MockGlob(mock_files).glob)
    return mock_files

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'path', MockOs())

def test_task_func_with_valid_input(mock_glob, mock_os):
    my_list = [1, 2]
    result = task_func(my_list)
    assert len(result) == 6  # 3 files * 2 rows per file (assuming each file has 2 rows)

def test_task_func_with_empty_list(mock_glob, mock_os):
    my_list = []
    result = task_func(my_list)
    assert len(result) == 3  # 3 files * 1 row per file (assuming each file has 1 row)

def test_task_func_with_non_list_input():
    with pytest.raises(TypeError):
        task_func("not_a_list")

def test_task_func_with_no_files_found(mock_glob, mock_os):
    mock_glob = []
    with pytest.raises(FileNotFoundError):
        task_func([1])

def test_task_func_with_insufficient_files(mock_glob, mock_os):
    my_list = [5]  # Requesting more files than available
    with pytest.raises(FileNotFoundError):
        task_func(my_list)