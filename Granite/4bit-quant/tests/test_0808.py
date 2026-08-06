import numpy as np
from scipy.stats import norm
from src_0808 import task_func
import pytest

def test_task_func():
    data = np.array([1, 2, 3, 4, 5])
    threshold = 2.0
    expected_outliers = [0, 4]
    expected_mean = 3
    expected_variance = 2

    outliers, mean, variance = task_func(data, threshold)

    assert outliers == expected_outliers
    assert mean == expected_mean
    assert variance == expected_variance

def test_task_func_with_default_threshold():
    data = np.array([1, 2, 3, 4, 5])
    expected_outliers = []
    expected_mean = 3
    expected_variance = 2

    outliers, mean, variance = task_func(data)

    assert outliers == expected_outliers
    assert mean == expected_mean
    assert variance == expected_variance

def test_task_func_with_no_outliers():
    data = np.array([1, 2, 3, 4, 5])
    threshold = 100
    expected_outliers = []
    expected_mean = 3
    expected_variance = 2

    outliers, mean, variance = task_func(data, threshold)

    assert outliers == expected_outliers
    assert mean == expected_mean
    assert variance == expected_variance