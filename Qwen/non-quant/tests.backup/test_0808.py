import pytest
from src_0808 import task_func
import numpy as np
from scipy.stats import norm

def test_task_func_no_outliers():
    data = np.array([1, 2, 3, 4, 5])
    expected_outliers = []
    expected_mean = np.mean(data)
    expected_var = np.var(data)
    
    outliers, mean, var = task_func(data)
    
    assert outliers == expected_outliers
    assert np.isclose(mean, expected_mean)
    assert np.isclose(var, expected_var)

def test_task_func_with_outliers():
    data = np.array([1, 2, 3, 4, 5, 100])
    expected_outliers = [5]
    expected_mean = np.mean(data)
    expected_var = np.var(data)
    
    outliers, mean, var = task_func(data)
    
    assert outliers == expected_outliers
    assert np.isclose(mean, expected_mean)
    assert np.isclose(var, expected_var)

def test_task_func_zero_std_dev():
    data = np.array([5, 5, 5, 5, 5])
    expected_outliers = []
    expected_mean = np.mean(data)
    expected_var = 0
    
    outliers, mean, var = task_func(data)
    
    assert outliers == expected_outliers
    assert np.isclose(mean, expected_mean)
    assert var == expected_var

def test_task_func_negative_data():
    data = np.array([-1, -2, -3, -4, -5])
    expected_outliers = []
    expected_mean = np.mean(data)
    expected_var = np.var(data)
    
    outliers, mean, var = task_func(data)
    
    assert outliers == expected_outliers
    assert np.isclose(mean, expected_mean)
    assert np.isclose(var, expected_var)

def test_task_func_mixed_data():
    data = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected_outliers = [0, 11]
    expected_mean = np.mean(data)
    expected_var = np.var(data)
    
    outliers, mean, var = task_func(data)
    
    assert outliers == expected_outliers
    assert np.isclose(mean, expected_mean)
    assert np.isclose(var, expected_var)