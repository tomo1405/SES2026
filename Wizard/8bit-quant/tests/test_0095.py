python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pytest

def task_func(mean, std_dev, num_samples):
    samples = np.random.normal(mean, std_dev, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mean = %.2f,  std = %.2f" % (mean, std_dev)
    ax.set_title(title)

    return samples, fig

def test_task_func():
    # Test case 1: mean = 0, std_dev = 1, num_samples = 1000
    mean = 0
    std_dev = 1
    num_samples = 1000
    samples, fig = task_func(mean, std_dev, num_samples)
    assert samples.shape == (num_samples,)
    assert fig is not None
    plt.close(fig)

    # Test case 2: mean = 1, std_dev = 2, num_samples = 500
    mean = 1
    std_dev = 2
    num_samples = 500
    samples, fig = task_func(mean, std_dev, num_samples)
    assert samples.shape == (num_samples,)
    assert fig is not None
    plt.close(fig)

    # Test case 3: mean = 2, std_dev = 3, num_samples = 100
    mean = 2
    std_dev = 3
    num_samples = 100
    samples, fig = task_func(mean, std_dev, num_samples)
    assert samples.shape == (num_samples,)
    assert fig is not None
    plt.close(fig)