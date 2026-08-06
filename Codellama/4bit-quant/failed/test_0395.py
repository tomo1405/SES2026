import pytest
from src_0395 import task_func

def test_task_func():
    # Test case 1: length = 10, seed = 0
    length = 10
    seed = 0
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 2: length = 10, seed = 1
    length = 10
    seed = 1
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 3: length = 10, seed = 2
    length = 10
    seed = 2
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 4: length = 10, seed = 3
    length = 10
    seed = 3
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 5: length = 10, seed = 4
    length = 10
    seed = 4
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 6: length = 10, seed = 5
    length = 10
    seed = 5
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 7: length = 10, seed = 6
    length = 10
    seed = 6
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 8: length = 10, seed = 7
    length = 10
    seed = 7
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 9: length = 10, seed = 8
    length = 10
    seed = 8
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result

    # Test case 10: length = 10, seed = 9
    length = 10
    seed = 9
    expected_result = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2}
    assert task_func(length, seed) == expected_result