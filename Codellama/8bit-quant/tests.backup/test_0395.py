import pytest
from src_0395 import task_func

def test_task_func():
    length = 10
    seed = 0
    expected_result = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10}

    result = task_func(length, seed)

    assert result == expected_result