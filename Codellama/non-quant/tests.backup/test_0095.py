import pytest
from src_0095 import task_func
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: mean = 0, std_dev = 1, num_samples = 100
    mean = 0
    std_dev = 1
    num_samples = 100
    samples, fig = task_func(mean, std_dev, num_samples)
    assert np.allclose(np.mean(samples), mean)
    assert np.allclose(np.std(samples), std_dev)
    assert len(samples) == num_samples
    assert isinstance(fig, plt.Figure)

    # Test case 2: mean = 10, std_dev = 2, num_samples = 50
    mean = 10
    std_dev = 2
    num_samples = 50
    samples, fig = task_func(mean, std_dev, num_samples)
    assert np.allclose(np.mean(samples), mean)
    assert np.allclose(np.std(samples), std_dev)
    assert len(samples) == num_samples
    assert isinstance(fig, plt.Figure)

    # Test case 3: mean = -5, std_dev = 1.5, num_samples = 200
    mean = -5
    std_dev = 1.5
    num_samples = 200
    samples, fig = task_func(mean, std_dev, num_samples)
    assert np.allclose(np.mean(samples), mean)
    assert np.allclose(np.std(samples), std_dev)
    assert len(samples) == num_samples
    assert isinstance(fig, plt.Figure)