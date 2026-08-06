import pytest
from src_0289 import task_func

def test_task_func():
    directory_path = "/path/to/directory"
    expected_output = {"key1": 10, "key2": 5, "key3": 8}
    actual_output = task_func(directory_path)
    assert actual_output == expected_output

def test_task_func_with_empty_directory():
    directory_path = "/path/to/empty/directory"
    expected_output = {}
    actual_output = task_func(directory_path)
    assert actual_output == expected_output

def test_task_func_with_nonexistent_directory():
    directory_path = "/path/to/nonexistent/directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)