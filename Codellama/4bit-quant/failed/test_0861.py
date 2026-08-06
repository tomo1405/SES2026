import pytest
from src_0861 import task_func

def test_task_func():
    # Test case 1: n = 10, pattern = '[a-zA-Z0-9]{3}'
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 2: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = 1234
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    seed = 1234
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern, seed) == expected_matches

    # Test case 3: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = 5678
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    seed = 5678
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern, seed) == expected_matches

    # Test case 4: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 5: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 6: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 7: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 8: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 9: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches

    # Test case 10: n = 10, pattern = '[a-zA-Z0-9]{3}', seed = None
    n = 10
    pattern = '[a-zA-Z0-9]{3}'
    expected_matches = ['abc', 'def', 'ghi']
    assert task_func(n, pattern) == expected_matches