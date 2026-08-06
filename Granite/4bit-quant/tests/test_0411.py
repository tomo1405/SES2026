import pandas as pd
import pytest
from src_0411 import task_func


def test_task_func():
    excel_directory = "path/to/excel/directory"
    file_name = "example.xlsx"
    column_name = "Date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    expected_output = pd.DataFrame({
        "Date": ["2022-01-01", "2022-01-02", "2022-01-03"],
        "Value": [10, 20, 30]
    })

    actual_output = task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert actual_output.equals(expected_output)

def test_file_not_found_error():
    excel_directory = "path/to/excel/directory"
    file_name = "nonexistent.xlsx"
    column_name = "Date"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    with pytest.raises(FileNotFoundError) as e:
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert "The file" in str(e.value)

def test_column_not_found_error():
    excel_directory = "path/to/excel/directory"
    file_name = "example.xlsx"
    column_name = "Invalid Column"
    start_date = "2022-01-01"
    end_date = "2022-01-31"

    with pytest.raises(ValueError) as e:
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert "Column" in str(e.value)

def test_date_format_error():
    excel_directory = "path/to/excel/directory"
    file_name = "example.xlsx"
    column_name = "Date"
    start_date = "2022/01/01"
    end_date = "2022/01/31"

    with pytest.raises(ValueError) as e:
        task_func(excel_directory, file_name, column_name, start_date, end_date)

    assert "Date format is incorrect" in str(e.value)