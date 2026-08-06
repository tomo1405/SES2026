import pytest
from src_0873 import task_func
import numpy as np

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = [4, 5, 6]
    assert task_func(data_list) == expected_result

def test_task_func_uneven_tuple_lengths():
    data_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_result = [4, 5, 6]
    assert task_func(data_list) == expected_result

def test_task_func_non_numeric_values():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
    expected_result = [4, 5, 6]
    assert task_func(data_list) == expected_result

def test_task_func_empty_list():
    data_list = []
    expected_result = []
    assert task_func(data_list) == expected_result