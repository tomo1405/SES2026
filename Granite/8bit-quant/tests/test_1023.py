import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError
from src_1023 import task_func
import pytest

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv", "column_name")

def test_empty_data():
    with pytest.raises(EmptyDataError):
        task_func("empty_file.csv", "column_name")

def test_column_not_found():
    with pytest.raises(ValueError):
        task_func("valid_file.csv", "nonexistent_column")

def test_date_format():
    df = task_func("valid_file.csv", "column_name", "%Y/%m/%d")
    assert df["column_name"].dt.strftime("%Y/%m/%d").tolist() == ["2023/01/01", "2023/01/02"]

def test_sorted_by_date():
    df = task_func("valid_file.csv", "column_name")
    assert df["column_name"].dt.date.tolist() == ["2023-01-02", "2023-01-01"]