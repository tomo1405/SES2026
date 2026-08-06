import numpy as np
from scipy.stats import norm
from src_0808 import task_func
import pytest

def test_task_func():
    data = np.array([1, 2, 3, 4, 5])
    threshold = 2.0
    expected_outliers = [0, 4]
    expected_mean = 3.0
    expected_variance = 2.0

    outliers, mean, variance = task_func(data, threshold)

    assert outliers == expected_outliers
    assert mean == expected_mean
    assert variance == expected_variance

def test_task_func_with_zero_std_dev():
    data = np.array([1, 1, 1, 1, 1])
    threshold = 2.0
    expected_outliers = []
    expected_mean = 1.0
    expected_variance = 0.0

    outliers, mean, variance = task_func(data, threshold)

    assert outliers == expected_outliers
    assert mean == expected_mean
    assert variance == expected_variance