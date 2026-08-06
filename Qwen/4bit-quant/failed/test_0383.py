import pytest
from src_0383 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_return_type():
    length = 1000
    result = task_func(length)
    assert isinstance(result, tuple), "The function should return a tuple"
    assert len(result) == 2, "The tuple should contain two elements"
    distribution, ax = result
    assert isinstance(distribution, np.ndarray), "The first element should be a numpy array"
    assert isinstance(ax, plt.Axes), "The second element should be a matplotlib Axes object"

def test_task_func_array_length():
    length = 500
    distribution, _ = task_func(length)
    assert len(distribution) == length, "The length of the distribution array should match the input length"

def test_task_func_distribution_mean():
    length = 10000
    distribution, _ = task_func(length)
    mean = np.mean(distribution)
    assert np.isclose(mean, 0, atol=0.1), "The mean of the distribution should be close to 0"

def test_task_func_distribution_std():
    length = 10000
    distribution, _ = task_func(length)
    std = np.std(distribution)
    assert np.isclose(std, 1, atol=0.1), "The standard deviation of the distribution should be close to 1"

def test_task_func_plot():
    length = 100
    _, ax = task_func(length)
    lines = ax.get_lines()
    assert len(lines) == 2, "The plot should have two lines (histogram and PDF)"
    assert lines[0].get_label() == 'Histogram', "The first line should be labeled 'Histogram'"
    assert lines[1].get_label() == 'PDF', "The second line should be labeled 'PDF'"