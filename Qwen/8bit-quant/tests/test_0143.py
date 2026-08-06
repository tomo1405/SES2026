import pytest
from src_0143 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    fig, axs = task_func()
    
    # Check if fig is a Figure object
    assert isinstance(fig, plt.Figure)
    
    # Check if axs is a list of Axes objects
    assert isinstance(axs, np.ndarray)
    assert len(axs) == 2
    assert all(isinstance(ax, plt.Axes) for ax in axs)
    
    # Check the first subplot (sine function)
    x_values = np.linspace(0, 2 * np.pi, 400)
    y_values = np.sin(x_values)
    lines = axs[0].get_lines()
    assert len(lines) == 1
    assert np.allclose(lines[0].get_xdata(), x_values)
    assert np.allclose(lines[0].get_ydata(), y_values)
    assert axs[0].get_title() == 'Sine function'
    assert axs[0].get_xlabel() == 'x'
    assert axs[0].get_ylabel() == 'sin(x)'
    
    # Check the second subplot (cosine function)
    y_values = np.cos(x_values)
    lines = axs[1].get_lines()
    assert len(lines) == 1
    assert np.allclose(lines[0].get_xdata(), x_values)
    assert np.allclose(lines[0].get_ydata(), y_values)
    assert axs[1].get_title() == 'Cosine function'
    assert axs[1].get_xlabel() == 'x'
    assert axs[1].get_ylabel() == 'cos(x)'