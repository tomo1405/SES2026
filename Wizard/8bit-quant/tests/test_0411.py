python
import os
import pandas as pd
from datetime import datetime
import pytest

from src_0411 import task_func

def test_task_func_valid_input():
    excel_directory = 'data'
    file_name = 'example.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    expected_df = pd.DataFrame({'Date': ['2021-06-01', '2021-07-01', '2021-08-01'], 'Value': [10, 20, 30]})

    actual_df = task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert actual_df.equals(expected_df)

def test_task_func_invalid_file():
    excel_directory = 'data'
    file_name = 'invalid.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    with pytest.raises(FileNotFoundError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_invalid_column():
    excel_directory = 'data'
    file_name = 'example.xlsx'
    column_name = 'Invalid'
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_invalid_date_format():
    excel_directory = 'data'
    file_name = 'example.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31-'

    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)