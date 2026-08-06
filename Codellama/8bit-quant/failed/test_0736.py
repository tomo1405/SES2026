import pytest
from src_0736 import task_func
import numpy as np

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = {'mean': 5.0, 'variance': 2.25}
    assert task_func(L) == expected

def test_task_func_empty_list():
    L = []
    expected = {'mean': np.nan, 'variance': np.nan}
    assert task_func(L) == expected

def test_task_func_single_element_list():
    L = [[1]]
    expected = {'mean': 1.0, 'variance': 0.0}
    assert task_func(L) == expected

def test_task_func_single_element_list_with_nan():
    L = [[np.nan]]
    expected = {'mean': np.nan, 'variance': np.nan}
    assert task_func(L) == expected

def test_task_func_single_element_list_with_inf():
    L = [[np.inf]]
    expected = {'mean': np.inf, 'variance': np.inf}
    assert task_func(L) == expected

def test_task_func_single_element_list_with_nan_and_inf():
    L = [[np.nan, np.inf]]
    expected = {'mean': np.nan, 'variance': np.nan}
    assert task_func(L) == expected