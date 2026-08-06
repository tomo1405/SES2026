import pytest
from src_0808 import task_func
import numpy as np

def test_task_func_no_outliers():
    data = np.array([1, 2, 3, 4, 5])
    outliers, mean, std_dev = task_func(data)
    assert outliers == []
    assert mean == 3
    assert std_dev == 1

def test_task_func_with_outliers():
    data = np.array([1, 2, 3, 4, 5, 100])
    outliers, mean, std_dev = task_func(data)
    assert outliers == [5]
    assert mean == 3
    assert std_dev == 1

def test_task_func_with_multiple_outliers():
    data = np.array([1, 2, 3, 4, 5, 100, 200, 300])
    outliers, mean, std_dev = task_func(data)
    assert outliers == [5, 6, 7]
    assert mean == 3
    assert std_dev == 1

def test_task_func_with_threshold():
    data = np.array([1, 2, 3, 4, 5, 100, 200, 300])
    outliers, mean, std_dev = task_func(data, threshold=3.0)
    assert outliers == [5, 6, 7]
    assert mean == 3
    assert std_dev == 1

def test_task_func_with_threshold_and_outliers():
    data = np.array([1, 2, 3, 4, 5, 100, 200, 300])
    outliers, mean, std_dev = task_func(data, threshold=2.0)
    assert outliers == [5, 6, 7]
    assert mean == 3
    assert std_dev == 1