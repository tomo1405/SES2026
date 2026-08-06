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
    assert np.allclose(np.mean(samples), mu)
    assert np.allclose(np.std(samples), sigma)
    assert len(samples) == sample_size

    # Test case 2: mu = 10, sigma = 2, sample_size = 500
    mu = 10
    sigma = 2
    sample_size = 500
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu)
    assert np.allclose(np.std(samples), sigma)
    assert len(samples) == sample_size

    # Test case 3: mu = -5, sigma = 10, sample_size = 1000
    mu = -5
    sigma = 10
    sample_size = 1000
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu)
    assert np.allclose(np.std(samples), sigma)
    assert len(samples) == sample_size

    # Test case 4: mu = 0, sigma = 1, sample_size = 10000
    mu = 0
    sigma = 1
    sample_size = 10000
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu)
    assert np.allclose(np.std(samples), sigma)
    assert len(samples) == sample_size

    # Test case 5: mu = 100, sigma = 10, sample_size = 100000
    mu = 100
    sigma = 10
    sample_size = 100000
    samples = task_func(mu, sigma, sample_size)
    assert np.allclose(np.mean(samples), mu)
    assert np.allclose(np.std(samples), sigma)
    assert len(samples) == sample_size