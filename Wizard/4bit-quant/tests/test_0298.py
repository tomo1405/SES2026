python
import itertools
import collections
import pytest

def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    return collections.Counter(sums)

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_result = {3: 2, 5: 2}
    assert task_func(elements, subset_size) == expected_result