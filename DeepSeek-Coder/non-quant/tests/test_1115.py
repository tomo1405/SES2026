import pytest
from src_1115 import task_func
from collections import defaultdict
from random import randint

def test_task_func():
    # Test case 1: Basic functionality
    dict1 = {'EMP$$123': 3, 'EMP$$456': 2, 'OTHER': 5}
    expected_output = {
        'EMP$$123': [randint(1, 100) for _ in range(3)],
        'EMP$$456': [randint(1, 100) for _ in range(2)]
    }
    assert task_func(dict1=dict1) == expected_output

    # Add more test cases as needed

# Add more test cases as needed