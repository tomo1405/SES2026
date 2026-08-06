import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Test that the function returns a matplotlib axis object
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    assert isinstance(ax, plt.Axes)

    # Test 2: Test that the function plots the correct data
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    x_data = np.linspace(-1, 1, 100)
    y_data = x_data**2
    assert np.allclose(ax.lines[0].get_data()[0], x_data)
    assert np.allclose(ax.lines[0].get_data()[1], y_data)

    # Test 3: Test that the function calculates the correct integral
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    y_int = integrate.cumulative_trapezoid(y_data, x_data, initial=0)
    assert np.allclose(ax.lines[1].get_data()[1], y_int)