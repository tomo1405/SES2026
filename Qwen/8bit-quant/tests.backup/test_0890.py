import pytest
from src_0890 import task_func
import pandas as pd
import numpy as np
import os

# Mocking os.path.join to control file paths
def mock_os_path_join(data_dir, csv_file):
    return f"{data_dir}/{csv_file}"

# Mocking pd.read_csv to simulate reading a CSV file
def mock_pd_read_csv(file_path):
    if file_path == "test_data/empty.csv":
        raise pd.errors.EmptyDataError("No data")
    elif file_path == "test_data/numeric_data.csv":
        return pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [5, np.nan, np.nan, 8]
        })
    elif file_path == "test_data/non_numeric_data.csv":
        return pd.DataFrame({
            'C': ['a', 'b', 'c'],
            'D': [1, 2, np.nan]
        })

# Monkeypatching
@pytest.fixture(autouse=True)
def patch_os_and_pandas(monkeypatch):
    monkeypatch.setattr(os.path, 'join', mock_os_path_join)
    monkeypatch.setattr(pd, 'read_csv', mock_pd_read_csv)

def test_task_func_empty_file():
    result = task_func("test_data", "empty.csv")
    assert result.empty

def test_task_func_numeric_data():
    result = task_func("test_data", "numeric_data.csv")
    expected_mean_A = (1 + 2 + 4) / 3
    expected_mean_B = (5 + 8) / 2
    assert result['A'].isnull().sum() == 0
    assert result['B'].isnull().sum() == 0
    assert np.isclose(result['A'].mean(), expected_mean_A)
    assert np.isclose(result['B'].mean(), expected_mean_B)

def test_task_func_non_numeric_data():
    result = task_func("test_data", "non_numeric_data.csv")
    assert result['C'].isnull().sum() == 0
    assert result['D'].isnull().sum() == 1
    assert result['D'].dtype == np.float64