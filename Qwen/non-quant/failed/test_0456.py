import pytest
from src_0456 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Mocking the plot function to prevent actual plotting during tests
plt.show = lambda: None

def test_task_func_mean():
    mean = 0
    std_dev = 1
    n = 1000
    samples = task_func(mean, std_dev, n)
    assert np.isclose(np.mean(samples), mean, atol=0.1)

def test_task_func_std_dev():
    mean = 0
    std_dev = 1
    n = 1000
    samples = task_func(mean, std_dev, n)
    assert np.isclose(np.std(samples), std_dev, atol=0.1)

def test_task_func_sample_size():
    mean = 0
    std_dev = 1
    n = 1000
    samples = task_func(mean, std_dev, n)
    assert len(samples) == n

def test_task_func_histogram():
    mean = 0
    std_dev = 1
    n = 1000
    with plt.ioff():  # Turn off interactive mode to prevent drawing
        fig, ax = plt.subplots()
        task_func(mean, std_dev, n)
        lines = ax.get_lines()
        assert len(lines) == 1  # There should be one line for the PDF plot
        assert len(ax.patches) == 30  # There should be 30 bins in the histogram

def test_task_func_plot_title():
    mean = 0
    std_dev = 1
    n = 1000
    with plt.ioff():  # Turn off interactive mode to prevent drawing
        fig, ax = plt.subplots()
        task_func(mean, std_dev, n)
        title = ax.get_title()
        expected_title = f'Normal Distribution: Mean = {mean}, Std Dev = {std_dev}'
        assert title == expected_title