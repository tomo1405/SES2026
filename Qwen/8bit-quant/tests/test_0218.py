import matplotlib.pyplot as plt
import numpy as np
from src_0218 import task_func


def test_task_func_default_parameters():
    ax, mean, std = task_func()
    assert isinstance(ax, plt.Axes)
    assert np.isclose(mean, 0, atol=0.1)
    assert np.isclose(std, 1, atol=0.1)

def test_task_func_custom_parameters():
    mu = 5
    sigma = 2
    sample_size = 5000
    seed = 42
    ax, mean, std = task_func(mu, sigma, sample_size, seed)
    assert isinstance(ax, plt.Axes)
    assert np.isclose(mean, mu, atol=0.1)
    assert np.isclose(std, sigma, atol=0.1)

def test_task_func_sample_size():
    sample_size = 10000
    ax, _, _ = task_func(sample_size=sample_size)
    assert len(ax.patches) == 30  # Number of bins in the histogram

def test_task_func_seed_reproducibility():
    mu = 3
    sigma = 0.5
    seed = 123
    _, mean1, std1 = task_func(mu, sigma, seed=seed)
    _, mean2, std2 = task_func(mu, sigma, seed=seed)
    assert np.isclose(mean1, mean2)
    assert np.isclose(std1, std2)