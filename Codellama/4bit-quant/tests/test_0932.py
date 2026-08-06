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

    # Test case 5: Multiple words
    assert task_func('hello world') == {'he': 1, 'el': 1, 'll': 1, 'lo': 1, 'wo': 1, 'or': 1, 'rd': 1}