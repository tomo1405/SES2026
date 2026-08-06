import pytest
from src_0379 import task_func
import os
import pandas as pd
from texttable import Texttable

# Mocking os.path.exists and glob.glob
class MockOsPathExists:
    def __init__(self, exists=True):
        self.exists = exists

    def __call__(self, path):
        return self.exists

class MockGlob:
    def __init__(self, files):
        self.files = files

    def __call__(self, pattern):
        return self.files

# Mocking pd.read_csv
class MockPdReadCsv:
    def __init__(self, data=None, raise_empty=False):
        self.data = data
        self.raise_empty = raise_empty

    def __call__(self, file):
        if self.raise_empty:
            raise pd.errors.EmptyDataError(f"Error when reading file '{file}'.")
        return self.data

def test_task_func_no_directory():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(data_dir='./nonexistent_dir/')
    assert str(excinfo.value) == "The directory './nonexistent_dir/' does not exist."

def test_task_func_no_csv_files():
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dir='./empty_dir/')
    assert str(excinfo.value) == "No CSV files found in the directory './empty_dir/'."

def test_task_func_with_csv_files(mocker):
    mock_os_path_exists = MockOsPathExists(exists=True)
    mock_glob = MockGlob(files=['./data/file1.csv', './data/file2.csv'])
    mock_pd_read_csv = MockPdReadCsv(data=pd.DataFrame([[1, 2], [3, 4]]))

    mocker.patch('src_0379.os.path.exists', mock_os_path_exists)
    mocker.patch('src_0379.glob.glob', mock_glob)
    mocker.patch('src_0379.pd.read_csv', mock_pd_read_csv)

    result = task_func(data_dir='./data/')
    expected_table = Texttable()
    expected_table.add_rows([
        ['File', 'Rows', 'Columns'],
        ['file1.csv', 2, 2],
        ['file2.csv', 2, 2]
    ])
    assert result == expected_table.draw()

def test_task_func_with_empty_csv_file(mocker):
    mock_os_path_exists = MockOsPathExists(exists=True)
    mock_glob = MockGlob(files=['./data/empty_file.csv'])
    mock_pd_read_csv = MockPdReadCsv(raise_empty=True)

    mocker.patch('src_0379.os.path.exists', mock_os_path_exists)
    mocker.patch('src_0379.glob.glob', mock_glob)
    mocker.patch('src_0379.pd.read_csv', mock_pd_read_csv)

    with pytest.raises(pd.errors.EmptyDataError) as excinfo:
        task_func(data_dir='./data/')
    assert str(excinfo.value) == "Error when reading file './data/empty_file.csv'."