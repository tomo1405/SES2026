import pytest
from src_0514 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Steps": [1000, 1200, 1100],
        "Calories Burned": [500, 550, 520],
        "Distance Walked": [3.2, 3.5, 3.3]
    }
    result, _ = task_func("Steps", data)
    assert result == {
        "sum": 3300,
        "mean": 1100.0,
        "min": 1000,
        "max": 1200
    }

def test_task_func_invalid_column():
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Steps": [1000, 1200, 1100],
        "Calories Burned": [500, 550, 520],
        "Distance Walked": [3.2, 3.5, 3.3]
    }
    with pytest.raises(KeyError):
        task_func("InvalidColumn", data)

def test_task_func_no_data():
    with pytest.raises(ValueError):
        task_func("Steps", {})

def test_task_func_negative_values():
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Steps": [1000, -1200, 1100],
        "Calories Burned": [500, 550, 520],
        "Distance Walked": [3.2, 3.5, 3.3]
    }
    with pytest.raises(ValueError):
        task_func("Steps", data)