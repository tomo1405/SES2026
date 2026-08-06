python
import random
import string
from collections import Counter
import pytest

def task_func(num_strings, string_length):
    strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(num_strings)]
    characters = ''.join(strings)
    character_counter = Counter(characters)
    most_common_characters = character_counter.most_common()

    return most_common_characters

def test_task_func():
    # Test case 1
    num_strings = 10
    string_length = 5
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10)]
    assert task_func(num_strings, string_length) == expected_result

    # Test case 2
    num_strings = 100
    string_length = 10
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result

    # Test case 3
    num_strings = 1000
    string_length = 100
    expected_result = [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]
    assert task_func(num_strings, string_length) == expected_result