import pytest
from src_0773 import task_func
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def test_task_func_default_values():
    mse = task_func()
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_with_random_seed():
    seed = 42
    mse1 = task_func(random_seed=seed)
    mse2 = task_func(random_seed=seed)
    assert mse1 == mse2

def test_task_func_with_custom_parameters():
    num_samples = 500
    k = 10
    d = 3
    mse = task_func(num_samples=num_samples, k=k, d=d)
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_scaled_data_mean_zero():
    seed = 42
    num_samples = 1000
    k = 5
    d = 2
    np.random.seed(seed)
    data = np.random.randn(num_samples, 1) * k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    assert np.isclose(scaled_data.mean(), 0, atol=1e-6)

def test_task_func_scaled_data_std_one():
    seed = 42
    num_samples = 1000
    k = 5
    d = 2
    np.random.seed(seed)
    data = np.random.randn(num_samples, 1) * k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    assert np.isclose(scaled_data.std(), 1, atol=1e-6)