import pytest
from src_0583 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test that the function returns a figure object
    fig = task_func()
    assert isinstance(fig, plt.Figure)

    # Test that the function plots a histogram with the correct number of bins
    ax = fig.axes[0]
    assert len(ax.patches) == 10

    # Test that the function plots a normal distribution with the correct mean and std
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 1000)
    p = stats.norm.pdf(x, mu, std)
    assert np.allclose(ax.lines[0].get_ydata(), p)

    # Test that the function plots a normal distribution with the correct mean and std
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 1000)
    p = stats.norm.pdf(x, mu, std)
    assert np.allclose(ax.lines[1].get_ydata(), p)