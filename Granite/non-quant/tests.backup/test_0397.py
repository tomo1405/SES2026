import pytest
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    if sample_size <= 0:
        raise ValueError('sample_size must be a positive integer.')

    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    density = stats.gaussian_kde(sample)

    x = np.linspace(min(sample), max(sample), sample_size)
    fig, ax = plt.subplots()
    ax.plot(x, density(x))
    
    return ax

def test_task_func():
    with pytest.raises(ValueError):
        task_func(0, 1, -1)
    ax = task_func(0, 1, 100)
    assert isinstance(ax, matplotlib.axes.Axes)