import pytest
from src_0512 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mocking matplotlib to prevent actual plotting
class MockAxes:
    def set_title(self, title):
        pass

    def pie(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_ax(mocker):
    return mocker.patch('matplotlib.pyplot.subplots', return_value=(plt.figure(), MockAxes()))

def test_task_func_with_empty_data(mock_ax):
    column = "Age"
    data = []
    result, ax = task_func(column, data)
    assert result == {"sum": 0, "mean": np.nan, "min": np.nan, "max": np.nan}
    assert isinstance(ax, MockAxes)

def test_task_func_with_valid_data(mock_ax):
    column = "Salary"
    data = [
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7]
    ]
    result, ax = task_func(column, data)
    expected_result = {
        "sum": 180000,
        "mean": 60000,
        "min": 50000,
        "max": 70000
    }
    assert result == expected_result
    assert isinstance(ax, MockAxes)

def test_task_func_with_invalid_column(mock_ax):
    column = "InvalidColumn"
    data = [
        [25, 50000, 3],
        [30, 60000, 5],
        [35, 70000, 7]
    ]
    with pytest.raises(KeyError):
        task_func(column, data)

def test_task_func_with_non_numeric_column(mock_ax):
    column = "Age"
    data = [
        ["twenty-five", 50000, 3],
        ["thirty", 60000, 5],
        ["thirty-five", 70000, 7]
    ]
    with pytest.raises(TypeError):
        task_func(column, data)