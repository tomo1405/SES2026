import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Check if the function returns a valid matplotlib axis object
    ax = task_func(lambda x: x**2)
    assert isinstance(ax, plt.Axes)

    # Test 2: Check if the function plots the correct function
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    assert np.allclose(ax.lines[0].get_ydata(), np.square(ax.lines[0].get_xdata()))

    # Test 3: Check if the function plots the correct integral
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    assert np.allclose(ax.lines[1].get_ydata(), integrate.cumulative_trapezoid(np.square(ax.lines[0].get_xdata()), ax.lines[0].get_xdata(), initial=0))

    # Test 4: Check if the function raises an error when the input function is not callable
    with pytest.raises(TypeError):
        task_func(1)

    # Test 5: Check if the function raises an error when the input x_range is not a tuple
    with pytest.raises(TypeError):
        task_func(lambda x: x**2, x_range=1)

    # Test 6: Check if the function raises an error when the input num_points is not an integer
    with pytest.raises(TypeError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points=1.5)