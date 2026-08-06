import pytest
from src_1115 import task_func
from collections import defaultdict
from random import randint

def test_task_func():
    # Test case 1: Test with an empty dictionary
    dict1 = {}
    expected_result = {}
    actual_result = task_func(dict1)
    assert actual_result == expected_result

    # Test case 2: Test with a dictionary containing valid data
    dict1 = {
        'EMP$$123': 5,
        'EMP$$456': 3,
        'EMP$$789': 2
    }
    expected_result = {
        'EMP$$123': [randint(1, 100) for _ in range(5)],
        'EMP$$456': [randint(1, 100) for _ in range(3)],
        'EMP$$789': [randint(1, 100) for _ in range(2)]
    }
    actual_result = task_func(dict1)
    assert actual_result == expected_result

    # Test case 3: Test with a dictionary containing invalid data
    dict1 = {
        'Invalid Prefix': 10,
        'EMP$$456': 3,
        'EMP$$789': 2
    }
    expected_result = {
        'EMP$$456': [randint(1, 100) for _ in range(3)],
        'EMP$$789': [randint(1, 100) for _ in range(2)]
    }
    actual_result = task_func(dict1)
    assert actual_result == expected_result