import matplotlib.pyplot as plt
import numpy as np
import pytest
from scipy.stats import norm
from src_0475 import task_func


def test_task_func():
    ax, samples = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(samples, np.ndarray)
    assert samples.shape == (1000,)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_samples=-1)
    with pytest.raises(ValueError):
        task_func(sigma=-1)

def test_task_func_seed():
    ax1, samples1 = task_func(random_seed=0)
    ax2, samples2 = task_func(random_seed=0)
    assert np.array_equal(samples1, samples2)

def test_task_func_distribution():
    ax, samples = task_func()
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, loc=0, scale=1)
    assert np.allclose(ax.lines[0].get_ydata(), y, atol=0.01)