import pytest
from src_0343 import task_func

def test_task_func():
    # Test case 1: elements is a list of strings, pattern is a valid regex pattern
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern) == expected_result

    # Test case 2: elements is a list of strings, pattern is a valid regex pattern, seed is specified
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 3: elements is a list of strings, pattern is an invalid regex pattern
    elements = ['hello', 'world']
    pattern = '[a-zA-Z]+'
    expected_result = []
    assert task_func(elements, pattern) == expected_result

    # Test case 4: elements is an empty list, pattern is a valid regex pattern
    elements = []
    pattern = r'[a-zA-Z]+'
    expected_result = []
    assert task_func(elements, pattern) == expected_result

    # Test case 5: elements is a list of strings, pattern is a valid regex pattern, seed is not specified
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern) == expected_result

    # Test case 6: elements is a list of strings, pattern is a valid regex pattern, seed is specified, but not used
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 7: elements is a list of strings, pattern is a valid regex pattern, seed is specified, but not used
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 8: elements is a list of strings, pattern is a valid regex pattern, seed is specified, but not used
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 9: elements is a list of strings, pattern is a valid regex pattern, seed is specified, but not used
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 10: elements is a list of strings, pattern is a valid regex pattern, seed is specified, but not used
    elements = ['hello', 'world']
    pattern = r'[a-zA-Z]+'
    seed = 100
    expected_result = ['hello', 'world']
    assert task_func(elements, pattern, seed) == expected_result