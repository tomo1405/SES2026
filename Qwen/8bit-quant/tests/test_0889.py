import pytest
from src_0889 import task_func
import pandas as pd
import os

# Mocking the os module to simulate file paths
class MockOs:
    @staticmethod
    def path_join(data_dir, file):
        return os.path.join(data_dir, file)

# Mocking the pandas module to simulate reading CSV files
class MockPd:
    @staticmethod
    def read_csv(file_path):
        # Simulate reading a CSV file and returning a DataFrame
        if file_path == 'data_dir/file1.csv':
            return pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        elif file_path == 'data_dir/file2.csv':
            return pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        else:
            raise FileNotFoundError(f"No such file: {file_path}")

    @staticmethod
    def concat(dfs, ignore_index):
        return pd.concat(dfs, ignore_index=ignore_index)

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr(os, 'path', MockOs)

@pytest.fixture
def mock_pd(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', MockPd.read_csv)
    monkeypatch.setattr(pd, 'concat', MockPd.concat)

def test_task_func(mock_os, mock_pd):
    data_dir = 'data_dir'
    csv_files = ['file1.csv', 'file2.csv']
    expected_df = pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8]})
    
    result_df = task_func(data_dir, csv_files)
    
    assert result_df.equals(expected_df)

def test_task_func_single_file(mock_os, mock_pd):
    data_dir = 'data_dir'
    csv_files = ['file1.csv']
    expected_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    
    result_df = task_func(data_dir, csv_files)
    
    assert result_df.equals(expected_df)

def test_task_func_no_files(mock_os, mock_pd):
    data_dir = 'data_dir'
    csv_files = []
    expected_df = pd.DataFrame()
    
    result_df = task_func(data_dir, csv_files)
    
    assert result_df.equals(expected_df)

def test_task_func_nonexistent_file(mock_os, mock_pd):
    data_dir = 'data_dir'
    csv_files = ['nonexistent.csv']
    
    with pytest.raises(FileNotFoundError):
        task_func(data_dir, csv_files)