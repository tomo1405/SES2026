import itertools
import math
import pytest
from pandas import Series
from src_0300 import task_func

def test_task_func():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    top_n = 2
    expected_product = math.prod([6, 7, 8])
    expected_top_sums = Series([8, 7])
    actual_product, actual_top_sums = task_func(elements, subset_size, top_n)
    assert actual_product == expected_product
    assert actual_top_sums.equals(expected_top_sums)

def test_task_func_invalid_subset_size():
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    top_n = 2
    with pytest.raises(ValueError):
        task_func(elements, subset_size, top_n)

def test_task_func_invalid_top_n():
    elements = [1, 2, 3, 4, 5]
    subset_size = 3
    top_n = 5
    with pytest.raises(ValueError):
        task_func(elements, subset_size, top_n)