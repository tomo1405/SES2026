import pytest
from src_0227 import task_func
import numpy as np
import math
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    data, ax = task_func()
    x_values = np.arange(0, 10, 0.1)
    expected_data = [(x, math.exp(x)) for x in x_values]
    assert list(data) == expected_data
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_range():
    data, ax = task_func(range_start=1, range_end=5, step=0.5)
    x_values = np.arange(1, 5, 0.5)
    expected_data = [(x, math.exp(x)) for x in x_values]
    assert list(data) == expected_data
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_range():
    data, ax = task_func(range_start=-2, range_end=2, step=1)
    x_values = np.arange(-2, 2, 1)
    expected_data = [(x, math.exp(x)) for x in x_values]
    assert list(data) == expected_data
    assert isinstance(ax, plt.Axes)

def test_task_func_large_step():
    data, ax = task_func(range_start=0, range_end=10, step=2)
    x_values = np.arange(0, 10, 2)
    expected_data = [(x, math.exp(x)) for x in x_values]
    assert list(data) == expected_data
    assert isinstance(ax, plt.Axes)

def test_task_func_no_points():
    with pytest.raises(ValueError):
        task_func(range_start=5, range_end=5, step=1)