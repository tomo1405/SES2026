import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert np.all(ax.get_xlabel() == "Index")
    assert np.all(ax.get_ylabel() == "Cumulative Probability")
    assert np.all(ax.get_title() == "Cumulative Probability Plot")
    assert np.all(ax.get_xdata() == np.arange(len(data)))
    assert np.all(ax.get_ydata() == np.cumsum(data) / np.sum(data))

def test_task_func_negative_input():
    data = np.array([1, 2, -3, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_nan_input():
    data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_non_numeric_input():
    data = np.array([1, 2, "a", 4, 5])
    with pytest.raises(TypeError):
        task_func(data)