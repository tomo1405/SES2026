import pytest
from src_1063 import task_func
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def test_task_func_empty_array():
    arr = np.array([])
    ax = task_func(arr)
    assert isinstance(ax, Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    assert len(ax.lines) == 0

def test_task_func_non_empty_array():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert isinstance(ax, Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    assert len(ax.lines) == 1
    line = ax.lines[0]
    expected_data = pd.Series([6, 15, 24], index=pd.date_range(start="1/1/2020", periods=3))
    assert np.allclose(line.get_ydata(), expected_data.values)
    assert all(line.get_xdata() == expected_data.index)

def test_task_func_single_row():
    arr = np.array([[1, 2, 3]])
    ax = task_func(arr)
    assert isinstance(ax, Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    assert len(ax.lines) == 1
    line = ax.lines[0]
    expected_data = pd.Series([6], index=pd.date_range(start="1/1/2020", periods=1))
    assert np.allclose(line.get_ydata(), expected_data.values)
    assert all(line.get_xdata() == expected_data.index)

def test_task_func_single_column():
    arr = np.array([[1], [2], [3]])
    ax = task_func(arr)
    assert isinstance(ax, Axes)
    assert ax.get_title() == "Time Series of Row Sums"
    assert len(ax.lines) == 1
    line = ax.lines[0]
    expected_data = pd.Series([1, 2, 3], index=pd.date_range(start="1/1/2020", periods=3))
    assert np.allclose(line.get_ydata(), expected_data.values)
    assert all(line.get_xdata() == expected_data.index)