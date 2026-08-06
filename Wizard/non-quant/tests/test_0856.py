python
import random
import string
import collections
import pytest

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    strings = [''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length)) for _ in range(n_strings)]
    character_counts = collections.Counter(''.join(strings))
    return dict(character_counts)

def test_task_func():
    # Test case 1
    n_strings = 10
    string_length = 10
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 2
    n_strings = 10
    string_length = 5
    expected_result = {char: n_strings * string_length for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 3
    n_strings = 1
    string_length = 10
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 4
    n_strings = 10
    string_length = 1
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 5
    n_strings = 0
    string_length = 10
    expected_result = {}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 6
    n_strings = 10
    string_length = 0
    expected_result = {}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 7
    n_strings = 10
    string_length = 100
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 8
    n_strings = 100
    string_length = 10
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 9
    n_strings = 1000
    string_length = 100
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result

    # Test case 10
    n_strings = 10000
    string_length = 1000
    expected_result = {char: n_strings for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result