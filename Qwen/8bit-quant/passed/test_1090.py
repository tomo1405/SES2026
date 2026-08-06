import pytest
from src_1090 import task_func
from collections import Counter
import numpy as np

def test_task_func_with_empty_list():
    result = task_func([])
    assert result == (0, {})

def test_task_func_with_single_tuple():
    result = task_func([(5, 'a')])
    assert result == (5, {'a': 1})

def test_task_func_with_multiple_tuples():
    result = task_func([(1, 'a'), (2, 'b'), (3, 'a')])
    assert result == (6, {'a': 2, 'b': 1})

def test_task_func_with_negative_numbers():
    result = task_func([(-1, 'x'), (-2, 'y'), (3, 'x')])
    assert result == (0, {'x': 2, 'y': 1})

def test_task_func_with_mixed_categories():
    result = task_func([(10, 'cat'), (20, 'dog'), (30, 'cat'), (40, 'bird')])
    assert result == (100, {'cat': 2, 'dog': 1, 'bird': 1})

def test_task_func_with_large_numbers():
    result = task_func([(10**6, 'large'), (10**7, 'large'), (10**8, 'small')])
    assert result == (111000000, {'large': 2, 'small': 1})