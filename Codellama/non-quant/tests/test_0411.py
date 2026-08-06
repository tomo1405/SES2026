import pandas as pd
import pytest
from src_0411 import task_func


def test_task_func_valid_input():
    excel_directory = "path/to/excel/directory"
    file_name = "file_name.xlsx"
    column_name = "date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    expected_df = pd.DataFrame({"date": ["2022-01-01", "2022-01-02", "2022-01-03"]})

    actual_df = task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert actual_df.equals(expected_df)

def test_task_func_invalid_input_file_not_found():
    excel_directory = "path/to/excel/directory"
    file_name = "file_name.xlsx"
    column_name = "date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    with pytest.raises(FileNotFoundError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_invalid_input_column_not_found():
    excel_directory = "path/to/excel/directory"
    file_name = "file_name.xlsx"
    column_name = "date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)

def test_task_func_invalid_input_date_format():
    excel_directory = "path/to/excel/directory"
    file_name = "file_name.xlsx"
    column_name = "date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, start_date, end_date)