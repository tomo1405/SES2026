import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0971 import task_func


def test_task_func_valid_input():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_input():
    data = np.array([-1, -2, -3, -4, -5])
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Input array contains negative numbers or NaNs." in str(exc_info.value)

def test_task_func_nan_input():
    data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Input array contains negative numbers or NaNs." in str(exc_info.value)

def test_task_func_non_numeric_input():
    data = np.array(["a", "b", "c", "d", "e"])
    with pytest.raises(TypeError) as exc_info:
        task_func(data)
    assert "Input array contains non-numeric values." in str(exc_info.value)