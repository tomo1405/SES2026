import pytest
from src_1023 import task_func
import pandas as pd
import os
from datetime import datetime

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.csv", "date_column")
    assert str(excinfo.value) == "The file non_existent_file.csv does not exist."

def test_task_func_empty_file():
    with open("empty_file.csv", "w") as f:
        pass
    result = task_func("empty_file.csv", "date_column")
    assert result.empty
    os.remove("empty_file.csv")

def test_task_func_column_not_found():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    df.to_csv("test_file.csv", index=False)
    with pytest.raises(ValueError) as excinfo:
        task_func("test_file.csv", "date_column")
    assert str(excinfo.value) == "The column date_column is not found in the file."
    os.remove("test_file.csv")

def test_task_func_valid_data():
    data = {
        "date_column": ["2023-10-01", "2023-10-02", "2023-10-03"],
        "value": [10, 20, 30]
    }
    df = pd.DataFrame(data)
    df.to_csv("test_file.csv", index=False)
    result = task_func("test_file.csv", "date_column")
    assert result.equals(df)
    os.remove("test_file.csv")

def test_task_func_future_dates():
    future_date = (datetime.now() + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    data = {
        "date_column": [future_date],
        "value": [10]
    }
    df = pd.DataFrame(data)
    df.to_csv("test_file.csv", index=False)
    result = task_func("test_file.csv", "date_column")
    assert result.empty
    os.remove("test_file.csv")

def test_task_func_past_dates():
    past_date = (datetime.now() - pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    data = {
        "date_column": [past_date],
        "value": [10]
    }
    df = pd.DataFrame(data)
    df.to_csv("test_file.csv", index=False)
    result = task_func("test_file.csv", "date_column")
    assert not result.empty
    os.remove("test_file.csv")