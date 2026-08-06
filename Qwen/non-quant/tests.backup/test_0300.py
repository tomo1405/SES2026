import pytest
from src_0300 import task_func
from pandas import Series

def test_task_func_empty_elements():
    elements = []
    subset_size = 2
    expected_product = 1
    expected_top_sums = Series([])
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_subset_size_greater_than_elements_length():
    elements = [1, 2, 3]
    subset_size = 5
    expected_product = 1
    expected_top_sums = Series([])
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_subset_size_zero():
    elements = [1, 2, 3]
    subset_size = 0
    expected_product = 1
    expected_top_sums = Series([])
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_single_element():
    elements = [5]
    subset_size = 1
    expected_product = 5
    expected_top_sums = Series([5])
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_multiple_elements():
    elements = [1, 2, 3]
    subset_size = 2
    expected_product = 12  # (1+2)*(1+3)*(2+3) = 3*4*5 = 60
    expected_top_sums = Series([5, 4])  # Top 2 sums: 5 (1+4), 4 (1+3)
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_top_n_greater_than_combinations():
    elements = [1, 2, 3]
    subset_size = 2
    top_n = 5
    expected_product = 12
    expected_top_sums = Series([5, 4, 3])  # All sums: 5, 4, 3
    assert task_func(elements, subset_size, top_n) == (expected_product, expected_top_sums)

def test_task_func_negative_elements():
    elements = [-1, -2, -3]
    subset_size = 2
    expected_product = 6  # (-1-2)*(-1-3)*(-2-3) = -3*-4*-5 = -60
    expected_top_sums = Series([-3, -4])  # Top 2 sums: -3 (-1-2), -4 (-1-3)
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)

def test_task_func_mixed_elements():
    elements = [-1, 2, -3, 4]
    subset_size = 3
    expected_product = 36  # (-1+2-3+4)*(-1+2-3)*(-1+2+4)*(-1-3+4)*(2-3+4) = 2*0*5*0*3 = 0
    expected_top_sums = Series([5, 3])  # Top 2 sums: 5 (2-3+4), 3 (-1+2+4)
    assert task_func(elements, subset_size) == (expected_product, expected_top_sums)