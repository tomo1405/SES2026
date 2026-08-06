import pytest
from collections import Counter
from src_0893 import task_func

def test_task_func_with_no_strings():
    assert task_func([]) == Counter()

def test_task_func_with_one_string():
    assert task_func(['a']) == Counter()

def test_task_func_with_multiple_strings():
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    expected_counts = Counter([string.count('}') for string in strings])
    assert task_func(strings) == expected_counts

def test_task_func_with_random_strings():
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    expected_counts = Counter([string.count('}') for string in strings])
    assert task_func(strings) == expected_counts