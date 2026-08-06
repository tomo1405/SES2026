import pytest
from src_0738 import task_func
import numpy as np
import math

def test_task_func_with_nested_lists():
    L = [[3, 1], [4, [5, 2]]]
    assert task_func(L) == 3.0

def test_task_func_with_flat_list():
    L = [1, 2, 3, 4, 5]
    assert task_func(L) == 3.0

def test_task_func_with_even_number_of_elements():
    L = [1, 2, 3, 4]
    assert task_func(L) == 2.5

def test_task_func_with_single_element():
    L = [1]
    assert task_func(L) == 1.0

def test_task_func_with_negative_numbers():
    L = [-5, -3, -1, -4, -2]
    assert task_func(L) == -3.0

def test_task_func_with_mixed_positive_and_negative_numbers():
    L = [-1, 2, -3, 4, -5]
    assert task_func(L) == -1.0

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_empty_nested_lists():
    with pytest.raises(ValueError):
        task_func([[], []])