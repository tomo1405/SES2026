import pytest
from src_0366 import task_func

def test_task_func_valid_input():
    n = 3
    file_name = 'test_file.json'
    seed = 77
    expected_output = {'apple': 1, 'banana': 1, 'cherry': 1}

    output = task_func(n, file_name, seed)

    with open(file_name, 'r') as f:
        actual_output = json.load(f)

    assert actual_output == expected_output

def test_task_func_invalid_input():
    n = 0
    file_name = 'test_file.json'
    seed = 77

    with pytest.raises(ValueError):
        task_func(n, file_name, seed)

def test_task_func_invalid_file_name():
    n = 3
    file_name = 'invalid_file.json'
    seed = 77

    with pytest.raises(FileNotFoundError):
        task_func(n, file_name, seed)