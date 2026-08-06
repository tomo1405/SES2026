import pytest
from src_1115 import task_func
from collections import defaultdict

def test_task_func_with_valid_prefix():
    input_dict = {'EMP$$1': 3, 'EMP$$2': 2}
    result = task_func(input_dict)
    assert len(result) == 2
    assert all(isinstance(salaries, list) for salaries in result.values())
    assert all(1 <= salary <= 100 for salaries in result.values() for salary in salaries)

def test_task_func_with_invalid_prefix():
    input_dict = {'EMP1': 3, 'EMP2': 2}
    result = task_func(input_dict)
    assert result == {}

def test_task_func_with_zero_employees():
    input_dict = {'EMP$$1': 0}
    result = task_func(input_dict)
    assert result == {'EMP$$1': []}

def test_task_func_with_negative_employees():
    input_dict = {'EMP$$1': -1}
    result = task_func(input_dict)
    assert result == {}

def test_task_func_with_empty_input():
    input_dict = {}
    result = task_func(input_dict)
    assert result == {}

def test_task_func_with_multiple_valid_prefixes():
    input_dict = {'EMP$$1': 2, 'EMP$$2': 3, 'EMP$$3': 1}
    result = task_func(input_dict)
    assert len(result) == 3
    assert all(isinstance(salaries, list) for salaries in result.values())
    assert all(1 <= salary <= 100 for salaries in result.values() for salary in salaries)