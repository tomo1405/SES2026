import pytest
from src_0123 import task_func
import numpy as np
import random

def test_task_func_appends_random_number():
    original_list = [1, 2, 3]
    result = task_func(original_list)
    assert len(original_list) == 4
    assert isinstance(original_list[-1], int)
    assert 0 <= original_list[-1] <= 100

def test_task_func_returns_numpy_array():
    result = task_func([])
    assert isinstance(result, np.ndarray)

def test_task_func_array_size_matches_sum_of_list():
    original_list = [1, 2, 3]
    result = task_func(original_list)
    expected_size = sum(original_list)
    assert len(result) == expected_size

def test_task_func_array_values_are_between_0_and_1():
    result = task_func([])
    assert all(0 <= value <= 1 for value in result)

def test_task_func_with_empty_list():
    result = task_func([])
    assert len(result) > 0  # Since a random number is appended

def test_task_func_with_large_numbers():
    original_list = [1000, 2000, 3000]
    result = task_func(original_list)
    expected_size = sum(original_list)
    assert len(result) == expected_size

def test_task_func_with_negative_numbers():
    original_list = [-1, -2, -3]
    result = task_func(original_list)
    expected_size = sum(original_list)
    assert len(result) == expected_size

def test_task_func_with_mixed_numbers():
    original_list = [1, -2, 3, -4]
    result = task_func(original_list)
    expected_size = sum(original_list)
    assert len(result) == expected_size