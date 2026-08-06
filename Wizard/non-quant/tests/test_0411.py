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
    end_date = '2021-01-31'
    expected_df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10', '2021-01-11', '2021-01-12', '2021-01-13', '2021-01-14', '2021-01-15', '2021-01-16', '2021-01-17', '2021-01-18', '2021-01-19', '2021-01-20', '2021-01-21', '2021-01-22', '2021-01-23', '2021-01-24', '2021-01-25', '2021-01-26', '2021-01-27', '2021-01-28', '2021-01-29', '2021-01-30', '2021-01-31'], 'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]})
    actual_df = task_func(excel_directory, file_name, column_name, start_date, end_date)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input - file does not exist
    excel_directory = 'data'
    file_name = 'invalid.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-01-31'
    with pytest.raises(FileNotFoundError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    # Test case 3: Invalid input - column does not exist
    excel_directory = 'data'
    file_name = 'test.xlsx'
    column_name = 'Invalid'
    start_date = '2021-01-01'
    end_date = '2021-01-31'
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    # Test case 4: Invalid input - date format is incorrect
    excel_directory = 'data'
    file_name = 'test.xlsx'
    column_name = 'Date'
    start_date = '2021-01-01'
    end_date = '2021-01-31-'
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)