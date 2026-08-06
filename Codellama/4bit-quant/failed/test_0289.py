import pytest
from src_0289 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    expected_result = {'key1': 2, 'key2': 3, 'key3': 4}

    result = task_func(directory_path)

    assert result == expected_result