import pytest
from src_0300 import task_func
from pandas import Series

def test_task_func_subset_size_greater_than_elements():
    elements = [1, 2, 3]
    subset_size = 4
    result = task_func(elements, subset_size)
    assert result == (1, [])

def test_task_func_subset_size_zero():
    elements = [1, 2, 3]
    subset_size = 0
    result = task_func(elements, subset_size)
    assert result == (1, [])

def test_task_func_valid_subset_size():
    elements = [1, 2, 3]
    subset_size = 2
    result = task_func(elements, subset_size)
    assert result[0] == 12  # (1+2)*(1+3)*(2+3) = 6*4*5 = 120
    assert result[1].equals(Series([5, 4]))

def test_task_func_single_element():
    elements = [5]
    subset_size = 1
    result = task_func(elements, subset_size)
    assert result == (5, Series([5]))

def test_task_func_empty_elements():
    elements = []
    subset_size = 1
    result = task_func(elements, subset_size)
    assert result == (1, [])

def test_task_func_top_n_greater_than_combinations():
    elements = [1, 2, 3]
    subset_size = 2
    top_n = 5
    result = task_func(elements, subset_size, top_n)
    assert result[0] == 120
    assert result[1].equals(Series([5, 4]))

def test_task_func_top_n_one():
    elements = [1, 2, 3]
    subset_size = 2
    top_n = 1
    result = task_func(elements, subset_size, top_n)
    assert result[0] == 120
    assert result[1].equals(Series([5]))