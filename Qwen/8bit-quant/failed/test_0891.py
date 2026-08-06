import pytest
from src_0891 import task_func
import pandas as pd
import os
import random

# Mocking os.path.join and pd.read_csv to avoid file system access and data reading
class MockPathJoin:
    def __call__(self, *args):
        return '/'.join(args)

class MockReadCSV:
    def __init__(self, data):
        self.data = data

    def __call__(self, file_path):
        if file_path == '/mock/data_dir/file1.csv':
            return pd.DataFrame(self.data['file1'])
        elif file_path == '/mock/data_dir/file2.csv':
            return pd.DataFrame(self.data['file2'])
        elif file_path == '/mock/data_dir/file3.csv':
            return pd.DataFrame(self.data['file3'])
        else:
            raise FileNotFoundError(f"No such file: {file_path}")

@pytest.fixture
def mock_os_path_join(monkeypatch):
    monkeypatch.setattr(os, 'path.join', MockPathJoin())

@pytest.fixture
def mock_pd_read_csv(monkeypatch):
    data = {
        'file1': {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']},
        'file2': {'col1': [4, 5, 6], 'col2': ['d', 'e', 'f']},
        'file3': {'col1': [7, 8, 9], 'col2': ['g', 'h', 'i']}
    }
    monkeypatch.setattr(pd, 'read_csv', MockReadCSV(data))

def test_task_func_with_seed(mock_os_path_join, mock_pd_read_csv):
    random.seed(42)
    data_dir = '/mock/data_dir'
    result_file, result_df = task_func(data_dir, seed=42)
    assert result_file in ['file1.csv', 'file2.csv', 'file3.csv']
    assert not result_df.empty

def test_task_func_without_seed(mock_os_path_join, mock_pd_read_csv):
    data_dir = '/mock/data_dir'
    result_file, result_df = task_func(data_dir)
    assert result_file in ['file1.csv', 'file2.csv', 'file3.csv']
    assert not result_df.empty

def test_task_func_empty_data_error(mock_os_path_join, monkeypatch):
    def mock_read_csv(file_path):
        raise pd.errors.EmptyDataError("No data")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    data_dir = '/mock/data_dir'
    result_file, result_df = task_func(data_dir)
    assert result_file in ['file1.csv', 'file2.csv', 'file3.csv']
    assert result_df.empty

def test_task_func_file_not_found_error(mock_os_path_join, monkeypatch):
    def mock_read_csv(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    data_dir = '/mock/data_dir'
    with pytest.raises(FileNotFoundError):
        task_func(data_dir)