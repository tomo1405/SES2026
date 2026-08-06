import pytest
from src_0411 import task_func
import pandas as pd
import os
from datetime import datetime

# Mocking the os.path.exists and pd.read_excel functions
def mock_os_path_exists(path):
    return True

def mock_pd_read_excel(file, engine):
    # Create a sample DataFrame for testing
    data = {
        'date_column': ['2023-01-01', '2023-01-15', '2023-02-01'],
        'value': [10, 20, 30]
    }
    return pd.DataFrame(data)

@pytest.fixture(autouse=True)
def patch_os_and_pandas(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr(pd, 'read_excel', mock_pd_read_excel)

def test_task_func_valid_dates():
    excel_directory = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'date_column'
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    result_df = task_func(excel_directory, file_name, column_name, start_date, end_date)
    assert len(result_df) == 2
    assert all(result_df['date_column'] >= datetime.strptime(start_date, '%Y-%m-%d'))
    assert all(result_df['date_column'] <= datetime.strptime(end_date, '%Y-%m-%d'))

def test_task_func_invalid_dates():
    excel_directory = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'date_column'
    start_date = '2023-01-01'
    end_date = '2022-12-31'

    with pytest.raises(ValueError, match="Date range is invalid. Start date should be before or equal to end date."):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_non_existent_file():
    excel_directory = '/path/to/excel'
    file_name = 'non_existent.xlsx'
    column_name = 'date_column'
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    with pytest.raises(FileNotFoundError, match="The file /path/to/excel/non_existent.xlsx does not exist."):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_non_existent_column():
    excel_directory = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'non_existent_column'
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    with pytest.raises(ValueError, match="Column non_existent_column does not exist in the DataFrame."):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_invalid_date_format():
    excel_directory = '/path/to/excel'
    file_name = 'data.xlsx'
    column_name = 'date_column'
    start_date = '2023-01-01'
    end_date = '2023/01/31'  # Invalid format

    with pytest.raises(ValueError, match="Date format is incorrect. Please use 'yyyy-mm-dd' format."):
        task_func(excel_directory, file_name, column_name, start_date, end_date)