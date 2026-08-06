import pytest
from src_0897 import task_func

def test_task_func():
    length = 5
    count = 10
    seed = 0
    expected_result = {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}

    result = task_func(length, count, seed)

    assert result == expected_result