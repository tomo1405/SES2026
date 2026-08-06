import matplotlib
import numpy as np
from src_0573 import task_func


def test_task_func():
    # Test that the function returns a matplotlib.axes.Axes object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function plots the maximum values correctly
    expected_max_values = np.array([randint(1, 100) for _ in range(100)])
    actual_max_values = ax.get_ydata()
    np.testing.assert_array_equal(expected_max_values, actual_max_values)

    # Test that the function sets the ylabel correctly
    assert ax.get_ylabel() == 'Maximum Values'