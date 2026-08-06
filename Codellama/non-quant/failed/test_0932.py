import pytest
from src_0932 import task_func

def test_task_func():
    # Test case 1: Empty string
    assert task_func('') == {}

    # Test case 2: Single character
    assert task_func('a') == {'a': 1}

    # Test case 3: Multiple characters
    assert task_func('hello') == {'he': 1, 'el': 1, 'll': 1, 'lo': 1}

    # Test case 4: Non-alphabetic characters
    assert task_func('hello123') == {'he': 1, 'el': 1, 'll': 1, 'lo': 1}

    # Test case 5: Duplicate characters
    assert task_func('hello123hello') == {'he': 2, 'el': 2, 'll': 2, 'lo': 2}