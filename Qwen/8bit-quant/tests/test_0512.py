import pytest
from src_0512 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

# Mocking plt.show to prevent actual plotting during tests
plt.show = lambda: None

def test_task_func_empty_data():
    column = "Salary"
    data = []
    result, ax = task_func(column, data)
    expected_result = {"sum": 0, "mean": np.nan, "min": np.nan, "max": np.nan}
    assert result == expected_result
    assert isinstance(ax, plt.Axes)

def test_task_func_non_empty_data():
    column = "Salary"
    data = [
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7]
    ]
    result, ax = task_func(column, data)
    expected_result = {
        "sum": 180000,
        "mean": 60000.0,
        "min": 50000,
        "max": 70000
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_column():
    column = "InvalidColumn"
    data = [
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7]
    ]
    with pytest.raises(KeyError):
        task_func(column, data)

def test_task_func_single_row_data():
    column = "Salary"
    data = [
        [25, 50000, 3]
    ]
    result, ax = task_func(column, data)
    expected_result = {
        "sum": 50000,
        "mean": 50000.0,
        "min": 50000,
        "max": 50000
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)

def test_task_func_all_zero_data():
    column = "Salary"
    data = [
        [25, 0, 3],
        [30, 0, 5],
        [35, 0, 7]
    ]
    result, ax = task_func(column, data)
    expected_result = {
        "sum": 0,
        "mean": 0.0,
        "min": 0,
        "max": 0
    }
    assert result == expected_result
    assert isinstance(ax, plt.Axes)