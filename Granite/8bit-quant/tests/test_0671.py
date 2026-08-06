import pytest
from src_0671 import task_func

def test_task_func():
    x = 'abracadabra'
    w = {'a': 1, 'b': 2, 'r': 3, 'c': 4, 'd': 5}
    expected_output = 'abra'
    actual_output = task_func(x, w)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_empty_string():
    x = ''
    w = {}
    expected_output = ''
    actual_output = task_func(x, w)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_single_character():
    x = 'a'
    w = {'a': 1}
    expected_output = 'a'
    actual_output = task_func(x, w)
    assert actual_output == expected_output, "Expected output does not match actual output"