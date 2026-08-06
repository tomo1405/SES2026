import pytest
from src_0572 import task_func

def test_task_func_valid_input():
    f_list = [lambda x: x + 1, lambda y: y * 2]
    file_path = "test.csv"
    task_func(f_list, file_path)
    # Add assertions to verify the output

def test_task_func_invalid_flist():
    f_list = ["not_callable", lambda x: x + 1]
    file_path = "test.csv"
    with pytest.raises(ValueError):
        task_func(f_list, file_path)

def test_task_func_empty_flist():
    f_list = []
    file_path = "test.csv"
    with pytest.raises(ValueError):
        task_func(f_list, file_path)

def test_task_func_invalid_file_path():
    f_list = [lambda x: x + 1]
    file_path = 123  # Invalid type for file_path
    with pytest.raises(ValueError):
        task_func(f_list, file_path)