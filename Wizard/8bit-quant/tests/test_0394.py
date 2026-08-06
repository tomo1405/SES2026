python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pytest

def task_func(mu, sigma, num_samples=1000, seed=77):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    fig = plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    plt.subplot(1, 2, 2)
    stats.probplot(samples, dist="norm", plot=plt)

    return fig

def test_task_func():
    # Test case 1
    mu = 0
    sigma = 1
    num_samples = 1000
    seed = 77
    expected_fig = plt.figure(figsize=(12, 6))
    expected_fig.add_subplot(1, 2, 1)
    expected_fig.hist(np.random.normal(mu, sigma, num_samples), bins=30, density=True, alpha=0.6, color='g')
    expected_fig.add_subplot(1, 2, 2)
    stats.probplot(np.random.normal(mu, sigma, num_samples), dist="norm", plot=expected_fig)
    assert task_func(mu, sigma, num_samples, seed) == expected_fig

    # Test case 2
    mu = 1
    sigma = 2
    num_samples = 500
    seed = 100
    expected_fig = plt.figure(figsize=(12, 6))
    expected_fig.add_subplot(1, 2, 1)
    expected_fig.hist(np.random.normal(mu, sigma, num_samples), bins=30, density=True, alpha=0.6, color='g')
    expected_fig.add_subplot(1, 2, 2)
    stats.probplot(np.random.normal(mu, sigma, num_samples), dist="norm", plot=expected_fig)
    assert task_func(mu, sigma, num_samples, seed) == expected_fig

    # Test case 3
    mu = 2
    sigma = 3
    num_samples = 100
    seed = 123
    expected_fig = plt.figure(figsize=(12, 6))
    expected_fig.add_subplot(1, 2, 1)
    expected_fig.hist(np.random.normal(mu, sigma, num_samples), bins=30, density=True, alpha=0.6, color='g')
    expected_fig.add_subplot(1, 2, 2)
    stats.probplot(np.random.normal(mu, sigma, num_samples), dist="norm", plot=expected_fig)
    assert task_func(mu, sigma, num_samples, seed) == expected_fig