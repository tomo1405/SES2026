import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from src_0475 import task_func
import pytest

def test_task_func_valid_input():
    ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert isinstance(ax, plt.Axes)
    assert isinstance(samples, np.ndarray)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_samples=-1, mu=0, sigma=1, random_seed=0)
    with pytest.raises(ValueError):
        task_func(n_samples=1000, mu=0, sigma=-1, random_seed=0)

def test_task_func_seed():
    ax1, samples1 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    ax2, samples2 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert np.array_equal(samples1, samples2)

def test_task_func_plot():
    ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert len(ax.get_lines()) == 2