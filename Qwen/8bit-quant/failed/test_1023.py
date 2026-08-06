import pytest
from src_1023 import task_func
import pandas as pd
import os
from datetime import datetime

# Mocking os.path.isfile to control file existence
def mock_isfile(path):
    return path == "existing_file.csv"

# Mocking pd.read_csv to simulate different scenarios
def mock_read_csv(path):
    if path == "empty_file.csv":
        raise pd.errors.EmptyDataError("No columns to parse from file")
    elif path == "non_empty_file.csv":
        return pd.DataFrame({
            'date_column': ['2023-10-01', '2023-10-15']
        })
    else:
        raise FileNotFoundError(f"The file {path} does not exist.")

# Mocking datetime.now to control the current date
def mock_now():
    return datetime(2023, 10, 10)

# Patching the required functions and methods
@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    monkeypatch.setattr(datetime, 'now', mock_now)

def test_task_func_existing_file_with_data():
    result = task_func("non_empty_file.csv", "date_column")
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result['date_column'].iloc[0] == datetime(2023, 10, 15)

def test_task_func_existing_file_with_no_data():
    result = task_func("empty_file.csv", "date_column")
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_task_func_non_existing_file():
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.csv does not exist."):
        task_func("non_existent_file.csv", "date_column")

def test_task_func_missing_column():
    with pytest.raises(ValueError, match="The column missing_column is not found in the file."):
        task_func("non_empty_file.csv", "missing_column")

def test_task_func_with_custom_date_format():
    result = task_func("non_empty_file.csv", "date_column", "%Y-%m-%d")
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result['date_column'].iloc[0] == datetime(2023, 10, 15)