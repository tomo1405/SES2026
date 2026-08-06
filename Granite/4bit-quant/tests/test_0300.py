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
    expected_product = 40
    expected_top_sums = Series([10, 9])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

def test_task_func_invalid_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    top_n = 2
    with pytest.raises(ValueError) as excinfo:
        task_func(elements, subset_size, top_n)
    assert "subset_size must be less than or equal to the length of elements" in str(excinfo.value)

def test_task_func_invalid_top_n():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    top_n = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(elements, subset_size, top_n)
    assert "top_n must be greater than or equal to 1" in str(excinfo.value)