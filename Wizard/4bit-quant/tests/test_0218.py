python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pytest

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    
    fig, ax = plt.subplots()
    ax.hist(sample, bins=30, density=True, alpha=0.5, label='Sample Histogram')
    
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2, label='Normal PDF')
    
    ax.set_title("Normal Distribution with $\\mu = %0.2f, \\sigma = %0.2f$" % (mu, sigma))
    ax.legend()    
    return ax, np.mean(sample), np.std(sample)

def test_task_func():
    # Test default values
    ax, mean, std = task_func()
    assert ax is not None
    assert mean == 0
    assert std == 1
    
    # Test with custom values
    ax, mean, std = task_func(mu=1, sigma=2, sample_size=100, seed=42)
    assert ax is not None
    assert mean == 1
    assert std == 2
    
    # Test with invalid values
    with pytest.raises(ValueError):
        task_func(mu=-1)
    with pytest.raises(ValueError):
        task_func(sigma=-1)
    with pytest.raises(ValueError):
        task_func(sample_size=-1)
    with pytest.raises(ValueError):
        task_func(seed=-1)