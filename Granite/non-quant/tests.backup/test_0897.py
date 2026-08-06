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
    expected_result = Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})
    result = task_func(length, count, seed)
    assert result == expected_result

def test_task_func_with_different_length():
    length = 3
    count = 10
    seed = 0
    expected_result = Counter({'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3})
    result = task_func(length, count, seed)
    assert result == expected_result

def test_task_func_with_different_count():
    length = 5
    count = 5
    seed = 0
    expected_result = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
    result = task_func(length, count, seed)
    assert result == expected_result

def test_task_func_with_different_seed():
    length = 5
    count = 10
    seed = 1
    expected_result = Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})
    result = task_func(length, count, seed)
    assert result == expected_result