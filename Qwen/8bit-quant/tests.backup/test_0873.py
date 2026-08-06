import pytest
from src_0873 import task_func
import numpy as np

def test_task_func_even_tuples():
    data_list = [(1, 2, 3), (4, 5, 6)]
    expected_result = [2.5, 3.5, 4.5]
    assert task_func(data_list) == expected_result

def test_task_func_uneven_tuples():
    data_list = [(1, 2), (3, 4, 5)]
    expected_result = [2.0, 3.0, 5.0]
    assert task_func(data_list) == expected_result

def test_task_func_mixed_data_types():
    data_list = [(1, 'a', 3), ('b', 5, 6)]
    expected_result = [1.0, 5.0, 6.0]
    assert task_func(data_list) == expected_result

def test_task_func_all_non_numeric():
    data_list = [('a', 'b'), ('c', 'd')]
    expected_result = [np.nan, np.nan]
    assert np.allclose(task_func(data_list), expected_result)

def test_task_func_empty_list():
    data_list = []
    expected_result = []
    assert task_func(data_list) == expected_result

def test_task_func_single_tuple():
    data_list = [(1, 2, 3)]
    expected_result = [1.0, 2.0, 3.0]
    assert task_func(data_list) == expected_result

def test_task_func_single_element_tuples():
    data_list = [(1,), (2,), (3,)]
    expected_result = [2.0]
    assert task_func(data_list) == expected_result