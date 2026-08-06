import pytest
from src_0670 import task_func

def test_task_func():
    x = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    expected_output = ('a', 'b')
    actual_output = task_func(x)
    assert actual_output == expected_output

def test_task_func_with_negative_values():
    x = {'a': 0, 'b': -1, 'c': 2, 'd': -3}
    expected_output = ('c', 'd')
    actual_output = task_func(x)
    assert actual_output == expected_output

def test_task_func_with_zero_values():
    x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    expected_output = ('a', 'b')
    actual_output = task_func(x)
    assert actual_output == expected_output