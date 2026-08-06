import pytest
from src_0508 import task_func

def test_task_func_valid_column():
    column = "Open"
    data = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12]
    ]
    result = task_func(column, data)
    assert result == {
        "sum": 16,
        "mean": 8.0,
        "min": 1,
        "max": 8
    }

def test_task_func_invalid_column():
    column = "Price"
    data = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12]
    ]
    with pytest.raises(ValueError, match="Invalid column name."):
        task_func(column, data)

def test_task_func_invalid_data_type():
    column = "Open"
    data = {
        "Date": [1, 2],
        "Open": [3, 4],
        "High": [5, 6],
        "Low": [7, 8],
        "Close": [9, 10],
        "Volume": [11, 12]
    }
    with pytest.raises(ValueError, match="Data must be a list of lists, with each inner list matching the length of the column names."):
        task_func(column, data)

def test_task_func_empty_data():
    column = "Open"
    data = []
    result = task_func(column, data)
    assert result == {
        "sum": 0,
        "mean": float("nan"),
        "min": float("nan"),
        "max": float("nan")
    }

def test_task_func_single_row_data():
    column = "Open"
    data = [[1, 2, 3, 4, 5, 6]]
    result = task_func(column, data)
    assert result == {
        "sum": 1,
        "mean": 1.0,
        "min": 1,
        "max": 1
    }