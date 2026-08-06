import pytest
from src_0098 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    expected_result = 11.098612288668109  # Result obtained from running the target code with the given numbers
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected_result = -11.098612288668109  # Result obtained from running the target code with the given numbers
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_zero():
    numbers = [0, 1, 2, 3, 4]
    expected_result = 0.0  # Result obtained from running the target code with the given numbers
    actual_result = task_func(numbers)
    assert actual_result == expected_result, "Task function returned an incorrect result"