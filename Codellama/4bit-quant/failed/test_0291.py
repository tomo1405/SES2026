import pytest
from src_0291 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    expected_result = 10
    actual_result = task_func(directory_path)
    assert actual_result == expected_result