import pytest
from src_0514 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_column():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    result, ax = task_func("Steps", data)
    assert isinstance(result, dict)
    assert "sum" in result
    assert "mean" in result
    assert "min" in result
    assert "max" in result
    assert result["sum"] == 4500
    assert result["mean"] == 1500
    assert result["min"] == 1000
    assert result["max"] == 2000

def test_task_func_invalid_column():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", 2000, 100, 1.0],
        ["2023-01-03", 1500, 75, 0.75]
    ]
    with pytest.raises(KeyError) as excinfo:
        task_func("InvalidColumn", data)
    assert str(excinfo.value) == "'InvalidColumn' is not a valid column. Choose from ['Date', 'Steps', 'Calories Burned', 'Distance Walked']."


def test_task_func_no_data():
    data = []
    with pytest.raises(ValueError) as excinfo:
        task_func("Steps", data)
    assert str(excinfo.value) == "No data to plot."

def test_task_func_negative_values():
    data = [
        ["2023-01-01", 1000, 50, 0.5],
        ["2023-01-02", -2000, 100, 1.0],  # Negative value
        ["2023-01-03", 1500, 75, 0.75]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func("Steps", data)
    assert str(excinfo.value) == "Numeric values for steps, calories burned, and distance walked must be non-negative."