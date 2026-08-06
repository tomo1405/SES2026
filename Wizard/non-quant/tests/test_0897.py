python
import pytest
from src_0897 import task_func

def test_task_func():
    # Test case 1
    length = 5
    count = 10
    seed = 0
    expected_result = {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
    assert task_func(length, count, seed) == expected_result
    
    # Test case 2
    length = 3
    count = 5
    seed = 1
    expected_result = {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
    assert task_func(length, count, seed) == expected_result
    
    # Test case 3
    length = 10
    count = 1
    seed = 2
    expected_result = {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
    assert task_func(length, count, seed) == expected_result