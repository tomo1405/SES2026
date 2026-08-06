import pytest
from src_0752 import task_func

def test_task_func():
    values = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.4, 0.5]
    n_samples = 1000

    histogram = task_func(values, weights, n_samples)

    assert len(histogram) == len(values)
    assert all(value in histogram for value in values)
    assert all(weight in histogram.values() for weight in weights)
    assert all(histogram[value] >= 0 for value in values)
    assert all(histogram[value] <= n_samples for value in values)