import pytest
from src_0856 import task_func

def test_task_func():
    # Test case 1: n_strings = 1, string_length = 1
    n_strings = 1
    string_length = 1
    expected_result = {'a': 1}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 2: n_strings = 2, string_length = 2
    n_strings = 2
    string_length = 2
    expected_result = {'ab': 2}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 3: n_strings = 3, string_length = 3
    n_strings = 3
    string_length = 3
    expected_result = {'abc': 3}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 4: n_strings = 4, string_length = 4
    n_strings = 4
    string_length = 4
    expected_result = {'abcd': 4}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 5: n_strings = 5, string_length = 5
    n_strings = 5
    string_length = 5
    expected_result = {'abcde': 5}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 6: n_strings = 6, string_length = 6
    n_strings = 6
    string_length = 6
    expected_result = {'abcdef': 6}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 7: n_strings = 7, string_length = 7
    n_strings = 7
    string_length = 7
    expected_result = {'abcdefg': 7}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 8: n_strings = 8, string_length = 8
    n_strings = 8
    string_length = 8
    expected_result = {'abcdefgh': 8}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 9: n_strings = 9, string_length = 9
    n_strings = 9
    string_length = 9
    expected_result = {'abcdefghi': 9}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 10: n_strings = 10, string_length = 10
    n_strings = 10
    string_length = 10
    expected_result = {'abcdefghij': 10}
    assert task_func(n_strings, string_length) == expected_result