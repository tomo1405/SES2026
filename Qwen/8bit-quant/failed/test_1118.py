import pytest
from src_1118 import task_func
import json
import collections

def test_task_func_with_valid_data():
    department_data = {
        'EMP$$': 3,
        'MAN$$': 2,
        'DEV$$': 1,
        'HR$$': 0
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert set(level_data.keys()) == set(department_data.keys())
    
    for prefix, levels in level_data.items():
        assert len(levels) == department_data[prefix]
        for level in levels:
            assert level in LEVELS

def test_task_func_with_invalid_prefix():
    department_data = {
        'INVALID$$': 3,
        'EMP$$': 2
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert 'INVALID$$' not in level_data
    assert len(level_data['EMP$$']) == 2
    for level in level_data['EMP$$']:
        assert level in LEVELS

def test_task_func_with_no_valid_employees():
    department_data = {
        'HR$$': 0,
        'DEV$$': 0
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert level_data == {'HR$$': [], 'DEV$$': []}

def test_task_func_with_empty_input():
    department_data = {}
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert level_data == {}

def test_task_func_with_negative_employees():
    department_data = {
        'EMP$$': -1,
        'MAN$$': 2
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert 'EMP$$' not in level_data
    assert len(level_data['MAN$$']) == 2
    for level in level_data['MAN$$']:
        assert level in LEVELS