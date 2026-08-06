import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test 1: Check that the function returns a matplotlib figure object
    fig = task_func(mu=0, sigma=1)
    assert isinstance(fig, plt.Figure)

    # Test 2: Check that the function plots a histogram with the correct number of bins
    num_bins = 30
    fig = task_func(mu=0, sigma=1, num_samples=1000, seed=77)
    ax = fig.axes[0]
    assert len(ax.patches) == num_bins

    # Test 3: Check that the function plots a probability plot with the correct distribution
    dist = "norm"
    fig = task_func(mu=0, sigma=1, num_samples=1000, seed=77)
    ax = fig.axes[1]
    assert ax.get_title() == "Probability Plot"
    assert ax.get_xlabel() == "Sample Values"
    assert ax.get_ylabel() == "Theoretical Quantiles"
    assert ax.get_legend() == "Normal Distribution"
    assert ax.get_xlim() == (-4, 4)
    assert ax.get_ylim() == (-4, 4)
    assert ax.get_xticks() == np.arange(-4, 4, 1)
    assert ax.get_yticks() == np.arange(-4, 4, 1)
    assert ax.get_xticklabels() == ["-4", "-3", "-2", "-1", "0", "1", "2", "3", "4"]
    assert ax.get_yticklabels() == ["-4", "-3", "-2", "-1", "0", "1", "2", "3", "4"]
    assert ax.get_lines()[0].get_xdata() == np.arange(-4, 4, 1)
    assert ax.get_lines()[0].get_ydata() == np.arange(-4, 4, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linestyle() == "-"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[0].get_label() == "Normal Distribution"
    assert ax.get_lines()[1].get_xdata() == np.arange(-4, 4, 1)
    assert ax.get_lines()[1].get_ydata() == np.arange(-4, 4, 1)
    assert ax.get_lines()[1].get_color() == "r"
    assert ax.get_lines()[1].get_linestyle() == "-"
    assert ax.get_lines()[1].get_linewidth() == 2
    assert ax.get_lines()[1].get_label() == "Theoretical Quantiles"