import pytest
from src_0863 import task_func

def test_task_func():
    n = 10  # You can adjust this value as needed
    seed = 42  # You can adjust this value as needed
    expected_result = {
        'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        'b': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        'c': ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
        'd': ['d', 'd', 'd', 'd', 'd', 'd', 'd'],
        'e': ['e', 'e', 'e', 'e', 'e', 'e'],
        'f': ['f', 'f', 'f', 'f', 'f'],
        'g': ['g', 'g', 'g', 'g'],
        'h': ['h', 'h', 'h'],
        'i': ['i', 'i'],
        'j': ['j'],
    }
    result = task_func(n, seed)
    assert result == expected_result