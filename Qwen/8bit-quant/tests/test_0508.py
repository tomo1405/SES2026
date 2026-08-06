import pytest
from src_0508 import task_func

def test_task_func_valid_column_and_data():
    column = "Close"
    data = [
        ["2023-01-01", 100, 105, 98, 102, 500],
        ["2023-01-02", 102, 107, 100, 104, 600],
        ["2023-01-03", 104, 109, 102, 106, 700]
    ]
    expected_result = {
        "sum": 312,
        "mean": 104.0,
        "min": 102,
        "max": 106
    }
    assert task_func(column, data) == expected_result

def test_task_func_invalid_column():
    column = "Price"
    data = [
        ["2023-01-01", 100, 105, 98, 102, 500],
        ["2023-01-02", 102, 107, 100, 104, 600],
        ["2023-01-03", 104, 109, 102, 106, 700]
    ]
    with pytest.raises(ValueError, match="Invalid column name."):
        task_func(column, data)

def test_task_func_invalid_data_type():
    column = "Close"
    data = "not a list"
    with pytest.raises(ValueError, match="Data must be a list of lists, with each inner list matching the length of the column names."):
        task_func(column, data)

def test_task_func_invalid_inner_list_length():
    column = "Close"
    data = [
        ["2023-01-01", 100, 105, 98, 102, 500],
        ["2023-01-02", 102, 107, 100],  # Incorrect length
        ["2023-01-03", 104, 109, 102, 106, 700]
    ]
    with pytest.raises(ValueError, match="Data must be a list of lists, with each inner list matching the length of the column names."):
        task_func(column, data)

def test_task_func_empty_data():
    column = "Close"
    data = []
    expected_result = {
        "sum": 0,
        "mean": float("nan"),
        "min": float("nan"),
        "max": float("nan")
    }
    assert task_func(column, data) == expected_result

def test_task_func_single_row_data():
    column = "Close"
    data = [["2023-01-01", 100, 105, 98, 102, 500]]
    expected_result = {
        "sum": 102,
        "mean": 102.0,
        "min": 102,
        "max": 102
    }
    assert task_func(column, data) == expected_result