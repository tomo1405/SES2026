import pytest
from src_0873 import task_func
import numpy as np

def test_task_func_with_even_tuples():
    data_list = [(1, 2, 3), (4, 5, 6)]
    expected_output = [2.5, 3.5, 4.5]
    assert task_func(data_list) == expected_output

def test_task_func_with_uneven_tuples():
    data_list = [(1, 2), (3, 4, 5), (6,)]
    expected_output = [3.0, 3.0, 5.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_mixed_types():
    data_list = [(1, 'a', 3), (4, 5, 'b')]
    expected_output = [2.5, 5.0, np.nan]
    assert np.allclose(task_func(data_list), expected_output, equal_nan=True)

def test_task_func_with_all_non_numeric():
    data_list = [('a', 'b'), ('c', 'd')]
    expected_output = [np.nan, np.nan]
    assert np.allclose(task_func(data_list), expected_output, equal_nan=True)

def test_task_func_with_empty_list():
    data_list = []
    expected_output = []
    assert task_func(data_list) == expected_output

def test_task_func_with_single_tuple():
    data_list = [(1, 2, 3)]
    expected_output = [1.0, 2.0, 3.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_single_element_tuples():
    data_list = [(1,), (2,), (3,)]
    expected_output = [2.0]
    assert task_func(data_list) == expected_output

def test_task_func_with_nan_in_input():
    data_list = [(np.nan, 2, 3), (4, np.nan, 6)]
    expected_output = [2.0, 4.0, 4.5]
    assert np.allclose(task_func(data_list), expected_output, equal_nan=True)