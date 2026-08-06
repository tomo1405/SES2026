import os
import pandas as pd
from datetime import datetime
from src_0411 import task_func
import pytest

@pytest.fixture
def excel_directory():
    return "path/to/excel/directory"

@pytest.fixture
def file_name():
    return "example.xlsx"

@pytest.fixture
def column_name():
    return "date_column"

@pytest.fixture
def start_date():
    return "2022-01-01"

@pytest.fixture
def end_date():
    return "2022-12-31"

def test_file_exists(excel_directory, file_name):
    with pytest.raises(FileNotFoundError):
        task_func(excel_directory, "nonexistent_file.xlsx", column_name, start_date, end_date)

def test_column_exists(excel_directory, file_name):
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, "nonexistent_column", start_date, end_date)

def test_date_format(excel_directory, file_name, column_name, start_date, end_date):
    with pytest.raises(ValueError):
        task_func(excel_directory, file_name, column_name, "01-01-2022", end_date)

def test_filter_data(excel_directory, file_name, column_name, start_date, end_date):
    df = pd.DataFrame({column_name: pd.date_range(start="2020-01-01", periods=100, freq="D")})
    filtered_df = task_func(excel_directory, file_name, column_name, start_date, end_date)
    assert len(filtered_df) == 365