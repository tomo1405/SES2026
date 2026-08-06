import pytest
from src_1115 import task_func

def test_task_func():
    dict1 = {'EMP$$1': 3, 'EMP$$2': 2, 'EMP$$3': 1}
    result = task_func(dict1)
    assert result == {'EMP$$1': [1, 2, 3], 'EMP$$2': [1, 2], 'EMP$$3': [1]}

def test_task_func_empty_dict():
    dict1 = {}
    result = task_func(dict1)
    assert result == {}

def test_task_func_invalid_prefix():
    dict1 = {'EMP$$1': 3, 'EMP$$2': 2, 'EMP$$3': 1, 'INVALID': 1}
    result = task_func(dict1)
    assert result == {'EMP$$1': [1, 2, 3], 'EMP$$2': [1, 2], 'EMP$$3': [1]}

def test_task_func_invalid_num_employees():
    dict1 = {'EMP$$1': 0, 'EMP$$2': 2, 'EMP$$3': 1}
    result = task_func(dict1)
    assert result == {'EMP$$1': [], 'EMP$$2': [1, 2], 'EMP$$3': [1]}