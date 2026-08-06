import pytest
from src_0449 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func_default_parameters():
    ax = task_func()
    x = np.linspace(0 - 3 * 1, 0 + 3 * 1, 100)
    y = norm.pdf(x, 0, 1)
    
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), y)

def test_task_func_custom_parameters():
    mu = 5
    sigma = 2
    ax = task_func(mu, sigma)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)
    
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), y)

def test_task_func_plot_limits():
    ax = task_func()
    assert ax.get_xlim() == (-3, 3)
    assert ax.get_ylim() == (0, 0.4)

def test_task_func_plot_title_and_labels():
    ax = task_func()
    assert ax.get_title() == ''
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''

def test_task_func_figure_and_axes():
    ax = task_func()
    assert isinstance(ax.figure, plt.Figure)
    assert isinstance(ax, plt.Axes)