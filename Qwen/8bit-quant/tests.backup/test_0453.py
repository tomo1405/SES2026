import pytest
from src_0453 import task_func
import numpy as np

def test_task_func_default():
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)
    assert predictions.shape[0] == 20  # 20% of 100 samples
    assert coefficients.shape[0] == 10  # 10 features

def test_task_func_custom_samples_and_features():
    predictions, coefficients, intercept, mse = task_func(n_samples=200, n_features=5)
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)
    assert predictions.shape[0] == 40  # 20% of 200 samples
    assert coefficients.shape[0] == 5  # 5 features

def test_task_func_random_seed():
    predictions1, _, _, _ = task_func(random_seed=42)
    predictions2, _, _, _ = task_func(random_seed=42)
    assert np.array_equal(predictions1, predictions2)

def test_task_func_no_random_seed():
    predictions1, _, _, _ = task_func()
    predictions2, _, _, _ = task_func()
    assert not np.array_equal(predictions1, predictions2)

def test_task_func_mse_positive():
    predictions, _, _, mse = task_func()
    assert mse >= 0

def test_task_func_coefficients_shape():
    predictions, coefficients, _, _ = task_func(n_features=7)
    assert coefficients.shape[0] == 7

def test_task_func_intercept_type():
    _, _, intercept, _ = task_func()
    assert isinstance(intercept, float)