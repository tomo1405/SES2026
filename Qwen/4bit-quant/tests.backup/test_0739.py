import pytest
from src_0739 import task_func
import numpy as np
from scipy.stats import iqr

def test_task_func_with_list():
    L = [1, 2, 3, 4, 5]
    expected_iqr = iqr(L)
    assert task_func(L) == expected_iqr

def test_task_func_with_nested_list():
    L = [[1, 2], [3, 4], [5]]
    expected_iqr = iqr(np.array(L).flatten())
    assert task_func(L) == expected_iqr

def test_task_func_with_single_element():
    L = [1]
    expected_iqr = iqr([1])
    assert task_func(L) == expected_iqr

def test_task_func_with_empty_list():
    L = []
    expected_iqr = iqr([])
    assert task_func(L) == expected_iqr

def test_task_func_with_all_identical_elements():
    L = [5, 5, 5, 5]
    expected_iqr = iqr([5, 5, 5, 5])
    assert task_func(L) == expected_iqr

def test_task_func_with_negative_numbers():
    L = [-5, -3, -1, 1, 3, 5]
    expected_iqr = iqr([-5, -3, -1, 1, 3, 5])
    assert task_func(L) == expected_iqr

def test_task_func_with_floats():
    L = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_iqr = iqr([1.5, 2.5, 3.5, 4.5, 5.5])
    assert task_func(L) == expected_iqr

def test_task_func_with_mixed_types():
    L = [1, 2.0, 3, 4.0, 5]
    expected_iqr = iqr([1, 2.0, 3, 4.0, 5])
    assert task_func(L) == expected_iqr