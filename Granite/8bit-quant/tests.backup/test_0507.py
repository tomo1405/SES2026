import pytest
from src_0507 import task_func

def test_task_func():
    data = [
        ["2023-01-01", 25, 60, 10, 0.2],
        ["2023-01-02", 28, 65, 15, 0.3],
        ["2023-01-03", 22, 55, 5, 0.1],
        ["2023-01-04", 30, 70, 12, 0.4],
    ]
    column = "Temperature"
    expected_result = {
        "sum": 125.0,
        "mean": 31.25,
        "min": 22.0,
        "max": 30.0,
    }
    result = task_func(column, data)
    assert result == expected_result

def test_task_func_empty_data():
    data = []
    column = "Temperature"
    expected_result = {
        "sum": 0.0,
        "mean": np.nan,
        "min": np.inf,
        "max": -np.inf,
    }
    result = task_func(column, data)
    assert result == expected_result