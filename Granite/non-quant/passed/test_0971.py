import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_0971 import task_func

def test_task_func():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"

def test_task_func_negative_numbers():
    data = np.array([-1, -2, -3, -4, -5])
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "Input array contains negative numbers or NaNs." in str(excinfo.value)

def test_task_func_nan_values():
    data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "Input array contains negative numbers or NaNs." in str(excinfo.value)

def test_task_func_non_numeric_values():
    data = np.array(["a", "b", "c", "d", "e"])
    with pytest.raises(TypeError) as excinfo:
        task_func(data)
    assert "Input array contains non-numeric values." in str(excinfo.value)