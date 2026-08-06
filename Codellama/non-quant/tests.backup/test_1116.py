import pytest
from src_1116 import task_func

def test_task_func():
    dict1 = {'A': 2, 'B': 3, 'C': 1}
    expected_employee_ids = ['A1234', 'A5678', 'B1234', 'B5678', 'B9012', 'C1234']
    assert task_func(dict1) == expected_employee_ids