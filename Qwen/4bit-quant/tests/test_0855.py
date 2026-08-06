import math

import pytest
from src_0855 import task_func


def test_task_func_type_error_non_list():
    with pytest.raises(TypeError, match="numbers should be a list of integers."):
        task_func("not a list")

def test_task_func_type_error_non_integers():
    with pytest.raises(TypeError, match="numbers should be a list of integers."):
        task_func([1, "two", 3])

def test_task_func_value_error_negative_numbers():
    with pytest.raises(ValueError, match="each number in numbers should be non negative."):
        task_func([-1, 2, 3])

def test_task_func_empty_list():
    result = task_func([])
    assert result == ([], [])

def test_task_func_single_element():
    result = task_func([1])
    expected_sums = [math.factorial(1)]
    expected_permutations = [(1,)]
    assert result == (expected_sums, expected_permutations)

def test_task_func_two_elements():
    result = task_func([1, 2])
    expected_sums = [math.factorial(1) + math.factorial(2), math.factorial(2) + math.factorial(1)]
    expected_permutations = [(1, 2), (2, 1)]
    assert result == (expected_sums, expected_permutations)

def test_task_func_three_elements():
    result = task_func([1, 2, 3])
    expected_sums = [
        math.factorial(1) + math.factorial(2) + math.factorial(3),
        math.factorial(1) + math.factorial(3) + math.factorial(2),
        math.factorial(2) + math.factorial(1) + math.factorial(3),
        math.factorial(2) + math.factorial(3) + math.factorial(1),
        math.factorial(3) + math.factorial(1) + math.factorial(2),
        math.factorial(3) + math.factorial(2) + math.factorial(1)
    ]
    expected_permutations = [
        (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
    ]
    assert result == (expected_sums, expected_permutations)