import pytest
from src_0513 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_data():
    data = [
        ["Product A", 10, 200],
        ["Product B", 15, 300],
        ["Product C", 20, 400]
    ]
    result, ax = task_func("Quantity Sold", data)
    assert result == {"sum": 45, "mean": 15, "min": 10, "max": 20}
    assert isinstance(ax, pd.DataFrame)

def test_task_func_negative_values():
    data = [
        ["Product A", -10, 200],
        ["Product B", 15, 300],
        ["Product C", 20, 400]
    ]
    with pytest.raises(ValueError, match="Value must not be negative"):
        task_func("Quantity Sold", data)

def test_task_func_nonexistent_column():
    data = [
        ["Product A", 10, 200],
        ["Product B", 15, 300],
        ["Product C", 20, 400]
    ]
    with pytest.raises(KeyError):
        task_func("Nonexistent Column", data)

def test_task_func_empty_data():
    data = []
    result, ax = task_func("Quantity Sold", data)
    assert result == {"sum": np.nan, "mean": np.nan, "min": np.nan, "max": np.nan}
    assert isinstance(ax, pd.DataFrame)