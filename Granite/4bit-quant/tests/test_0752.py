import pytest
from src_0752 import task_func

def test_task_func():
    values = [1, 2, 3, 4, 5]
    weights = [1, 2, 3, 4, 5]
    n_samples = 1000
    histogram = task_func(values, weights, n_samples)
    assert isinstance(histogram, dict)
    assert all(isinstance(key, int) and isinstance(value, int) for key, value in histogram.items())
    assert sum(histogram.values()) == n_samples