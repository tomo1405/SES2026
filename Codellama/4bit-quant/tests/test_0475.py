import matplotlib
import numpy as np
import pytest
from src_0475 import task_func


def test_task_func():
    # Test with valid inputs
    ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(samples, np.ndarray)
    assert samples.shape == (1000,)
    assert np.all(samples >= 0)
    assert np.all(samples <= 1)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(n_samples=0, mu=0, sigma=1, random_seed=0)
    with pytest.raises(ValueError):
        task_func(n_samples=1000, mu=0, sigma=0, random_seed=0)
    with pytest.raises(ValueError):
        task_func(n_samples=1000, mu=0, sigma=-1, random_seed=0)

    # Test with different random seeds
    ax1, samples1 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    ax2, samples2 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=1)
    assert not np.array_equal(samples1, samples2)

    # Test with different number of samples
    ax1, samples1 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    ax2, samples2 = task_func(n_samples=2000, mu=0, sigma=1, random_seed=0)
    assert np.array_equal(samples1, samples2[:1000])

    # Test with different mu and sigma
    ax1, samples1 = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    ax2, samples2 = task_func(n_samples=1000, mu=1, sigma=2, random_seed=0)
    assert not np.array_equal(samples1, samples2)