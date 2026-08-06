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
    expected_result = {char: n_strings * string_length for char in VALID_CHARACTERS}
    assert task_func(n_strings, string_length) == expected_result