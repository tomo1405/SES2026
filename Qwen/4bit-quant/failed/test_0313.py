import pytest
from src_0313 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_bins():
    distribution, ax = task_func()
    assert len(distribution) == 1000
    assert len(ax.patches) == 30

def test_task_func_custom_bins():
    distribution, ax = task_func(bins=50)
    assert len(distribution) == 1000
    assert len(ax.patches) == 50

def test_task_func_distribution_values():
    distribution, _ = task_func()
    assert isinstance(distribution, list)
    assert all(isinstance(x, float) for x in distribution)

def test_task_func_plot():
    _, ax = task_func()
    assert isinstance(ax, plt.Axes)

def test_task_func_distribution_mean():
    distribution, _ = task_func()
    mean = np.mean(distribution)
    assert np.isclose(mean, 0, atol=0.1)

def test_task_func_distribution_std():
    distribution, _ = task_func()
    std = np.std(distribution)
    assert np.isclose(std, 1, atol=0.1)