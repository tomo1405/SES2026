import pytest
from src_0889 import task_func
import pandas as pd
import os

# Mocking os.path.join and pd.read_csv to avoid file I/O operations
class MockOsPath:
    @staticmethod
    def join(*args):
        return os.path.join(*args)

class MockPdReadCsv:
    def __init__(self, data):
        self.data = data

    def __call__(self, path):
        return pd.DataFrame(self.data)

@pytest.fixture
def mock_os_path(monkeypatch):
    monkeypatch.setattr(os.path, 'join', MockOsPath.join)

@pytest.fixture
def mock_pd_read_csv(monkeypatch):
    def side_effect(path):
        if path == os.path.join('data_dir', 'file1.csv'):
            return pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        elif path == os.path.join('data_dir', 'file2.csv'):
            return pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        else:
            raise FileNotFoundError(f"No such file: {path}")
    
    monkeypatch.setattr(pd, 'read_csv', side_effect)

def test_task_func(mock_os_path, mock_pd_read_csv):
    data_dir = 'data_dir'
    csv_files = ['file1.csv', 'file2.csv']
    expected_output = pd.DataFrame({
        'A': [1, 2, 5, 6],
        'B': [3, 4, 7, 8]
    })

    result = task_func(data_dir, csv_files)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_nonexistent_file(mock_os_path, mock_pd_read_csv):
    data_dir = 'data_dir'
    csv_files = ['file1.csv', 'nonexistent.csv']

    with pytest.raises(FileNotFoundError):
        task_func(data_dir, csv_files)