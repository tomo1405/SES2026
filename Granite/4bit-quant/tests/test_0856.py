import pytest
from src_0856 import task_func

def test_task_func():
    n_strings = 10
    string_length = 5
    expected_output = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    actual_output = task_func(n_strings, string_length)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1, 5)
    with pytest.raises(ValueError):
        task_func(10, -5)