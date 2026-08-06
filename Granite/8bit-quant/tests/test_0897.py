import pytest
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    random.seed(seed)
    strings = [''.join(random.choices(['a', 'b', 'c', 'd', 'e'], k=length)) for _ in range(count)]
    letter_frequency = Counter(itertools.chain(*strings))
    
    return letter_frequency

def test_task_func():
    length = 5
    count = 10
    seed = 0
    expected_result = Counter({'a': 20, 'b': 20, 'c': 20, 'd': 20, 'e': 20})
    actual_result = task_func(length, count, seed)
    assert actual_result == expected_result

def test_task_func_with_different_length():
    length = 3
    count = 10
    seed = 0
    expected_result = Counter({'a': 30, 'b': 30, 'c': 30, 'd': 30, 'e': 30})
    actual_result = task_func(length, count, seed)
    assert actual_result == expected_result

def test_task_func_with_different_count():
    length = 5
    count = 5
    seed = 0
    expected_result = Counter({'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10})
    actual_result = task_func(length, count, seed)
    assert actual_result == expected_result

def test_task_func_with_different_seed():
    length = 5
    count = 10
    seed = 1
    expected_result = Counter({'a': 20, 'b': 20, 'c': 20, 'd': 20, 'e': 20})
    actual_result = task_func(length, count, seed)
    assert actual_result != expected_result