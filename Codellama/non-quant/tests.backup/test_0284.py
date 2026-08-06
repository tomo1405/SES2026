import pytest
from src_0284 import task_func

def test_task_func():
    json_files_path = './json_files/'
    key = 'name'
    expected_result = {'John': 2, 'Jane': 1, 'Jim': 1}

    result = task_func(json_files_path, key)

    assert result == expected_result