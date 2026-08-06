python
import random
from collections import Counter
import pytest

def task_func(values, weights, n_samples):
    samples = random.choices(values, weights=weights, k=n_samples)
    histogram = dict(Counter(samples))

    return histogram

def test_task_func():
    values = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]
    n_samples = 10000

    histogram = task_func(values, weights, n_samples)

    assert len(histogram) == len(values)
    for value in values:
        assert value in histogram
        assert 0 <= histogram[value] <= n_samples