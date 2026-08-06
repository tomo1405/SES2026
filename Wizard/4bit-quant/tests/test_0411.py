python
import os
import pandas as pd
from datetime import datetime
import pytest

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    excel_file = os.path.join(excel_directory, file_name)
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"The file {excel_file} does not exist.")

    df = pd.read_excel(excel_file, engine='openpyxl')

    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame.")

    try:
        df[column_name] = pd.to_datetime(df[column_name])
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Date format is incorrect. Please use 'yyyy-mm-dd' format.") from e

    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]

    return filtered_df

def test_task_func():
    # Test case 1: Valid input
    excel_directory = 'data'
    file_name = 'test.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31'
    expected_output = pd.DataFrame({'Date': ['2021-05-01', '2021-06-01', '2021-07-01'], 'Value': [10, 20, 30]})
    actual_output = task_func(excel_directory, file_name, column_name, start_date, end_date)
    assert actual_output.equals(expected_output)

    # Test case 2: Invalid input - file does not exist
    excel_directory = 'data'
    file_name = 'invalid.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31'
    with pytest.raises(FileNotFoundError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    # Test case 3: Invalid input - column does not exist
    excel_directory = 'data'
    file_name = 'test.xlsx'
    column_name = 'Invalid'
    start_date = '2021-01-01'
    end_date = '2021-12-31'
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    # Test case 4: Invalid input - date format is incorrect
    excel_directory = 'data'
    file_name = 'test.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-12-31-'
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)