import pytest
from src_0300 import task_func

def test_task_func_valid_input():
    elements = [1, 2, 3, 4, 5]
    subset_size = 2
    expected_product = 120
    expected_top_sums = [12, 9, 6]
    product, top_sums = task_func(elements, subset_size)
    assert product == expected_product
    assert top_sums.equals(expected_top_sums)

def test_task_func_invalid_input():
    elements = [1, 2, 3, 4, 5]
    subset_size = 6
    expected_product = 1
    expected_top_sums = []
    product, top_sums = task_func(elements, subset_size)
    assert product == expected_product
    assert top_sums.equals(expected_top_sums)

def test_task_func_empty_input():
    elements = []
    subset_size = 2
    expected_product = 1
    expected_top_sums = []
    product, top_sums = task_func(elements, subset_size)
    assert product == expected_product
    assert top_sums.equals(expected_top_sums)