import pytest
from src_1118 import task_func

def test_task_func():
    department_data = {
        'EMP$$': 5,
        'MAN$$': 3,
        'DEV$$': 2,
        'HR$$': 1
    }
    expected_output = '{"EMP$$": ["Mid", "Senior", "Junior", "Junior", "Senior"], "MAN$$": ["Mid", "Junior", "Senior"], "DEV$$": ["Junior", "Mid"], "HR$$": ["Senior"]}'
    actual_output = task_func(department_data)
    assert actual_output == expected_output, "Output does not match the expected output"

def test_task_func_with_invalid_input():
    department_data = {
        'Invalid Prefix': 5,
        'MAN$$': 3,
        'DEV$$': 2,
        'HR$$': 1
    }
    with pytest.raises(ValueError) as excinfo:
        task_func(department_data)
    assert "Invalid prefix: Invalid Prefix" in str(excinfo.value), "Invalid prefix error message is missing"