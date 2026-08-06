import matplotlib
import numpy as np
import pytest
from src_0256 import task_func

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]
# Test case 1: Test if the input is an instance of Axes
def test_input_is_axes():
    ax = matplotlib.axes.Axes()
    assert task_func(ax, 0) is ax
# Test case 2: Test if the input is not an instance of Axes
def test_input_is_not_axes():
    with pytest.raises(ValueError):
        task_func(1, 0)
# Test case 3: Test if the function plots the correct function
def test_plots_correct_function():
    ax = matplotlib.axes.Axes()
    ax = task_func(ax, 1)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = FUNCTIONS[1](x)
    assert np.array_equal(ax.lines[0].get_ydata(), y)
# Test case 4: Test if the rlabel position is set correctly
def test_rlabel_position_set_correctly():
    ax = matplotlib.axes.Axes()
    ax = task_func(ax, 2)
    assert ax.rlabel_position == 90