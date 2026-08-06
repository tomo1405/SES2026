import pytest
from src_0512 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7],
        [40, 80000, 9]
    ]

def test_task_func_with_valid_data(sample_data):
    column = "Salary"
    result, ax = task_func(column, sample_data)

    expected_result = {
        "sum": 260000,
        "mean": 65000.0,
        "min": 50000,
        "max": 80000
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_data():
    column = "Salary"
    result, ax = task_func(column, [])

    expected_result = {
        "sum": 0,
        "mean": np.nan,
        "min": np.nan,
        "max": np.nan
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_column(sample_data):
    column = "InvalidColumn"
    with pytest.raises(KeyError):
        task_func(column, sample_data)

def test_task_func_with_single_row_data(sample_data):
    column = "Salary"
    single_row_data = [sample_data[0]]
    result, ax = task_func(column, single_row_data)

    expected_result = {
        "sum": 50000,
        "mean": 50000.0,
        "min": 50000,
        "max": 50000
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)