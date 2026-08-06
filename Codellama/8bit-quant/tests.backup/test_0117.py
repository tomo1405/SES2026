import pytest
from src_0117 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: mu = 0, sigma = 1, sample_size = 100
    mu = 0
    sigma = 1
    sample_size = 100
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu, atol=1e-2)
    assert np.allclose(np.std(samples), sigma, atol=1e-2)
    assert len(samples) == sample_size

    # Test case 2: mu = 10, sigma = 2, sample_size = 50
    mu = 10
    sigma = 2
    sample_size = 50
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu, atol=1e-2)
    assert np.allclose(np.std(samples), sigma, atol=1e-2)
    assert len(samples) == sample_size

    # Test case 3: mu = -5, sigma = 1.5, sample_size = 200
    mu = -5
    sigma = 1.5
    sample_size = 200
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu, atol=1e-2)
    assert np.allclose(np.std(samples), sigma, atol=1e-2)
    assert len(samples) == sample_size