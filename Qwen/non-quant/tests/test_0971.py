import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_positive_numbers():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert np.allclose(ax.lines[0].get_xdata(), np.arange(len(data)))
    assert np.allclose(ax.lines[0].get_ydata(), np.cumsum(data) / np.sum(data))

def test_task_func_single_element():
    data = np.array([1])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert np.allclose(ax.lines[0].get_xdata(), np.arange(len(data)))
    assert np.allclose(ax.lines[0].get_ydata(), np.cumsum(data) / np.sum(data))

def test_task_func_zero_sum():
    data = np.array([0, 0, 0])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert np.allclose(ax.lines[0].get_xdata(), np.arange(len(data)))
    assert np.allclose(ax.lines[0].get_ydata(), np.zeros_like(data))

def test_task_func_negative_numbers():
    data = np.array([-1, 2, 3])
    with pytest.raises(ValueError, match="Input array contains negative numbers or NaNs."):
        task_func(data)

def test_task_func_nan_values():
    data = np.array([1, np.nan, 3])
    with pytest.raises(ValueError, match="Input array contains negative numbers or NaNs."):
        task_func(data)

def test_task_func_non_numeric_values():
    data = np.array([1, 'a', 3])
    with pytest.raises(TypeError, match="Input array contains non-numeric values."):
        task_func(data)