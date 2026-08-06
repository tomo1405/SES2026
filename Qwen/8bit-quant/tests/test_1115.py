import pytest
from src_1115 import task_func
from collections import defaultdict
from random import randint

def test_task_func_with_valid_prefix():
    input_dict = {'EMP$$001': 3, 'EMP$$002': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 2
    for prefix, salaries in result.items():
        assert prefix in input_dict
        assert len(salaries) == input_dict[prefix]
        assert all(isinstance(salary, int) and 1 <= salary <= 100 for salary in salaries)

def test_task_func_with_invalid_prefix():
    input_dict = {'XYZ001': 3, 'EMP$$002': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'EMP$$002' in result
    assert len(result['EMP$$002']) == 2
    assert all(isinstance(salary, int) and 1 <= salary <= 100 for salary in result['EMP$$002'])

def test_task_func_with_empty_input():
    input_dict = {}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 0

def test_task_func_with_no_valid_employees():
    input_dict = {'EMP$$001': 0, 'EMP$$002': 0}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 2
    for prefix, salaries in result.items():
        assert prefix in input_dict
        assert len(salaries) == 0

def test_task_func_with_negative_employees():
    input_dict = {'EMP$$001': -1, 'EMP$$002': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'EMP$$002' in result
    assert len(result['EMP$$002']) == 2
    assert all(isinstance(salary, int) and 1 <= salary <= 100 for salary in result['EMP$$002'])