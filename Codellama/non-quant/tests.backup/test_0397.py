import pytest
from src_0397 import task_func

def test_task_func_positive_sample_size():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_negative_sample_size():
    mu = 0
    sigma = 1
    sample_size = -1
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_zero_sample_size():
    mu = 0
    sigma = 1
    sample_size = 0
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_positive_seed():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 1
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_negative_seed():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = -1
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_zero_seed():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_positive_mu():
    mu = 1
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_negative_mu():
    mu = -1
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_zero_mu():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_positive_sigma():
    mu = 0
    sigma = 1
    sample_size = 10
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert ax is not None

def test_task_func_negative_sigma():
    mu = 0
    sigma = -1
    sample_size = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)

def test_task_func_zero_sigma():
    mu = 0
    sigma = 0
    sample_size = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(mu, sigma, sample_size, seed)