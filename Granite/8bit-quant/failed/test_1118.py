import pytest
from src_1118 import task_func

def test_task_func():
    department_data = {
        'EMP$$': 10,
        'MAN$$': 5,
        'DEV$$': 8,
        'HR$$': 3
    }
    expected_output = '{"EMP$$": ["Mid", "Senior", "Junior", "Junior", "Mid", "Senior", "Junior", "Junior", "Mid", "Senior"], "MAN$$": ["Junior", "Junior", "Mid", "Mid", "Senior"], "DEV$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid"], "HR$$": ["Junior", "Mid", "Senior"]}'
    
    actual_output = task_func(department_data)
    
    assert actual_output == expected_output, "Task function output does not match the expected output"

def test_task_func_invalid_input():
    department_data = {
        'Invalid Prefix': 10,
        'MAN$$': 5,
        'DEV$$': 8,
        'HR$$': 3
    }
    
    with pytest.raises(ValueError) as excinfo:
        task_func(department_data)
    
    assert "Invalid prefix: 'Invalid Prefix'" in str(excinfo.value), "Task function did not raise the expected ValueError for invalid input"