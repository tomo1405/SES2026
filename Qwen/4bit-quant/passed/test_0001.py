import pytest
from src_0001 import task_func

def test_task_func_default_input():
    result = task_func()
    assert isinstance(result, float)

def test_task_func_single_element():
    result = task_func([5])
    assert result == 0.0

def test_task_func_two_elements():
    result = task_func([1, 2])
    assert result == 1.0

def test_task_func_three_elements():
    result = task_func([1, 2, 3])
    # The exact value can vary due to shuffling, but it should be close to this
    assert abs(result - 2.0) < 1e-6

def test_task_func_four_elements():
    result = task_func([1, 2, 3, 4])
    # The exact value can vary due to shuffling, but it should be close to this
    assert abs(result - 3.0) < 1e-6

def test_task_func_large_numbers():
    result = task_func([10, 20, 30, 40, 50])
    # The exact value can vary due to shuffling, but it should be close to this
    assert abs(result - 30.0) < 1e-6

def test_task_func_negative_numbers():
    result = task_func([-1, -2, -3])
    # The exact value can vary due to shuffling, but it should be close to this
    assert abs(result - 2.0) < 1e-6

def test_task_func_mixed_positive_negative():
    result = task_func([-1, 0, 1])
    # The exact value can vary due to shuffling, but it should be close to this
    assert abs(result - 1.0) < 1e-6