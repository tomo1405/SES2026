import pytest
from src_0410 import task_func
import os
import pandas as pd
import numpy as np

# Mocking the os.path.exists and pd.read_excel functions
def mock_os_path_exists(path):
    return True

def mock_pd_read_excel(file_path):
    # Create a sample DataFrame
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    return pd.DataFrame(data)

def test_task_func_valid_file_and_column():
    excel_file_path = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'A'

    # Monkey patch os.path.exists and pd.read_excel
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(os.path, 'exists', mock_os_path_exists)
        mp.setattr(pd, 'read_excel', mock_pd_read_excel)

        result = task_func(excel_file_path, file_name, column_name)

    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'std_dev' in result
    assert result['mean'] == 3.0
    assert result['median'] == 3.0
    assert np.isclose(result['std_dev'], np.std([1, 2, 3, 4, 5]))

def test_task_func_file_not_found():
    excel_file_path = '/path/to/excel'
    file_name = 'nonexistent.xlsx'
    column_name = 'A'

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(excel_file_path, file_name, column_name)

    assert str(excinfo.value) == "No file found at /path/to/excel/nonexistent.xlsx"

def test_task_func_column_not_found():
    excel_file_path = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'C'

    # Monkey patch os.path.exists and pd.read_excel
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(os.path, 'exists', mock_os_path_exists)
        mp.setattr(pd, 'read_excel', mock_pd_read_excel)

    with pytest.raises(ValueError) as excinfo:
        task_func(excel_file_path, file_name, column_name)

    assert str(excinfo.value) == "Column 'C' not found in the Excel file."