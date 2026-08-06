import pytest
from src_0343 import task_func

def test_task_func():
    # Test case 1: Empty elements list
    elements = []
    pattern = '[a-zA-Z]+'
    seed = 100
    expected_result = ([], False)
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 2: Non-empty elements list with no match
    elements = ['hello', 'world']
    pattern = '[0-9]+'
    seed = 100
    expected_result = (['%hello%', '%world%'], False)
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 3: Non-empty elements list with match
    elements = ['hello', 'world']
    pattern = '[a-zA-Z]+'
    seed = 100
    expected_result = (['%hello%', '%world%'], True)
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 4: Non-empty elements list with multiple matches
    elements = ['hello', 'world', 'hello']
    pattern = '[a-zA-Z]+'
    seed = 100
    expected_result = (['%hello%', '%world%', '%hello%'], True)
    assert task_func(elements, pattern, seed) == expected_result

    # Test case 5: Non-empty elements list with no match due to seed
    elements = ['hello', 'world']
    pattern = '[a-zA-Z]+'
    seed = 101
    expected_result = (['%hello%', '%world%'], False)
    assert task_func(elements, pattern, seed) == expected_result