import pytest
from src_1115 import task_func
from collections import defaultdict
from random import randint

def test_task_func():
    dict1 = {
        'EMP$$John': 5,
        'EMP$$Jane': 3,
        'TMP$$Bob': 2
    }
    expected_result = {
        'EMP$$John': [randint(1, 100) for _ in range(5)],
        'EMP$$Jane': [randint(1, 100) for _ in range(3)]
    }
    result = task_func(dict1)
    assert result == expected_result

def test_task_func_with_invalid_prefix():
    dict1 = {
        'TMP$$Bob': 2
    }
    expected_result = {}
    result = task_func(dict1)
    assert result == expected_result

def test_task_func_with_empty_dict():
    dict1 = {}
    expected_result = {}
    result = task_func(dict1)
    assert result == expected_result