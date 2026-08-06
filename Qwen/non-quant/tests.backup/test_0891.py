import pytest
from src_0891 import task_func
import pandas as pd
import os
import random

# Mocking os.path.exists to simulate file existence
def mock_os_path_exists(path):
    return True

# Mocking pd.read_csv to simulate reading a CSV file
def mock_pd_read_csv(path):
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Mocking random.randint to control randomness
def mock_random_randint(a, b):
    return 1  # Always return the first file and at least one row

@pytest.fixture(autouse=True)
def patch_modules(monkeypatch):
    monkeypatch.setattr(os, 'path.exists', mock_os_path_exists)
    monkeypatch.setattr(pd, 'read_csv', mock_pd_read_csv)
    monkeypatch.setattr(random, 'randint', mock_random_randint)

def test_task_func_with_seed():
    data_dir = '/test_data'
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
    seed = 42

    file, selected_rows = task_func(data_dir, csv_files, seed)

    assert file == 'file1.csv'
    assert isinstance(selected_rows, pd.DataFrame)
    assert not selected_rows.empty

def test_task_func_without_seed():
    data_dir = '/test_data'
    csv_files = ['file1.csv', 'file2.csv', 'file3.csv']

    file, selected_rows = task_func(data_dir, csv_files)

    assert file in csv_files
    assert isinstance(selected_rows, pd.DataFrame)
    assert not selected_rows.empty

def test_task_func_empty_file():
    data_dir = '/test_data'
    csv_files = ['empty_file.csv']

    def mock_pd_read_csv_empty(path):
        raise pd.errors.EmptyDataError

    with pytest.raises(pd.errors.EmptyDataError):
        task_func(data_dir, csv_files)

    # Reset the mock to its original state
    pd.read_csv = mock_pd_read_csv

def test_task_func_nonexistent_file():
    data_dir = '/test_data'
    csv_files = ['nonexistent_file.csv']

    def mock_os_path_exists_nonexistent(path):
        return False

    with pytest.raises(FileNotFoundError):
        task_func(data_dir, csv_files)

    # Reset the mock to its original state
    os.path.exists = mock_os_path_exists