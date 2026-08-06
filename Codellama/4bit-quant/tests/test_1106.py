import pytest
from src_1106 import task_func

def test_task_func():
    # Test case 1: R script generates output file within the specified duration
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 10
    expected_result = (True, 'File generated successfully within the specified duration.')
    assert task_func(r_script_path, output_path, duration) == expected_result

    # Test case 2: R script does not generate output file within the specified duration
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 0.1
    expected_result = (False, 'File not generated within the specified duration.')
    assert task_func(r_script_path, output_path, duration) == expected_result