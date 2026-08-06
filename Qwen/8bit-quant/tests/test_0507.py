import pytest
from src_0507 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        ["2023-01-01", 22, 60, 5, 0],
        ["2023-01-02", 24, 55, 10, 0.1],
        ["2023-01-03", 21, 65, 8, 0],
        ["2023-01-04", 23, 50, 12, 0.2],
        ["2023-01-05", 25, 70, 15, 0]
    ]

def test_task_func_with_valid_column(sample_data):
    column = "Temperature"
    result = task_func(column, sample_data)
    
    assert isinstance(result, dict)
    assert "sum" in result
    assert "mean" in result
    assert "min" in result
    assert "max" in result
    assert "plot" in result
    
    expected_sum = sum(row[1] for row in sample_data)
    expected_mean = np.mean([row[1] for row in sample_data])
    expected_min = min(row[1] for row in sample_data)
    expected_max = max(row[1] for row in sample_data)
    
    assert result["sum"] == expected_sum
    assert np.isclose(result["mean"], expected_mean)
    assert result["min"] == expected_min
    assert result["max"] == expected_max
    assert isinstance(result["plot"], plt.Axes)

def test_task_func_with_empty_data():
    column = "Temperature"
    result = task_func(column, [])
    
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
    assert isinstance(result["plot"], plt.Axes)

def test_task_func_with_invalid_column(sample_data):
    column = "Pressure"
    with pytest.raises(KeyError):
        task_func(column, sample_data)