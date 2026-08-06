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

def test_task_func_minimum_samples():
    r_squared, model = task_func(num_samples=2, noise_strength=0, random_seed=42, test_size=0.5)
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1
    assert isinstance(model, LinearRegression)

def test_task_func_invalid_test_size():
    with pytest.raises(ValueError):
        task_func(num_samples=1, noise_strength=1, random_seed=None, test_size=0.5)

def test_task_func_random_seed_consistency():
    r_squared_1, _ = task_func(num_samples=100, noise_strength=0, random_seed=42)
    r_squared_2, _ = task_func(num_samples=100, noise_strength=0, random_seed=42)
    assert r_squared_1 == r_squared_2

def test_task_func_no_noise():
    r_squared, _ = task_func(num_samples=100, noise_strength=0, random_seed=42)
    assert r_squared >= 0.9  # Expecting high R-squared due to no noise

def test_task_func_high_noise():
    r_squared, _ = task_func(num_samples=100, noise_strength=10, random_seed=42)
    assert r_squared < 0.5  # Expecting low R-squared due to high noise