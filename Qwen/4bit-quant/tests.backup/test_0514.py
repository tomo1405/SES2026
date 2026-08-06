import pytest
from src_0514 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mocking the plotting functionality
class MockAxes:
    def set_ylabel(self, label):
        pass

    def set_title(self, title):
        pass

class MockPlot:
    def line(self, x, y):
        return MockAxes()

plt.plot = MockPlot()

def test_task_func_valid_column():
    data = [
        ["2023-01-01", 1000, 50, 2.0],
        ["2023-01-02", 2000, 75, 3.5],
        ["2023-01-03", 1500, 60, 3.0]
    ]
    result, ax = task_func("Steps", data)
    assert result == {
        "sum": 4500,
        "mean": 1500.0,
        "min": 1000,
        "max": 2000
    }
    assert isinstance(ax, MockAxes)

def test_task_func_invalid_column():
    data = [
        ["2023-01-01", 1000, 50, 2.0],
        ["2023-01-02", 2000, 75, 3.5],
        ["2023-01-03", 1500, 60, 3.0]
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
        ["2023-01-01", -1000, 50, 2.0],
        ["2023-01-02", 2000, 75, 3.5],
        ["2023-01-03", 1500, 60, 3.0]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func("Steps", data)
    assert str(excinfo.value) == "Numeric values for steps, calories burned, and distance walked must be non-negative."