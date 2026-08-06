python
import random
from string import ascii_uppercase
import pytest

def task_func(dict1):
    employee_ids = []
    
    for prefix, num_employees in dict1.items():
        for _ in range(num_employees):
            random_str = ''.join(random.choice(ascii_uppercase) for _ in range(5))
            employee_ids.append(f'{prefix}{random_str}')

    return employee_ids

def test_task_func():
    # Test case 1
    dict1 = {'A': 2, 'B': 3}
    expected_result = ['A00001', 'A00002', 'B00001', 'B00002', 'B00003']
    assert task_func(dict1) == expected_result

    # Test case 2
    dict1 = {'C': 1, 'D': 0}
    expected_result = ['C00001']
    assert task_func(dict1) == expected_result

    # Test case 3
    dict1 = {'E': 5, 'F': 5}
    expected_result = ['E00001', 'E00002', 'E00003', 'E00004', 'E00005', 'F00001', 'F00002', 'F00003', 'F00004', 'F00005']
    assert task_func(dict1) == expected_result