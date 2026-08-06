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
import pytest

def test_task_func():
    # Test case 1: Check if ValueError is raised when sample_size is 0
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=0)

    # Test case 2: Check if the returned ax object has the expected properties
    mu = 0
    sigma = 1
    sample_size = 100
    ax = task_func(mu, sigma, sample_size)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_title() == f'Gaussian KDE Density Plot (mu={mu}, sigma={sigma}, sample_size={sample_size})'