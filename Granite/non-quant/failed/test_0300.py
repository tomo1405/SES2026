import itertools
import math
from pandas import Series
def task_func(elements, subset_size, top_n=2):
    if subset_size > len(elements) or subset_size <= 0:
        return 1, []

    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations if len(combination) != 0]
    product = math.prod(sums)
    top_sums = sorted(sums, reverse=True)[:top_n]
    top_sums = Series(top_sums)
    return product, top_sums
import pytest

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = 2
    expected_output = (210, Series([10, 15]))
    actual_output = task_func(elements, subset_size, top_n)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_invalid_input():
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    top_n = 2
    with pytest.raises(ValueError):
        task_func(elements, subset_size, top_n)