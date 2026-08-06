python
import pytest
from src_0508 import task_func

def test_task_func_valid_column():
    column = "Close"
    data = [
        ["Date", "Open", "High", "Low", "Close", "Volume"],
        ["2021-01-01", 100, 105, 95, 100, 1000],
        ["2021-01-02", 105, 110, 99, 105, 2000],
        ["2021-01-03", 99, 101, 97, 99, 3000],
    ]
    expected_result = {
        "sum": 4050,
        "mean": 100.0,
        "min": 97,
        "max": 105,
    }
    assert task_func(column, data) == expected_result

def test_task_func_invalid_column():
    column = "Invalid"
    data = [
        ["Date", "Open", "High", "Low", "Close", "Volume"],
        ["2021-01-01", 100, 105, 95, 100, 1000],
        ["2021-01-02", 105, 110, 99, 105, 2000],
        ["2021-01-03", 99, 101, 97, 99, 3000],
    ]
    with pytest.raises(ValueError):
        task_func(column, data)

def test_task_func_invalid_data():
    column = "Close"
    data = [
        ["Date", "Open", "High", "Low", "Close", "Volume"],
        ["2021-01-01", 100, 105, 95, 100, 1000],
        ["2021-01-02", 105, 110, 99, 105, 2000],
        ["2021-01-03", 99, 101, 97, 99],
    ]
    with pytest.raises(ValueError):
        task_func(column, data)

def test_task_func_empty_data():
    column = "Close"
    data = [
        ["Date", "Open", "High", "Low", "Close", "Volume"],
    ]
    expected_result = {
        "sum": 0,
        "mean": float("nan"),
        "min": float("nan"),
        "max": float("nan"),
    }
    assert task_func(column, data) == expected_result