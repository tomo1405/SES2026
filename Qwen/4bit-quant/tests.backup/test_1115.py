import pytest
from src_1115 import task_func
from collections import defaultdict

def test_task_func_with_valid_prefix():
    input_dict = {'EMP$$123': 3, 'EMP$$456': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(isinstance(v, list) and len(v) == num for k, v in result.items() for num in input_dict.values())

def test_task_func_with_invalid_prefix():
    input_dict = {'XYZ123': 3, 'EMP$$456': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'EMP$$456' in result and len(result['EMP$$456']) == 2

def test_task_func_with_empty_input():
    input_dict = {}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 0

def test_task_func_with_no_valid_entries():
    input_dict = {'ABC123': 3, 'DEF456': 2}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 0

def test_task_func_with_zero_employees():
    input_dict = {'EMP$$123': 0}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'EMP$$123' in result and len(result['EMP$$123']) == 0

def test_task_func_with_negative_employees():
    input_dict = {'EMP$$123': -1}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 0

def test_task_func_with_large_number_of_employees():
    input_dict = {'EMP$$123': 100}
    result = task_func(input_dict)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'EMP$$123' in result and len(result['EMP$$123']) == 100
    assert all(1 <= salary <= 100 for salary in result['EMP$$123'])