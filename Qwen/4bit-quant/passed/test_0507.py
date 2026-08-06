import pytest
from src_0507 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = [
        ["2023-01-01", 20, 50, 10, 0],
        ["2023-01-02", 22, 55, 12, 0.5],
        ["2023-01-03", 18, 60, 11, 0]
    ]
    column = "Temperature"
    result = task_func(column, data)

    assert isinstance(result, dict)
    assert "sum" in result
    assert "mean" in result
    assert "min" in result
    assert "max" in result
    assert "plot" in result

    expected_sum = 20 + 22 + 18
    expected_mean = expected_sum / 3
    expected_min = 18
    expected_max = 22

    assert result["sum"] == expected_sum
    assert np.isclose(result["mean"], expected_mean)
    assert result["min"] == expected_min
    assert result["max"] == expected_max

def test_task_func_with_empty_data():
    data = []
    column = "Temperature"
    result = task_func(column, data)

    assert isinstance(result, dict)
    assert "sum" in result
    assert "mean" in result
    assert "min" in result
    assert "max" in result
    assert "plot" in result

    assert result["sum"] == 0
    assert result["mean"] is np.nan
    assert result["min"] == np.inf
    assert result["max"] == -np.inf

def test_task_func_with_nonexistent_column():
    data = [
        ["2023-01-01", 20, 50, 10, 0],
        ["2023-01-02", 22, 55, 12, 0.5],
        ["2023-01-03", 18, 60, 11, 0]
    ]
    column = "Pressure"  # This column does not exist in the data
    with pytest.raises(KeyError):
        task_func(column, data)