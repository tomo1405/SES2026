import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.arange(len(data)))
    assert np.allclose(ydata, np.cumsum(data) / np.sum(data))

def test_task_func_negative_numbers():
    data = np.array([-1, 2, 3, 4, 5])
    with pytest.raises(ValueError, match="Input array contains negative numbers or NaNs."):
        task_func(data)

def test_task_func_nan_values():
    data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError, match="Input array contains negative numbers or NaNs."):
        task_func(data)

def test_task_func_non_numeric_values():
    data = np.array([1, 2, 'a', 4, 5])
    with pytest.raises(TypeError, match="Input array contains non-numeric values."):
        task_func(data)

def test_task_func_empty_array():
    data = np.array([])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.array([]))
    assert np.allclose(ydata, np.array([]))

def test_task_func_single_element():
    data = np.array([5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.array([0]))
    assert np.allclose(ydata, np.array([1.0]))