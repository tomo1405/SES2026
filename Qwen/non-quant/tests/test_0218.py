import pytest
from src_0218 import task_func
import numpy as np

def test_task_func_default_parameters():
    ax, mean, std = task_func()
    assert np.isclose(mean, 0, atol=0.1)
    assert np.isclose(std, 1, atol=0.1)

def test_task_func_custom_parameters():
    mu = 5
    sigma = 2
    sample_size = 5000
    seed = 42
    ax, mean, std = task_func(mu, sigma, sample_size, seed)
    assert np.isclose(mean, mu, atol=0.1)
    assert np.isclose(std, sigma, atol=0.1)

def test_task_func_different_seed():
    _, mean1, std1 = task_func(seed=1)
    _, mean2, std2 = task_func(seed=2)
    assert mean1 != mean2
    assert std1 != std2

def test_task_func_small_sample_size():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax, mean, std = task_func(mu, sigma, sample_size, seed)
    assert np.isclose(mean, mu, atol=0.5)
    assert np.isclose(std, sigma, atol=0.5)