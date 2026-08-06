import pytest
from src_0873 import task_func
import numpy as np

def test_task_func_with_even_tuples():
    data_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_output = [4.0, 5.0, 6.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_uneven_tuples():
    data_list = [(1, 2), (3, 4, 5), (6,)]
    expected_output = [3.0, 3.0, np.nan]
    assert np.allclose(task_func(data_list), expected_output, equal_nan=True)

def test_task_func_with_non_numeric_values():
    data_list = [(1, 'a', 3), (4, 5, 'b'), (7, 8, 9)]
    expected_output = [4.0, 5.0, 8.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_empty_list():
    data_list = []
    expected_output = []
    assert task_func(data_list) == expected_output

def test_task_func_with_all_non_numeric():
    data_list = [('a', 'b', 'c'), ('d', 'e', 'f')]
    expected_output = [np.nan, np.nan, np.nan]
    assert np.allclose(task_func(data_list), expected_output, equal_nan=True)

def test_task_func_with_single_tuple():
    data_list = [(1, 2, 3)]
    expected_output = [1.0, 2.0, 3.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_mixed_types():
    data_list = [(1, 'a', 3.5), (4, 5, 'b'), (7, 8, 9)]
    expected_output = [4.0, 5.0, 8.0]
    assert task_func(data_list) == expected_output