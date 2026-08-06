import pytest
from src_0773 import task_func
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def test_task_func_default_values():
    mse = task_func()
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_custom_values():
    mse = task_func(num_samples=500, k=10, d=5, random_seed=42)
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_random_seed_consistency():
    mse1 = task_func(random_seed=42)
    mse2 = task_func(random_seed=42)
    assert mse1 == mse2

def test_task_func_no_random_seed():
    mse1 = task_func()
    mse2 = task_func()
    assert mse1 != mse2

def test_task_func_zero_variance():
    mse = task_func(k=0, random_seed=42)
    assert mse == 0

def test_task_func_large_k():
    mse = task_func(k=100, random_seed=42)
    assert mse > 0

def test_task_func_small_d():
    mse = task_func(d=0.1, random_seed=42)
    assert mse > 0

def test_task_func_large_d():
    mse = task_func(d=100, random_seed=42)
    assert mse > 0

def test_task_func_with_zero_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=0)