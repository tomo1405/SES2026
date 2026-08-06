import pytest
from src_0513 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mocking the plot method to avoid actual plotting
@pytest.fixture
def mock_plot(monkeypatch):
    def mock_bar(self, x, y, title=None):
        pass
    monkeypatch.setattr(pd.DataFrame, 'plot', mock_bar)

def test_task_func_valid_data(mock_plot):
    column = "Quantity Sold"
    data = [
        ["Product A", 10, 200],
        ["Product B", 15, 300],
        ["Product C", 5, 100]
    ]
    result, ax = task_func(column, data)
    assert result == {
        "sum": 30,
        "mean": 10.0,
        "min": 5,
        "max": 15
    }
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_data(mock_plot):
    column = "Quantity Sold"
    data = [
        ["Product A", -10, 200],
        ["Product B", 15, 300],
        ["Product C", 5, 100]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func(column, data)
    assert str(excinfo.value) == "Value must not be negative"

def test_task_func_nonexistent_column(mock_plot):
    column = "Nonexistent Column"
    data = [
        ["Product A", 10, 200],
        ["Product B", 15, 300],
        ["Product C", 5, 100]
    ]
    with pytest.raises(KeyError):
        task_func(column, data)

def test_task_func_empty_data(mock_plot):
    column = "Quantity Sold"
    data = []
    with pytest.raises(IndexError) as excinfo:
        task_func(column, data)
    assert str(excinfo.value) == "index 0 is out of bounds for axis 0 with size 0"