from datetime import datetime

import pandas as pd
from src_1023 import task_func


def test_task_func_valid_input():
    csv_file_path = "test_data.csv"
    column_name = "date"
    date_format = "%Y-%m-%d"
    expected_output = pd.DataFrame({"date": [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]})

    output = task_func(csv_file_path, column_name, date_format)

    assert output.equals(expected_output)

def test_task_func_invalid_input():
    csv_file_path = "test_data.csv"
    column_name = "date"
    date_format = "%Y-%m-%d"
    expected_output = pd.DataFrame()

    output = task_func(csv_file_path, column_name, date_format)

    assert output.equals(expected_output)

def test_task_func_invalid_column():
    csv_file_path = "test_data.csv"
    column_name = "date"
    date_format = "%Y-%m-%d"
    expected_output = pd.DataFrame()

    output = task_func(csv_file_path, column_name, date_format)

    assert output.equals(expected_output)

def test_task_func_invalid_date_format():
    csv_file_path = "test_data.csv"
    column_name = "date"
    date_format = "%Y-%m-%d"
    expected_output = pd.DataFrame()

    output = task_func(csv_file_path, column_name, date_format)

    assert output.equals(expected_output)