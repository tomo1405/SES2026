import pytest
from src_1115 import task_func
from collections import defaultdict
from random import randint

def test_task_func():
    dict1 = {
        'EMP$$123': 5,
        'EMP$$456': 3,
        'TMP$$789': 1
    }
    expected_output = {
        'EMP$$123': [randint(1, 100) for _ in range(5)],
        'EMP$$456': [randint(1, 100) for _ in range(3)]
    }
    actual_output = task_func(dict1)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    dict1 = {
        'TMP$$123': 5,
        'TMP$$456': 3,
        'TMP$$789': 1
    }
    with pytest.raises(ValueError):
        task_func(dict1)