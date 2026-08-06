import pytest
from src_0001 import task_func
from random import shuffle
import itertools

def test_task_func_default():
    assert task_func() == 1.0

def test_task_func_single_element():
    assert task_func([5]) == 0.0

def test_task_func_two_elements():
    assert task_func([1, 2]) == 1.0

def test_task_func_three_elements():
    assert task_func([1, 2, 3]) == 2.0

def test_task_func_four_elements():
    assert task_func([1, 2, 3, 4]) == 3.0

def test_task_func_five_elements():
    assert task_func([1, 2, 3, 4, 5]) == 4.0

def test_task_func_with_custom_list():
    assert task_func([10, 20, 30]) == 20.0

def test_task_func_with_negative_numbers():
    assert task_func([-1, -2, -3]) == 2.0

def test_task_func_with_mixed_numbers():
    assert task_func([-1, 0, 1]) == 1.0

def test_task_func_with_repeated_numbers():
    assert task_func([1, 1, 1]) == 0.0

def test_task_func_with_large_numbers():
    assert task_func([100, 200, 300, 400]) == 300.0