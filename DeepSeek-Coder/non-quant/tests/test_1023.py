import pytest
from src_1023 import task_func
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv", "column_name")

def test_task_func_empty_file():
    with open("temp_empty.csv", "w") as f:
        pass
    try:
        result = task_func("temp_empty.csv", "column_name")
        assert result.empty
    finally:
        os.remove("temp_empty.csv")

def test_task_func_column_not_found():
    with open("temp.csv", "w") as f:
        f.write("col1,col2\n1,2\n3,4")
    try:
        result = task_func("temp.csv", "non_existent_column")
        assert result.empty
    finally:
        os.remove("temp.csv")

def test_task_func_valid_file():
    with open("temp.csv", "w") as f:
        f.write("date\n2023-01-01\n2023-01-02")
    try:
        result = task_func("temp.csv", "date")
        assert not result.empty
    finally:
        os.remove("temp.csv")