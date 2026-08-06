import pytest
from src_0227 import task_func
import numpy as np
import math

def test_task_func_defaults():
    data, ax = task_func()
    assert isinstance(data, tuple)
    assert len(data) == 2
    assert isinstance(data[0], float)
    assert isinstance(data[1], float)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

def test_task_func_custom_range():
    data, ax = task_func(range_start=1, range_end=5, step=0.5)
    assert isinstance(data, tuple)
    assert len(data) == 2
    assert isinstance(data[0], float)
    assert isinstance(data[1], float)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

def test_task_func_data_points():
    data, _ = task_func(range_start=0, range_end=1, step=0.1)
    expected_data = [(x, math.exp(x)) for x in np.arange(0, 1, 0.1)]
    for (x, exp_x), (expected_x, expected_exp_x) in zip(data, expected_data):
        assert math.isclose(x, expected_x)
        assert math.isclose(exp_x, expected_exp_x)

def test_task_func_plot_points():
    _, ax = task_func(range_start=0, range_end=1, step=0.1)
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    expected_xdata = np.arange(0, 1, 0.1)
    expected_ydata = [math.exp(x) for x in expected_xdata]
    for x, expected_x in zip(xdata, expected_xdata):
        assert math.isclose(x, expected_x)
    for y, expected_y in zip(ydata, expected_ydata):
        assert math.isclose(y, expected_y)