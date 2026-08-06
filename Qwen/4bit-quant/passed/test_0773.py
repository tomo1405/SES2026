import pytest
from src_0773 import task_func
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def test_task_func_default():
    mse = task_func()
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_with_random_seed():
    mse1 = task_func(random_seed=42)
    mse2 = task_func(random_seed=42)
    assert mse1 == mse2

def test_task_func_with_custom_parameters():
    mse = task_func(num_samples=500, k=3, d=1)
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_with_zero_variance():
    mse = task_func(num_samples=1000, k=0, d=2)
    assert mse == 0

def test_task_func_with_large_k():
    mse = task_func(k=10)
    assert isinstance(mse, float)
    assert mse > 0

def test_task_func_with_large_d():
    mse = task_func(d=10)
    assert isinstance(mse, float)
    assert mse > 0

def test_task_func_with_no_scaling():
    data = np.random.randn(1000, 1) * 5 + 2
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    mse = mean_squared_error(data, scaled_data)
    assert mse == task_func(num_samples=1000, k=5, d=2, random_seed=None)