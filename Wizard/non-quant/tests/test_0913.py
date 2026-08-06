python
import pytest
from src_0913 import task_func

def test_task_func():
    # Test case 1
    letters = ['a', 'b', 'c']
    repetitions = 2
    expected_result = {'a': 2, 'b': 2, 'c': 2}
    assert task_func(letters, repetitions) == expected_result
    
    # Test case 2
    letters = ['a', 'b', 'c']
    repetitions = 3
    expected_result = {'a': 3, 'b': 3, 'c': 3}
    assert task_func(letters, repetitions) == expected_result
    
    # Test case 3
    letters = ['a', 'b', 'c']
    repetitions = 0
    expected_result = {}
    assert task_func(letters, repetitions) == expected_result
    
    # Test case 4
    letters = []
    repetitions = 2
    expected_result = {}
    assert task_func(letters, repetitions) == expected_result
    
    # Test case 5
    letters = ['a', 'b', 'c']
    repetitions = -1
    expected_result = {}
    assert task_func(letters, repetitions) == expected_result