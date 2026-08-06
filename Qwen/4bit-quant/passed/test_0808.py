import pytest
from src_0808 import task_func
import numpy as np

def test_task_func_no_outliers():
    data = np.array([1, 2, 3, 4, 5])
    outliers, mean, variance = task_func(data)
    assert outliers == []
    assert np.isclose(mean, 3.0)
    assert np.isclose(variance, 2.0)

def test_task_func_with_outliers():
    data = np.array([1, 2, 3, 4, 5, 100])
    outliers, mean, variance = task_func(data)
    assert outliers == [5]
    assert np.isclose(mean, 3.0)
    assert np.isclose(variance, 2.0)

def test_task_func_all_outliers():
    data = np.array([100, 200, 300])
    outliers, mean, variance = task_func(data)
    assert outliers == [0, 1, 2]
    assert np.isclose(mean, 200.0)
    assert np.isclose(variance, 20000.0)

def test_task_func_zero_std_dev():
    data = np.array([1, 1, 1, 1])
    outliers, mean, variance = task_func(data)
    assert outliers == []
    assert np.isclose(mean, 1.0)
    assert np.isclose(variance, 0.0)

def test_task_func_empty_data():
    data = np.array([])
    outliers, mean, variance = task_func(data)
    assert outliers == []
    assert np.isnan(mean)
    assert np.isnan(variance)