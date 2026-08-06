import pytest
from src_0291 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    expected_result = 10

    result = task_func(directory_path)

    assert result == expected_result