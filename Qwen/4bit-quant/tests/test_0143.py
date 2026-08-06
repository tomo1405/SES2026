import matplotlib.pyplot as plt
import numpy as np
from src_0143 import task_func


def test_task_func():
    fig, axs = task_func()
    
    # Check if fig is a matplotlib Figure object
    assert isinstance(fig, plt.Figure), "fig should be a matplotlib Figure object"
    
    # Check if axs is a numpy array of AxesSubplot objects
    assert isinstance(axs, np.ndarray), "axs should be a numpy array"
    assert len(axs) == 2, "axs should contain exactly 2 AxesSubplot objects"
    assert all(isinstance(ax, plt.Axes) for ax in axs), "All elements in axs should be matplotlib AxesSubplot objects"
    
    # Check if the plots have the correct titles and labels
    assert axs[0].get_title() == 'Sine function', "The first plot should have the title 'Sine function'"
    assert axs[0].get_xlabel() == 'x', "The first plot should have the x-label 'x'"
    assert axs[0].get_ylabel() == 'sin(x)', "The first plot should have the y-label 'sin(x)'"
    
    assert axs[1].get_title() == 'Cosine function', "The second plot should have the title 'Cosine function'"
    assert axs[1].get_xlabel() == 'x', "The second plot should have the x-label 'x'"
    assert axs[1].get_ylabel() == 'cos(x)', "The second plot should have the y-label 'cos(x)'"
    
    # Check if the plots have the correct data
    x_values = np.linspace(0, 2 * np.pi, 400)
    assert np.allclose(axs[0].lines[0].get_xdata(), x_values), "The first plot should have x-values from 0 to 2*pi"
    assert np.allclose(axs[0].lines[0].get_ydata(), np.sin(x_values)), "The first plot should have y-values as sin(x)"
    
    assert np.allclose(axs[1].lines[0].get_xdata(), x_values), "The second plot should have x-values from 0 to 2*pi"
    assert np.allclose(axs[1].lines[0].get_ydata(), np.cos(x_values)), "The second plot should have y-values as cos(x)"