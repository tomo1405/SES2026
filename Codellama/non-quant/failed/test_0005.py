import pytest
from src_0005 import task_func

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    expected_result = {'a': 3, 'b': 3, 'c': 3}
    assert task_func(d) == expected_result

    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}
    expected_result = {'a': 3, 'b': 3, 'c': 3, 'd': 3}
    assert task_func(d) == expected_result

    d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12], 'e': [13, 14, 15]}
    expected_result = {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3}
    assert task_func(d) == expected_result