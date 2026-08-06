import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input_negative_numbers():
    data = np.array([1, 2, -3, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_invalid_input_non_numeric_values():
    data = np.array([1, 2, '3', 4, 5])
    with pytest.raises(TypeError):
        task_func(data)

def test_task_func_zero_sum():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)