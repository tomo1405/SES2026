import pytest
from src_0752 import task_func

def test_task_func():
    values = [1, 2, 3, 4, 5]
    weights = [1, 1, 1, 1, 1]
    n_samples = 1000
    histogram = task_func(values, weights, n_samples)
    assert isinstance(histogram, dict)
    assert all(isinstance(key, int) for key in histogram.keys())
    assert all(isinstance(value, int) for value in histogram.values())
    assert sum(histogram.values()) == n_samples