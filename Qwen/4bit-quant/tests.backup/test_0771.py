import pytest
from src_0771 import task_func

def test_task_func_default_values():
    r_squared, _ = task_func()
    assert isinstance(r_squared, float)
    assert 0 <= r_squared <= 1

def test_task_func_with_random_seed():
    r_squared1, _ = task_func(random_seed=42)
    r_squared2, _ = task_func(random_seed=42)
    assert r_squared1 == r_squared2

def test_task_func_minimum_num_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=1, test_size=0.5)

def test_task_func_test_size_too_small():
    with pytest.raises(ValueError):
        task_func(num_samples=2, test_size=0.5)

def test_task_func_large_noise():
    r_squared, _ = task_func(noise_strength=10)
    assert 0 <= r_squared <= 1

def test_task_func_no_noise():
    r_squared, _ = task_func(noise_strength=0)
    assert 0 <= r_squared <= 1

def test_task_func_custom_test_size():
    r_squared, _ = task_func(test_size=0.3)
    assert 0 <= r_squared <= 1