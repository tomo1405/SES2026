import pytest
from src_0009 import task_func
from collections import Counter
from random import seed

def test_task_func_with_empty_input():
    seed(0)
    result = task_func([])
    assert result == Counter()

def test_task_func_with_single_element():
    seed(0)
    result = task_func([['1', '2']])
    assert result == Counter({0: 3, 1: 2, 2: 1})

def test_task_func_with_multiple_elements():
    seed(0)
    result = task_func([['1', '2'], ['3', '4']])
    assert result == Counter({0: 6, 1: 4, 2: 2, 3: 1})

def test_task_func_with_zero_sum():
    seed(0)
    result = task_func([['0', '0']])
    assert result == Counter({0: 2})

def test_task_func_with_large_numbers():
    seed(0)
    result = task_func([['99', '100']])
    assert result == Counter({0: 199, 1: 99, 2: 49, 3: 24, 4: 12, 5: 6, 6: 3, 7: 1})

def test_task_func_with_custom_range():
    seed(0)
    result = task_func([['1', '2']], RANGE=50)
    assert result == Counter({0: 3, 1: 2, 2: 1})