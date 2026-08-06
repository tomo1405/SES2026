import pytest
from src_0508 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_input():
    data = [
        ["2023-01-01", 100, 110, 90, 105, 1000],
        ["2023-01-02", 105, 115, 95, 102, 1500]
    ]
    result = task_func("Close", data)
    assert result == {
        "sum": 205,
        "mean": 102.5,
        "min": 90,
        "max": 115
    }

def test_task_func_invalid_column():
    data = [
        ["2023-01-01", 100, 110, 90, 105, 1000],
        ["2023-01-02", 105, 115, 95, 102, 1500]
    ]
    with pytest.raises(ValueError):
        task_func("InvalidColumn", data)

def test_task_func_invalid_data():
    data = [
        ["2023-01-01", 100, 110, 90, 105],  # Missing volume
    ]
    with pytest.raises(ValueError):
        task_func("Close", data)

def test_task_func_empty_data():
    data = []
    result = task_func("Close", data)
    assert result == {
        "sum": 0,
        "mean": float("nan"),
        "min": float("nan"),
        "max": float("nan"),
    }