import pytest
from src_0382 import task_func
import pandas as pd
import os

# Mocking os.path.exists and pd.read_csv
class MockOsPathExists:
    def __init__(self, exists):
        self.exists = exists

    def __call__(self, path):
        return self.exists

class MockPdReadCsv:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __call__(self, path):
        return self.dataframe

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    monkeypatch.setattr(os, 'path.exists', MockOsPathExists(True))

@pytest.fixture
def mock_pd_read_csv(monkeypatch):
    data = {
        'feature1': [1, 2, 3, 4],
        'feature2': [5, 6, 7, 8],
        'Index': [9, 10, 11, 12]
    }
    df = pd.DataFrame(data)
    monkeypatch.setattr(pd, 'read_csv', MockPdReadCsv(df))

def test_task_func_file_not_found(mock_os_path_exists, monkeypatch):
    monkeypatch.setattr(os, 'path.exists', MockOsPathExists(False))
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent.csv')
    assert str(excinfo.value) == "The file 'non_existent.csv' does not exist."

def test_task_func_target_column_not_found(mock_os_path_exists, mock_pd_read_csv, monkeypatch):
    with pytest.raises(ValueError) as excinfo:
        task_func(target_column='NonExistentColumn')
    assert str(excinfo.value) == "The specified target column 'NonExistentColumn' does not exist in the CSV file."

def test_task_func_success(mock_os_path_exists, mock_pd_read_csv):
    ax, importances = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, list)
    assert len(importances) == 2  # Assuming there are 2 features in the dataset

def test_task_func_with_nan_values(mock_os_path_exists, monkeypatch):
    data_with_nan = {
        'feature1': [1, 2, None, 4],
        'feature2': [5, None, 7, 8],
        'Index': [9, 10, 11, 12]
    }
    df_with_nan = pd.DataFrame(data_with_nan)
    monkeypatch.setattr(pd, 'read_csv', MockPdReadCsv(df_with_nan))
    ax, importances = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, list)
    assert len(importances) == 2  # Assuming there are 2 features in the dataset after dropping NaNs