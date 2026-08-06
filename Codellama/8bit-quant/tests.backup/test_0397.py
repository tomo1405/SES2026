import pytest
from src_0397 import task_func

def test_task_func_positive_sample_size():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_negative_sample_size():
    mu = 0
    sigma = 1
    sample_size = -1
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_non_integer_sample_size():
    mu = 0
    sigma = 1
    sample_size = 10.5
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_invalid_seed():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = -1
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_valid_seed():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert isinstance(ax, matplotlib.axes.Axes)