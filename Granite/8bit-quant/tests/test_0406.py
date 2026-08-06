import pytest
from src_0406 import task_func
import random
import matplotlib.pyplot as plt

def test_task_func_with_zero_points():
    points = 0
    y, ax = task_func(points)
    assert len(y) == points
    assert ax.lines[0].get_xdata().size == points
    assert ax.lines[0].get_ydata().size == points

def test_task_func_with_positive_points():
    points = 10
    y, ax = task_func(points)
    assert len(y) == points
    assert ax.lines[0].get_xdata().size == points
    assert ax.lines[0].get_ydata().size == points

def test_task_func_with_negative_points():
    points = -5
    with pytest.raises(ValueError):
        task_func(points)

def test_task_func_with_string_points():
    points = "abc"
    with pytest.raises(TypeError):
        task_func(points)