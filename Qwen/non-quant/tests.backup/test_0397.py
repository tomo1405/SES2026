import pytest
from src_0397 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_invalid_sample_size():
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=-1)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=0)

def test_task_func_positive_sample_size():
    ax = task_func(mu=0, sigma=1, sample_size=100)
    assert isinstance(ax, plt.Axes)

def test_task_func_reproducibility():
    ax1 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    ax2 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    line1, = ax1.get_lines()
    line2, = ax2.get_lines()
    np.testing.assert_array_equal(line1.get_ydata(), line2.get_ydata())

def test_task_func_different_seed():
    ax1 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    ax2 = task_func(mu=0, sigma=1, sample_size=100, seed=43)
    line1, = ax1.get_lines()
    line2, = ax2.get_lines()
    assert not np.array_equal(line1.get_ydata(), line2.get_ydata())