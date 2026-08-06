import pytest
from src_0739 import task_func
import numpy as np
from scipy.stats import iqr

def test_task_func_with_integers():
    L = [1, 2, 3, 4, 5]
    expected_iqr = iqr(L)
    assert task_func(L) == expected_iqr

def test_task_func_with_floats():
    L = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_iqr = iqr(L)
    assert task_func(L) == expected_iqr

def test_task_func_with_nested_lists():
    L = [[1, 2], [3, 4], [5]]
    expected_iqr = iqr([1, 2, 3, 4, 5])
    assert task_func(L) == expected_iqr

def test_task_func_with_empty_list():
    L = []
    with pytest.raises(ValueError):
        task_func(L)

def test_task_func_with_single_element():
    L = [42]
    expected_iqr = iqr([42])
    assert task_func(L) == expected_iqr

def test_task_func_with_negative_numbers():
    L = [-5, -3, -1, 1, 3, 5]
    expected_iqr = iqr(L)
    assert task_func(L) == expected_iqr

def test_task_func_with_mixed_positive_and_negative_numbers():
    L = [-10, 0, 10, 20, 30]
    expected_iqr = iqr(L)
    assert task_func(L) == expected_iqr