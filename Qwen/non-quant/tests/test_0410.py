import pytest
from src_0410 import task_func
import os
import pandas as pd
import numpy as np

# Mocking os.path.exists and pd.read_excel
def mock_os_path_exists(path):
    return True

def mock_pd_read_excel(file_path):
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    return pd.DataFrame(data)

# Patching the functions
@pytest.fixture(autouse=True)
def patch_os_and_pandas(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr(pd, 'read_excel', mock_pd_read_excel)

def test_task_func_valid_column():
    excel_file_path = '/path/to/excel'
    file_name = 'test.xlsx'
    column_name = 'A'
    result = task_func(excel_file_path, file_name, column_name)
    expected_result = {
        'mean': 3.0,
        'median': 3.0,
        'std_dev': 1.4142135623730951
    }
    assert result == expected_result

def test_task_func_invalid_column():
    excel_file_path = '/path/to/excel'
    file_name = 'test.xlsx'
    column_name = 'C'
    with pytest.raises(ValueError) as excinfo:
        task_func(excel_file_path, file_name, column_name)
    assert str(excinfo.value) == "Column 'C' not found in the Excel file."

def test_task_func_file_not_found():
    excel_file_path = '/path/to/excel'
    file_name = 'nonexistent.xlsx'
    column_name = 'A'
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(excel_file_path, file_name, column_name)
    assert str(excinfo.value) == f"No file found at {os.path.join(excel_file_path, file_name)}"