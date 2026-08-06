import pytest
from src_0891 import task_func
import os
import pandas as pd

# Mocking os.path.join and pd.read_csv to avoid file system access and actual CSV reading
def mock_os_path_join(*args):
    return os.path.join(*args)

def mock_pd_read_csv(file_path):
    # Create a sample DataFrame for testing
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    return pd.DataFrame(data)

# Patching the functions
os.path.join = mock_os_path_join
pd.read_csv = mock_pd_read_csv

def test_task_func():
    # Test with default parameters
    data_dir = '/path/to/data'
    result = task_func(data_dir)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert result[0] in ['file1.csv', 'file2.csv', 'file3.csv']
    assert isinstance(result[1], pd.DataFrame)
    assert not result[1].empty

    # Test with custom seed
    seed = 42
    result_with_seed = task_func(data_dir, seed=seed)
    assert result_with_seed[0] == result[0]  # Same file should be selected with the same seed

    # Test with custom csv_files
    custom_csv_files = ['custom1.csv', 'custom2.csv']
    result_custom_files = task_func(data_dir, csv_files=custom_csv_files)
    assert result_custom_files[0] in custom_csv_files

    # Test with empty DataFrame
    def mock_empty_pd_read_csv(file_path):
        raise pd.errors.EmptyDataError("Empty DataFrame")

    pd.read_csv = mock_empty_pd_read_csv
    result_empty_df = task_func(data_dir)
    assert isinstance(result_empty_df[1], pd.DataFrame)
    assert result_empty_df[1].empty