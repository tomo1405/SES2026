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
    assert task_func(10, 5) == [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10)]

    # Test case 2
    assert task_func(10, 10) == [('a', 10), ('b', 10), ('c', 10), ('d', 10), ('e', 10), ('f', 10), ('g', 10), ('h', 10), ('i', 10), ('j', 10)]

    # Test case 3
    assert task_func(1, 10) == [('a', 1)]

    # Test case 4
    assert task_func(100, 1) == [('a', 100)]

    # Test case 5
    assert task_func(100, 100) == [('a', 100)]