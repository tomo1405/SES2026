import json

from src_1118 import task_func


def test_task_func_valid_prefixes():
    department_data = {
        'EMP$$': 2,
        'DEV$$': 3,
        'HR$$': 1
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    for prefix in department_data.keys():
        assert prefix in level_data
        assert len(level_data[prefix]) == department_data[prefix]
        for level in level_data[prefix]:
            assert level in LEVELS

def test_task_func_invalid_prefixes():
    department_data = {
        'XYZ$$': 2,
        'ABC$$': 3
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert len(level_data) == 0

def test_task_func_zero_employees():
    department_data = {
        'EMP$$': 0,
        'DEV$$': 0
    }
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    for prefix in department_data.keys():
        assert prefix in level_data
        assert len(level_data[prefix]) == 0

def test_task_func_empty_input():
    department_data = {}
    result = task_func(department_data)
    level_data = json.loads(result)
    
    assert isinstance(level_data, dict)
    assert len(level_data) == 0