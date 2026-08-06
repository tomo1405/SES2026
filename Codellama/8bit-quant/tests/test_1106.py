import pytest
from src_1106 import task_func

def test_task_func_valid_input():
    # Test with valid input
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 10
    expected_result = (True, 'File generated successfully within the specified duration.')
    assert task_func(r_script_path, output_path, duration) == expected_result

def test_task_func_invalid_input():
    # Test with invalid input
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 0
    expected_result = (False, 'File not generated within the specified duration.')
    assert task_func(r_script_path, output_path, duration) == expected_result