import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from src_0383 import task_func
import pytest

def test_task_func_output_type():
    length = 100
    distribution, ax = task_func(length)
    assert isinstance(distribution, np.ndarray), "Output should be a numpy array"
    assert isinstance(ax, plt.Axes), "Output should be a matplotlib Axes object"

def test_task_func_output_shape():
    length = 100
    distribution, ax = task_func(length)
    assert distribution.shape == (length,), "Output array should have shape (length,)"
    assert ax.get_lines()[0].get_xdata().shape == (length,), "X-data of line plot should have shape (length,)"
    assert ax.get_lines()[1].get_xdata().shape == (length,), "X-data of line plot should have shape (length,)"

def test_task_func_output_values():
    length = 10000
    distribution, ax = task_func(length)
    assert np.mean(distribution) == 0, "Mean of distribution should be close to 0"
    assert np.std(distribution) == 1, "Standard deviation of distribution should be close to 1"
    assert np.all(np.sort(distribution) == ax.get_lines()[0].get_xdata()), "X-data of histogram should be sorted"
    assert np.all(norm.pdf(np.sort(distribution), 0, 1) == ax.get_lines()[1].get_ydata()), "Y-data of PDF plot should match theoretical PDF"