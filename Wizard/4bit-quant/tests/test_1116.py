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
    dict1 = {'A': 3, 'B': 2}
    expected_result = ['A1234', 'A5678', 'A90AB', 'B1234', 'B5678']
    assert task_func(dict1) == expected_result

    # Test case 2
    dict1 = {'C': 1, 'D': 0}
    expected_result = ['C1234', 'C5678', 'C90AB']
    assert task_func(dict1) == expected_result

    # Test case 3
    dict1 = {'E': 5, 'F': 5}
    expected_result = ['E1234', 'E5678', 'E90AB', 'F1234', 'F5678', 'F90AB']
    assert task_func(dict1) == expected_result

    # Test case 4
    dict1 = {'G': 10, 'H': 10}
    expected_result = ['G1234', 'G5678', 'G90AB', 'H1234', 'H5678', 'H90AB', 'I1234', 'I5678', 'I90AB', 'J1234']
    assert task_func(dict1) == expected_result