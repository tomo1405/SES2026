import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Check if the function returns a valid matplotlib axis object
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    assert isinstance(ax, plt.Axes)

    # Test 2: Check if the function plots the correct data
    ax = task_func(lambda x: x**2, x_range=(-1, 1), num_points=100)
    assert np.allclose(ax.lines[0].get_data()[0], np.linspace(-1, 1, 100))
    assert np.allclose(ax.lines[0].get_data()[1], np.linspace(-1, 1, 100)**2)
    assert np.allclose(ax.lines[1].get_data()[0], np.linspace(-1, 1, 100))
    assert np.allclose(ax.lines[1].get_data()[1], integrate.cumulative_trapezoid(np.linspace(-1, 1, 100)**2, np.linspace(-1, 1, 100), initial=0))

    # Test 3: Check if the function handles invalid input correctly
    with pytest.raises(ValueError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points=0)
    with pytest.raises(ValueError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points=-100)
    with pytest.raises(ValueError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points=100.5)
    with pytest.raises(ValueError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points="100")
    with pytest.raises(ValueError):
        task_func(lambda x: x**2, x_range=(-1, 1), num_points=None)