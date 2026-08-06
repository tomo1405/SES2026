import pytest
from src_0098 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    expected_result = 10.0
    assert task_func(numbers) == expected_result

def test_task_func_with_empty_list():
    numbers = []
    expected_result = 0.0
    assert task_func(numbers) == expected_result

def test_task_func_with_single_element_list():
    numbers = [1]
    expected_result = 0.0
    assert task_func(numbers) == expected_result

def test_task_func_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected_result = -10.0
    assert task_func(numbers) == expected_result

def test_task_func_with_floating_point_numbers():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected_result = 10.0
    assert task_func(numbers) == expected_result

def test_task_func_with_large_numbers():
    numbers = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]
    expected_result = 10.0
    assert task_func(numbers) == expected_result