import pytest
from src_0575 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_output():
    ax = task_func()
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."

def test_task_func_plot_data():
    ax = task_func()
    lines = ax.get_lines()
    assert len(lines) == 2, "The plot should have exactly two lines: one for data and one for the fit."
    
    data_line = lines[0]
    fit_line = lines[1]
    
    assert data_line.get_label() == 'data', "The first line should be labeled 'data'."
    assert fit_line.get_label().startswith('fit:'), "The second line should be labeled with the fit parameters."

def test_task_func_array_length():
    ax = task_func(array_length=50)
    x = ax.lines[0].get_xdata()
    assert len(x) == 50, "The length of the x data should match the specified array_length."

def test_task_func_noise_level():
    ax = task_func(noise_level=0.1)
    y = ax.lines[0].get_ydata()
    x = ax.lines[0].get_xdata()
    noise = y - np.sin(x)
    assert np.allclose(np.std(noise), 0.1, atol=0.05), "The standard deviation of the noise should match the specified noise_level."

def test_task_func_default_parameters():
    ax = task_func()
    x = ax.lines[0].get_xdata()
    assert len(x) == 100, "The default array_length should be 100."
    y = ax.lines[0].get_ydata()
    noise = y - np.sin(x)
    assert np.allclose(np.std(noise), 0.2, atol=0.05), "The default noise_level should be 0.2."

def test_task_func_fit_parameters():
    ax = task_func()
    fit_line = ax.lines[1]
    label = fit_line.get_label()
    a, b = map(float, label.split('=')[1].split(','))
    assert np.isclose(a, 1, atol=0.5), "The fitted parameter a should be close to 1."
    assert np.isclose(b, 1, atol=0.5), "The fitted parameter b should be close to 1."