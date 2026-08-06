import pytest
from src_0143 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    fig, axs = task_func()
    
    # Check if fig is a Figure instance
    assert isinstance(fig, plt.Figure), "fig should be an instance of matplotlib.figure.Figure"
    
    # Check if axs is a list of AxesSubplot instances
    assert len(axs) == 2, "axs should contain exactly two axes"
    assert all(isinstance(ax, plt.Axes) for ax in axs), "Both elements in axs should be instances of matplotlib.axes.Axes"
    
    # Check the first subplot (sine function)
    x_values, sin_values = axs[0].lines[0].get_data()
    np.testing.assert_array_almost_equal(x_values, np.linspace(0, 2 * np.pi, 400))
    np.testing.assert_array_almost_equal(sin_values, np.sin(x_values))
    assert axs[0].get_title() == 'Sine function'
    assert axs[0].get_xlabel() == 'x'
    assert axs[0].get_ylabel() == 'sin(x)'
    
    # Check the second subplot (cosine function)
    x_values, cos_values = axs[1].lines[0].get_data()
    np.testing.assert_array_almost_equal(x_values, np.linspace(0, 2 * np.pi, 400))
    np.testing.assert_array_almost_equal(cos_values, np.cos(x_values))
    assert axs[1].get_title() == 'Cosine function'
    assert axs[1].get_xlabel() == 'x'
    assert axs[1].get_ylabel() == 'cos(x)'

# To run the tests, you can use the following command in your terminal:
# pytest -v <path_to_this_file>