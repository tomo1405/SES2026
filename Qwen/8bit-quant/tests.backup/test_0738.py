import pytest
from src_0738 import task_func
import numpy as np
import math

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_single_element():
    assert task_func([5]) == 5

def test_task_func_with_even_number_of_elements():
    assert task_func([1, 3, 5, 7]) == 4.0

def test_task_func_with_odd_number_of_elements():
    assert task_func([1, 3, 5, 7, 9]) == 5

def test_task_func_with_nested_lists():
    assert task_func([[1, 2], [3, [4, 5]]]) == 3.0

def test_task_func_with_negative_numbers():
    assert task_func([-5, -3, -1, 1, 3, 5]) == 0.0

def test_task_func_with_mixed_positive_and_negative_numbers():
    assert task_func([-10, 0, 10]) == 0

def test_task_func_with_floats():
    assert task_func([1.5, 2.5, 3.5, 4.5]) == 3.0

def test_task_func_with_large_numbers():
    assert task_func([1000000, 2000000, 3000000, 4000000]) == 2500000.0