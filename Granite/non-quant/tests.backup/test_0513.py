import pandas as pd
import numpy as np
import pytest
from src_0513 import task_func

def test_task_func():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300],
    ]
    column = "Quantity Sold"
    expected_result = {
        "sum": 60,
        "mean": 20.0,
        "min": 10,
        "max": 30,
    }
    expected_ax_title = "Bar Chart of Quantity Sold"
    result, ax = task_func(column, data)
    assert result == expected_result
    assert ax.get_title() == expected_ax_title

def test_task_func_with_negative_values():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", -30, 300],
    ]
    column = "Quantity Sold"
    with pytest.raises(ValueError) as exc_info:
        task_func(column, data)
    assert "Value must not be negative" in str(exc_info.value)