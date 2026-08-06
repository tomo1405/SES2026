import pytest
from src_0771 import task_func

def test_task_func_default_parameters():
    r_squared, model = task_func()
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1
    assert isinstance(model, LinearRegression)

def test_task_func_custom_parameters():
    r_squared, model = task_func(num_samples=1000, noise_strength=0.5, random_seed=42, test_size=0.3)
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1
    assert isinstance(model, LinearRegression)

def test_task_func_min_num_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=2, test_size=0.5)

def test_task_func_max_num_samples():
    r_squared, model = task_func(num_samples=1000, test_size=0.999)
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1
    assert isinstance(model, LinearRegression)

def test_task_func_random_seed():
    r_squared_1, _ = task_func(random_seed=42)
    r_squared_2, _ = task_func(random_seed=42)
    assert r_squared_1 == r_squared_2

def test_task_func_no_noise():
    r_squared, model = task_func(noise_strength=0)
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1
    assert isinstance(model, LinearRegression)