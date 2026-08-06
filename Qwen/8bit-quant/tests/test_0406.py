import pytest
from src_0406 import task_func
import matplotlib.pyplot as plt

def test_task_func_output():
    points = 5
    y, ax = task_func(points)
    
    assert isinstance(y, list), "The first return value should be a list."
    assert len(y) == points, f"The length of the list should be equal to the number of points ({points})."
    assert all(isinstance(i, float) and 0 <= i <= 1 for i in y), "All elements in the list should be floats between 0 and 1."

    assert isinstance(ax, plt.Axes), "The second return value should be a matplotlib Axes object."

def test_task_func_plot():
    points = 3
    y, ax = task_func(points)
    
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line plot."
    assert len(lines[0].get_xdata()) == points, "The x data should have the same number of points as specified."
    assert len(lines[0].get_ydata()) == points, "The y data should have the same number of points as specified."

def test_task_func_with_zero_points():
    points = 0
    y, ax = task_func(points)
    
    assert y == [], "For zero points, the list should be empty."
    assert ax.get_lines() == [], "For zero points, there should be no lines in the plot."

def test_task_func_with_negative_points():
    with pytest.raises(ValueError):
        task_func(-1)