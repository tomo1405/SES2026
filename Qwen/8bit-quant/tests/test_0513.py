import pytest
from src_0513 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_data():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    result, ax = task_func("Quantity Sold", data)
    assert result == {"sum": 60, "mean": 20.0, "min": 10, "max": 30}

def test_task_func_negative_values():
    data = [
        ["Product A", -10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func("Quantity Sold", data)
    assert str(excinfo.value) == "Value must not be negative"

def test_task_func_invalid_column():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    with pytest.raises(KeyError):
        task_func("Invalid Column", data)

def test_task_func_empty_data():
    data = []
    result, ax = task_func("Quantity Sold", data)
    assert result == {"sum": 0, "mean": np.nan, "min": np.nan, "max": np.nan}