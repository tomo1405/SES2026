import pytest
from src_0513 import task_func
import pandas as pd
import numpy as np

def test_task_func_positive_values():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300],
    ]
    column = "Quantity Sold"
    result, ax = task_func(column, data)
    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30
    assert ax.title.get_text() == "Bar Chart of Quantity Sold"

def test_task_func_negative_values():
    data = [
        ["Product A", -10, 100],
        ["Product B", 20, -200],
        ["Product C", 30, 300],
    ]
    column = "Quantity Sold"
    with pytest.raises(ValueError):
        task_func(column, data)

def test_task_func_invalid_column():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300],
    ]
    column = "Invalid Column"
    with pytest.raises(KeyError):
        task_func(column, data)