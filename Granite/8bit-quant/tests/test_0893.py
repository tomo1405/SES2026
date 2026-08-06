import pytest
from collections import Counter
from src_0893 import task_func

def test_task_func_with_no_strings():
    assert task_func([]) == Counter()

def test_task_func_with_strings_without_pattern():
    strings = ['abc', 'def', 'ghi']
    expected_counts = Counter([0, 0, 0])
    assert task_func(strings) == expected_counts

def test_task_func_with_strings_with_pattern():
    strings = ['abc}', 'def}', 'ghi}']
    expected_counts = Counter([1, 1, 1])
    assert task_func(strings) == expected_counts

def test_task_func_with_random_strings():
    strings = ['abc', 'def', 'ghi', 'jkl}', 'mno}', 'pqr}']
    expected_counts = Counter([0, 0, 0, 1, 1, 1])
    assert task_func(strings) == expected_counts