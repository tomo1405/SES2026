import pytest
from src_0513 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = {
        "Product": ["A", "B", "C"],
        "Quantity Sold": [10, 20, 30],
        "Total Sales": [100, 200, 300]
    }
    result, _ = task_func("Quantity Sold", data)
    assert result == {
        "sum": 60,
        "mean": 20.0,
        "min": 10,
        "max": 30
    }

    data_negative = {
        "Product": ["A", "B", "C"],
        "Quantity Sold": [-10, 20, 30],
        "Total Sales": [100, -200, 300]
    }
    with pytest.raises(ValueError):
        task_func("Quantity Sold", data_negative)